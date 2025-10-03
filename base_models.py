class BaseModel:
    def __init__(self, name):
        self._name = name  # encapsulation

    def run(self, x):
        print(f"{self._name} base run called with:", x)
        return f"{self._name} result"

class LoggingMixin:
    def log(self, message):
        print("[LOG]:", message)
