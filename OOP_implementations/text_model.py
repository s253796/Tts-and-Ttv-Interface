from app.utils.decorators import timeit, memoize
from app.wrappers.base_models import BaseModel, LoggingMixin

class TextModel(BaseModel, LoggingMixin):
    def __init__(self, name):
        super().__init__(name)

    @timeit
    @memoize
    def run(self, text):
        self.log("Running TextModel")
        return super().run(text)
