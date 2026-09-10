from random import shuffle

class card:
    def __init__(self, id, text, money):
        self.id = id
        self.text = text
        self.money = money

com_chest1 = card(1, 'Advance to "Go". (Collect Ls200)', 0) #1
com_chest2 = card(2, 'Bank error in your favor. Collect Ls200', 200)
com_chest3 = card(3, "Doctor's fees. Pay Ls50.", -50)
com_chest4 = card(4, "From sale of stock you get Ls50.", 50)
com_chest5 = card(5, "Get Out of Jail Free", 0) #5
com_chest6 = card(6, "Go to Jail.", 0) #6
com_chest7 = card(7, "Grand Opera Night. Collect Ls50 from every player for opening night seats.", 0) #7
com_chest8 = card(8, "Holiday Fund matures. Receive Ls100.", 100)
com_chest9 = card(9, "Income tax refund. Collect LS20.", 20)
com_chest10 = card(10, "It is your birthday. Collect LS10 from every player.", 0) #10
com_chest11 = card(11, "Life insurance matures – Collect Ls100.", 100)
com_chest12 = card(12, "Hospital Fees. Pay Ls50.", -50)
com_chest13 = card(13, "School fees. Pay Ls50.", -50)
com_chest14 = card(14, "Receive Ls25 consultancy fee.", 25)
com_chest15 = card(15, "You are assessed for street repairs: Pay Ls40 per house and Ls115 per hotel you own.", 0) #15
com_chest16 = card(16, "You have won second prize in a beauty contest. Collect Ls10.", 10)
com_chest17 = card(17, "You inherit Ls100.", 100)

chests = [com_chest1,com_chest2,com_chest3,com_chest4,com_chest5,com_chest6,com_chest7,com_chest8,com_chest9,com_chest10,com_chest11,com_chest12,com_chest13,com_chest14,com_chest15,com_chest16,com_chest17]
shuffle(chests)

chance1 = card(1, "Advance to Go (Collect Ls200).", 0) #1
chance2 = card(2, "Advance to Illinois Avenue. If you pass Go, collect Ls200", 0) #2
chance3 = card(3, "Advance to Boardwalk. If you pass Go, collect Ls200", 0) #3
chance4 = card(4, "Advance to St. Charles Place. If you pass Go, collect Ls200", 0) #4
chance5 = card(5, "Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled.", 0) #5 or 6
chance6 = card(6, "Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled.", 0) #5 or 6
chance7 = card(7, "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.", 0) #7
chance8 = card(8, "Bank pays you dividend of Ls50", 50)
chance9 = card(9, "Get Out of Jail Free.", 0) #9
chance10 = card(10, "Go Back 3 Spaces.", 0) #10
chance11 = card(11, "Go to Jail. Go directly to Jail, do not pass Go, do not collect Ls200.", 0) #11
chance12 = card(12, "Make general repairs on all your property. For each house pay Ls25. For each hotel pay Ls100.", 0) #12
chance13 = card(13, "Speeding fine Ls15.", -15)
chance14 = card(14, "Take a trip to Reading Railroad. If you pass Go, collect Ls200.", 0) #14
chance15 = card(15, "You have been elected Chairman of the Board. Pay each player Ls50.", 0) #15
chance16 = card(16, "Your building loan matures. Collect Ls150.", 150)

chances = [chance1,chance2,chance3,chance4,chance5,chance6,chance7,chance8,chance9,chance10,chance11,chance12,chance13,chance14,chance15,chance16]
shuffle(chances)
