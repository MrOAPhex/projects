def main():
    print("")
    print("====Laskin====")
    print("Anna operaatiot (x y): ")
    x, y = map(int, input().split())
    print("Anna operaatio:")
    z = input("")
    print("====Tulos====")
    if z == "+":
        print(x+y)
    if z == "-":
        print(x-y)
    if z == "*":
        print(x*y)
    if z == "/":
        print(x/y)
    print("====loppu====")

main()
