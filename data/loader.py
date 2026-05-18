"""
Loads manual context for benchmark test cases.
Context is used both for RAG-style prompting and for evaluation scoring.
"""
import csv
import json
import os
from pathlib import Path

DATA_DIR = Path(__file__).parent
PROJECT_ROOT = DATA_DIR.parent


def load_test_cases() -> list[dict]:
    with open(DATA_DIR / "test_cases.json", encoding="utf-8") as f:
        return json.load(f)


def load_suzuki_corpus(csv_path: str | None = None) -> dict[str, list[str]]:
    """Returns {manual_name: [text_chunk, ...]} from Suzuki dataset CSV."""
    path = csv_path or PROJECT_ROOT / "suzuki_dataset_v3.csv"
    corpus: dict[str, list[str]] = {}
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            manual = row["MANUAL"].strip()
            text = row["TEXTO"].strip()
            if text:
                corpus.setdefault(manual, []).append(text)
    return corpus


def load_markdown_manual(md_path: str) -> str:
    """Loads a markdown manual file as a single string."""
    with open(md_path, encoding="utf-8") as f:
        return f.read()


def get_context_for_case(case: dict, corpus: dict[str, list[str]], max_chars: int = 1500) -> str:
    """
    Retrieves the most relevant manual context for a test case.
    Uses keyword matching to rank chunks from the source manual.
    Falls back to the local AKT markdown for AKT cases.
    """
    source = case.get("source_manual", "")
    keywords = case.get("context_keywords", [])

    # AKT cases: use the local markdown file
    if "akt" in source.lower():
        akt_path = PROJECT_ROOT / "[TM]_akt_manual_de_taller_akt_ak_2020.md"
        if akt_path.exists():
            content = load_markdown_manual(str(akt_path))
            return _extract_relevant_section(content, keywords, max_chars)

    # Suzuki cases: retrieve from corpus
    chunks = corpus.get(source, [])
    if not chunks:
        # Fuzzy: try partial name match
        for key in corpus:
            if source.split("_")[-2] in key or source.split("_")[-1] in key:
                chunks = corpus[key]
                break

    if not chunks:
        return ""

    scored = _rank_chunks(chunks, keywords)
    return _build_context(scored, max_chars)


def _rank_chunks(chunks: list[str], keywords: list[str]) -> list[tuple[int, str]]:
    """Returns chunks sorted by keyword hit count descending."""
    scored = []
    for chunk in chunks:
        lower = chunk.lower()
        hits = sum(1 for kw in keywords if kw.lower() in lower)
        scored.append((hits, chunk))
    return sorted(scored, key=lambda x: x[0], reverse=True)


def _build_context(scored_chunks: list[tuple[int, str]], max_chars: int) -> str:
    result = []
    total = 0
    for i, (_, chunk) in enumerate(scored_chunks):
        if total + len(chunk) > max_chars:
            if i == 0:
                # Always include at least the best chunk, truncated if needed
                result.append(chunk[:max_chars])
            break
        result.append(chunk)
        total += len(chunk)
    return "\n\n".join(result)


def _extract_relevant_section(text: str, keywords: list[str], max_chars: int) -> str:
    """Splits markdown into paragraphs and returns top-scoring paragraphs."""
    paragraphs = [p.strip() for p in text.split("\n\n") if len(p.strip()) > 50]
    scored = _rank_chunks(paragraphs, keywords)
    return _build_context(scored, max_chars)
