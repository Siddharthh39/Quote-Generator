import tkinter as tk
from tkinter import messagebox
import random

# List of quotes
quotes = [
    "Believe you can and you're halfway there. -Theodore Roosevelt",
    "The only way to do great work is to love what you do. -Steve Jobs",
    "Don't let yesterday take up too much of today. -Will Rogers",
    "You are never too old to set another goal or to dream a new dream. -C.S. Lewis",
    "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. -Winston Churchill"
]

def generate_quote():
    # Select a random quote
    random_quote = random.choice(quotes)

    # Display the random quote in a message box
    messagebox.showinfo("Random Quote", random_quote)

# Create the main window
root = tk.Tk()
root.title("Random Quote Generator")

# Define geometry and set minimum and maximum sizes
root.geometry("400x200")
root.minsize(300, 150)
root.maxsize(800, 400)

# Create a button to generate a random quote
generate_button = tk.Button(root, text="Generate Random Quote", command=generate_quote)
generate_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Run the Tkinter event loop
root.mainloop()
