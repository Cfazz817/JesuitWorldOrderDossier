starz = "****************************************"
class BriefBiography:
    instances = []

    def __init__(self, name: str, education: list, religion: list,
                 occupations: list, alive: bool, date_of_birth: str,
                 locale_of_origin: str, locales_of_operation: list,
                 known_for: list, jesidue_class_attributes: list, orders_knighthoods=["none"]):
        self.name = str(name)
        self.education = list(education)
        self.religion = list(religion)
        self.occupations = list(occupations)
        self.alive = bool(alive)
        self.date_of_birth = str(date_of_birth)
        self.locale_of_origin = str(locale_of_origin)
        self.locales_of_operation = list(locales_of_operation)
        self.known_for = list(known_for)
        self.jesidue_class_attributes = list(jesidue_class_attributes)
        self.orders_knighthoods = list(orders_knighthoods)
        BriefBiography.instances.append(self)

    def overview(self):
        print("Full Bio Contains:")
        for attr, value in vars(self).items():
            if isinstance(value, list):
                print(f"******************** {attr} ********************")
                for i in value:
                    print(f"-{i}")
                print("\n")
            else:
                print(f"******************** {attr} ********************\n {value} ")

    def fetch_jesidue_locations(self):
        print(f"******************** {self.name} has jesidue in: ********************")
        for locations in self.jesidue_class_attributes:
            print(locations)

    def fetch_religion(self):
        print(f"******************** {self.name}'s religious persuasion(s) ********************")
        for religs in self.religion:
            print(religs)

    def known_for(self):
        print(f"******************** {self.name} is known for: ********************")
        for thing in self.known_for:
            print(thing)

    def get_occupations(self):
        print(f"******************** {self.name}'s occupation(s) and tenure(s) ********************")
        for positions in self.occupations:
            print(positions)

    def get_education_information(self):
        print(f"******************** {self.name}'s Ala Mater(s) ********************")
        for schools in self.education:
            print(schools)

    def fetch_orders_knighthoods(self):
        print(f"******************** Knighthoods/orders {self.name} belongs to ********************")
        for knighthoods in self.orders_knighthoods:
            print(knighthoods)

    def get_birthplace_and_Locales_of_operation(self):
        print(f"{starz}")
        print(f"{self.name} was born in {self.locale_of_origin} on {self.date_of_birth}")
        print(f"{starz}\n")
        print(f"******************** {self.name}'s areas of operation ********************")
        for places in self.locales_of_operation:
            print(places)

    def get_birthdate(self):
        print(f"{starz}")
        print(f"{self.name}'s birthdate is {self.date_of_birth}")

    def is_subject_alive(self):
        print(f"{starz}")
        if self.alive:
            print(f"{self.name} is still living")
        else:
            print(f"{self.name} is dead")


timothy_leary = \
    (BriefBiography("Timothy Leary",["College of the Holy Cross", "United States Military Academy at West Point",
    "University of Alabama (B.A. in Psychology)",
    "Ohio State University (Army Specialized Training Program)", "Washington State University (M.A. in Psychology)",
    "University of California, Berkeley (Ph.D. in Clinical Psychology)"], ["Roman Catholic"],
    ["Professor", "Intelligence Asset"], False, "10/22/1920", "Springfield, Massachusetts",
    ["Newton, Massachusetts: While lecturing at Harvard University",
    "Europe (Italy, Spain, Florence): After his research grant was terminated and following his first wife's death",
    "Millbrook, New York, where he conducted psychedelic experiments", "Cuernavaca, Mexico"
    "Where he first experienced hallucinogenic mushrooms", "Southern California (Beverly Hills): After being freed from prison"],
    ["Advocating for the mass use of hallucinogenic drugs during the 1960's era"],
    ["education", "religion", "locales_of_operation"]))

allen_dulles = \
    (BriefBiography("Allen Welsh Dulles", ["Homeschooled", "Auburn High School in Auburn, New York",
    "the École Alsa tienne in Paris", "Princeton University", "George Washington University"], ["'Presbyterian'"],
    ["U.S. Diplomatic Service Officer", "U.S. Delegate / Legal Adviser, Versailles Peace Conference", "Lawyer",
    "International Lawyer, Sullivan & Cromwell", "Corporate Board Member / Advisor", "Chief of OSS Station, Bern, Switzerland",
    "Consultant to U.S. Intelligence Community","Deputy Director for Plans, CIA", "CIA Director",
    "Author and Public Commentator on Intelligence", "Member, Warren Commission"],False, "4/17/1893",
    "Watertown, NY", ["Watertown, New York, USA",
    "Washington, D.C., USA", "New York City, New York, USA", "Bern, Switzerland", "Vienna, Austria", "Berlin, Germany",
    "Paris, France","Versailles, France","London, United Kingdom", "Rome, Italy", "Tehran, Iran", "Ankara, Turkey",
    "Guatemala City, Guatemala", "Havana, Cuba", "Mexico City, Mexico", "New Delhi, India", "Seoul, South Korea", "Beijing, China",
    "Hanoi, Vietnam", "North Africa"],["CIA Director", "Nazi collaborator", "Operation Sunrise",
    "Guatemalan Coup for United Fruit", "Serving Clients in The Third Reich for Sullivan and Cromwell"],
    ["occupations", "locales_of_operation"]))
john_dulles = \
    (BriefBiography("John Foster Dulles", ["Ethical Culture School","Princeton University", "University of Geneva"],
    ["Presbyterian"],["Lawyer", "International Law Practitioner", "International Law Consultant / Advisor",
    "U.S. Delegate / Advisor, League of Nations", "Special Advisor, U.S. State Department",
    "Legal Counsel / Advisor, U.S. Government", "Secretary of State, U.S. Government",
    "Author / Commentator on International Affairs"], False, "2/25/1888","Washington, DC",
    [ "Watertown, USA", "Washington, D.C., USA", "New York City, USA", "Paris, France", "Versailles, France",
    "Berlin, Germany", "London, United Kingdom", "Geneva, Switzerland", "San Francisco, USA", "Tokyo, Japan", "Seoul, South Korea",
    "Manila, Philippines", "Taipei, Taiwan", "Hanoi, Vietnam", "Rome, Italy", "Bonn, Germany"],["Nazi Collaborator",
    "Secretary of State", "Fathered a Jesuit"], ["religion", "known_for" "occupations", "orders_knighthoods"]))
william_casey = (
    BriefBiography("William Joseph Casey",["Fordham University", "Catholic University of America",
    "St. John's University School of Law"], ["Roman Catholic"], ["Lawyer","Research Director, "
    "Office of Strategic Services (OSS)","Special Assistant to the Secretary of State", "Chairman, Securities and Exchange Commission (SEC)",
    "Under Secretary of State for Economic Affairs","President, Export-Import Bank of the United States","Campaign Manager, "
    "Ronald Reagan Presidential Campaign","Director of Central Intelligence (CIA) (1981–1987)"], False, "3/13/1913",
    "Elmhurst, Queens, New York",["Elmhurst, Queens, New York, USA", "New York City, New York, USA",
    "Washington, D.C., USA", "Langley, Virginia, USA", "Europe","United Kingdom", "France", "Germany", "Italy", "Middle East",
    "Central America", "South America", "Afghanistan", "Japan"],["CIA Director",
    "Expanded cover operations during the cold war", "Iran Contra", "Anti-Communist","Died before he could testify",
    "Supporting the Afghan Mujahideen against the USSR", "Covert operations in Central America",
    "Reversed the post-watergate 'retrenchment' of US Intellegence"],["Education", "Religion", "Occupations",
    "Locales of Operation", "Known For"],["SMOM"]))
william_colby = BriefBiography("William Egan Colby", ["St. Ignatius Loyola School, Washington, D.C.",
    "Gonzaga College High School, Washington, D.C.","Princeton University", "Columbia Law School",
    "United States Army officer training", "OSS intelligence training","Jedburgh Team special operations training"],
    ["Roman Catholic"], ["United States Army officer", "OSS officer", "Jedburgh Team special operations officer",
    "CIA officer", "CIA station chief", "Chief of Station, Saigon", "Director of the Phoenix Program", "Senior counterinsurgency strategist",
    "Executive Director-Comptroller of the CIA", "Deputy Director for Operations (CIA)", "Director of Central Intelligence", "Lawyer",
    "Author","Public speaker", "Intelligence consultant", "Academic lecturer"], True, "1/4/1920",
    "St. Paul, Minnesota", ["Washington, D.C. & United States", "United Kingdom", "France",
    "Norway", "Rome, Italy", "Italy", "Saigon, Vietnam","South Vietnam","Laos", "Cambodia", "Global / worldwide intelligence oversight"],
    ["Director of Central Intelligence (DCI)", "Oversight of the U.S. Intelligence Community",
    "Covered up CIA drug trafficking during the Church Committee investigations", "Leadership of the Phoenix Program in Vietnam",
    "Expertise in counterinsurgency, insurgency and covert operations","World War II OSS officer and Jedburgh Team operative",
    "Author and lecturer on intelligence, law, and ethics", "Cleaned up the Image of intelligence operations",
    "Oversaw the 'Blown-Cover-Is-Cover' subterfuge that was the 'Church Hearings'"],["Education", "Occupations",
    "Religion", "Known For"])
