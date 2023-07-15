import parso
from tkinter import filedialog, messagebox, scrolledtext
import tkinter as tk

def format_code():
    try:
        source_code = original_text.get(1.0, tk.END)
        module = parso.parse(source_code)
        formatted_code = module.get_code()
        formatted_text.delete(1.0, tk.END)
        formatted_text.insert(tk.END, formatted_code)
    except Exception as e:
        messagebox.showerror('Error', f"Error while formatting code: {e}")

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(file_path, 'r') as file:
        code = file.read()
    original_text.delete(1.0, tk.END)
    original_text.insert(tk.END, code)

root = tk.Tk()
root.title("Python Code Formatter")

load_file_button = tk.Button(root, text="Load Python File", command=load_file)
load_file_button.pack()

format_code_button = tk.Button(root, text="Format Code", command=format_code)
format_code_button.pack()

original_label = tk.Label(root, text="Original Code")
original_label.pack()
original_text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
original_text.pack()

formatted_label = tk.Label(root, text="Formatted Code")
formatted_label.pack()
formatted_text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
formatted_text.pack()

root.mainloop()
