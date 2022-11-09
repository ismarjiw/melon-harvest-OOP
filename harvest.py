############
# Part 1   #
############



class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller):
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        """Initialize a melon."""

        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        
        self.pairings.append(pairing)
        
        # watermelon = MelonType()
        # watermelon.add_pairing(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        if new_code not in self.code:
            self.code = []
            self.code.append(new_code)

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    Muskmelon = MelonType('muskmelon','musk', 1998, 'green', False, True)
    Casaba = MelonType('casaba', 'cas', 2003, 'orange', True, False)
    Crenshaw = MelonType('crenshaw', 'cren', 1996, 'green', True, False)
    Yellow_Watermelon = MelonType('yellow watermelon', 'yw', 2013, 'yellow', True, False)

    Muskmelon.add_pairing('mint')
    Casaba.add_pairing('strawberries and mint')
    Crenshaw.add_pairing('prosciutto')
    Yellow_Watermelon.add_pairing('ice cream')
    
    all_melon_types.append(Muskmelon)
    all_melon_types.append(Casaba)
    all_melon_types.append(Crenshaw)
    all_melon_types.append(Yellow_Watermelon)
    
    return all_melon_types



def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    
    for melon in melon_types:
        print(f'{melon.name} pairs with' )
        for pairing in melon.pairings:
            print(pairing)

#print_pairing_info(make_melon_types())


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    dictionary = {}

    for melon in melon_types:
        dictionary[melon.code] = [melon]

    return dictionary

#make_melon_type_lookup(make_melon_types())


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
