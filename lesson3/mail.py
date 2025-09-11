class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.track = track
        self.cost = cost
        self.from_address = from_address
        self.to_address = to_address

    def __str__(self):
        return (f'Отправление {self.track} из {self.from_address} в {self.to_address}. Стоимость {self.cost} рублей')
