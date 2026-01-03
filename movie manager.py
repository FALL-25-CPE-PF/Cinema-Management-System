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
