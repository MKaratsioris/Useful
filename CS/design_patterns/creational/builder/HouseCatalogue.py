from HouseBuilder import HouseBuilder
from House import House

class HouseCatalogue:
    @staticmethod
    def simple_house(
        floors: str = "simple wood", 
        doors: str = "simple wood", 
        roof: str = "flat"
        ) -> House:
        return HouseBuilder()\
                .floors(floors)\
                .doors(doors)\
                .roof(roof)\
                .build()
    
    @staticmethod
    def mansion(
        floors: str = "marble", 
        doors: str = "oak wood", 
        roof: str = "Ceramic triangle"
        ) -> House:
        return HouseBuilder()\
                .floors(floors)\
                .doors(doors)\
                .roof(roof)\
                .build()