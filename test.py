from simple_tools import (
    print_debug,
    logging_debug,
    async_logging_debug,
)

@print_debug(prefix="**")
def adition(a: int,b: int):
    return a+b

@logging_debug(prefix="*")
def multiplication(a: int, b: int):
    return a*b

@async_logging_debug(prefix="*")
def divition(a: int, b: int):
    return a/b


def main():
    a = "a"
    b = "b"
    print(adition(a,b))
    print(multiplication(a,b))
    print(divition(a,b))

if __name__ == '__main__':
    main()
