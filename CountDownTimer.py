import tkinter as tk
from tkinter import messagebox
import time
import threading

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        
        self.label = tk.Label(root, text="Enter time in seconds:", font=("Helvetica", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, width=20, font=("Helvetica", 12))
        self.entry.pack(pady=5)
        
        self.start_button = tk.Button(root, text="Start", command=self.start_timer, font=("Helvetica", 12))
        self.start_button.pack(pady=5)
        
        self.time_label = tk.Label(root, text="", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

    def start_timer(self):
        try:
            self.time_left = int(self.entry.get())
            if self.time_left < 0:
                raise ValueError("Time must be a non-negative integer.")
        except ValueError as e:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
            return
        
        self.entry.config(state='disabled')
        self.start_button.config(state='disabled')
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            minutes, seconds = divmod(self.time_left, 60)
            time_formatted = f"{minutes:02d}:{seconds:02d}"
            self.time_label.config(text=time_formatted)
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.time_label.config(text="Time's up!")
            messagebox.showinfo("Countdown Timer", "Time's up!")
            self.entry.config(state='normal')
            self.start_button.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    timer = CountdownTimer(root)
    root.mainloop()
