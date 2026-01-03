def add_movie():
    name = input("Movie name: ")
    category = input("Category: ")
    time = input("Show time: ")
    price = input("Ticket price: ")
    seats = input("Available seats: ")

    with open("MOVIE_FILE.txt", "a") as f:
        f.write(f"{name},{category},{time},{price},{seats}\n")

    print("✅ Movie added successfully!")
