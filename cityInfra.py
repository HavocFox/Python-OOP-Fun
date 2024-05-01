class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.party = []
        self.partycount = 0

    def add_participant(self, partygoer):
        if isinstance(self, Event):
            print(f"Adding {partygoer} to {self.name}'s list of participants. ")
            self.party.append(partygoer)
            self.partycount = self.partycount + 1

    def get_participant_count(self):
        print(f"There are {self.partycount} participants in {self.name}'s list.")


Aiden = Event(name = "Aiden", date = "10/12/2020")
Norm = Event(name = "Norm", date = "01/17/2021")
Emma = Event(name = "Emma", date = "04/15/2025")
Liam = Event(name = "Liam", date = "11/19/2012")
Olivia = Event(name = "Olivia", date = "11/12/2022")
William = Event(name = "William", date = "12/13/2021")

Aiden.add_participant("Norm")
Aiden.add_participant("Emma")
Norm.add_participant("Liam")
Aiden.add_participant("Olivia")
Norm.add_participant("William")

print("\n")
Aiden.get_participant_count()
Norm.get_participant_count()