from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    @property
    def calculate_total_population(self):
        return sum(room.members_count for room in self.rooms)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum(room.total_expenses for room in self.rooms)
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        room_result = [self.__pay_for_room(room) for room in self.rooms]
        return '\n'.join(room_result)

    def status(self):
        return f"Total population: {self.calculate_total_population}\n" + \
               "\n".join(room.__repr__() for room in self.rooms)

    def __pay_for_room(self, room: Room):
        if room.budget < room.total_expenses:
            self.__remove_room(room)
            return f"{room.family_name} does not have enough budget and must leave the hotel."
        room.budget -= room.total_expenses
        return f"{room.family_name} paid {room.total_expenses:.2f}$ and have {room.budget:.2f}$ left."

    def __remove_room(self, room):
        self.rooms.remove(room)


