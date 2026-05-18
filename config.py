"""
Model registry and API configuration.
Set API keys via environment variables or a .env file.
"""
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

OLLAMA_BASE_URL = "http://localhost:11434"

# Model registry — add or remove entries freely.
# Each entry: display_name -> {type, model_id, [api_key]}
# type: "ollama" | "openrouter" | "openai"
MODELS = {
    # Local models via Ollama
    # gemma2:2b → pull with: ollama pull gemma2:2b
    "gemma_2b": {
        "type": "ollama",
        "model_id": "gemma2:2b",
        "display": "Gemma 2B (E2B)",
        "skip_if_missing": True,
    },
    # gemma4:latest is the 8B Q4 model currently on this machine
    # For true E4B (4B param), pull: ollama pull gemma4:4b
    "gemma_4b": {
        "type": "ollama",
        "model_id": "gemma4:latest",
        "display": "Gemma 4 8B (E4B proxy)",
    },
    # Gemma 9B (currently labelled gemma:latest on this machine)
    "gemma_9b": {
        "type": "ollama",
        "model_id": "gemma:latest",
        "display": "Gemma 9B (local)",
    },
    # Placeholder for the fine-tuned model (plug in model_id when ready)
    "gemma_2b_finetuned": {
        "type": "ollama",
        "model_id": "gemma2b-moto:latest",  # set when fine-tuned model is available
        "display": "Gemma 2B Fine-tuned",
        "skip_if_missing": True,
    },
    # Cloud SOTA models via OpenRouter
    "gpt4o": {
        "type": "openrouter",
        "model_id": "openai/gpt-4o",
        "display": "GPT-4o",
    },
    "mistral_large": {
        "type": "openrouter",
        "model_id": "mistralai/mistral-large",
        "display": "Mistral Large",
    },
    "qwen_72b": {
        "type": "openrouter",
        "model_id": "qwen/qwen-2.5-72b-instruct",
        "display": "Qwen 2.5 72B",
    },
    # Optional: compare against Claude Sonnet
    "claude_sonnet": {
        "type": "openrouter",
        "model_id": "anthropic/claude-sonnet-4-5",
        "display": "Claude Sonnet 4.5",
    },
}

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
