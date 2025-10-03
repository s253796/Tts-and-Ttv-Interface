from transformers import pipeline
from app.utils.decorators import timeit, memoize

# base class (encapsulation: hides model details)
class BaseModel:
    def __init__(self, model_id, task):
        self._model_id = model_id
        self._task = task
        self._pipeline = None

    def load(self):
        if self._pipeline is None:
            self._pipeline = pipeline(self._task, model=self._model_id)
        return self._pipeline

    def run(self, x):
        pipe = self.load()
        return pipe(x)

# logging mixin for multiple inheritance
class LoggingMixin:
    def log(self, message):
        print("[LOG]:", message)

#tText model: multiple inheritance + method overriding
class TextModel(BaseModel, LoggingMixin):
    def __init__(self, model_id):
        super().__init__(model_id, task="text-classification")

    def run(self, text):
        self.log("Running text model")
        return super().run(text)

# Audio model: multiple decorators
class AudioModel(BaseModel):
    def __init__(self, model_id):
        super().__init__(model_id, task="automatic-speech-recognition")

    @timeit
    @memoize
    def run(self, audio_file):
        return super().run(audio_file)
