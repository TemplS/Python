from address import Address
from mail import Mailing


point1 = Address("625046", "Тюмень", "Широтная", "108", "20")
point2 = Address("119017", "Москва", "Лаврпушинский пер", "10", "нет")


send_mail = Mailing(point1, point2, 2237, 2312984)

print(send_mail)
