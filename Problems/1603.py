class ParkingSystem:
    __slots__ = ['_parking']

    def __init__(self, big: int, medium: int, small: int):
        self._parking = {
            1: big,
            2: medium,
            3: small
        }

    def addCar(self, carType: int) -> bool:
        available_spots = self._parking[carType]
        if available_spots:
            self._parking[carType] = available_spots - 1
            return True

n1 = ParkingSystem

n1.addCar('addCar',1)

# print(n1.big)