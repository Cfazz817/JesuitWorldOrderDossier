class BriefBiography:
    def __init__(self, name: str, education: list, religion: str,
                 occupation: str, alive: bool, date_of_birth: str,
                 locale_of_origin: str, locales_of_operation: list,
                 known_for: list, orders_knighthoods: list):
        self.name = name
        self.education = list(education)
        self.religion = str(religion)
        self.occupation = str(occupation)
        self.alive = bool(alive)
        self.date_of_birth = str(date_of_birth)
        self.locale_of_origin = str(locale_of_origin)
        self.locales_of_operation = list(locales_of_operation)
        self.known_for = list(known_for)
        self.orders_knighthoods = list(orders_knighthoods)

