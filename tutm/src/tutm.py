import tkinter as tk
from tkinter import scrolledtext
import logging
from scapy.layers import *

class LogViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Log Viewer")

        # Create a scrolled text widget to display logs
        self.log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
        self.log_text.pack(padx=10, pady=10)

        # Configure logging to redirect logs to the GUI
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        #logging.basicConfig(filename='utm_log.txt', level=logging.INFO)
        self.log_handler = TextHandler(self.log_text)
        logging.getLogger().addHandler(self.log_handler)

def main():
    root = tk.Tk()
    app = LogViewerApp(root)
    root.mainloop()

class TextHandler(logging.Handler):
    def __init__(self, widget):
        logging.Handler.__init__(self)
        self.widget = widget

    def emit(self, record):
        msg = self.format(record)
        self.widget.insert(tk.END, msg + '\n')
        self.widget.yview(tk.END)  # Auto-scroll to the bottom

if __name__ == "__main__":
    main()
