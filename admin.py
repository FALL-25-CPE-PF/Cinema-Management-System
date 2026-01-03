from movie_manager import add_movie, view_movie, remove_movie, update_seats
admin_password = "admin123"
def admin_mode():
    password=input("Enter admin password: ")
    if password != admin_password:
        print("Incorrect password.")
        return
    while True:
        print("\n===== ADMIN MODE =====")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Remove Movie")
        print("4. Update Seats")
        print("5. View Bookings")
        print("6. Total Revenue")
        print("7. Logout")

        choice = input("Choice: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            view_movie()
        elif choice == "3":
            remove_movie()
        elif choice == "4":
            update_seats()
        # elif choice == "5":
        #     view_bookings()
        # elif choice == "6":
        #     total_revenue()
        elif choice == "7":
            print("Logging out of admin mode.")
            break
        else:
            print("Invalid option!")
