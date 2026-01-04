from movie_manager import view_movie
def book_ticket():
    movies = view_movie()
    if not movies:
        return

    try:
        choice = int(input("Select movie: "))
        tickets = int(input("Number of tickets: "))
        customer = input("Customer name: ")

        name, category, time, price, seats = movies[choice - 1].strip().split(",")
        seats = int(seats)

        if tickets > seats:
            print("❌ Not enough seats!")
            return

        total = tickets * int(price)
        movies[choice - 1] = f"{name},{category},{time},{price},{seats - tickets}\n"

        with open("MOVIE_FILE.txt", "w") as f:
            f.writelines(movies)

        with open("BOOKING_FILE.txt", "a") as f:
            f.write(f"{customer},{name},{tickets},{total}\n")

        print("✅ Booking successful! Total: Rs", total)
    except:
        print("❌ Invalid input!")
