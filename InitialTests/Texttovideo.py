import torch
from diffusers import CogVideoXPipeline
from diffusers.utils import export_to_video

print(f"CUDA available: {torch.cuda.is_available()}")
print(f"GPU name: {torch.cuda.get_device_name()}")

pipe = CogVideoXPipeline.from_pretrained(
    "THUDM/CogVideoX-2b",
    torch_dtype=torch.float16
)

# Explicitly move pipeline to GPU
pipe = pipe.to("cuda")

print(f"Pipeline device: {pipe.device}")
print("Starting generation...")

video = pipe(
    prompt="A cat", 
    num_inference_steps=20,
    num_frames=25
).frames[0]

print("Generation complete!")

export_to_video(video, "cat_video.mp4", fps=8)
print("Video saved as cat_video.mp4")
