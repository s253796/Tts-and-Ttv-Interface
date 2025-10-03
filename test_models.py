from app.wrappers.text_model import TextModel
from app.wrappers.audio_model import AudioModel

print("=== Testing TextModel ===")
text_model = TextModel("MyTextModel")
result_text = text_model.run("Hello world!")
print("Result:", result_text)

print("=== Testing AudioModel ===")
audio_model = AudioModel("MyAudioModel")
result_audio = audio_model.run("sample_audio.wav")
print("Result:", result_audio)

