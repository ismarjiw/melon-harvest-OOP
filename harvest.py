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

    def __init__(self, name, code, shape, color, field, harvester): #make_melons_by_id
        self.name = name
        self.code = code
        self.shape = shape
        self.color = color
        self.field = field
        self.harvester = harvester 
        # self.melons_by_id = melons_by_id
        


    def is_sellable(self):
        '''return True or False based on whether melon is able to be sold'''

        if self.shape > 5 and self.color > 5 and self.field != 3:
            return True
        else:
            return False 

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    all_melons = []

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila') #name, code
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila') #name, code
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila') #name, code
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila') #name, code
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael') #name, code
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael') #name, code
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael') #name, code
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael') #name, code
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila') #name, code

    all_melons.append(melon_1)
    all_melons.append(melon_2)
    all_melons.append(melon_3)
    all_melons.append(melon_4)
    all_melons.append(melon_5)
    all_melons.append(melon_6)
    all_melons.append(melon_7)
    all_melons.append(melon_8)
    all_melons.append(melon_9)

    # for melon in all_melons:
    #     print(f'Melon {melon.name}')
    #     print(f'Melon type: {melon.code}')
    #     print(f'Shape rating: {melon.shape}')
    #     print(f'Color rating {melon.color}')
    #     print(f'Harvested from field {melon.field}')
    #     print(f'Harvested by {melon.harvester}')

    return all_melons 


# print(make_melon_type_lookup(make_melons))
# melons_by_id = make_melon_type_lookup(make_melons(make_melon_types()))
# melons_by_id = melons_by_id.keys()
# print(melons_by_id)
melons = make_melons(make_melon_types())



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        SOLD = '(CAN BE SOLD)'
        NOT_SOLD = '(NOT SELLABLE)'
        if melon.is_sellable():
            print(f'Harvested by {melon.harvester} from fied {melon.field} + {SOLD}')
        else:
            print(f'Harvested by {melon.harvester} from fied {melon.field} + {NOT_SOLD}')

print(get_sellability_report(melons))

#did make_melons end up working?