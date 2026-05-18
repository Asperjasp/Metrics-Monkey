"""Adapter for locally hosted models via Ollama."""
import json
import requests
from .base import BaseModel
from config import OLLAMA_BASE_URL


class OllamaModel(BaseModel):
    def __init__(self, model_id: str, display_name: str, timeout: int = 300):
        super().__init__(model_id, display_name)
        self.timeout = timeout

    def query(self, question: str, context: str = "", system_prompt: str = "") -> str:
        user_content = question
        if context:
            user_content = f"CONTEXTO DEL MANUAL / MANUAL CONTEXT:\n{context}\n\n---\n\nPREGUNTA / QUESTION: {question}"

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_content})

        payload = {
            "model": self.model_id,
            "messages": messages,
            "stream": False,
            "options": {"temperature": 0.1},  # low temp for factual recall
        }

        resp = requests.post(
            f"{OLLAMA_BASE_URL}/api/chat",
            json=payload,
            timeout=self.timeout,
        )
        resp.raise_for_status()
        data = resp.json()
        return data["message"]["content"].strip()

    def is_available(self) -> bool:
        try:
            resp = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
            tags = resp.json()
            available = [m["name"] for m in tags.get("models", [])]
            return any(self.model_id in name or name.startswith(self.model_id.split(":")[0]) for name in available)
        except Exception:
            return False
