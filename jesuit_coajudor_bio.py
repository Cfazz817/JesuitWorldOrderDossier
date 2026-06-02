from dataclasses import dataclass, field, asdict
import json

@dataclass
class BriefBiography:
    name: str
    education: list = field(default_factory=list)
    religion: list = field(default_factory=list)
    occupations: list = field(default_factory=list)
    alive: bool = field(default=False)
    date_of_birth: str = field(default_factory=str)
    locale_of_origin: str = field(default_factory=str)
    locales_of_operation: list = field(default_factory=list)
    known_for: list = field(default_factory=list)
    jesidue_class_attributes: list = field(default_factory=list)
    orders_knighthoods: list = field(default_factory=lambda: ['none'])

    @staticmethod
    def load_from_json(filepath: str):
        with open(filepath, 'r') as f:
            data = json.load(f)
        return [BriefBiography(**item) for item in data]

    @staticmethod
    def save_to_json(bios: list, filepath):
        list_of_dicts = [asdict(bio) for bio in bios]
        with open(filepath, 'w') as f:
            json.dump(list_of_dicts, f, indent=4)

class ConsoleView:

    def __init__(self, bio: BriefBiography):
        self.bio = bio
        self.starz = "****************************************"

    def overview(self):
        print("Full Bio Contains:")
        for attr, value in asdict(self.bio).items():
            if isinstance(value, list):
                print(f"******************** {attr} ********************")
                for i in value:
                    print(f"-{i}")
                print("\n")
            else:
                print(f"******************** {attr} ********************\n {value} ")


    def fetch_jesidue_locations(self):
        print(f"******************** {self.bio.name} has jesidue in: ********************")
        for locations in self.bio.jesidue_class_attributes:
            print(locations)


    def fetch_religion(self):
        print(f"******************** {self.bio.name}'s religious persuasion(s) ********************")
        for religs in self.bio.religion:
            print(religs)


    def known_for(self):
        print(f"******************** {self.bio.name} is known for: ********************")
        for thing in self.bio.known_for:
            print(thing)


    def get_occupations(self):
        print(f"******************** {self.bio.name}'s occupation(s) and tenure(s) ********************")
        for positions in self.bio.occupations:
            print(positions)


    def get_education_information(self):
        print(f"******************** {self.bio.name}'s Ala Mater(s) ********************")
        for schools in self.bio.education:
            print(schools)


    def fetch_orders_knighthoods(self):
        print(f"******************** Knighthoods/orders {self.bio.name} belongs to ********************")
        for knighthoods in self.bio.orders_knighthoods:
            print(knighthoods)


    def get_birthplace_and_Locales_of_operation(self):
        print(f"{self.starz}")
        print(f"{self.bio.name} was born in {self.bio.locale_of_origin} on {self.bio.date_of_birth}")
        print(f"{self.starz}\n")
        print(f"******************** {self.bio.name}'s areas of operation ********************")
        for places in self.bio.locales_of_operation:
            print(places)


    def get_birthdate(self):
        print(f"{self.starz}")
        print(f"{self.bio.name}'s birthdate is {self.bio.date_of_birth}")


    def is_subject_alive(self):
        print(f"{self.starz}")
        if self.bio.alive:
            print(f"{self.bio.name} is still living")
        else:
            print(f"{self.bio.name} is dead")

