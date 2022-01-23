from simple_tools import print_debug

@print_debug(prefix="**")
def adition(a: int,b: int):
    return a+b

def main():
    a = "s"
    b = "b"
    print(adition(a,b))

if __name__ == '__main__':
    main()
