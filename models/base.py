"""Abstract interface every model adapter must implement."""
from abc import ABC, abstractmethod


class BaseModel(ABC):
    def __init__(self, model_id: str, display_name: str):
        self.model_id = model_id
        self.display_name = display_name

    @abstractmethod
    def query(self, question: str, context: str = "", system_prompt: str = "") -> str:
        """
        Send a question (with optional manual context) and return the model's response.
        Raises an exception on API/connection failure.
        """

    def is_available(self) -> bool:
        """Quick health check. Override if needed."""
        return True

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.display_name})"
