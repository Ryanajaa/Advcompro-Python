class Product:
    def __init__(self, product_name, product_price, in_stock=bool()):
        self.pname = product_name
        self.pprice = product_price
    
    def apply_discount(self, percent):
        self.pprice = self.pprice - (self.pprice * percent / 100)
    
    def available(self):
        if self.in_stock:
            return "In stock"
        else:
            return "Out of stock"
        
class CartItem(Product):
    def __init__(self, product_name, product_price, quantity, in_stock=bool()):
        super().__init__(product_name, product_price, in_stock)
        self.quantity = quantity

    def totalcost(self):
        return self.quantity * self.pprice
    
    def additem(self):
        self.quantity += 1

    def removeitem(self):
        if self.quantity > 1:
            self.quantity -= 1

    def display(self):
        print(f"Product Name: {self.pname}")
        print(f"Quantity: {self.quantity}")
        print(f"Product Price: ${self.pprice}")
        print(f"Total Cost: ${self.totalcost()}")
    
Milk = CartItem("Milk",5,20,"yes")
Butter = CartItem("Butter",10,1,"yes")

Milk.display()
Milk.apply_discount(10)
print()
Milk.display()
print()
Butter.display()
Butter.removeitem()
Butter.display()