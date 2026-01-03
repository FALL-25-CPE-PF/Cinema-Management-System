#------------ADD MOVIES------------------#
def add_movie():
    name = input("Movie name: ")
    category = input("Category: ")
    time = input("Show time: ")
    price = input("Ticket price: ")
    seats = input("Available seats: ")

    with open("MOVIE_FILE.txt", "a") as f:
        f.write(f"{name},{category},{time},{price},{seats}\n")

    print("✅ Movie added successfully!")

#----------VIEW MOVIES-----------------#
def view_movie():
    try:
        with open("MOVIE_FILE.txt","r") as f:
            movies = f.readlines()
        if not movies:
            print("Currently No Movies Available")
            return movies
        print("\n--- AVAILABLE MOVIES ---")
        for i, m in enumerate(movies, start=1):
            name, category, time, price, seats = m.strip().split(",")
            print(f"{i}. {name} | {category} | {time} | Rs {price} | Seats: {seats}")
        return movies
    except FileNotFoundError:
        print("System Hacked all data Deleted!!!")

#-----------REMOVE MOVIES----------------#
def remove_movie():
    movies = view_movie()
    if not movies:
        return

    try:
        choice = int(input("Enter movie number to remove: "))
        movies.pop(choice - 1)

        with open("MOVIE_FILE.txt", "w") as f:
            f.writelines(movies)

        print("✅ Movie removed successfully!")
    except:
        print("❌ Invalid input!")
#-----------UPDATE SEATS-----------------#
def update_seats():
    movies = view_movie()
    if not movies:
        return

    try:
        choice = int(input("Select movie number: "))
        change = int(input("Seats -(number) or +(number): "))

        data = movies[choice - 1].strip().split(",")
        seats = int(data[4]) + change

        if seats < 0:
            print("❌ Seats cannot be negative!")
            return

        data[4] = str(seats)
        movies[choice - 1] = ",".join(data) + "\n"

        with open("MOVIE_FILE.txt", "w") as f:
            f.writelines(movies)

        print("✅ Seats updated!")
    except:
        print("❌ Invalid input!")
