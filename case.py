def get_valid_input(input_string, valid_options):
    """
    Get valid input for option
    :param input_string: string
    :param valid_options: list
    :return:
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    """
    Class for property representation
    """
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        """
        Initialize new property
        :param self: Property
        :param square_feet: str
        :param beds: str
        :param baths: str
        :param kwargs: dict
        :return: None
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Display info about property
        :param self: Property
        :return: None
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        Get info from user
        :return: dict
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    Class for apartment representation
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        """
        Initialize new Apartment
        :param balcony: str
        :param laundry: str
        :param kwargs: dict
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Display info about Apartment
        :return: none
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        """
        Get info from user
        :return: dict
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does the property have? ",
                                  Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony? ",
                                  Apartment.valid_balconies)
        parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    Class for house representation
    """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        """
        Initialize new House
        :param num_stories: str
        :param garage: str
        :param fenced: str
        :param kwargs: dict
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Display info about house
        :return: none
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        get info from user
        :return: dict
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({"fenced": fenced, "garage": garage,
                            "num_stories": num_stories})
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    Class for purchase representation
    """
    def __init__(self, price='', taxes='', **kwargs):
        """
        Initialize wne property
        :param self: Purchase
        :param price: str
        :param taxes: str
        :param kwargs: dict
        :return: none
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        display info about purchase
        :param self: Purchase
        :return: none
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        Get info from user
        :return: dict
        """
        return dict(price=input("What is the selling price? "),
                    taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    Class for rental representation
    """
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        """
        Initialize new rental
        :param self: Rental
        :param furnished: str
        :param utilities: str
        :param rent: str
        :param kwargs: dict
        :return: none
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        display info about rental
        :param self: Rental
        :return: none
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        Get info from user
        :return: dict
        """
        return dict(rent=input("What is the monthly rent? "),
                    utilities=input("What are the estimated utilities? "),
                    furnished=get_valid_input("Is the property furnished? ", ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """
    class for house rental representation
    """
    def prompt_init():
        """
        get info from user
        :return: dict
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """
    Class for apartment rental representation
    """
    def prompt_init():
        """
        get info from user
        :return: dict
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """
    Class for apartment purchase representation
    """
    def prompt_init():
        """
        get info from user
        :return: dict
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    class for house purchase representation
    """
    def prompt_init():
        """
        get info from user
        :return: dict
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Class for agent representation
    """
    def __init__(self):
        """
        initialize new agent
        :param self: Agent
        :return: none
        """
        self.property_list = []

    def display_properties(self):
        """
        display info about property available
        :param self: Agent
        :return: none
        """
        for property in self.property_list:
            property.display()

    type_map = {("house", "rental"): HouseRental,
                ("house", "purchase"): HousePurchase,
                ("apartment", "rental"): ApartmentRental,
                ("apartment", "purchase"): ApartmentPurchase}

    def add_property(self):
        """
        Add new property
        :param self: Agent
        :return: none
        """
        property_type = get_valid_input("What type of property? ",
                                        ("house", "apartment")).lower()
        payment_type = get_valid_input("What payment type? ",
                                       ("purchase", "rental")).lower()
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def find_cheapest_rent(self):
        """
        find cheapest rent
        :param self: Agent
        :return: Property
        """
        cheapest = 1000000
        property_info = "Nothing available"
        for element in self.property_list:
            try:
                if element.rent < cheapest:
                    cheapest = elemenet.rent
                    property_info = element
            except:
                pass
        property_info.display()

    def find_cheapest_purchase(self):
        """
        Find cheapest property
        :param self: Agent
        :return: Property
        """
        cheapest = 1000000
        property_info = "Nothing available"
        for element in self.property_list:
            try:
                if element.price + element.taxes < cheapest:
                    cheapest = element.proce + element.taxes
                    property_info = element
            except:
                pass
        property_info.display()
