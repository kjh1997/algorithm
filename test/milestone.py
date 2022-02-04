def sum(a,b) -> float:
    return a+b
print(type(sum(4,6)))


def funName(x: str, y: float = 6.5) -> int:
    print(type(x))
    return x + y


value = funName(3)
print(value)