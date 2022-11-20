from Model.game import Game
from Model.accessory import Accessory
from Model.platform import Platform
from Model.order import Order
from Model.user import User
from datetime import datetime
import pickle


global games_dir
global platforms_dir
global accessories_dir
games_dir = "../static/assets/products/games/"
platforms_dir = "../static/assets/products/platforms/"
accessories_dir = "../static/assets/products/accessories/"


class Management:
    def __init__(self):
        # if I don't use in the data and start over
        # self.all_products_sorted_by_name = []
        # self.all_products_sorted_by_price = []
        # self.all_products = []
        # self.all_users = []
        # self.create_all_products()
        self.read_products_lists_data()
        self.read_users_lists_data()
        self.the_user = None
        self.order = Order()



    def add_product_to_lists(self, new_product):
        self.add_product_to_sorted_list_by_name(new_product)
        self.add_product_to_sorted_list_by_price(new_product)
        self.add_product_to_all_products(new_product)
        self.save_products_lists_data()


    def add_product_to_all_products(self, new_product):
        if not new_product in self.all_products:
            self.all_products.append(new_product)
            return True
        return False


    def add_product_to_sorted_list_by_name(self, new_product):
        # add the first one
        if len(self.all_products_sorted_by_name) == 0:
            self.all_products_sorted_by_name.append(new_product)
            return True
        # add to the beginning
        elif self.all_products_sorted_by_name[0].name > new_product.name and not self.all_products_sorted_by_name[
            0].__eq__(new_product):
            self.all_products_sorted_by_name.insert(0, new_product)
            return True
        # add to the end
        elif self.all_products_sorted_by_name[-1].name < new_product.name and not \
                self.all_products_sorted_by_name[-1].__eq__(new_product):
            self.all_products_sorted_by_name.append(new_product)
            return True
        # add between
        else:
            for index in range(len(self.all_products_sorted_by_name) - 1):
                if self.all_products_sorted_by_name[index].name < new_product.name and \
                        self.all_products_sorted_by_name[index + 1].name > new_product.name:
                    if not new_product.__eq__(self.all_products_sorted_by_name[index]) and not new_product.__eq__(
                            self.all_products_sorted_by_name[index + 1]):
                        self.all_products_sorted_by_name.insert(index + 1, new_product)
                        return True
        # already inside the list so we don't add
        return False


    def add_product_to_sorted_list_by_price(self, new_product):
        # add the first one
        if len(self.all_products_sorted_by_price) == 0:
            self.all_products_sorted_by_price.append(new_product)
            return True
        # add to the beginning
        elif self.all_products_sorted_by_price[0].price >= new_product.price and not self.all_products_sorted_by_price[
            0].__eq__(new_product):
            self.all_products_sorted_by_price.insert(0, new_product)
            return True
        # add to the end
        elif self.all_products_sorted_by_price[-1].price <= new_product.price and not \
                self.all_products_sorted_by_price[-1].__eq__(new_product):
            self.all_products_sorted_by_price.append(new_product)
            return True
        # add between
        else:
            for index in range(len(self.all_products_sorted_by_price) - 1):
                if self.all_products_sorted_by_price[index].price <= new_product.price and \
                        self.all_products_sorted_by_price[index + 1].price >= new_product.price:
                    if not new_product.__eq__(self.all_products_sorted_by_price[index]) and not new_product.__eq__(
                            self.all_products_sorted_by_price[index + 1]):
                        self.all_products_sorted_by_price.insert(index + 1, new_product)
                        return True
        # already inside the list so we don't add
        return False


    #check product with name and platform
    def search_by_name_product(self, product_name):
        low = 0
        high = len(self.all_products_sorted_by_name) - 1
        while low <= high:
            middle = int((low + high) / 2)
            #found
            if product_name == self.all_products_sorted_by_name[middle].name:
                return self.all_products_sorted_by_name[middle]
            elif product_name > self.all_products_sorted_by_name[middle].name:
                low = middle + 1
            else:
                high = middle - 1
        #not found
        return -1


    def get_all_products_from_one_type(self, the_type, sort_value):
        arr = []
        #return list of products from one type(Game, Platform, Accessory) sorted by name
        if sort_value == "name":
            for product in self.all_products_sorted_by_name:
               if product.__class__.__name__ == the_type:
                   arr.append(product)
            return arr
        # return list of products from one type(Game, Platform, Accessory) sorted by price
        elif sort_value == "price":
            for product in self.all_products_sorted_by_price:
               if product.__class__.__name__ == the_type:
                   arr.append(product)
            return arr
        # return list of products from one type(Game, Platform, Accessory) unsorted
        else:
            for product in self.all_products:
               if product.__class__.__name__ == the_type:
                   arr.append(product)
            return arr


    def get_all_products_from_one_type_and_same_platform(self, the_type, sort_value, platform):
        arr = []
        #return list of products from one type and same platform(Game, Platform, Accessory) sorted by name
        if sort_value == "name":
            for product in self.all_products_sorted_by_name:
               if product.__class__.__name__ == the_type and product.platform == platform:
                   arr.append(product)
            return arr
        # return list of products from one type and same platform(Game, Platform, Accessory) sorted by price
        elif sort_value == "price":
            for product in self.all_products_sorted_by_price:
               if product.__class__.__name__ == the_type and product.platform == platform:
                   arr.append(product)
            return arr
        # return list of products from one type and same platform(Game, Platform, Accessory) unsorted
        else:
            for product in self.all_products:
               if product.__class__.__name__ == the_type and product.platform == platform:
                   arr.append(product)
            return arr

    # save data to binary file
    def save_users_list_data(self):
        file = open("Model/data/all_users_list_file.txt", "wb")  # open file in write binary mode
        pickle.dump(self.all_users, file)  # dump list data into file
        file.close()  # close file pointer

    # read data from binary file
    def read_users_lists_data(self):
        file = open("Model/data/all_users_list_file.txt", "rb")  # open file in read binary mode
        self.all_users = pickle.load(file)  # read binary data from file and store in list
        file.close()


    #save data to binary file
    def save_products_lists_data(self):
        file1 = open("Model/data/all_products_list_file.txt", "wb")  # open file in write binary mode
        pickle.dump(self.all_products, file1)  # dump list data into file
        file1.close()  # close file pointer

        file2 = open("Model/data/all_products_list_sorted_by_name_file.txt", "wb")  # open file in write binary mode
        pickle.dump(self.all_products_sorted_by_name, file2)  # dump list data into file
        file2.close()  # close file pointer

        file3 = open("Model/data/all_products_list_sorted_by_price_file.txt", "wb")  # open file in write binary mode
        pickle.dump(self.all_products_sorted_by_price, file3)  # dump list data into file
        file3.close()  # close file pointer


    #read data from binary file
    def read_products_lists_data(self):
        file1 = open("Model/data/all_products_list_file.txt", "rb")  # open file in read binary mode
        self.all_products = pickle.load(file1)  # read binary data from file and store in list
        file1.close()

        file2 = open("Model/data/all_products_list_sorted_by_name_file.txt", "rb")  # open file in read binary mode
        self.all_products_sorted_by_name = pickle.load(file2)  # read binary data from file and store in list
        file2.close()

        file3 = open("Model/data/all_products_list_sorted_by_price_file.txt", "rb")  # open file in read binary mode
        self.all_products_sorted_by_price = pickle.load(file3)  # read binary data from file and store in list
        file3.close()


    # create all products
    def create_all_products(self):
        #games
        call_of_duty_modern_warfare_2_ps5 = Game("Call Of Duty: Modern Warfare 2 PS5", 80, f"{games_dir}CALL-OF-DUTY-MODERN-WARFARE-2-PS5/CALL-OF-DUTY-MODERN-WARFARE-2-PS5.jpg", "Call of Duty: Modern Warfare II is an upcoming first-person shooter game developed by Infinity Ward and published by Activision. It is a direct sequel to the 2019 reboot, and will serve as the nineteenth installment in the overall Call of Duty series. It is scheduled to be released on October 28, 2022.", "Activision", "PlayStation 5", [f"{games_dir}CALL-OF-DUTY-MODERN-WARFARE-2-PS5/1.jpg", f"{games_dir}CALL-OF-DUTY-MODERN-WARFARE-2-PS5/2.png", f"{games_dir}CALL-OF-DUTY-MODERN-WARFARE-2-PS5/3.jpg"])
        call_of_duty_modern_warfare_2_xbox_series_x = Game("Call Of Duty: Modern Warfare 2 Xbox Series X", 80, f"{games_dir}CALL-OF-DUTY-MODERN-WARFARE-2-XBOX/CALL-OF-DUTY-MODERN-WARFARE-2-XBOX.jpg", "Call of Duty: Modern Warfare II is an upcoming first-person shooter game developed by Infinity Ward and published by Activision. It is a direct sequel to the 2019 reboot, and will serve as the nineteenth installment in the overall Call of Duty series. It is scheduled to be released on October 28, 2022.", "Activision", "Xbox Series X", [f"{games_dir}CALL-OF-DUTY-MODERN-WARFARE-2-XBOX/1.jpg", f"{games_dir}CALL-OF-DUTY-MODERN-WARFARE-2-XBOX/2.png", f"{games_dir}CALL-OF-DUTY-MODERN-WARFARE-2-XBOX/3.jpg"])

        fifa_23_ps5 = Game("FIFA 23 – PS5", 70, f"{games_dir}FIFA-23-PS5/FIFA-23-PS5.jpg", "FIFA 23 is a football simulation video game published by Electronic Arts. It is the 30th and final installment in the FIFA series that is developed by EA Sports, and released worldwide on 30 September 2022.\nThe game is the final under the partnership between EA and FIFA. Future football games by EA without the inclusion of the FIFA name are set to be named under the banner of EA Sports FC.", "EA Sports", "PlayStation 5", [f"{games_dir}FIFA-23-PS5/1.jpg", f"{games_dir}FIFA-23-PS5/2.jpg", f"{games_dir}FIFA-23-PS5/3.jpg"])
        fifa_23_xbox_series_x = Game("FIFA 23 – Xbox Series X", 70, f"{games_dir}FIFA-23-XBOX-SERIES-X/FIFA-23-XBOX-SERIES-X.jpg", "FIFA 23 is a football simulation video game published by Electronic Arts. It is the 30th and final installment in the FIFA series that is developed by EA Sports, and released worldwide on 30 September 2022.\nThe game is the final under the partnership between EA and FIFA. Future football games by EA without the inclusion of the FIFA name are set to be named under the banner of EA Sports FC.", "EA Sports", "Xbox Series X", [f"{games_dir}FIFA-23-XBOX-SERIES-X/1.jpg", f"{games_dir}FIFA-23-XBOX-SERIES-X/2.jpg", f"{games_dir}FIFA-23-XBOX-SERIES-X/3.jpg"])

        NBA_2K23_standard_edition_ps5 = Game("NBA 2K23 – Standard Edition PS5", 75, f"{games_dir}NBA-2K23-Standard-Edition-PS5/NBA-2K23-Standard-Edition-PS5.jpg", "NBA 2K23 is a basketball video game developed by Visual Concepts and published by 2K Sports, based on the National Basketball Association (NBA). It is the 24th installment in the NBA 2K franchise and the successor to NBA 2K22. The game was released on September 9, 2022.", "2K Sports", "PlayStation 5", [f"{games_dir}NBA-2K23-Standard-Edition-PS5/1.jpg", f"{games_dir}NBA-2K23-Standard-Edition-PS5/2.jpg", f"{games_dir}NBA-2K23-Standard-Edition-PS5/3.jpg"])
        NBA_2K23_standard_edition_xbox_series_x = Game("NBA 2K23 – STANDARD EDITION | XBOX SERIES X", 75, f"{games_dir}NBA-2K23-STANDARD-EDITION-XBOX-SERIES-X/NBA-2K23-STANDARD-EDITION-XBOX-SERIES-X.png", "NBA 2K23 is a basketball video game developed by Visual Concepts and published by 2K Sports, based on the National Basketball Association (NBA). It is the 24th installment in the NBA 2K franchise and the successor to NBA 2K22. The game was released on September 9, 2022.", "2K Sports", "Xbox Series X", [f"{games_dir}NBA-2K23-STANDARD-EDITION-XBOX-SERIES-X/1.jpg", f"{games_dir}NBA-2K23-STANDARD-EDITION-XBOX-SERIES-X/2.jpg", f"{games_dir}NBA-2K23-STANDARD-EDITION-XBOX-SERIES-X/3.jpg"])

        #platforms
        Playstation_5 = Platform("Playstation 5", 710, f"{platforms_dir}PS5/PS5.jpg", "The PlayStation 5 (PS5) is a home video game console developed by Sony Interactive Entertainment. Announced in 2019 as the successor to the PlayStation 4, the PS5 was released on November 12, 2020, in Australia, Japan, New Zealand, North America, and South Korea, with worldwide release following a week later.", "Sony Interactive Entertainment", "PlayStation 5", [f"{platforms_dir}PS5/1.jpg", f"{platforms_dir}PS5/2.png", f"{platforms_dir}PS5/3.jpg"])
        Xbox_Series_X = Platform("Xbox Series X", 625, f"{platforms_dir}XBOX-SERIES-X/XBOX-SERIES-X.jpg", "The Xbox Series X and the Xbox Series S (collectively, the Xbox Series X/S[b]) are home video game consoles developed by Microsoft. They were both released on November 10, 2020, as the fourth generation of the Xbox console family, succeeding the Xbox One. Along with Sony's PlayStation 5, also released in November 2020, the Xbox Series X and Series S are part of the ninth generation of video game consoles.", "Microsoft", "Xbox Series X", [f"{platforms_dir}XBOX-SERIES-X/1.jpg", f"{platforms_dir}XBOX-SERIES-X/2.jpg", f"{platforms_dir}XBOX-SERIES-X/3.jpg"])

        # #accessories
        ps5_controller_black = Accessory("Sony Ps5 DualSense Controller Midnight Black", 85, f"{accessories_dir}ps5_controller_black/ps5_controller_black.jpg", "The DualSense wireless controller for PS5 offers immersive haptic feedback, dynamic adaptive triggers and a built-in microphone, all integrated into an iconic design.", "Sony Interactive Entertainment", "PlayStation 5",[f"{accessories_dir}ps5_controller_black/1.jpg", f"{accessories_dir}ps5_controller_black/2.jpg", f"{accessories_dir}ps5_controller_black/3.jpg"])
        ps5_controller_white = Accessory("Sony Ps5 DualSense Controller White", 85, f"{accessories_dir}ps5_controller_white/ps5_controller_white.jpg", "The DualSense wireless controller for PS5 offers immersive haptic feedback, dynamic adaptive triggers and a built-in microphone, all integrated into an iconic design.", "Sony Interactive Entertainment", "PlayStation 5", [f"{accessories_dir}ps5_controller_white/1.webp", f"{accessories_dir}ps5_controller_white/2.jpg", f"{accessories_dir}ps5_controller_white/3.jpg"])
        xbox_series_x_controller_white = Accessory("Xbox Series X Wireless Controller – Robot White", 80, f"{accessories_dir}xbox_series_x_controller_white/xbox_series_x_controller_white.jpg", "For Xbox Series X|S, we’ve streamlined the Xbox Wireless Controller for comfort, performance, and instant sharing. The controller also works great with Xbox One, Windows 10/11, and cloud gaming devices.", "Microsoft", "Xbox Series X", [f"{accessories_dir}xbox_series_x_controller_white/1.jpg", f"{accessories_dir}xbox_series_x_controller_white/2.jpg", f"{accessories_dir}xbox_series_x_controller_white/3.jpg"])
        xbox_series_x_controller_black = Accessory("Xbox Series X Wireless Controller – Robot black", 80, f"{accessories_dir}xbox_series_x_controller_black/xbox_series_x_controller_black.jpg", "For Xbox Series X|S, we’ve streamlined the Xbox Wireless Controller for comfort, performance, and instant sharing. The controller also works great with Xbox One, Windows 10/11, and cloud gaming devices.", "Microsoft", "Xbox Series X", [f"{accessories_dir}xbox_series_x_controller_black/1.jpg", f"{accessories_dir}xbox_series_x_controller_black/2.jpg", f"{accessories_dir}xbox_series_x_controller_black/3.jpg"])

        self.add_product_to_lists(call_of_duty_modern_warfare_2_ps5)
        self.add_product_to_lists(call_of_duty_modern_warfare_2_xbox_series_x)
        self.add_product_to_lists(fifa_23_ps5)
        self.add_product_to_lists(fifa_23_xbox_series_x)
        self.add_product_to_lists(NBA_2K23_standard_edition_ps5)
        self.add_product_to_lists(NBA_2K23_standard_edition_xbox_series_x)

        self.add_product_to_lists(Playstation_5)
        self.add_product_to_lists(Xbox_Series_X)

        self.add_product_to_lists(ps5_controller_white)
        self.add_product_to_lists(ps5_controller_black)
        self.add_product_to_lists(xbox_series_x_controller_black)
        self.add_product_to_lists(xbox_series_x_controller_white)


    def add_user(self,new_user):
        # add the first one
        if len(self.all_users) == 0:
            self.all_users.append(new_user)
        # add to the beginning
        elif new_user.email < self.all_users[0].email:
            self.all_users.insert(0, new_user)
        # add to the end
        elif new_user.email > self.all_users[-1].email:
            self.all_users.append(new_user)
        else:
            for index in range(len(self.all_users)-1):
                if new_user.email > self.all_users[index].email and new_user.email < self.all_users[index + 1].email:
                    self.all_users.insert(index + 1, new_user)
        self.save_users_list_data()
        return True


    # check user with email
    def search_by_email_user(self, email):
        low = 0
        high = len(self.all_users) - 1
        while low <= high:
            middle = int((low + high) / 2)
            # found
            if email == self.all_users[middle].email:
                return self.all_users[middle]
            elif email > self.all_users[middle].email:
                low = middle + 1
            else:
                high = middle - 1
        # not found
        return -1


    #search navbar
    def search_navbar(self, search):
        search_split = search.split(" ")
        for tav in search_split:
            if len(tav) < 2:
                search_split.remove(tav)
        print(search_split)
        arr = []
        for product in self.all_products:
            counter = 0
            for part in search_split:
                if part.upper() in product.name.upper():
                    counter += 1
            if counter > 0:
                if len(arr) == 0:
                    arr.append({
                        "product": product,
                        "times": counter
                    })
                elif arr[0]["times"] <= counter:
                    arr.insert(0, {
                        "product": product,
                        "times": counter
                    })
                elif arr[-1]["times"] >= counter:
                    arr.append({
                        "product": product,
                        "times": counter
                    })
                else:
                    for index in range(len(arr) - 1):
                        if counter <= arr[index]["times"] and counter >= arr[index + 1]["times"]:
                            arr.insert(index + 1, {
                                "product": product,
                                "times": counter
                            })
                            break
        return arr


    # server mathods
    def sign_in(self, email, password):
        msg = ""
        the_user = self.search_by_email_user(email)
        if the_user == -1:
            msg += "We dont have a user with that email account!"
        elif not the_user.log_in(password):
            msg += "Incorrect password!"
        else:
            self.the_user = the_user
        return msg


    def register(self, email, password):
        msg = ""
        new_user = User()
        if self.search_by_email_user(email) != -1:
            return "We already have a user with that email account!"
        if not new_user.set_email(email):
            if msg == "":
                msg += "You can only register with yahoo or gmail!"
            else:
                msg += " , You can only register with yahoo or gmail!"
        if not new_user.set_password(password):
            if msg == "":
                msg += "Password must be at least 6 characters!"
            else:
                msg += " , Password must be at least 6 characters!"
        if msg == "":
            self.add_user(new_user)
            msg = "You have successfully registered"
        return msg


    def cart_operations(self, product_name, operation):
        product = self.search_by_name_product(product_name)
        if operation == "add":
            self.order.add_to_cart(product)
        elif operation == "remove":
            self.order.remove_from_cart(product, "remove")
        elif operation == "+1":
            self.order.add_to_cart(product)
        elif operation == "-1":
            self.order.remove_from_cart(product, "-1")


    def order_form(self, first_name, last_name, city, address):
        msg = ""
        if len(first_name) == 0:
            msg += "First name must be at least one character!"
        if len(last_name) == 0:
            if msg == "":
                msg += "Last name must be at least one character!"
            else:
                msg += ", Last name must be at least one character!"
        if len(city) == 0:
            if msg == "":
                msg += "City name must be at least one character!"
            else:
                msg += ", City name must be at least one character!"
        if len(address) == 0:
            if msg == "":
                msg += "Address name must be at least one character!"
            else:
                msg += ", Address name must be at least one character!"
        if msg == "":
            self.order.details = {
                "first_name": first_name,
                "last_name": last_name,
                "city": city,
                "address": address,
                "date": datetime.today().strftime('%d/%m/%Y'),
                "time": datetime.today().strftime('%H:%M')
            }
            self.order.id = int(self.order.read_ID_GENERATOR()) + 1
            self.the_user.orders.insert(0, self.order)
            self.order.save_ID_GENERATOR(self.order.id)
            self.save_users_list_data()
            self.order = Order()
        return msg