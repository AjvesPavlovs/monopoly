class Tile:
    def __init__(self, name, price, rent0, rent1, rent2, rent3, rent4, rent5, color, type):
        self.name = name
        self.price = price
        self.rent0 = rent0
        self.rent1 = rent1
        self.rent2 = rent2
        self.rent3 = rent3
        self.rent4 = rent4
        self.rent5 = rent5
        self.color = color
        self.type = type
        self.owner = None
        self.houses = 0
        self.hotel = False
        self.price_per_house = 0
        self.mortgaged = False

        if self.color == "brown" or self.color == "light_blue":
            self.price_per_house = 50
        if self.color == "purple" or self.color == "orange":
            self.price_per_house = 100
        if self.color == "red" or self.color == "yellow":
            self.price_per_house = 150
        if self.color == "green" or self.color == "darb_blue":
            self.price_per_house = 200

    def calculate_rent(self, number, owner):
        rent = 0
        if self.mortgaged:
            rent = 0
        else:
            if self.type == "street":
                match self.houses:
                    case 0:
                        set = False
                        rent = self.rent0
                        number_of_color = 0
                        if self.owner:       
                            for item in owner.properties:
                                if item.color == self.color:
                                    number_of_color += 1
                            if self.color == "brown" or self.color == "blue":
                                if number_of_color == 2:
                                    set = True
                            else:
                                if number_of_color ==  3:
                                    set = True
                            if set:
                                rent = self.rent0*2

                    case 1:
                        rent = self.rent1
                    case 2:
                        rent = self.rent2
                    case 3:
                        rent = self.rent3
                    case 4:
                        rent = self.rent4
                    case 5:
                        rent = self.rent5
            elif self.type == "station":
                number_of_stations = 0
                if self.owner:       
                    for item in owner.properties:
                        if item.type == "station":
                            number_of_stations += 1

                rent = self.rent0 * (2**(number_of_stations-1))
            elif self.type == "company":
                number_of_companies = 0
                if self.owner:       
                    for item in self.properties:
                        if item.type == "company":
                            number_of_companies += 1
                if number_of_companies == 1:
                    rent = number*4
                else:
                    rent = number*10
        return rent

list_of_tiles = [
Tile("Start", 0, 0, 0, 0, 0, 0, 0, "", "free space"),
Tile("Mediterranian Avenue", 60, 2, 10, 30, 90, 160, 250, "brown", "street"),
Tile("Community Chest", 0, 0, 0, 0, 0, 0, 0, "", "community chest"),
Tile("Baltic Avenue", 60, 4, 20, 60, 180, 320, 450, "brown", "street"),
Tile("Income Tax", 200, 0, 0, 0, 0, 0, 0, "", "tax"),
Tile("Reading Railroad", 200, 25, 0, 0, 0, 0, 0, "", "station"),
Tile("Central Avenue", 100, 6, 30, 90, 270, 400, 550, "light blue", "street"),
Tile("Chance", 0, 0, 0, 0, 0, 0, 0, "", "chance"),
Tile("Vermont Avenue", 100, 6, 30, 90, 270, 400, 550, "light blue", "street"),
Tile("Connecticut Avenue", 120, 8, 40, 100, 300, 450, 600, "light blue", "street"),
Tile("Just Visiting / Jail", 0, 0, 0, 0, 0, 0, 0, "", "free space"),
Tile("St. Charles Place", 140, 10, 50, 150, 450, 625, 750, "purple", "street"),
Tile("Electric Company", 150, 'tu jau zini', 0, 0, 0, 0, 0, "", "company"),
Tile("States Avenue", 140, 10, 50, 150, 450, 625, 750, "purple", "street"),
Tile("Virginia Avenue", 160, 12, 60, 180, 500, 700, 900, "purple", "street"),
Tile("Pensylvania Railroad", 200, 25, 0, 0, 0, 0, 0, "", "station"),
Tile("St. James Place", 180, 14, 70, 200, 550, 750, 950, "orange", "street"),
Tile("Community Chest", 0, 0, 0, 0, 0, 0, 0, "", "community chest"),
Tile("Tenesee Avenue", 180, 14, 70, 200, 550, 750, 950, "orange", "street"),
Tile("New York Avenue", 200, 16, 80, 220, 600, 800, 1000, "orange", "street"),
Tile("Free Parking", 0, 0, 0, 0, 0, 0, 0, "", "free space"),
Tile("Kentucky Avenue", 220, 18, 90, 250, 700, 875, 1050, "red", "street"),
Tile("Chance", 0, 0, 0, 0, 0, 0, 0, "", "chance"),
Tile("Indiana Avenue", 220, 18, 90, 250, 700, 875, 1050, "red", "street"),
Tile("Illinois Avenue", 240, 20, 100, 300, 750, 925, 1100, "red", "street"),
Tile("B. & O. Railroad", 200, 25, 0, 0, 0, 0, 0, "", "station"),
Tile("Atlantic Avenue", 260, 22, 110, 330, 800, 975, 1150, "yellow", "street"),
Tile("Ventnor Avenue", 260, 22, 110, 330, 800, 975, 1150, "yellow", "street"),
Tile("Water Company", 150, 'tu jau zini', 0, 0, 0, 0, 0, "", "company"),
Tile("Marvin Gardens", 280, 24, 120, 360, 850, 1025, 1200, "yellow", "street"),
Tile("Go To Jail", 0, 0, 0, 0, 0, 0, 0, "", "free space"), # sutisana uz cietumu strada laikam
Tile("Pacific Avenue", 300, 26, 130, 390, 900, 1100, 1275, "green", "street"),
Tile("North Carolina Avenue", 300, 26, 130, 390, 900, 1100, 1275, "green", "street"),
Tile("Community Chest", 0, 0, 0, 0, 0, 0, 0, "", "community chest"),
Tile("Pensylvania Avenue", 320, 28, 150, 450, 1000, 1200, 1400, "green", "street"),
Tile("Short Line", 200, 25, 0, 0, 0, 0, 0, "", "station"),
Tile("Chance", 0, 0, 0, 0, 0, 0, 0, "", "chance"),
Tile("Park Place", 350, 35, 175, 500, 1100, 1300, 1500, "blue", "street"),
Tile("Luxury Tax", 100, 0, 0, 0, 0, 0, 0, "", "tax"),
Tile("Boardwalk", 400, 50, 200, 600, 1400, 1700, 2000, "blue", "street")
]
