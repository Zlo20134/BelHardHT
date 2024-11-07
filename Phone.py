class Phone:
    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year


    def receive_call(self, name):
        print(f"Звонит {name}")


    def get_info(self):
        return (self.brand, self.model, self.issue_year)


    def __str__(self):
        return f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}"


phone = Phone("Apple", "iPhone 16", 2024)

phone.receive_call("Антон")


print(phone)
