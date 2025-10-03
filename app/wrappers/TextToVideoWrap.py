from utils.decorators import timeit, memoize
from wrappers.base_models import BaseModel, LoggingMixin

class CogVideoXGenerator(BaseModel, LoggingMixin):
    """CogVideoX wrapper for text-to-video generation using diffusers"""
    
    def __init__(self):
        """Initialize text-to-video generator with default settings"""
        self.model_name = "THUDM/CogVideoX-2b"
        self._pipe = None
        self._is_loaded = False
    
    def load_model(self):
        """Load CogVideoX model with fallback for systems without dedicated GPU"""
        try: 
            from diffusers import CogVideoXPipeline
            import torch
        
            print("Loading text-to-video model...")
            self._pipe = CogVideoXPipeline.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16
            )
        
            # Check for CUDA availability
            if torch.cuda.is_available():
                self._pipe = self._pipe.to("cuda")
                print("Using GPU acceleration")
            else:
                print("Warning: No CUDA GPU detected. Video generation will be very slow.")
                print("Consider using a system with dedicated GPU for practical use.")
        
            self._is_loaded = True
        
        except Exception as e:
            print(f"Error loading video model: {e}")
            self._is_loaded = False
    @timeit
    @memoize
    def generate_video(self, prompt, output_filename="video_output.mp4"):
        """Generate video from text prompt and save as MP4 file"""
        if not self._is_loaded:
            return "Error: Model not loaded. Call load_model() first."
        try:
            from diffusers.utils import export_to_video
            import os
            from pathlib import Path
        
            # Save to app folder
            app_folder = Path(__file__).parent.parent
            full_path = os.path.join(app_folder, output_filename)
        
            print(f"Generating video... this may take over 30 min")
            print(f"Will save to: {full_path}")
        
            video = self._pipe(
                prompt=prompt,
                num_inference_steps=20,
                num_frames=25
            ).frames[0]
        
            export_to_video(video, full_path, fps=8)
        
            if os.path.exists(full_path):
                print(f"✓ Video saved at: {full_path}")
            else:
                print(f"✗ WARNING: Video file not found!")
            
            return full_path
        
        except Exception as e:
            print(f"Error: {e}")
            return f"Error generating video: {e}"
    
    def __str__(self):
        return f"CogVideoXGenerator(model={self.model_name}, loaded={self._is_loaded})"
