import tkinter as tk
from tkinter import ttk, filedialog

class InputPanel(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Input")
        self.input_kind = tk.StringVar(value="Text")
        self.text = tk.Text(self, height=6, width=44)
        self.file_path = tk.StringVar(value="")

        ttk.Label(self, text="Type:").grid(row=0, column=0, sticky="w")
        ttk.OptionMenu(self, self.input_kind, "Text", "Text", "Image", "Audio").grid(row=0, column=1, sticky="ew")

        ttk.Label(self, text="Text / Prompt:").grid(row=1, column=0, sticky="w")
        self.text.grid(row=2, column=0, columnspan=2, sticky="ew", pady=4)

        def choose_file():
            path = filedialog.askopenfilename()
            if path:
                self.file_path.set(path)

        ttk.Button(self, text="Choose File", command=choose_file).grid(row=3, column=0, sticky="w")
        ttk.Label(self, textvariable=self.file_path, wraplength=260).grid(row=3, column=1, sticky="w")

        for i in range(2): self.columnconfigure(i, weight=1)

    def get_input(self):
        return self.input_kind.get(), self.text.get("1.0","end").strip(), (self.file_path.get() or None)

class ModelPanel(ttk.LabelFrame):
    def __init__(self, master, models):
        super().__init__(master, text="Model")
        self._cb = None
        names = [m["name"] for m in models]
        self._key_by_name = {m["name"]: m["key"] for m in models}

        ttk.Label(self, text="Select:").grid(row=0, column=0, sticky="w")
        self.model_combo = ttk.Combobox(self, values=names, state="readonly", width=35)
        if names: self.model_combo.set(names[0])
        self.model_combo.grid(row=0, column=1, sticky="ew")

        run_btn = ttk.Button(self, text="Run", command=self._run_clicked)
        run_btn.grid(row=1, column=0, columnspan=2, pady=8)

        self.columnconfigure(1, weight=1)

    def get_selected_model(self):
        return self._key_by_name.get(self.model_combo.get())

    def bind_run(self, cb): self._cb = cb
    def _run_clicked(self): 
        if self._cb: self._cb()

class OutputPanel(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Output")
        self.label = tk.Label(self, anchor="nw", justify="left")
        self.label.pack(fill=tk.BOTH, expand=True)
        self.text = tk.Text(self, height=16)
        self.text.pack(fill=tk.BOTH, expand=True)

    def show(self, result: dict):
        typ = result.get("type")
        if typ == "text":
            self.label.config(image=""); self.label.image = None
            self.text.delete("1.0","end"); self.text.insert("1.0", result.get("text",""))
        elif typ == "image":
            self.text.delete("1.0","end"); self.text.insert("1.0","[image output displayed here]")
        elif typ == "audio":
            self.text.delete("1.0","end")
            self.text.insert("1.0", f"Audio saved at: {result.get('path')}\nOpen it to play.")
        elif typ == "video":
            self.text.delete("1.0","end")
            self.text.insert("1.0", f"Video saved at: {result.get('path')}\nOpen it to preview.")
        else:
            self.text.delete("1.0","end"); self.text.insert("1.0","No output.")

class InfoPanel(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Model Info")
        self.tv = tk.Text(self, height=7, width=44, wrap="word")
        self.tv.pack(fill=tk.BOTH, expand=True)

    def set_text(self, s:str):
        self.tv.delete("1.0","end"); self.tv.insert("1.0", s)

class OOPPanel(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="OOP Explanation (short)")
        msg = (
            "- Inheritance: custom frames extend tkinter base classes\n"
            "- Polymorphism: one run handler works for different models\n"
            "- Encapsulation: ModelRunner hides model details from GUI\n"
            "- Overriding: adapters override base processing methods\n"
            "- Decorators: (OOP lane) add logging/validation around calls\n"
        )
        self.text = tk.Text(self, height=8, width=44, wrap="word")
        self.text.insert("1.0", msg)
        self.text.pack(fill=tk.BOTH, expand=True)
