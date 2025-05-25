from HouseBuilder import HouseBuilder
from HouseCatalogue import HouseCatalogue as hc

simple_house_1 = HouseBuilder()\
                .floors("simple wood")\
                .doors("simple wood")\
                .roof("flat")\
                .build()

print(f"{simple_house_1=}")


simple_house_2 = hc.simple_house()
mansion = hc.mansion()

print(f"{simple_house_2=}")
print(f"{mansion=}")