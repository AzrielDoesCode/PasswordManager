import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.geometry("400x300")
        
        # Start with the title screen
        self.show_title_screen()
    
    def show_title_screen(self):
        # Clear any existing widgets
        self.clear_frame()
        
        title_label = tk.Label(self, text="Welcome to Password Manager", font=("Arial", 16))
        title_label.pack(pady=20)
        
        start_button = tk.Button(self, text="Start", command=self.show_main_menu, width=10)
        start_button.pack(pady=10)
        
        quit_button = tk.Button(self, text="Quit", command=self.quit, width=10)
        quit_button.pack(pady=10)
    
    def show_main_menu(self):
        self.clear_frame()
        
        menu_label = tk.Label(self, text="Main Menu", font=("Arial", 14))
        menu_label.pack(pady=20)
        
        # Buttons for each function screen
        functions = [
            ("Create New Password", self.show_create_password_screen),
            ("View Saved Passwords", self.show_view_passwords_screen),
            ("Update Existing Password", self.show_update_password_screen),
            ("Delete Password", self.show_delete_password_screen),
            ("Generate Encryption Key", self.show_generate_key_screen),
            ("Load Encryption Key", self.show_load_key_screen)
        ]
        
        for func_name, func in functions:
            button = tk.Button(self, text=func_name, command=func, width=25)
            button.pack(pady=5)
    
    # Example function screens
    def show_create_password_screen(self):
        self.show_function_screen("Create New Password", "Create Password functionality goes here.")

    def show_view_passwords_screen(self):
        self.show_function_screen("View Saved Passwords", "Display Saved Passwords here.")

    def show_update_password_screen(self):
        self.show_function_screen("Update Existing Password", "Update Password functionality goes here.")

    def show_delete_password_screen(self):
        self.show_function_screen("Delete Password", "Delete Password functionality goes here.")

    def show_generate_key_screen(self):
        self.show_function_screen("Generate Encryption Key", "Generate Key functionality goes here.")

    def show_load_key_screen(self):
        self.show_function_screen("Load Encryption Key", "Load Key functionality goes here.")
    
    # Function screen template
    def show_function_screen(self, title, message):
        self.clear_frame()
        
        label = tk.Label(self, text=title, font=("Arial", 14))
        label.pack(pady=20)
        
        message_label = tk.Label(self, text=message, font=("Arial", 12))
        message_label.pack(pady=10)
        
        back_button = tk.Button(self, text="Back to Menu", command=self.show_main_menu, width=15)
        back_button.pack(pady=20)
    
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
