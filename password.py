import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Password Generator")

        # Variables to store user input
        self.length_var = tk.StringVar()  # Variable to hold password length
        self.result_var = tk.StringVar()  # Variable to hold generated password
        self.use_lowercase_var = tk.BooleanVar()  # Checkbox for lowercase letters
        self.use_uppercase_var = tk.BooleanVar()  # Checkbox for uppercase letters
        self.use_digits_var = tk.BooleanVar()     # Checkbox for digits
        self.use_symbols_var = tk.BooleanVar()    # Checkbox for symbols

        # Set default values
        self.length_var.set("12")  # Default password length
        self.use_lowercase_var.set(True)  # Default to include lowercase letters
        self.use_uppercase_var.set(True)  # Default to include uppercase letters
        self.use_digits_var.set(True)     # Default to include digits
        self.use_symbols_var.set(True)    # Default to include symbols

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Password Length
        label_length = tk.Label(self.master, text="Password Length:", font=("Arial", 14))
        entry_length = tk.Entry(self.master, textvariable=self.length_var, font=("Arial", 14))
        label_length.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_length.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Character Set Checkboxes
        checkbox_lower = tk.Checkbutton(self.master, text="Lowercase", variable=self.use_lowercase_var, font=("Arial", 14))
        checkbox_upper = tk.Checkbutton(self.master, text="Uppercase", variable=self.use_uppercase_var, font=("Arial", 14))
        checkbox_digits = tk.Checkbutton(self.master, text="Digits", variable=self.use_digits_var, font=("Arial", 14))
        checkbox_symbols = tk.Checkbutton(self.master, text="Symbols", variable=self.use_symbols_var, font=("Arial", 14))

        checkbox_lower.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        checkbox_upper.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        checkbox_digits.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        checkbox_symbols.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Generate and Copy Buttons
        button_generate = tk.Button(self.master, text="Generate Password", command=self.generate_password, font=("Arial", 14))
        button_copy = tk.Button(self.master, text="Copy to Clipboard", command=self.copy_to_clipboard, font=("Arial", 14))

        button_generate.grid(row=3, column=0, columnspan=2, pady=10)
        button_copy.grid(row=4, column=0, columnspan=2, pady=5)

        # Result Entry
        label_result = tk.Label(self.master, text="Generated Password:", font=("Arial", 14))
        entry_result = tk.Entry(self.master, textvariable=self.result_var, state="readonly", font=("Arial", 14))

        label_result.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        entry_result.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        # Set focus to password length entry upon startup
        entry_length.focus()

    def generate_password(self):
        # Get password length from the entry
        password_length = self.length_var.get()

        # Validate if the entered value is a positive integer and not too long
        try:
            password_length = int(password_length)
            if password_length <= 0:
                raise ValueError
            if password_length > 1000:  # Maximum reasonable length
                raise ValueError("Password length too long")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for password length.")
            return

        # Build the character set based on selected checkboxes
        characters = ""
        if self.use_lowercase_var.get():
            characters += string.ascii_lowercase
        if self.use_uppercase_var.get():
            characters += string.ascii_uppercase
        if self.use_digits_var.get():
            characters += string.digits
        if self.use_symbols_var.get():
            characters += string.punctuation

        # Check if at least one character set is selected
        if not characters:
            messagebox.showerror("Error", "Please select at least one character set.")
            return

        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(password_length))
        self.result_var.set(password)

    def copy_to_clipboard(self):
        # Copy the generated password to the clipboard
        password = self.result_var.get()
        if password:
            try:
                pyperclip.copy(password)
                messagebox.showinfo("Success", "Password copied to clipboard!")
            except pyperclip.PyperclipException:
                messagebox.showerror("Error", "Copying to clipboard failed. Please try again.")
        else:
            messagebox.showerror("Error", "No password generated to copy.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
