print("=== jenis pelanggan ===")
print("1 = member")
print("2 = non member")
pelanggan = int(input("masukan jenis pelanggan anda: "))
belanja = float(input("masukan jumlah belanja anda: "))

match pelanggan:
    case 1:
        if belanja >= 100.000:
            print("anda dapat diskon 10%")
        else:
            print("anda tidak dapat diskon")
    case 2:
        if belanja >= 100.000:
            print("anda dapat diskon 5%")
        else:
            print("anda tidak dapat diskon")