from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms: [Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.room_cost + room.expenses

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        message = []
        rooms_to_remove = []
        for room in self.rooms:
            total_cost = room.room_cost + room.expenses

            if total_cost <= room.budget:
                room.budget -= total_cost
                message.append(f"{room.family_name} paid {total_cost:.2f}$ and have {room.budget:.2f}$ left.")

            else:
                rooms_to_remove.append(room)
                message.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        if rooms_to_remove:
            [self.rooms.remove(r) for r in rooms_to_remove]

        return '\n'.join(message)

    def status(self):
        message = [f"Total population: {sum(r.members_count for r in self.rooms)}"]

        for room in self.rooms:
            message.append(f"{room.family_name} with {room.members_count} members."
                           f" Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")

            for n, c in enumerate(room.children):
                cost_for_one_month = c.get_monthly_expense()
                message.append(f"--- Child {n + 1} monthly cost: {cost_for_one_month:.2f}$")

            appliances = sum(a.get_monthly_expense() * room.members_count for a in room.appliances)
            message.append(f"--- Appliances monthly cost: {appliances:.2f}$")

        return "\n".join(message)
