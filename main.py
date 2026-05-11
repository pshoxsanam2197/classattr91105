# 3-m

class Phone:
    factory = "China"
    charger_type = "Type-C"

    def __init__(self, brand, model, memory, price):
        self.brand = brand
        self.model = model
        self.memory = memory
        self.price = price

    def show_phone(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Memory: {self.memory}")
        print(f"Price: {self.price}")
        print(f"Factory: {Phone.factory}")
        print(f"Charger: {Phone.charger_type}")

    def change_price(self, new_price):
        self.price = new_price

    def upgrade_memory(self, new_memory):
        self.memory = new_memory

phone1 = Phone("Samsung", "S24", 256, 1200)
phone2 = Phone("iPhone", "15 Pro", 512, 1500)
phone3 = Phone("Xiaomi", "Redmi Note", 128, 400)

print("\n=== Oldingi holat ===")
phone1.show_phone()

phone1.change_price(1300)
phone1.upgrade_memory(512)

print("\n=== Keyingi holat ===")
phone1.show_phone()
