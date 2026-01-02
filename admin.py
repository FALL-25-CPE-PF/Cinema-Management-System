from config import admin_password
def admin_mode():
    password=input("Enter admin password: ")
    if password != admin_password:
        print("Incorrect password.")
        return
   