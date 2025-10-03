import tkinter as tk
from tkinter import ttk, messagebox
from views import InputPanel, ModelPanel, OutputPanel, InfoPanel, OOPPanel
from controllers.model_runner import ModelRunner

def launch_app():
    root = tk.Tk()
    root.title("HIT137 AI Demo")
    root.geometry("1000x680")

    runner = ModelRunner()

    # Layout
    body = ttk.Frame(root, padding=10)
    body.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    left = ttk.Frame(body)
    left.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
    right = ttk.Frame(body)
    right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Widgets (left)
    input_panel = InputPanel(left);                 input_panel.pack(fill=tk.X, pady=6)
    model_panel = ModelPanel(left, runner.list_models()); model_panel.pack(fill=tk.X, pady=6)
    info_panel  = InfoPanel(left);                  info_panel.pack(fill=tk.X, pady=6)
    oop_panel   = OOPPanel(left);                   oop_panel.pack(fill=tk.BOTH, expand=True, pady=6)

    # Widgets (right)
    output_panel = OutputPanel(right);              output_panel.pack(fill=tk.BOTH, expand=True, pady=6)

    # Actions
    def on_run():
        try:
            model_key = model_panel.get_selected_model()
            input_kind, text_value, file_path = input_panel.get_input()
            result = runner.run(model_key, input_kind, text_value, file_path)
            output_panel.show(result)
            info_panel.set_text(runner.describe(model_key))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    model_panel.bind_run(on_run)
    root.mainloop()
