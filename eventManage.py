class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

        reg_num = 0
        type = "default"
        owner = "default"

    def update_owner(self, new_owner):
        Vehicle.owner = new_owner
        print(f"The new owner of the {self.type} is now {new_owner}.")


Vanny = Vehicle(reg_num = 1090, type = "Honda Odyssey", owner = "Vanessa")
Cabby = Vehicle(reg_num = 2468, type = "Toyota Corolla", owner = "Chris")
Fleetmaster = Vehicle(reg_num = 7890, type = "Chevrolet Suburban", owner = "Emily")
Rogue = Vehicle(reg_num = 6423, type = "Nissan Altima", owner = "Michael")


van_own = input(f"Please enter the new owner of the {Vanny.type}. ")
Vanny.update_owner(van_own)
cab_own = input(f"Please enter the new owner of the {Cabby.type}. ")
Cabby.update_owner(cab_own)
fleet_own = input(f"Please enter the new owner of the {Fleetmaster.type}. ")
Fleetmaster.update_owner(fleet_own)
rog_own = input(f"Please enter the new owner of the {Rogue.type}. ")
Rogue.update_owner(rog_own)