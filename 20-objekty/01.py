class Auto:
    def __init__(self, znacka, model, rok):
        self.znacka = znacka
        self.model = model
        self.rok = rok
        self.zapnute = False

    def zapni_svetlo(self):
        self.zapnute = True
        print(f"{self.znacka} {self.model} - Svetlo je zapnute.")

    def vypni_svetlo(self):
        self.zapnute = False
        print(f"{self.znacka} {self.model} - Svetlo je vypnute.")

    def info(self):
        print(f"AUTO: {self.znacka} {self.model}, rok vyroby {self.rok}")

auto = Auto("BMW", "e34", 1995)

auto.info()
auto.zapni_svetlo()
auto.vypni_svetlo()