print("==menu pilihan minuman==")
print("1.es teh - Rp5.000")
print("es jeruk - Rp7.000")
print("3.kopi - Rp8.000")
print("4.susu - Rp6.000")

pilihan = int(input("masukan pilihan minuman anda (1-4): "))

match pilihan:
  case 1:
        print("menu: es teh, Harga: rp5.000")
  case 2:
        print("menu: es jeruk, Harga: rp7.000")
  case 3:
        print("menu: kopi, Harga: rp8.000")
  case 4:
        print("menu: susu, Harga: rp6.000")
  case _:
    print("menu tidak ada")