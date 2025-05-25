from timeit import repeat
from orjson import loads, dumps
if __name__ == "__main__":
    with (
        open("/home/mkar/Desktop/Python/libraries/input.json") as fi, 
        open("/home/mkar/Desktop/Python/libraries/output.json", "wb") as of
    ):
        data = loads(fi.read())
        print(data)
        of.write(dumps(data))
    
    print("\n\nBenchmark Read-JSON\n\n")
    with open("/home/mkar/Desktop/Python/libraries/input.json") as f:
        data = f.read()
        
        t_json = min(
            repeat(
                "json.loads(data)",
                setup="import json",
                globals={"data": data},
                number=1_000_00
            )
        )
        
        t_orjson = min(
            repeat(
                "orjson.loads(data)",
                setup="import orjson",
                globals={"data": data},
                number=1_000_00
            )
        )
        
        print(f"json: {t_json:.3f}s")
        print(f"orjson: {t_orjson:.3f}s")
        print(f"orjson if {t_json / t_orjson:.2f} faster")