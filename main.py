import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyshorteners
import clipboard
import webbrowser

class UrlShortenerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('URL Shortener')
        self.root.geometry('600x400')
        self.root.configure(bg='#f0f0f0')

        self.style = ttk.Style()
        self.style.theme_use('clam')  # You can experiment with different ttk themes

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.title_label = ttk.Label(self.frame, text="URL Shortener", font=('Helvetica', 24, 'bold'), foreground="#333333")
        self.title_label.pack(pady=(20, 10))

        self.url_label = ttk.Label(self.frame, text="Paste Your URL Here:", font=('Helvetica', 12, 'bold'))
        self.url_label.pack(anchor='w')

        self.url_entry = ttk.Entry(self.frame, font=('Helvetica', 12), width=50)
        self.url_entry.pack(anchor='w', pady=(0, 10))

        self.create_button = ttk.Button(self.frame, text="Create Short URL", command=self.create, style='My.TButton')
        self.create_button.pack(anchor='w', pady=(0, 10))

        self.short_url_label = ttk.Label(self.frame, text="Shortened URL:", font=('Helvetica', 12, 'bold'))
        self.short_url_label.pack(anchor='w')

        self.short_url_entry = ttk.Entry(self.frame, font=('Helvetica', 12, 'bold'), foreground="#512DA8")
        self.short_url_entry.pack(anchor='w', pady=(0, 10))

        self.copy_button = ttk.Button(self.frame, text="Copy", command=self.copy_to_clipboard, style='My.TButton')
        self.copy_button.pack(side='left', padx=(0, 10))

        self.visit_button = ttk.Button(self.frame, text="Visit Short URL", command=self.visit_short_url, style='My.TButton')
        self.visit_button.pack(side='left')

        self.clear_button = ttk.Button(self.root, text="Clear", command=self.clear, style='My.TButton')
        self.clear_button.pack(pady=10)

        self.style.configure('My.TButton', font=('Helvetica', 10, 'bold'), foreground="white", background="#512DA8")
        
        self.root.mainloop()

    def create(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please paste a URL.")
            return

        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        self.short_url_entry.delete(0, tk.END)
        self.short_url_entry.insert(tk.END, short_url)

    def copy_to_clipboard(self):
        short_url = self.short_url_entry.get()
        clipboard.copy(short_url)

    def visit_short_url(self):
        short_url = self.short_url_entry.get()
        webbrowser.open(short_url)

    def clear(self):
        self.url_entry.delete(0, tk.END)
        self.short_url_entry.delete(0, tk.END)

if __name__ == '__main__':
    UrlShortenerApp()
