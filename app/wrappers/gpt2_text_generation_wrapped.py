class GPT2TextGenerator:
    """A wrapper class for GPT2 text generation"""
    def __init__(self):
        """Default settings for text generator"""
        self.model_name = "openai-community/gpt2"
        self.pipe = None
        self.is_loaded = False

    def load_model (self):
        """Load GPT2 model pipeline for text generation."""
        try:
            from transformers import pipeline
            self.pipe = pipeline("text-generation", model=self.model_name)
            self.is_loaded = True
        except Exception as e:
            print(f"Error loading model: {e}")
            self.is_loaded = False

    def generate_text(self, prompt, max_length=50):
        """Generate text from prompt with max of 50 tokens"""
        if not self.is_loaded:
            return "Error: Model not loaded. Call load_model() first."
        try:
            result = self.pipe(prompt, max_length=max_length)
            return result[0]['generated_text']
        except Exception as e:
            return f"Error generating text: {e}"
        # debugging
    def __str__(self):
        return f"GPT2TextGenerator(model={self.model_name}, loaded={self.is_loaded})"