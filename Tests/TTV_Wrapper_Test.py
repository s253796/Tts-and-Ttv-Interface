"""Basic test for text-to-video model only: By default video generation on this is not enabled to avoid accidentally using a lot of time and resource to make video"""
from TextToVideoWrap import CogVideoXGenerator

def test_ttv():
    print("Testing Text-to-Video Model")
    print("WARNING: Video generation can well exceed 30 minutes depending on GPU")
    ttv = CogVideoXGenerator()
    ttv.load_model()
    
    if ttv._is_loaded:
        # Uncomment below lines to generate test. Video generation can take a long time and use heavy resources.
        # video_file = ttv.generate_video("Fish jumps out of bowl", "test_video.mp4")
        # print(f"Success! Video saved as: {video_file}")
        print("Test model loaded successfully- uncomment video file lines to generate video.")
    else:
        print("Failed to load TTV model")

if __name__ == "__main__":
    test_ttv()