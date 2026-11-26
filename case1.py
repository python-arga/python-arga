print(" === NAMA BULAN ===")
print("1.januari")
print("2.februari")
print("3.maret")
print("4.april")
print("5.mei")
print("6.juni")

bulan = int(input("masukan no bulan: (1-6)"))
match bulan :
    case 1:
        print("januari")
    case 2:
        print("februari")
    case 3:
        print("maret")
    case 4:
        print("april")
    case 5:
        print("mei")
    case 6:
        print("juni")
    case _:
        print("bulan tidak ada")