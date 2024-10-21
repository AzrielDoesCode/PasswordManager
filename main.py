from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.key = None 
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()  # Generate a key using the library
        with open(path, 'wb') as f:
            f.write(self.key)

        print(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:  # Corrected 'pass' to 'path'
            self.key = f.read()

    def create_passfile(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            with open(path, 'w') as f:  # Open file to write initial values
                for key, value in initial_values.items():
                    encrypted = Fernet(self.key).encrypt(value.encode())
                    f.write(f"{key}:{encrypted.decode()}\n")  # Write encrypted password

    def load_passfile(self, path):
        self.password_file = path
        
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()  # Changed 'encoded()' to 'encode()'

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:  # Check if the password file exists
            with open(self.password_file, 'a') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(f"{site}:{encrypted.decode()}\n")  # Fixed 'sit' to 'site'

    def get_pass(self, site):  # Added 'site' parameter to the method
        return self.password_dict.get(site)

def main():
    password = {
        "email": "1234567",
        "facebook": "1357913",
        "github": "9876543",
        "youtube": "myyoutubepass"  # Added a comma here
    }     
    pm = PasswordManager()

    print("""What do you want to do?
          1. Create a new key
          2. Load a Key
          3. Create new pass file
          4. Load old pass file
          5. Add a pass
          6. Get a pass
          q  Quit
          """)
    
