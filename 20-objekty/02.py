class Auto:
    def __init__(self, znacka, farba):
        self.znacka = znacka
        self.farba = farba

    def info(self):
        print(f"{self.znacka}, farba {self.farba}")

auta = [

    Auto("Mustang", "červená"),
    Auto("Corvette", "ružová"),
    Auto("Koenigsegg", "černá"),
    Auto("Dodge", "bielá"),
    Auto("Nissan", "fialová"),
    Auto("Subaru", "modrá")
]

for auto in auta:
    auto.info()