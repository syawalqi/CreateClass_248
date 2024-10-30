class Persegip:
    def __init__(self, panjang, lebar) -> None:
        self.panjang = panjang
        self.lebar = lebar
    def luas(self):
        return self.panjang * self.lebar
    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    def __str__(self) -> str:
        return f"Persegi panjang dengan panjang {self.panjang} cm dan lebar {self.lebar} cm"

def main():
    try: 
        panjang = int(input("Masukkan panjang: "))
        lebar = int(input("Masukkan lebar: "))
        p = Persegip(panjang, lebar)
        if panjang > 0 and lebar > 0:
            print(f"{p} memiliki keliling {p.keliling()} cm")
            print(f"{p} memiliki luas {p.luas()} cm²")
        else:
            print("Panjang dan lebar harus lebih dari 0.")
    except ValueError:
        print("Masukkan angka.")

if __name__ == "__main__":
    main()

    













