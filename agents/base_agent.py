from abc import ABC, abstractmethod
from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage
from utils.config import Config

class BaseAgent(ABC):
    def __init__(self, name: str, callbacks=None):
        self.name = name
        self.callbacks = callbacks or []
        self.llm = self._initialize_llm()

    def _initialize_llm(self):
        if Config.model_config.provider == "ollama":
            return ChatOpenAI(
                base_url="http://localhost:1234/v1",
                api_key="not-needed",
                callbacks=self.callbacks
            )
        else:
            raise ValueError(f"Unknown provider: {Config.model_config.provider}")
        
    def _invoke_llm(self, prompt: str) -> str:
        """Invoke LLM with consistent callbacks"""
        try:
            response = self.llm.invoke(
                [HumanMessage(content=prompt)]
            )
            return response.content
            
        except Exception as e:
            print(f"\nError invoking LLM: {str(e)}")
            return f"Error: {str(e)}"
    
    @abstractmethod
    def process(self, query: str) -> str:
        pass