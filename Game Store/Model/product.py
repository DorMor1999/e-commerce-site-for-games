from abc import ABC

all_products_sorted_by_name = []
all_products_sorted_by_price = []


# base class
class Product(ABC):
    def __init__(self, name, price, link_photo_profile, description, publisher, platform, carousel_photos_links):
        self.name = name
        self.price = price
        self.link_photo_profile = link_photo_profile
        self.description = description
        self.publisher = publisher
        self.platform = platform
        self.carousel_photos_links = carousel_photos_links

    def __eq__(self, other):
        if other.__class__.__name__ != self.__class__.__name__:
            return False
        return self.name == other.name and self.platform == other.platform


