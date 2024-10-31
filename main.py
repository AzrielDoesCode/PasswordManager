from cryptography.fernet import Fernet as Fn

class PasswordManager:
    def __init__(self):
        self.key = None 
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):  #instance method used : self represents the object of the class 'PasswordManager'
        self.key = Fn.generate_key() #Generated a key using library
        with open(path, 'wb') as f:
            f.write(self.key)

        print(self.key)

    def load_key(self, path):
        with open(pass,'rb') as f:
        self.key = f.read()

    def create_passfile(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None :
            for key, value in initial_values.items():
                pass #hmm DO later ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def load_passfile(self, path):
        self.password_file = path
        
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encoded()).decode()

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:  #contains some data
            with open (self.password_file, 'a') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(sit + ":" + encrypted.decode() +  "\n")

    def get_pass(self,):
        return self.password_dict.get[site]

def main():
    password = {
        "email": "1234567",
        "facebook": "1357913",
        "github": "9876543"
        "youtube": "myyoutubepass"

        }     
    pm = PasswordManager()

    print("""what do you want to do ?
          1. Create a new key
          2. Load a Key
          3. Create new pass file
          4. Load old pass file
          5. Add a pass
          6. Get a pass
          q  Quit

          """)
    
    done = False

    while not done:
        choice = input("Enter your choice: ")
        if choice == "1" :
            path = input ("Enter the path to save the key: ")
            pm.create_key(path)

        elif choice == "2":
            path = input ("Enter the path to load the key: ")
            pm.load_key(path)

        elif choice == "3":
                path = input ("Enter the path to save the pass file: ")
                pm.create_passfile(path, initial_values=password)

        elif choice == "4":
            path = input ("Enter the path to load the pass file: ")
            pm.load_passfile(path)

        elif choice == "5":
            site = input("Enter the site name: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)

        elif choice == "6":
            site = input("Enter the site name: ")
            print(f"Password for {site} is {pm.get_pass(site)}")

        elif choice == "q":
            done = True
            print("Bye")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()  

pm.create_key("mykey.key")  #PASSING THE FILE used for Path var


'''
def gen_key():
    key = Fn.generate_key()
    with open("secret.key", "wb") as key_file:
        return key
'''