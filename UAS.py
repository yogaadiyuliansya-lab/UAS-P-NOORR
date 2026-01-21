import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    kesempatan = 15

    print("\n=== Permainan Tebak Angka ===")
    print("Saya sudah memilih angka antara 1 sampai 100.")
    print(f"Anda memiliki {kesempatan} kesempatan.")
    print("Coba tebak!")

    while kesempatan > 0:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
        except ValueError:
            print("Harap masukkan angka yang valid!")
            continue

        kesempatan -= 1

        if tebakan < angka_rahasia:
            print("Angka Anda lebih kecil.")
        elif tebakan > angka_rahasia:
            print("Angka Anda lebih besar.")
        else:
            print("Selamat! Tebakan Anda benar 🎉")
            return

        print(f"Sisa kesempatan: {kesempatan}")

    print(f"\nKesempatan habis 😢 Angka yang benar adalah {angka_rahasia}")

def main():
    while True:
        tebak_angka()
        ulang = input("Apakah Anda ingin mengulang? (y/n): ").lower()
        if ulang != 'y':
            print("Terima kasih sudah bermain. Sampai jumpa!")
            break

# Jalankan program
main()
