from Chances_chests import chances, chests
from properties import Tile

def Move(self, player, d1, d2):
    player.move(d1 + d2)
    spot = player.position
    property_landed = self.board[spot]
    print(f"{player.name} lands on space {spot}. It is {property_landed.name}.")

    if spot == 30:
        print(f"{player.name} lands on Go to Jail!")
        player.position = 10
        player.in_jail = True
        player.jail_turns = 0

    elif property_landed.type == 'street' or property_landed.type == 'station' or property_landed.type == 'company':
        print(f"Landed on {property_landed.name}. Price: Ls{property_landed.price}, Starting rent: Ls{property_landed.rent0}")
        if not property_landed.owner:
            choice = input(f"Do you want to buy {property_landed.name} for Ls{property_landed.price}? (yes/no): ").strip().lower()
            if choice == 'yes' and player.pay(property_landed.price):
                property_landed.owner = player
                player.properties.append(property_landed)
                print(f"{player.name} buys {property_landed.name}.")
                print(f"Jusu nauda: {player.money}")
            else:
                print("Tev babku nav!!")
                print(f"Tev ir Ls{player.money}")
                player.add_debt("bank", property_landed.price)
                print(f"{player.name} has taken a debt of Ls{property_landed.price} from the bank.")
        elif property_landed.owner != player:
            rent = property_landed.calculate_rent(d1+d2, property_landed.owner)
            if player.pay(rent):
                property_landed.owner.earn(rent)
                print(f"{player.name} pays Ls{rent} to {property_landed.owner.name}.")
            else:
                print(f"{player.name} cannot afford the rent!") #prikolas
                print(f"Jusu nauda: {player.money}")
                player.add_debt(property_landed.owner, rent)
                print(f"{player.name} has taken a debt of Ls{rent} from {property_landed.owner.name}.")


    elif property_landed.type == 'community chest': # when lands on community chest
        card = chests[0]
        print(card.text)
        chests.pop(0)
        chests.append(card)
        player.earn(card.money)
        id = card.id
        match id:

            case 1:
                steps = 40-spot
                player.move(steps)
                
            case 5:
                print("Now you have the pardon card!")
                player.properties.append(Tile("Pardon Card", 0, 0, 0, 0, 0, 0, 0, "", "pardon card"))

            case 6:
                player.position = 10
                player.in_jail = True
                player.jail_turns = 0

            case 7:
                for item in self.players:
                    if item != player:
                        item.money -= 50
                        player.money +=50
                        print(f"{item.name} paid {player.name} 50 latus")

            case 10:
                for item in self.players:
                    if item != player:
                        item.money -= 10
                        player.money +=10
                        print(f"{item.name} paid {player.name} 10 latus")

            case 15:
                houses = 0
                hotels = 0
                for item in player.properties:
                    if item.houses < 5:
                        houses += item.houses
                    else:
                        hotels += 1
                debt = houses*40+hotels*115
                print(f"You have to pay Ls{debt}")

                if player.pay(debt):
                    print(f"Jusu nauda: {player.money}")
                else:
                    print("Tev babku nav!")
                    print(f"Jusu nauda: {player.money}")
                    player.add_debt("bank", debt)
                    print(f"{player.name} has taken a debt of Ls{debt} from bank.")


    elif property_landed.type == 'chance': # when lands on chance
        card = chances[0]
        print(card.text)
        chances.pop(0)
        chances.append(card)
        player.earn(card.money)
        id = card.id

        match id:
            case 1:
                steps = 40-spot
                player.move(steps)

            case 2:
                if spot <= 24: #check vai ir pagajis garam
                    steps = 24-spot
                else:
                    steps = 64-spot
                player.move(steps)
                spot = player.position
                property_landed = self.board[spot]
                print(f"Landed on {property_landed.name}. Price: ${property_landed.price}, Starting rent: ${property_landed.rent0}")
                if not property_landed.owner:
                    choice = input(f"Do you want to buy {property_landed.name} for ${property_landed.price}? (yes/no): ").strip().lower()
                    if choice == 'yes':
                        if player.pay(property_landed.price):
                            property_landed.owner = player
                            player.properties.append(property_landed)
                            print(f"{player.name} buys {property_landed.name}.")
                            print(f"Jusu nauda: {player.money}")
                        else:
                            print("Tev babku nav!")
                            print(f"Tev ir Ls{player.money}")
                            player.add_debt(property_landed.owner, rent)
                            print(f"{player.name} has taken a debt of Ls{rent} from {property_landed.owner.name}.")

                elif property_landed.owner != player:
                    rent = property_landed.calculate_rent(0, property_landed.owner)
                    if player.pay(rent):
                        property_landed.owner.earn(rent)
                        print(f"{player.name} pays ${rent} to {property_landed.owner.name}.")
                        print(f"Jusu nauda: {player.money}")
                    else:
                        print(f"{player.name} cannot afford the rent!")
                        print(f"Jusu nauda: {player.money}")
                        player.add_debt(property_landed.owner, rent)
                        print(f"{player.name} has taken a debt of Ls{rent} from {property_landed.owner.name}.")
            
            case 3:
                steps = 39-spot
                player.move(steps)
                spot = player.position
                property_landed = self.board[spot]
                print(f"Landed on {property_landed.name}. Price: ${property_landed.price}, Starting rent: ${property_landed.rent0}")
                if not property_landed.owner:
                    choice = input(f"Do you want to buy {property_landed.name} for ${property_landed.price}? (yes/no): ").strip().lower()
                    if choice == 'yes':
                        if player.pay(property_landed.price):
                            property_landed.owner = player
                            player.properties.append(property_landed)
                            print(f"{player.name} buys {property_landed.name}.")
                            print(f"Jusu nauda: {player.money}")
                        else:
                            print("Tev babku nav!")
                            print(f"Tev ir Ls{player.money}")
                            player.add_debt("bank", property_landed.price)
                            print(f"{player.name} has taken a debt of Ls{property_landed.price} from the bank.")
                    
                elif property_landed.owner != player:
                    rent = property_landed.calculate_rent(0, property_landed.owner)
                    if player.pay(rent):
                        property_landed.owner.earn(rent)
                        print(f"{player.name} pays ${rent} to {property_landed.owner.name}.")
                        print(f"Jusu nauda: {player.money}")
                    else:
                        print(f"{player.name} cannot afford the rent!")
                        print(f"Jusu nauda: {player.money}")
                        player.add_debt(property_landed.owner, rent)
                        print(f"{player.name} has taken a debt of Ls{rent} from {property_landed.owner.name}.")

            case 4:
                if spot <= 11: #check vai ir pagajis garam
                    steps = 11-spot
                else:
                    steps = 51-spot
                player.move(steps)
                spot = player.position
                property_landed = self.board[spot]
                print(f"Landed on {property_landed.name}. Price: ${property_landed.price}, Starting rent: ${property_landed.rent0}")
                if not property_landed.owner:
                    choice = input(f"Do you want to buy {property_landed.name} for ${property_landed.price}? (yes/no): ").strip().lower()
                    if choice == 'yes':
                        if player.pay(property_landed.price):
                            property_landed.owner = player
                            player.properties.append(property_landed)
                            print(f"{player.name} buys {property_landed.name}.")
                            print(f"Jusu nauda: {player.money}")
                        else:
                            print("Tev babku nav!")
                            print(f"Tev ir Ls{player.money}")
                            player.add_debt("bank", property_landed.price)
                            print(f"{player.name} has taken a debt of Ls{property_landed.price} from the bank.")

                elif property_landed.owner != player:
                    rent = property_landed.calculate_rent(0, property_landed.owner)
                    if player.pay(rent):
                        property_landed.owner.earn(rent)
                        print(f"{player.name} pays ${rent} to {property_landed.owner.name}.")
                        print(f"Jusu nauda: {player.money}")
                    else:
                        print(f"{player.name} cannot afford the rent and is bankrupt!")
                        print(f"Jusu nauda: {player.money}")
                        player.add_debt(property_landed.owner, rent)
                        print(f"{player.name} has taken a debt of Ls{rent} from {property_landed.owner.name}.")
            
            case 5:
                atlikums = spot % 10
                if atlikums < 5:
                    steps = 5-atlikums
                else:
                    steps = 15-atlikums
                player.move(steps)
                spot = player.position
                property_landed = self.board[spot]
                print(f"Landed on {property_landed.name}. Price: ${property_landed.price}, Starting rent: ${property_landed.rent0}")
                if not property_landed.owner:
                    choice = input(f"Do you want to buy {property_landed.name} for ${property_landed.price}? (yes/no): ").strip().lower()
                    if choice == 'yes':
                        if player.pay(property_landed.price):
                            property_landed.owner = player
                            player.properties.append(property_landed)
                            print(f"{player.name} buys {property_landed.name}.")
                            print(f"Jusu nauda: {player.money}")
                        else:
                            print("Tev nav babku, bet tas nekas")
                            print(f"Tev ir Ls{player.money}")
                            player.add_debt("bank", property_landed.price)
                            print(f"{player.name} has taken a debt of Ls{property_landed.price} from the bank.")

                elif property_landed.owner != player:
                    rent = property_landed.calculate_rent(0, property_landed.owner)
                    if player.pay(rent):
                        property_landed.owner.earn(rent)
                        print(f"{player.name} pays ${rent} to {property_landed.owner.name}.")
                        print(f"Jusu nauda: {player.money}")
                    else:
                        print(f"{player.name} cannot afford the rent and is bankrupt!") #prikolas
                        print(f"Jusu nauda: {player.money}")
                        player.add_debt(property_landed.owner, rent)
                        print(f"{player.name} has taken a debt of Ls{rent} from {property_landed.owner.name}.")

            case 6:
                atlikums = spot % 10
                if atlikums < 5:
                    steps = 5-atlikums
                else:
                    steps = 15-atlikums
                player.move(steps)
                spot = player.position
                property_landed = self.board[spot]
                print(property_landed.owner)

                print(f"Landed on {property_landed.name}. Price: ${property_landed.price}, Starting rent: ${property_landed.rent0}")
                if not property_landed.owner:
                    choice = input(f"Do you want to buy {property_landed.name} for ${property_landed.price}? (yes/no): ").strip().lower()
                    if choice == 'yes':
                        if player.pay(property_landed.price):
                            property_landed.owner = player
                            player.properties.append(property_landed)
                            print(f"{player.name} buys {property_landed.name}.")
                            print(f"Jusu nauda: {player.money}")
                        else:
                            print(f"{player.name} cannot afford the rent and is bankrupt!") #prikolas
                            print(f"Jusu nauda: {player.money}")
                            player.add_debt("bank", property_landed.price)
                            print(f"{player.name} has taken a debt of Ls{property_landed.price} from the bank.")

                elif property_landed.owner != player:
                    rent = property_landed.calculate_rent(0, property_landed.owner)
                    if player.pay(rent):
                        property_landed.owner.earn(rent)
                        print(f"{player.name} pays ${rent} to {property_landed.owner.name}.")
                        print(f"Jusu nauda: {player.money}")
                    else:
                        print(f"{player.name} cannot afford the rent!")
                        print(f"Jusu nauda: {player.money}")
                        player.add_debt(property_landed.owner, rent)
                        print(f"{player.name} has taken a debt of Ls{rent} from {property_landed.owner.name}.")

            case 7:
                    if spot == 7:
                        steps = 5
                    elif spot == 22:
                        steps = 6
                    elif spot == 36:
                        steps = 16
                    player.move(steps)
                    spot = player.position
                    property_landed = self.board[spot]
                    print(f"Landed on {property_landed.name}. Price: ${property_landed.price}, Starting rent: ${property_landed.rent0}")
                    if not property_landed.owner:
                        choice = input(f"Do you want to buy {property_landed.name} for ${property_landed.price}? (yes/no): ").strip().lower()
                        if choice == 'yes':
                            if player.pay(property_landed.price):
                                property_landed.owner = player
                                player.properties.append(property_landed)
                                print(f"{player.name} buys {property_landed.name}.")
                                print(f"Jusu nauda: {player.money}")
                            else:
                                print(f"{player.name} cannot afford the rent!") #prikolas
                                print(f"Jusu nauda: {player.money}")
                                player.add_debt("bank", property_landed.price)
                                print(f"{player.name} has taken a debt of Ls{property_landed.price} from the bank.")

                    elif property_landed.owner != player:
                        input("Press Enter to roll the dice...")
                        d1, d2 = self.roll_dice()
                        print(f"{player.name} rolls {d1} and {d2}")
                        rent = property_landed.calculate_rent(d1+d2, property_landed.owner)
                        if player.pay(rent):
                            property_landed.owner.earn(rent)
                            print(f"{player.name} pays ${rent} to {property_landed.owner.name}.")
                            print(f"Jusu nauda: {player.money}")
                        else:
                            print(f"{player.name} cannot afford the rent and is bankrupt!") #prikolas
                            print(f"Jusu nauda: {player.money}")
                            player.add_debt(property_landed.owner, rent)
                            print(f"{player.name} has taken a debt of Ls{rent} from {property_landed.owner.name}.")

                            
            case 9:
                print("Now you have the pardon card!")
                player.properties.append(Tile("Pardon Card", 0, 0, 0, 0, 0, 0, 0, "", "pardon card"))

            case 10:
                player.move(-3)
                spot = player.position
                property_landed = self.board[spot]
                print(f"{player.name} lands on space {spot}. It is {property_landed.name}.")

                if property_landed.type == 'street' or property_landed.type == 'station' or property_landed.type == 'company':
                    print(f"Landed on {property_landed.name}. Price: ${property_landed.price}, Starting rent: ${property_landed.rent0}")
                    if not property_landed.owner:
                        choice = input(f"Do you want to buy {property_landed.name} for ${property_landed.price}? (yes/no): ").strip().lower()
                        if choice == 'yes':
                            if player.pay(property_landed.price):
                                property_landed.owner = player
                                player.properties.append(property_landed)
                                print(f"{player.name} buys {property_landed.name}.")
                                print(f"Jusu nauda: {player.money}")
                            else:
                                print(f"{player.name} cannot afford the rent and is bankrupt!") #prikolas
                                print(f"Jusu nauda: {player.money}")
                                player.add_debt("bank", property_landed.price)
                                print(f"{player.name} has taken a debt of Ls{property_landed.price} from the bank.")

                    elif property_landed.owner != player:
                        rent = property_landed.calculate_rent(d1+d2, property_landed.owner)
                        if player.pay(rent):
                            property_landed.owner.earn(rent)
                            print(f"{player.name} pays ${rent} to {property_landed.owner.name}.")
                            print(f"Jusu nauda: {player.money}")
                        else:
                            print(f"{player.name} cannot afford the rent and is bankrupt!") #prikolas
                            print(f"Jusu nauda: {player.money}")
                            player.add_debt(property_landed.owner, rent)
                            print(f"{player.name} has taken a debt of Ls{rent} from {property_landed.owner.name}.")

                elif property_landed.type == "tax":
                    if player.pay(property_landed.price):
                        print("Kartochka tika pienemta, esi samaksajis "+str(property_landed.price)+" latus")
                    else:
                        print(f"Jusu nauda: {player.money}")
                        print("Tev nepietiek naudas, bomzhs esi!")
                        player.add_debt("bank", property_landed.price)
                        print(f"{player.name} has taken a debt of Ls{property_landed.price} from the bank.")


            case 11:
                player.position = 10
                player.in_jail = True
                player.jail_turns = 0

            case 12:
                houses = 0
                hotels = 0
                for item in player.properties:
                    if item.houses < 5:
                        houses += item.houses
                    else:
                        hotels += 1
                debt = houses*25+hotels*100
                print(f"You have to pay Ls{debt}")
                if player.pay(debt):
                    print("Tranzakcija tika izpildita!")
                else:
                    print("Tev babku nav, dolbaeb!")
                    print(f"Jusu nauda: {player.money}")
                    player.add_debt("bank", debt)
                    print(f"{player.name} has taken a debt of Ls{debt} from the bank.")
            case 14:
                if spot == 7:
                    steps = 38
                elif spot == 22:
                    steps = 23
                elif spot == 36:
                    steps = 9
                player.move(steps)
                spot = player.position
                property_landed = self.board[spot]
                print(f"Landed on {property_landed.name}. Price: ${property_landed.price}, Starting rent: ${property_landed.rent0}")
                if not property_landed.owner:
                    choice = input(f"Do you want to buy {property_landed.name} for ${property_landed.price}? (yes/no): ").strip().lower()
                    if choice == 'yes':
                        if player.pay(property_landed.price):
                            property_landed.owner = player
                            player.properties.append(property_landed)
                            print(f"{player.name} buys {property_landed.name}.")
                            print(f"Jusu nauda: {player.money}")
                        else:
                            print(f"{player.name} cannot afford the rent and is bankrupt!") #prikolas
                            print(f"Jusu nauda: {player.money}")
                            player.add_debt("bank", property_landed.price)
                            print(f"{player.name} has taken a debt of Ls{property_landed.price} from the bank.")
                elif property_landed.owner != player:
                    input("Press Enter to roll the dice...")
                    d1, d2 = self.roll_dice()
                    print(f"{player.name} rolls {d1} and {d2}")
                    rent = property_landed.calculate_rent(d1+d2, property_landed.owner)
                    if player.pay(rent):
                        property_landed.owner.earn(rent)
                        print(f"{player.name} pays ${rent} to {property_landed.owner.name}.")
                        print(f"Jusu nauda: {player.money}")
                    else:
                        print(f"{player.name} cannot afford the rent and is bankrupt!") #prikolas
                        print(f"Jusu nauda: {player.money}")
                        player.add_debt(property_landed.owner, rent)
                        print(f"{player.name} has taken a debt of Ls{rent} from {property_landed.owner.name}.")

            case 15:
                for item in self.players:
                    if item != player:
                        item.money += 50
                        player.money -=50
                        print(f"{player.name} paid {item.name} 50 latus")
    elif property_landed.type == "tax":
        print(f"Pay Ls{property_landed.price}")
        if player.pay(property_landed.price):
            print("Kartochka tika pienemta, esi brivs")
        else:
            print(f"Jusu nauda: {player.money}")
            print("Tu bomzhs esi!")
            player.add_debt("bank", property_landed.price)
            print(f"{player.name} has taken a debt of Ls{property_landed.price} from the bank.")