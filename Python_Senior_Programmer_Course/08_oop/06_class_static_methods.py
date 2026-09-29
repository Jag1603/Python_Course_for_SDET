class Math:
    @staticmethod
    def add(a,b): return a+b
    @classmethod
    def name(cls): return cls.__name__
print(Math.add(1,2), Math.name())