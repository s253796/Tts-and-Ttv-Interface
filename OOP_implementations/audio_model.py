from app.utils.decorators import timeit, memoize
from app.wrappers.base_models import BaseModel, LoggingMixin

class AudioModel(BaseModel, LoggingMixin):
    @timeit
    @memoize
    def run(self, audio_file):
        self.log(f"Processing audio file: {audio_file}")
        return super().run(audio_file)
