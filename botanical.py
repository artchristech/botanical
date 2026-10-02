import os
from pathlib import Path
from anthropic import Anthropic

class Botanical:
    def __init__(self, model: str = "claude-sonnet-4-20250514"):
        self.client = Anthropic()
        self.model = model
        self.system = self._load_prompt()
        self.symbols = ""
        self.history = []
    
    def _load_prompt(self) -> str:
        path = Path(__file__).parent / "system_prompt.txt"
        return path.read_text()
    
    def call(self, user_input: str) -> str:
        self.history.append({"role": "user", "content": user_input})
        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            system=self.system,
            messages=self.history
        )
        output = response.content[0].text
        self.history.append({"role": "assistant", "content": output})
        self.symbols += output + "\n"
        return output
    
    def is_complete(self) -> bool:
        return "◾" in self.symbols
    
    def _legend(self) -> str:
        return "\n".join(line for line in self.system.splitlines() if " = " in line)

    def decode(self, problem: str) -> str:
        decode_prompt = (
            f"Problem:\n{problem}\n\n"
            f"Symbol legend:\n{self._legend()}\n\n"
            f"Symbolic program:\n{self.symbols}\n"
            "Translate this symbolic program into a plain-English answer to the problem."
        )
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{"role": "user", "content": decode_prompt}]
        )
        return response.content[0].text
    
    def reset(self):
        self.symbols = ""
        self.history = []
