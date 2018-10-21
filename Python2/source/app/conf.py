'''
configurationals
'''

class SpecificationChoices(object):
    STRUCTURE = 1
    KITCHENS = 2
    MAIN_BATHROOMS = 3
    BALCONIES = 4
    WALLS = 5
    FLOORS = 6
    CIELINGS = 7
    CUPBOARDS = 8
    HEATING = 9
    LIGHTINING =10
    LIFTS = 11
    JOINERY =12
    SPECIFICATION_CHOICES = (
        (STRUCTURE, 'Structure'),
        (KITCHENS, 'Kitchens'),
        (MAIN_BATHROOMS, 'Main Bathrooms'),
        (BALCONIES, 'Balconies'),
        (WALLS, 'Walls'),
        (FLOORS, 'Floors'),
        (CIELINGS, 'Cielings'),
        (CUPBOARDS, 'Cupboards'),
        (HEATING, 'Heating/Ventilation'),
        (LIGHTINING, 'Lightining/Electrical'),
        (LIFTS, 'Lifts'),
        (JOINERY, 'Joinery')
    )

class PropertyTypeChoices(object):
    APARTMENT = 1
    INDEPENDENT_HOUSE = 2
    HOSTEL = 3
    PAYING_GUEST = 4
    GUEST_HOUSE = 5
    HOLIDAY_HOME = 6
    FARM_HOUSE = 7
    RESIDENTIAL_LAND = 8
    SHOP = 9
    SHOWROOM = 10
    OFFICE_SPACE = 11
    SHOPPING_MALL_SPACE = 12
    HOTEL = 13
    INDUSTRIAL_BUILDING = 14
    BUSINESS_CENTER = 15
    PROPERTY_TYPE_CHOICES = (
        (APARTMENT, 'Apartment/Flat'),
        (INDEPENDENT_HOUSE, 'Independent House'),
        (HOSTEL, 'Hostel'),
        (PAYING_GUEST, 'Paying Guest'),
        (GUEST_HOUSE, 'Guest House'),
        (HOLIDAY_HOME, 'Holiday Home'),
        (FARM_HOUSE, 'Farm House'),
        (RESIDENTIAL_LAND, 'Residential Plot/Land'),
        (SHOP, 'Shop'),
        (SHOWROOM, 'Showroom'),
        (OFFICE_SPACE, 'Office Space'),
        (SHOPPING_MALL_SPACE, 'Shopping Mall Space'),
        (HOTEL, 'Hotel/Resort'),
        (INDUSTRIAL_BUILDING, 'Industrial Building'),
        (BUSINESS_CENTER, 'Business Center'),
    )