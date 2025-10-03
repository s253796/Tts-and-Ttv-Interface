from utils.decorators import timeit, memoize
from wrappers.base_models import BaseModel, LoggingMixin

class SpeechT5TextToSpeech(BaseModel, LoggingMixin):
    """SpeechT5 wrapped for easier access using enapsulation methods"""
    
    def __init__(self):
        """Initialize text-to-speech generator with default settings"""
        self.model_name = "microsoft/speecht5_tts"
        self._pipe = None
        self._speaker_embedding = None
        self._is_loaded = False
    
    def load_model(self):
        """Load SpeechT5 model pipeline and speaker embeddings"""
        try:
            from transformers import pipeline
            from datasets import load_dataset
            import torch

            print("Loading text-to-speech model...")
            
            self._pipe = pipeline("text-to-speech", model=self.model_name)
            embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
            self._speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
            self._is_loaded = True
            print("Text-to-speech model loaded successfully")
        except Exception as e:
            print(f"Error loading text-to-speech model: {e}")
            self._is_loaded = False
    @timeit
    @memoize
    def generate_speech(self, text, output_filename="audio_output.wav"):
        """Generate speech from text and save as audio file"""
        if not self._is_loaded:
            return "Error: Model not loaded. Call load_model() first."
        try:
            import soundfile as sf
            import os
            from pathlib import Path
        
            # Save to app folder (where main.py is)
            app_folder = Path(__file__).parent.parent
            full_path = os.path.join(app_folder, output_filename)

            print(f"Attempting to save file to: {full_path}")
        
            speech = self._pipe(text, forward_params={"speaker_embeddings": self._speaker_embedding})
        
            print(f"Audio generated successfully")
        
            sf.write(full_path, speech["audio"], samplerate=speech["sampling_rate"])
        
            print(f"sf.write() completed")
        
            if os.path.exists(full_path):
                print(f"✓ File confirmed at: {full_path}")
            else:
                print(f"✗ WARNING: File not found after writing!")
            
            return full_path
        except Exception as e:
            print(f"Error: {e}")
            return f"Error generating speech: {e}"
    
    def __str__(self):
        return f"SpeechT5TextToSpeech(model={self.model_name}, loaded={self._is_loaded})"