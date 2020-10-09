############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        self.pairings.append(pairing)
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        print(f'{new_code}')
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""
    # "Yellow Watermelon", "Crenshaw", "Casaba", "Muskmelon"
   
# name: muskmelon Reporting code: musk First harvest in 1998 Color: green Pairs well with mint Seedless Bestseller
# Name: Casaba Reporting code: cas First harvest in 2003 Color: orange Pairs well with strawberries and mint Has seeds
# Name: Crenshaw Reporting code: cren First harvest in 1996 Color: green Pairs well with proscuitto Has seeds
# Name: Yellow Watermelon Reporting code: yw First harvest in 2013 Color: yellow Pairs well with ice cream Has seeds Bestseller

    all_melon_types = []
    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)

    casaba = MelonType("cas", 2003, "orange", False, True, "Casaba")
    casaba.add_pairing(["stawberries", "mint"])
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", 1996, "green",True, False, "Crenshaw")
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)
    # Fill in the rest
    print(all_melon_types)
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    
    for melon in melon_types:
        print (f"{melon_types.name}")
        for pairs in melon_types.pairings:
            print (f"pairs with {melon_types.pairings}")
    # Fill in the rest

def make_melon_type_lookup(melon_types):
   
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_types = {}
    for melon in melon_types:
        if melon.code not in melon_types:
            key = melon.code
            melon_types[melon.code] = [melon.first_harvest, melon.color, melon.is_seedless ,
            melon.is_bestseller, melon.name]


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, num_harvested, harvester):
    # Fill in the rest
    # Needs __init__ and is_sellable methods
        self.melon_type = melon_types
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.num_harvested = num_harvested
        self.harvester = harvester
        
    def is_sellable(self):
        """Determine whether this melon can be sold."""
        if self.shape_rating > 5  and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        harvested_by = f'Harvested by {melon.harvester}'
        field_num = f'Field #{melon.field}'
        status = 'CAN BE SOLD' if melon.is_sellable() else 'NOT SELLABLE'
        print(f'{harvested_by} from {field_num} {status}')
    # Fill in the rest 


# print_pairing_info(make_melon_types())
# print(make_melon_types())
if __name__ == "__main__":
    melon_types = make_melon_types()
    melon_lookup = make_melon_type_lookup
    melons = make_melons(melon_types)