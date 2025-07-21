import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Initialize translator
translator = Translator()

# Create main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x400")
root.resizable(False, False)

# Language list
languages = list(LANGUAGES.values())
lang_keys = list(LANGUAGES.keys())


# translation = translator.translate("Hello", dest='fr')
# print(translation.text)

# Functions
def translate_text():
    try:
        src_lang = lang_keys[languages.index(source_lang.get())]
        dest_lang = lang_keys[languages.index(target_lang.get())]
        text = input_text.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Input Required", "Please enter text to translate.")
            return

        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# GUI Layout
tk.Label(root, text="Language Translator", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

# Source Language
tk.Label(frame, text="From:", font=("Arial", 12)).grid(row=0, column=0)
source_lang = ttk.Combobox(frame, values=languages, state="readonly", width=20)
source_lang.set("english")
source_lang.grid(row=0, column=1, padx=10)

# Target Language
tk.Label(frame, text="To:", font=("Arial", 12)).grid(row=0, column=2)
target_lang = ttk.Combobox(frame, values=languages, state="readonly", width=20)
target_lang.set("french")
target_lang.grid(row=0, column=3, padx=10)

# Text Boxes
input_text = tk.Text(root, height=7, width=70)
input_text.pack(pady=10)

translate_btn = tk.Button(root, text="Translate", font=("Arial", 12), command=translate_text)
translate_btn.pack(pady=5)

output_text = tk.Text(root, height=7, width=70)
output_text.pack(pady=10)

# Start GUI loop
root.mainloop()