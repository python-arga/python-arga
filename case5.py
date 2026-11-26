
print("=== PROGRAM PEMILIHAN FILM BIOSKOP ===")

usia = int(input("Masukkan usia Anda: "))

if usia >= 17:
    print("Pilihan Genre Film:")
    print("1. Horor")
    print("2. Komedi")
    print("3. Keluarga")
    print("4. Aksi")

    genre = input("Pilih genre film (1-4): ")

    if genre == "1":
        print("Pilihan Film Horor:")
        print("1. Horor Indonesia")
        print("2. Horor Luar Negeri")
        pilihan = input("Pilih film: ")

        if pilihan == "1":
            judul = "Horor Indonesia"
        elif pilihan == "2":
            judul = "Horor Luar Negeri"
        else:
            judul = "tidak ada"

    elif genre == "2":
        print("Pilihan Film Komedi:")
        print("1. Komedi Indonesia")
        print("2. Komedi Luar Negeri")
        pilihan = input("Pilih film: ")

        if pilihan == "1":
            judul = "Komedi Indonesia"
        elif pilihan == "2":
            judul = "Komedi Luar Negeri"
        else:
            judul = "tidak ada"

    elif genre == "3":
        print("Pilihan Film Keluarga:")
        print("1. Keluarga Indonesia")
        print("2. Keluarga Luar Negeri")
        pilihan = input("Pilih film: ")

        if pilihan == "1":
            judul = "Keluarga Indonesia"
        elif pilihan == "2":
            judul = "Keluarga Luar Negeri"
        else:
            judul = "tidak ada"

    elif genre == "4":
        print("\nPilihan Film Aksi:")
        print("1. Hollywood")
        print("2. Indonesia")
        print("3. Bollywood")
        pilihan = input("Pilih film: ")

        if pilihan == "1":
            judul = "Film Aksi Hollywood"
        elif pilihan == "2":
            judul = "Film Aksi Indonesia"
        elif pilihan == "3":
            judul = "Film Aksi Bollywood"
        else:
            judul = "tidak ada"

    else:
        judul = "tidak ada"

else:
    print("Pilihan Film Animasi:")
    print("1. Animasi 2 Dimensi")
    print("2. Animasi 3 Dimensi")

    animasi = input("Pilih jenis animasi (1-2): ")

    if animasi == "1":
        print("Pilihan Film 2 Dimensi:")
        print("1. Naruto")
        print("2. One Piece")
        pilihan = input("Pilih film: ")

        if pilihan == "1":
            judul = "Naruto"
        elif pilihan == "2":
            judul = "One Piece"
        else:
            judul = "tidak ada"

    elif animasi == "2":
        print("Pilihan Film 3 Dimensi:")
        print("1. Nemo")
        print("2. Kungfu Panda")
        pilihan = input("Pilih film: ")

        if pilihan == "1":
            judul = "Nemo"
        elif pilihan == "2":
            judul = "Kungfu Panda"
        else:
            judul = "tidak ada"

    else:
        judul = "tidak ada"

if judul:
    print("Selamat Menyaksikan", judul)
else:
    print("pilihan anda tidak ada")
