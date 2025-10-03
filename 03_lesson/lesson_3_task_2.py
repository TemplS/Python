from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3310", "+79053132060"),
    Smartphone("Motorola", "Edge", "+79055315900"),
    Smartphone("Huawei", "9X Pro Max Ultra G", "+79222132060"),
    Smartphone("Poko", "1999Z Turbo Mega X", "+79222323232"),
    Smartphone("Nubia", "Red Magic 9 Pro", "+79083221074")
]

for Smartphone in catalog:
    print(f'{Smartphone.brand} - {Smartphone.model}. {Smartphone.number}.')
