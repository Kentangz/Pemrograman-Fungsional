import matplotlib.pyplot as plt

# akun
# nama user : pass : pass user
users = {
    "nana": {"password": "nana123"},
    "nini": {"password": "nini123"},
    "nunu": {"password": "nunu123"},
    "nene": {"password": "nene123"},
    "nono": {"password": "nono123"}
}
# data film
# nama film, genre, waktu tayang, tiket
events =[
    ("Interstellar", "Drama", "2024-10-01 19:00", 15),
    ("Barbie", "Pop", "2024-10-05 20:00", 25),
    ("The Raid", "Action", "2024-10-10 18:30", 20),
    ("Avatar", "Sci-fi", "2024-10-15 21:00", 20),
    ("5cm/s","Anime","2024-10-15 21:00",30)
]

# bookingan user
# nama user: film, atas nama
bookings = {
    
    "nana": [
        {"event": events[1], "name": "kim satria"},
        {"event": events[2], "name": "kevin ferduz"},
        {"event": events[3], "name": "nana"}
    ],
    "nini": [
        {"event": events[1], "name": "nini"},
        {"event": events[1], "name": "adel"},
        {"event": events[3], "name": "flora"},
        {"event": events[3], "name": "nabila"}
    ],
    "nunu": [
        {"event": events[2], "name": "alex"},
        {"event": events[2], "name": "jhon burhan"}
    ],
    "nene": [
        {"event": events[4], "name": "nene"},
        {"event": events[4], "name": "lala"},
        {"event": events[4], "name": "lili"},
        {"event": events[4], "name": "lulu"},
        {"event": events[4], "name": "lele"},
        {"event": events[4], "name": "lolo"},
        {"event": events[4], "name": "slamet"}

    ],
    "nono": [
        {"event": events[0], "name": "david"},
        {"event": events[2], "name": "frank"}
    ]
}

# extract film, ticket 
import matplotlib.pyplot as plt
# extract film, ticket
film = [event[0] for event in events]
ticket = [event[3] for event in events]

# user ticket count
user_labels = list(bookings.keys())
user_ticket_count = [len(bookings[user]) for user in user_labels]

#users booked each film
film_booking_count = {film_name: sum(1 for user in bookings for booking in bookings[user] if booking["event"][0] == film_name) for film_name in film}


plt.figure(figsize=(15,8))

# Line plot
plt.subplot(1, 2, 1)
plt.title("Number of Bookings per Film")
plt.ylim([0,10])
plt.plot(film, film_booking_count.values(), linestyle='-', color='blue')
plt.xlabel("Film")
plt.ylabel("Number of Bookings")
plt.grid(True)

# Scatter plot for number of bookings per film
plt.subplot(2, 2, 4)
plt.title("Tickets Available per Film")
size = 150
plt.scatter(film, ticket,s=size, color='purple')
plt.xlabel("Film")
plt.ylabel("Tickets Available")
plt.grid(True)

# Pie chart for tickets booked by each user
plt.subplot(2, 2, 2)
plt.title("Tickets Booked by User")
explode = [0, 0, 0, 0.1, 0]
plt.pie(user_ticket_count, labels=user_labels,shadow=True, autopct='%1.0f%%',explode=explode, startangle=90)

# Show the plot
plt.tight_layout()
plt.show()