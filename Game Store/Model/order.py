# ID_GENERATOR = 1000


class Order():
    def __init__(self):
        # global ID_GENERATOR
        # ID_GENERATOR += 1
        # self.id = ID_GENERATOR
        self.id = None
        self.cart = []
        self.total_price = 0
        self.total_items = 0
        self.details = None


    def add_to_cart(self, new_item):
        self.total_price += new_item.price
        self.total_items += 1
        for item in self.cart:
            if new_item == item["product"]:
                item["quantity"] += 1
                item["price"] += new_item.price
                return True
        self.cart.append({"product": new_item, "quantity": 1, "price": new_item.price})


    def remove_from_cart(self, remove_item, operation):
        for item in self.cart:
            if remove_item == item["product"]:
                if operation == "-1":
                    item["quantity"] -= 1
                    self.total_items -= 1
                    item["price"] -= remove_item.price
                    self.total_price -= remove_item.price
                else:
                    self.total_price -= item["price"]
                    self.total_items -= item["quantity"]
                    self.cart.remove(item)
                return True

    #save ID_GENERATOR number to file
    def save_ID_GENERATOR(self, ID_GENERATOR):
        file = open("Model/data/ID_GENERATOR_file.txt", "w")
        file.write(f"{ID_GENERATOR}")
        file.close()

    # save ID_GENERATOR number from file
    def read_ID_GENERATOR(self):
        file = open("Model/data/ID_GENERATOR_file.txt", "r")
        return file.read()