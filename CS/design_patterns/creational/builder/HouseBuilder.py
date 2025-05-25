from House import House

class HouseBuilder:
    def __init__(self) -> None:
        self._floors: str = None
        self._doors: str = None
        self._roof: str = None
    
    def floors(self, floors: str):
        self._floors = floors
        return self
    
    def doors(self, doors: str):
        self._doors = doors
        return self
    
    def roof(self, roof: str):
        self._roof = roof
        return self
    
    def build(self):
        self._house = House()
        self._house._floors = self._floors
        self._house._doors = self._doors
        self._house._roof = self._roof
        return self._house