Problem description

                     4.	Hotel Rooms

In a folder called project create two files: hotel.py and room.py
In the room.py file, create a class called Room. Upon initialization, it should receive
a number (int) and a capacity (int). It should also have an attribute called guests (0 by default)
and is_taken (False by default). The class should have 2 additional methods:
•	take_room(people) - if the room is not taken, and there is enough space, the guests 
take the room. Otherwise, the method should return "Room number {number} cannot be taken"
•	free_room() - if the room is taken, free it. Otherwise, return "Room number {number} is not taken"
In the hotel.py file, create a class called Hotel. Upon initialization, it should receive
a name (str). It should also have 2 more attributes: rooms (empty list of rooms) and 
guests (0 by default). The class should have 5 more methods:
•	from_stars(stars_count: int) - creates a new instance with name "{stars_count} stars Hotel"
•	add_room(room: Room) - adds the room to the list of rooms
•	take_room(room_number, people) - finds the room with that number and tries to 
accommodate the guests in the room
•	free_room(room_number) - finds the room with that number and tries to free it
•	status() - returns information about the hotel in the following format:
"Hotel {name} has {guests} total guests
Free rooms: {numbers of all free rooms separated by comma and space}
Taken rooms: {numbers of all taken rooms separated by comma and space}"



_______________________________________________
Example

Test Code	(no input data in this task)


from project.hotel import Hotel

from project.room import Room

hotel = Hotel.from_stars(5)


first_room = Room(1, 3)

second_room = Room(2, 2)

third_room = Room(3, 1)


hotel.add_room(first_room)

hotel.add_room(second_room)

hotel.add_room(third_room)

hotel.take_room(1, 4)

hotel.take_room(1, 2)

hotel.take_room(3, 1)

hotel.take_room(3, 1)

print(hotel.status())



_______________________________________________
Output

Hotel 5 stars Hotel has 3 total guests

Free rooms: 2

Taken rooms: 1, 3


_______________________________________________