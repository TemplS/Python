class Address:
    def __init__(self, index, city, street, num, appart):
        self.index = index
        self.city = city
        self.street = street
        self.num = num
        self.appart = appart

    def __str__(self):
        return f'{self.index}, {self.city}, {self.street}, {self.num} - {self.appart} '
