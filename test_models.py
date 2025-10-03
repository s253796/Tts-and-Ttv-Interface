# test_models.py
from models import TextModel, AudioModel

# Small test text for the TextModel
test_text = "I really enjoy learning AI and Python!"

# Initialize TextModel
text_model = TextModel("distilbert/distilbert-base-uncased-finetuned-sst-2-english")
print("Running TextModel...")
text_result = text_model.run(test_text)
print("TextModel result:", text_result)
print("-" * 40)

# Small test audio for AudioModel
# Replace 'sample_audio.wav' with a small audio file you have
audio_file = "sample_audio.wav"

audio_model = AudioModel("openai/whisper-small")
print("Running AudioModel...")
try:
    audio_result = audio_model.run(audio_file)
    print("AudioModel result:", audio_result)
except FileNotFoundError:
    print(f"Audio file '{audio_file}' not found. Please add a small .wav file to test.")
