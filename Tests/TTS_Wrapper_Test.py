"""Basic test for text-to-speech model only"""
from TexttospeechWrap import SpeechT5TextToSpeech

def test_tts():
    print("Testing Text-to-Speech Model")
    tts = SpeechT5TextToSpeech()
    tts.load_model()
    
    if tts._is_loaded:
        audio_file = tts.generate_speech("Testing, testing one, two, three.", "test_audio.wav")
        print(f"Success! Audio saved as: {audio_file}")
    else:
        print("Failed to load TTS model")

if __name__ == "__main__":
    test_tts()