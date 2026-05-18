"""Adapter for cloud models via OpenRouter (GPT-4o, Mistral, Qwen, etc.)."""
import requests
from .base import BaseModel
from config import OPENROUTER_API_KEY, OPENAI_API_KEY

OPENROUTER_BASE = "https://openrouter.ai/api/v1"
OPENAI_BASE = "https://api.openai.com/v1"


class OpenRouterModel(BaseModel):
    def __init__(self, model_id: str, display_name: str, timeout: int = 60):
        super().__init__(model_id, display_name)
        self.timeout = timeout
        # Use OpenAI directly for gpt models if OpenAI key is set, else fall through to OpenRouter
        self._use_openai_direct = (
            model_id.startswith("openai/") and OPENAI_API_KEY and not OPENROUTER_API_KEY
        )

    def query(self, question: str, context: str = "", system_prompt: str = "") -> str:
        user_content = question
        if context:
            user_content = f"MANUAL CONTEXT:\n{context}\n\n---\n\nQUESTION: {question}"

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_content})

        if self._use_openai_direct:
            return self._call_openai(messages)
        return self._call_openrouter(messages)

    def _call_openrouter(self, messages: list) -> str:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/metrics-monkey",
            "X-Title": "Metrics-Monkey Moto Benchmark",
        }
        payload = {
            "model": self.model_id,
            "messages": messages,
            "temperature": 0.1,
        }
        resp = requests.post(
            f"{OPENROUTER_BASE}/chat/completions",
            headers=headers,
            json=payload,
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()

    def _call_openai(self, messages: list) -> str:
        model_id = self.model_id.replace("openai/", "")
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {"model": model_id, "messages": messages, "temperature": 0.1}
        resp = requests.post(
            f"{OPENAI_BASE}/chat/completions",
            headers=headers,
            json=payload,
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()

    def is_available(self) -> bool:
        return bool(OPENROUTER_API_KEY or OPENAI_API_KEY)
