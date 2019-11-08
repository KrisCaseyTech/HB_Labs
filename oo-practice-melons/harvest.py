############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, 
                        is_bestseller):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 'Muskmelon', 1998, 'green',
                     True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 'Casaba', 2003, 'orange',
                    False, False)
    cas.add_pairing('mint')
    cas.add_pairing('strawberry')
    all_melon_types.append(cas)

    cren = MelonType('cren', 'Crenshaw', 1996, 'green',
                    False, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow',
                    False, False)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)
    # Fill in the rest

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        name = melon.name
        print()
        print(f"{name} pairs with")

        for melon_pairing in melon.pairings:
            print(f"- {melon_pairing}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    dict_codes = {}

    for melon in melon_types:
        code = melon.code
        dict_codes[code] = melon

    return dict_codes


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, harvest_field, harvest_by):
        
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvest_by = harvest_by

    def is_sellable(self):

        if self.shape_rating > 5 & self.color_rating > 5 & self.harvest_field != 3:
            return True

        return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon = []

    melon_dict = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melon_dict["yw"], 8, 7, 2, "Sheila")
    melon.append(melon_1)
    melon_2 = Melon(melon_dict["yw"], 3, 4, 2, "Sheila")
    melon.append(melon_2)
    melon_3 = Melon(melon_dict["yw"], 9, 8, 3, "Sheila")
    melon.append(melon_3)
    melon_4 = Melon(melon_dict["cas"], 10, 6, 35, "Sheila")
    melon.append(melon_4)
    melon_5 = Melon(melon_dict["cren"], 8, 9, 35, "Michael")
    melon.append(melon_5)
    melon_6 = Melon(melon_dict["cren"], 8, 2, 35, "Michael")
    melon.append(melon_6)
    melon_7 = Melon(melon_dict["cren"], 2, 3, 4, "Michael")
    melon.append(melon_7)
    melon_8 = Melon(melon_dict["musk"], 6, 7, 4, "Michael")
    melon.append(melon_8)
    melon_9 = Melon(melon_dict["yw"], 7, 10, 3, "Sheila")
    melon.append(melon_9)

    return melon

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



# Sellable = shape & Color > 5 & not field 3