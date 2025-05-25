class House:
        def __repr__(self) -> str:
            return '\n'.join(f"{k}: {v}" for k, v in self.__dict__.items())