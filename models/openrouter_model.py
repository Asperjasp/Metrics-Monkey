"""
Adapter for cloud models via OpenRouter, direct OpenAI, or Mistral API.
All three APIs speak the OpenAI chat-completions format.
"""
import requests
from .base import BaseModel
from config import OPENROUTER_API_KEY, OPENAI_API_KEY, MISTRAL_API_KEY

OPENROUTER_BASE = "https://openrouter.ai/api/v1"
OPENAI_BASE     = "https://api.openai.com/v1"
MISTRAL_BASE    = "https://api.mistral.ai/v1"


class OpenRouterModel(BaseModel):
    """OpenRouter — covers Qwen, Claude, and any other OpenRouter model."""
    def __init__(self, model_id: str, display_name: str, timeout: int = 60):
        super().__init__(model_id, display_name)
        self.timeout = timeout

    def query(self, question: str, context: str = "", system_prompt: str = "") -> str:
        user_content = _user_content(question, context)
        messages = _build_messages(system_prompt, user_content)
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/Asperjasp/Metrics-Monkey",
            "X-Title": "Metrics-Monkey Moto Benchmark",
        }
        resp = requests.post(
            f"{OPENROUTER_BASE}/chat/completions",
            headers=headers,
            json={"model": self.model_id, "messages": messages, "temperature": 0.1},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()

    def is_available(self) -> bool:
        return bool(OPENROUTER_API_KEY)


class OpenAIModel(BaseModel):
    """Direct OpenAI API (GPT-4o, GPT-4o-mini, etc.)."""
    def __init__(self, model_id: str, display_name: str, timeout: int = 60):
        super().__init__(model_id, display_name)
        self.timeout = timeout

    def query(self, question: str, context: str = "", system_prompt: str = "") -> str:
        user_content = _user_content(question, context)
        messages = _build_messages(system_prompt, user_content)
        resp = requests.post(
            f"{OPENAI_BASE}/chat/completions",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
            json={"model": self.model_id, "messages": messages, "temperature": 0.1},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()

    def is_available(self) -> bool:
        return bool(OPENAI_API_KEY)


class MistralModel(BaseModel):
    """Direct Mistral API (mistral-large-latest, mistral-small-latest, etc.)."""
    def __init__(self, model_id: str, display_name: str, timeout: int = 60):
        super().__init__(model_id, display_name)
        self.timeout = timeout

    def query(self, question: str, context: str = "", system_prompt: str = "") -> str:
        user_content = _user_content(question, context)
        messages = _build_messages(system_prompt, user_content)
        resp = requests.post(
            f"{MISTRAL_BASE}/chat/completions",
            headers={"Authorization": f"Bearer {MISTRAL_API_KEY}", "Content-Type": "application/json"},
            json={"model": self.model_id, "messages": messages, "temperature": 0.1},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()

    def is_available(self) -> bool:
        return bool(MISTRAL_API_KEY)


# ── helpers ───────────────────────────────────────────────────────────────────

def _user_content(question: str, context: str) -> str:
    if context:
        return f"MANUAL CONTEXT:\n{context}\n\n---\n\nQUESTION: {question}"
    return question

def _build_messages(system_prompt: str, user_content: str) -> list:
    msgs = []
    if system_prompt:
        msgs.append({"role": "system", "content": system_prompt})
    msgs.append({"role": "user", "content": user_content})
    return msgs
