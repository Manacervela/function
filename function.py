def exchange_nzd_usd(nzd):
    return nzd/1.60

def exchange_usd_nzd(usd):
    return usd*1.60

#Money exchange

while True:
    print("""\t.:MENU:.
1. usd to nzd
2. nzd to usd
3. Exit""")
    option = int(input("type a menu option: "))

    print()

    if option == 1:
        nzd = float(input("Type the amount you want to exchange: "))
        print(f"usd -> ${exchange_nzd_usd(nzd):.2f}")

    elif option==2:
        usd = float(input("Type amount of usd: "))
        print(f"nzd -> S/{exchange_usd_nzd(usd):.2f}")

    elif option==3:
        break

    else:
        print("Wrong menu option")

    print()