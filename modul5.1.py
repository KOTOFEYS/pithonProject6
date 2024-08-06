class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        self.new_floor = new_floor
        floor = 1
        while floor <= new_floor:
            if self.number_of_floors < new_floor or new_floor < 1:
                print("Такого этажа не существует")
                break
            else:
                print(floor)
                floor += 1



h1 = House('ЖК Горский', 30)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)