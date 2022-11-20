from Model.product import Product


class Game(Product):
    def __init__(self, name, price, link_photo_profile, description, publisher, platform, carousel_photos_links):
        super().__init__(name, price, link_photo_profile, description, publisher, platform, carousel_photos_links)
