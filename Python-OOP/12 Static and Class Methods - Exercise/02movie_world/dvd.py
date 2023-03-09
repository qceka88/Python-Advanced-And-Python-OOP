from calendar import month_name


class DVD:

    def __init__(self, name: str, id_number: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_number
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_number: int, name: str, date: str, age_restriction: int):
        day, month, year = [int(i) for i in date.split(".")]

        return cls(name, id_number, year, month_name[month], age_restriction)

    def __repr__(self):
        message = f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has " \
                  f"age restriction {self.age_restriction}. Status: {'' if self.is_rented else 'not '}rented"

        return message
