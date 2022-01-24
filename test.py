from simple_tools import (
    print_debug,
    logging_debug,
)

@print_debug(prefix="**")
def adition(a: int,b: int):
    return a+b

@logging_debug(prefix="*")
def multiplication(a: int, b: int):
    return a*b

def main():
    a = 1
    b = 2
    print(adition(a,b))
    print(multiplication(a,b))

if __name__ == '__main__':
    main()
