"""
Model registry and API configuration.
Set API keys in a .env file (never commit .env).
"""
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENAI_API_KEY     = os.getenv("OPENAI_API_KEY", "")
MISTRAL_API_KEY    = os.getenv("MISTRAL_API_KEY", "")

OLLAMA_BASE_URL    = "http://localhost:11434"

# ── Model registry ─────────────────────────────────────────────────────────────
# type: "ollama" | "openrouter" | "openai" | "mistral"
MODELS = {
    # ── LOCAL models (Ollama) ────────────────────────────────────────────────
    "gemma_e2b": {
        "type": "ollama",
        "model_id": "gemma2:2b",
        "display": "Gemma E2B (2B local)",
        "group": "local",
    },
    "gemma_e4b": {
        "type": "ollama",
        "model_id": "gemma4:latest",
        "display": "Gemma E4B (8B local)",
        "group": "local",
    },
    # ── Fine-tuned placeholder (owner: Juan Bernardo) ────────────────────────
    # When ready: ollama create gemma2b-moto -f Modelfile
    # Then set model_id = "gemma2b-moto:latest" and remove skip_if_missing
    "gemma_e2b_finetuned": {
        "type": "ollama",
        "model_id": "gemma2b-moto:latest",
        "display": "Gemma E2B Fine-tuned 🔧",
        "group": "finetuned",
        "skip_if_missing": True,
    },
    # ── FOUNDATIONAL / cloud models ──────────────────────────────────────────
    "gpt4o": {
        "type": "openai",
        "model_id": "gpt-4o",
        "display": "GPT-4o",
        "group": "foundational",
    },
    "mistral_large": {
        "type": "mistral",
        "model_id": "mistral-large-latest",
        "display": "Mistral Large",
        "group": "foundational",
    },
    "qwen_72b": {
        "type": "openrouter",
        "model_id": "qwen/qwen-2.5-72b-instruct",
        "display": "Qwen 2.5 72B",
        "group": "foundational",
    },
    "claude_sonnet": {
        "type": "openrouter",
        "model_id": "anthropic/claude-sonnet-4-5",
        "display": "Claude Sonnet",
        "group": "foundational",
    },
}

# Ordered display groups for reports
MODEL_GROUPS = ["local", "finetuned", "foundational"]

SYSTEM_PROMPT_ES = (
    "Eres un mecánico experto en motocicletas. "
    "Responde de forma precisa, práctica y segura basándote en el contexto del manual de taller proporcionado. "
    "Si no sabes algo con certeza, dilo claramente. "
    "Incluye advertencias de seguridad relevantes cuando aplique."
)

SYSTEM_PROMPT_EN = (
    "You are an expert motorcycle mechanic. "
    "Answer accurately, practically, and safely based on the workshop manual context provided. "
    "If you are not certain about something, state it clearly. "
    "Include relevant safety warnings when applicable."
)

JUDGE_PROMPT_TEMPLATE = """You are evaluating an AI assistant's response to a motorcycle repair question.

QUESTION: {question}

REFERENCE CONTEXT (from workshop manual):
{context}

MODEL RESPONSE:
{response}

Score the response on these criteria (0-10 each):
1. Technical accuracy: Is the information correct and consistent with the manual?
2. Completeness: Does it fully answer the question?
3. Safety awareness: Does it mention relevant safety precautions?
4. Practical usefulness: Can a mechanic follow this to actually do the repair?
5. Hallucination: Does it invent specs or steps NOT in the manual? (10=no hallucinations, 0=many)

Return ONLY a JSON object like:
{{"accuracy": 8, "completeness": 7, "safety": 9, "usefulness": 8, "no_hallucination": 7, "overall": 7.8, "comment": "brief note"}}"""
