"""
Generates benchmark visualisation PNGs for the repo and team report.
Outputs to results/figures/
"""
import json
import os
from pathlib import Path
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


METRICS_DISPLAY = {
    "keyword_coverage":   "Keyword\nCoverage",
    "rouge_l":            "ROUGE-L",
    "spec_recall":        "Spec\nRecall",
    "step_completeness":  "Step\nCompleteness",
    "hallucination_risk": "Hallucination\nRisk (↑=safer)",
    "length_score":       "Length\nScore",
    "safety_compliance":  "Safety\nCompliance",
    "composite":          "COMPOSITE",
}

PALETTE = [
    "#2196F3", "#FF5722", "#4CAF50", "#9C27B0",
    "#FF9800", "#00BCD4", "#F44336", "#8BC34A",
]

DIFFICULTY_COLORS = {"easy": "#4CAF50", "medium": "#FF9800", "hard": "#F44336"}
CATEGORY_COLORS   = {
    "specification": "#2196F3", "diagnostic": "#FF5722",
    "procedure": "#9C27B0",    "maintenance": "#4CAF50",
    "safety": "#FF9800",
}


def _load(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _figures_dir(base: str = "results") -> Path:
    d = Path(base) / "figures"
    d.mkdir(parents=True, exist_ok=True)
    return d


# ── Figure 1: Overall radar / spider chart per model ─────────────────────────

def plot_radar(results: dict, out_dir: Path):
    metric_keys = [k for k in METRICS_DISPLAY if k != "composite"]
    labels = [METRICS_DISPLAY[k] for k in metric_keys]
    N = len(labels)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, size=9)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(["0.2", "0.4", "0.6", "0.8", "1.0"], size=7, color="grey")
    ax.grid(color="grey", linestyle="--", linewidth=0.5, alpha=0.5)

    model_scores = _aggregate_by_metric(results)
    patches = []
    for i, (model, scores) in enumerate(model_scores.items()):
        vals = [scores.get(k, 0) for k in metric_keys]
        vals += vals[:1]
        color = PALETTE[i % len(PALETTE)]
        ax.plot(angles, vals, linewidth=2, color=color)
        ax.fill(angles, vals, alpha=0.15, color=color)
        patches.append(mpatches.Patch(color=color, label=model))

    ax.legend(handles=patches, loc="upper right", bbox_to_anchor=(1.35, 1.15), fontsize=9)
    ax.set_title("Metric Radar — All Models", size=13, pad=20, weight="bold")
    path = out_dir / "radar.png"
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  saved {path}")
    return path


# ── Figure 2: Composite bar chart with error bars ─────────────────────────────

def plot_composite_bars(results: dict, out_dir: Path):
    model_scores = _aggregate_by_metric(results)
    models = list(model_scores.keys())
    composites = [model_scores[m].get("composite", 0) for m in models]

    # Compute std dev across cases
    stds = []
    for model in models:
        vals = [
            c["models"].get(model, {}).get("scores", {}).get("composite", 0) or 0
            for c in results["results"]
            if c["models"].get(model, {}).get("scores")
        ]
        stds.append(np.std(vals) if vals else 0)

    fig, ax = plt.subplots(figsize=(max(6, len(models) * 1.8), 5))
    colors = [PALETTE[i % len(PALETTE)] for i in range(len(models))]
    bars = ax.bar(models, composites, color=colors, width=0.55, zorder=3)
    ax.errorbar(models, composites, yerr=stds, fmt="none", color="black", capsize=5, linewidth=1.5, zorder=4)

    for bar, val, std in zip(bars, composites, stds):
        ax.text(bar.get_x() + bar.get_width() / 2, val + std + 0.02,
                f"{val:.3f}", ha="center", va="bottom", fontsize=10, weight="bold")

    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Composite Score (0–1)", fontsize=11)
    ax.set_title("Overall Composite Score by Model\n(error bars = std dev across 25 cases)", fontsize=12, weight="bold")
    ax.axhline(0.7, color="green", linestyle="--", linewidth=1, alpha=0.7, label="Target threshold (0.70)")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.4, zorder=0)
    ax.set_xticklabels(models, rotation=15, ha="right", fontsize=9)
    fig.tight_layout()
    path = out_dir / "composite_bars.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  saved {path}")
    return path


# ── Figure 3: Heatmap — model × metric ────────────────────────────────────────

def plot_metric_heatmap(results: dict, out_dir: Path):
    metric_keys = [k for k in METRICS_DISPLAY if k != "composite"]
    model_scores = _aggregate_by_metric(results)
    models = list(model_scores.keys())

    matrix = np.array([[model_scores[m].get(k, 0) for k in metric_keys] for m in models])
    xlabels = [METRICS_DISPLAY[k] for k in metric_keys]

    fig, ax = plt.subplots(figsize=(len(metric_keys) * 1.4, max(3, len(models) * 1.1)))
    im = ax.imshow(matrix, cmap="RdYlGn", vmin=0, vmax=1, aspect="auto")
    plt.colorbar(im, ax=ax, fraction=0.02, pad=0.04, label="Score (0–1)")

    ax.set_xticks(range(len(xlabels)))
    ax.set_xticklabels(xlabels, rotation=30, ha="right", fontsize=9)
    ax.set_yticks(range(len(models)))
    ax.set_yticklabels(models, fontsize=9)

    for i in range(len(models)):
        for j in range(len(metric_keys)):
            val = matrix[i, j]
            ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                    color="black" if 0.3 < val < 0.85 else "white", fontsize=8)

    ax.set_title("Metric Heatmap — Model × Metric", fontsize=12, weight="bold")
    fig.tight_layout()
    path = out_dir / "heatmap.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  saved {path}")
    return path


# ── Figure 4: Scores by difficulty ────────────────────────────────────────────

def plot_by_difficulty(results: dict, out_dir: Path):
    diffs = ["easy", "medium", "hard"]
    model_diff: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))

    for case in results["results"]:
        d = case["difficulty"]
        for model, mdata in case["models"].items():
            if mdata.get("scores"):
                model_diff[model][d].append(mdata["scores"]["composite"])

    models = list(model_diff.keys())
    x = np.arange(len(diffs))
    width = 0.8 / max(len(models), 1)

    fig, ax = plt.subplots(figsize=(8, 5))
    for i, model in enumerate(models):
        means = [np.mean(model_diff[model].get(d, [0])) for d in diffs]
        offset = (i - len(models) / 2 + 0.5) * width
        bars = ax.bar(x + offset, means, width * 0.9, label=model, color=PALETTE[i % len(PALETTE)], zorder=3)

    ax.set_xticks(x)
    ax.set_xticklabels([d.capitalize() for d in diffs], fontsize=11)
    ax.set_ylabel("Composite Score", fontsize=11)
    ax.set_ylim(0, 1.05)
    ax.set_title("Composite Score by Difficulty Level", fontsize=12, weight="bold")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.4, zorder=0)
    for diff, color in DIFFICULTY_COLORS.items():
        idx = diffs.index(diff)
        ax.axvspan(idx - 0.5, idx + 0.5, alpha=0.05, color=color)
    fig.tight_layout()
    path = out_dir / "by_difficulty.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  saved {path}")
    return path


# ── Figure 5: Per-question score strip (all 25 cases) ─────────────────────────

def plot_per_question(results: dict, out_dir: Path):
    cases = results["results"]
    models = list(cases[0]["models"].keys()) if cases else []

    ids = [c["case_id"] for c in cases]
    n_cases = len(ids)
    fig, ax = plt.subplots(figsize=(max(12, n_cases * 0.7), 5))

    for i, model in enumerate(models):
        scores = []
        for case in cases:
            mdata = case["models"].get(model, {})
            scores.append(mdata["scores"]["composite"] if mdata.get("scores") else 0)
        ax.plot(range(n_cases), scores, marker="o", markersize=5,
                linewidth=1.5, label=model, color=PALETTE[i % len(PALETTE)])

    ax.set_xticks(range(n_cases))
    ax.set_xticklabels(ids, rotation=45, ha="right", fontsize=7)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Composite Score", fontsize=11)
    ax.set_title("Per-Question Composite Score", fontsize=12, weight="bold")
    ax.axhline(0.7, color="green", linestyle="--", linewidth=1, alpha=0.6, label="Target 0.70")
    ax.legend(fontsize=9, loc="lower right")
    ax.grid(alpha=0.3)

    # Color background by category
    cat_map = {c["case_id"]: c["category"] for c in cases}
    for j, cid in enumerate(ids):
        cat = cat_map.get(cid, "")
        color = CATEGORY_COLORS.get(cat, "#eeeeee")
        ax.axvspan(j - 0.5, j + 0.5, alpha=0.07, color=color)

    # Category legend
    cat_patches = [mpatches.Patch(color=v, alpha=0.4, label=k) for k, v in CATEGORY_COLORS.items()]
    ax2 = ax.twinx()
    ax2.set_yticks([])
    ax2.legend(handles=cat_patches, title="Category", loc="upper right", fontsize=7)

    fig.tight_layout()
    path = out_dir / "per_question.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  saved {path}")
    return path


# ── Helpers ───────────────────────────────────────────────────────────────────

def _aggregate_by_metric(results: dict) -> dict[str, dict[str, float]]:
    """Returns {model: {metric: mean_score}}."""
    data: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for case in results["results"]:
        for model, mdata in case["models"].items():
            if mdata.get("scores"):
                for metric, val in mdata["scores"].items():
                    if isinstance(val, (int, float)):
                        data[model][metric].append(val)
    return {
        model: {metric: round(sum(vals) / len(vals), 3) for metric, vals in metrics.items()}
        for model, metrics in data.items()
    }


# ── Entry point ───────────────────────────────────────────────────────────────

def generate_all(results_path: str, out_base: str = "results") -> list[Path]:
    results = _load(results_path)
    out_dir = _figures_dir(out_base)
    print(f"Generating figures → {out_dir}/")
    paths = [
        plot_radar(results, out_dir),
        plot_composite_bars(results, out_dir),
        plot_metric_heatmap(results, out_dir),
        plot_by_difficulty(results, out_dir),
        plot_per_question(results, out_dir),
    ]
    return paths


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m results.visualize <results_json>")
        sys.exit(1)
    generate_all(sys.argv[1])
