print("=== kategori ujian ===")
print("1 = teori")
print("2 = praktik")

kategori = int(input("masukan kategori anda: "))
nilai = int(input("masukan nilai anda: "))

match kategori:
    case 1:
        if nilai >= 75:
            print("anda lulus")
        else:
            print("anda belum lulus")
    case 2:
        if nilai >= 75:
            print("anda lulus")
        else:
            print("anda belum lulus")
    case _:
        print("kategori ujian tidak valid")