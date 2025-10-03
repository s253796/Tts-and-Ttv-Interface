from typing import Dict, Any, Optional

# Wrapped models inside app/wrappers/
try:
    from app.wrappers.gpt2_text_generation_wrapped import GPT2TextGenerator
except Exception:
    GPT2TextGenerator = None

try:
    from app.wrappers.TexttospeechWrap import SpeechT5TextToSpeech
except Exception:
    SpeechT5TextToSpeech = None

try:
    from app.wrappers.TextToVideoWrap import CogVideoXGenerator
except Exception:
    CogVideoXGenerator = None


class ModelRunner:
    """
    Uniform return format for GUI:
      {"type":"text","text": "..."}
      {"type":"audio","path":"tts_output.wav"}
      {"type":"video","path":"ttv_output.mp4"}
      {"type":"image","image": <PIL.Image>}  # not used here
    """
    def __init__(self):
        self._txtgen: Optional[GPT2TextGenerator] = None
        self._tts:    Optional[SpeechT5TextToSpeech] = None
        self._ttv:    Optional[CogVideoXGenerator] = None

        self._models = [
            {"key": "txtgen", "name": "Text Generation (GPT-2)",      "task": "text-generation"},
            {"key": "tts",    "name": "Text → Speech (SpeechT5 TTS)", "task": "text-to-speech"},
            {"key": "ttv",    "name": "Text → Video (CogVideoX 2B)",  "task": "text-to-video"},
        ]

    # --- lazy loaders ---
    def _ensure_txtgen(self):
        if self._txtgen is None:
            if GPT2TextGenerator is None:
                raise RuntimeError("GPT2 wrapper not found. Check app/wrappers and imports.")
            self._txtgen = GPT2TextGenerator()
            self._txtgen.load_model()

    def _ensure_tts(self):
        if self._tts is None:
            if SpeechT5TextToSpeech is None:
                raise RuntimeError("SpeechT5 wrapper not found. Check app/wrappers and imports.")
            self._tts = SpeechT5TextToSpeech()
            self._tts.load_model()

    def _ensure_ttv(self):
        if self._ttv is None:
            if CogVideoXGenerator is None:
                raise RuntimeError("CogVideoX wrapper not found. Check app/wrappers and imports.")
            self._ttv = CogVideoXGenerator()
            self._ttv.load_model()

    # --- API for GUI ---
    def list_models(self):
        return self._models

    def describe(self, key: str) -> str:
        if key == "txtgen":
            return "Generates a continuation from your prompt using a GPT-2 wrapper (HF transformers)."
        if key == "tts":
            return "Converts text to speech using Microsoft SpeechT5 and saves a WAV file."
        if key == "ttv":
            return "Creates a short MP4 from a text prompt with CogVideoX (compute-heavy; GPU recommended)."
        return "Model details not found."

    def run(self, model_key: str, input_kind: str, text_value: str = "", file_path: str = None) -> Dict[str, Any]:
        if model_key == "txtgen":
            self._ensure_txtgen()
            if not text_value:
                return {"type": "text", "text": "Please enter a prompt for text generation."}
            out = self._txtgen.generate_text(prompt=text_value, max_length=80)
            return {"type": "text", "text": out}

        elif model_key == "tts":
            self._ensure_tts()
            if not text_value:
                return {"type": "text", "text": "Enter text to convert to speech (TTS)."}
            audio_path = self._tts.generate_speech(text_value, output_filename="tts_output.wav")
            if isinstance(audio_path, str) and audio_path.lower().endswith((".wav",".mp3",".flac",".ogg")):
                return {"type": "audio", "path": audio_path}
            return {"type": "text", "text": str(audio_path)}  # show error string

        elif model_key == "ttv":
            self._ensure_ttv()
            if not text_value:
                return {"type": "text", "text": "Enter a prompt to generate a short video."}
            video_path = self._ttv.generate_video(text_value, output_filename="ttv_output.mp4")
            if isinstance(video_path, str) and video_path.lower().endswith(".mp4"):
                return {"type": "video", "path": video_path}
            return {"type": "text", "text": str(video_path)}  # show error string

        return {"type": "text", "text": "Unknown model selection."}
