import json

class Storage:
    
    def __init__(self, filename="src/storage/history.json"):
        self.filename = filename

    def save(self, data: dict) -> None:
        history = self.load()
        history.append(data)
        with open(self.filename, "w") as file:
            json.dump(history, file, indent=4)

    def load(self) -> list:
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
