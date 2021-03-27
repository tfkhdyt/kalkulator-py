import os

class Kalkulator:
    def __init__(self, angka1, operator, angka2):
        self.angka1 = angka1
        self.operator = operator
        self.angka2 = angka2

    def tambah(self):
        print(f"{self.angka1} + {self.angka2} = {self.angka1 + self.angka2}")

    def kurang(self):
        print(f"{self.angka1} - {self.angka2} = {self.angka1 - self.angka2}")

    def kali(self):
        print(f"{self.angka1} * {self.angka2} = {self.angka1 * self.angka2}")

    def bagi(self):
        print(f"{self.angka1} / {self.angka2} = {round(self.angka1 / self.angka2, 2)}")

    def mod(self):
        print(f"{self.angka1} % {self.angka2} = {self.angka1 % self.angka2}")

    def result(self):
        if self.operator == '+':
            Kalkulator.tambah(self)

        elif self.operator == '-':
            Kalkulator.kurang(self)

        elif self.operator == '*':
            Kalkulator.kali(self)

        elif self.operator == '/':
            Kalkulator.bagi(self)

        elif self.operator == '%':
            Kalkulator.mod(self)

while(True):
    try:
        width = os.get_terminal_size().columns

        print(" Kalkulator ".center(width, "="))
        angka1 = int(input("\n              Masukkan Angka 1  = "))
        operator = input("              Pilih Operator    = ")
        angka2 = int(input("              Masukkan Angka 2  = "))
        print()
        print(" Hasil ".center(width, "="))
        print()

        calc = Kalkulator(angka1, operator, angka2)

        print("              ",end="")

        calc.result()

        print()
        print("".center(width, "="))
        ulang = input("\n              Ulang? (y/n) : ")

        if ulang == 'y':
            os.system("clear")
            continue
        else:
            print()
            print("".center(width, "="))
            break
    except:
        print("".center(width, "="))
        print("\n              Input tidak valid!")
        ulang = input("\n              Ulang? (y/n) : ")

        if ulang == 'y':
            os.system("clear")
            continue
        else:
            print()
            print("".center(width, "="))
            break
