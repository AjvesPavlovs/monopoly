from random import randint
from properties import list_of_tiles, Tile
from Chances_chests import chances, chests
from Player import Player
from Move import Move
#nauda, kad nepietiek

class MonopolyGame:
    def __init__(self, players):
        self.players = [Player(name) for name in players]
        self.board = self.create_board()
        self.current_player_index = 0
        self.victory = False

    def create_board(self):
        return list_of_tiles

    def roll_dice(self):
        # return 2, 2
        return randint(1, 6), randint(1, 6)
    def find_player(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None
    
    def take_turn(self):
        # print(self.current_player_index)
        player = self.players[self.current_player_index]

        if not player.alive:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
        else:
            print(f"\n--- {player.name}'s Turn ---")
            print("kada darbiba? (1 - mest kaulus, 2 - maksat cietuma (50 latu), 3 - parvaldit ipasumu (hatas, iekilasana), 4 - trade, 5 - bankrots, 6 - pabeigt gajienu, 7 - atmaksat paradu): ")
            action = input()     
            if player.in_jail and not player.rolled_dice:
                if player.jail_turns < 3:
                    if action == "1": # Dice rolling in prison
                        if not player.rolled_dice:
                            d1, d2 = self.roll_dice()
                            print(F"{player.name} rolls {d1} and {d2}")
                            player.rolled_dice = True
                        
                            if d1 == d2:
                                player.in_jail = False
                                player.jail_turns = 0
                                print(f"{player.name} rolls doubles and gets out of jail.")
                                player.rolled_dice = True
                                Move(self, player, d1, d2)

                            else:
                                player.jail_turns += 1
                                print(f"{player.name} is still in jail (Turn {player.jail_turns}).")
                        else:
                            print("tu to jau dariji")
                        
                    elif action == "2": # Pay for prison
                        if player.pay(50):
                            print(f"{player.name} leaves the jail")
                            print(f"Jusu nauda: {player.money}")
                            player.in_jail = False
                            player.rolled_dice = True
                        else:
                            print("Nepietiek lidzeklu uz kartes!")
                            print(f"Jusu nauda: {player.money}")

                else:
                    print(f"{player.name} leaves the jail")
                    player.in_jail = False  
            elif action == "1": # Regular dice rolling
                if not player.rolled_dice:
                    # input("Press Enter to roll the dice...")
                    d1, d2 = self.roll_dice()
                    print(f"{player.name} rolls {d1} and {d2}")

                    if d1 == d2: # praverka uz double
                        player.double_turns += 1
                        # print(player.double_turns)
                    else: 
                        player.rolled_dice = True
                    if player.double_turns == 3:
                        player.position = 10
                        player.in_jail = True
                        player.jail_turns = 0
                        player.double_turns = 0
                        print("Tu esi cietuma!")
                        player.rolled_dice = True
                    else:
                        Move(self, player, d1, d2)


                else:
                    print("Nedrikst")
        
            elif action == "3": # property management
                print("Jusu ipasumi:")
                counter = 1
                for item in player.properties:
                    print(f"{counter} - {item.name}")
                    counter += 1
                if player.properties:
                    index = int(input(f"Izvelaties poziciju, ko mainisiet! (no 1 lidz {len(player.properties)})"))
                    if index >= 1 and index <= len(player.properties):
                        sel_property = player.properties[index-1]
                        
                        print(f"Jus izvlejaties {sel_property.name}.")

                        property_action = input("Izvelieties, ko darisiet! (1 - taisit majas, 2 - jaunkt nost majas, 3 - iekilat, 4 - atkilat, 5 - atpakal)")
                        
                        if property_action == "1": # house building
                            if sel_property.type == "street":
                                set = False
                                number_of_color = 0 
                                for item in player.properties:
                                    if item.color == sel_property.color:
                                        number_of_color += 1
                                if sel_property.color == "brown" or sel_property.color == "blue":
                                    if number_of_color == 2:
                                        set = True
                                else:
                                    if number_of_color ==  3:
                                        set = True
                                if set:
                                    print(f"Te ir uzceltas {sel_property.houses} majas")
                                    print(f"Cena par maju ir {sel_property.price_per_house}")
                                    if sel_property.houses >= 5:
                                        ans = input("Pirksiet maju?(y/n)")
                                        if ans == "y":
                                            if player.money >= sel_property.price_per_house:
                                                player.pay(sel_property.price_per_house)
                                                sel_property.houses += 1
                                                print(f"Jusu nauda: {player.money}")
                                            else:
                                                print("Nabag, tev nav naudas!")
                                                print(f"Jusu nauda: {player.money}")
                                        else:
                                            print("ok")
                                    else:
                                        print("Tev jau ir hotelciks, debiliki")
                                else:
                                    print("Tev nav komplekta, dauni!")
                            else:
                                print("To var darit tikai ar ielam, kuram krasas. Sharish?")
                        if property_action == "2": # house dismantling
                                if sel_property.type == "street":
                                    set = False
                                    number_of_color = 0 
                                    for item in player.properties:
                                        if item.color == sel_property.color:
                                            number_of_color += 1
                                    if sel_property.color == "brown" or sel_property.color == "blue":
                                        if number_of_color == 2:
                                            set = True
                                    else:
                                        if number_of_color ==  3:
                                            set = True
                                    if set:
                                        print(f"Te ir uzceltas {sel_property.houses} majas")
                                        print(f"Atmaksa par majas nojauksanu ir {sel_property.price_per_house/2}")
                                        if sel_property.houses > 0:
                                            ans = input("Jauksiet nost maju?(y/n)")
                                            if ans == "y":
                                                if player.money >= sel_property.price_per_house:
                                                    player.earn(sel_property.price_per_house/2)
                                                    sel_property.houses -= 1
                                                else:
                                                    print("Nabag, tev nav naudas!")
                                            else:
                                                print("ok")
                                        else:
                                            print("Dalbajob, tev nav maju")
                                    else:
                                        print("Tev nav komplekta, dauni!")
                                else:
                                    print("To var darit tikai ar ielam, kuram krasas. Sharish?")
                        
                        if property_action == "3": #Mortgage
                            if sel_property.houses == 0 or sel_property.name == "Pardon card":
                                if sel_property.name == "Pardon card":
                                    print("Dabusi 50 Latus ok? (y/n)")
                                    if input() == "y":
                                        player.earn(50)
                                        player.properties.remove(sel_property)
                                else:
                                    resp = input(f"Atmaksa bus {sel_property.price/2}. Turpinat?(y/n)")
                                    if resp == "y":
                                        sel_property.mortgaged = True
                                        player.earn(sel_property.price/2)
                                    else:
                                        print("Nu i nevajag")
                            else:
                                print("Par daudz maju!")
                        elif property_action == "4": # Unmortgage
                            if sel_property.mortgaged:
                                unmortgage_money = round((sel_property.price/2)*1.1)
                                print(f"Cena bir {unmortgage_money}")
                                ans = input("Taisam sito sudu?(y/n)")
                                if ans == "y":
                                    if player.pay(unmortgage_money):
                                        print(f"Du hast Ls{player.money}")
                                    else:
                                        print("Tev naudas nav!")
                                        print(f"Du hast Ls{player.money}")
                            else:
                                print("Aleeg, tavs izveletais ipasums nav nezmaz iekilats")
                        elif property_action == "5":
                            pass
                        else:
                            print("Baigi smiekligs juties?")
                else:
                    print("Tev nav ipasumu!")

            elif action == "5": # Bankrupt
                confirmation = input("Tocna? (y/n): ")
                if confirmation.lower() == 'y':
                    for item in player.properties:
                        item.owner = None
                        item.houses = 0
                        item.hotel = False
                        item.mortgaged = False

                    player.alive = False
                    print("Bankrots")

                    player.rolled_dice = True
                    player.next_turn = True
                    try:    
                        print(f"{player.name} now has Ls{player.money}")
                        player.rolled_dice = True
                        player.next_turn = True

                        num_of_players = 0
                        for item in self.players: # Victory
                            if item.alive:
                                num_of_players += 1
                        if num_of_players == 1:
                            self.victory = True
                    except Exception:
                        print("Nav tada player")

            elif action == "6": # Next turn
                if player.rolled_dice:
                    if len(player.debts) < 1:
                        player.next_turn = True
                        try:    
                            print(f"{player.name} now has Ls{player.money}")
                            player.rolled_dice = False
                            player.next_turn = False
                            self.current_player_index = (self.current_player_index + 1) % len(self.players)
                        except Exception:
                            print("Nav tada player")
                    else:
                        print("Samaksa parudus, chuvak!")
                else:
                    print("Tu vel nepagaji, chel")
            elif action == "7": # Pay off debts
                if player.debts:
                    print("Jusu paradi:")
                    for i, debt in enumerate(player.debts):
                        print(f"{i + 1} - {debt.recipient}: Ls{debt.amount}")
                    index = int(input("Izvelieties, kuru paradu gribat atmaksat: ")) - 1
                    if 0 <= index < len(player.debts):
                        debt = player.debts[index]
                        if player.pay(debt.amount):
                            recipient = self.find_player(debt.recipient)
                            if recipient:
                                recipient.earn(debt.amount)
                            print(f"Parads {debt.recipient} ir atmaksats!")
                            player.debts.pop(index)
                        else:
                            print("Tev nav naudas, lai atmaksa paradu!")
                    else:
                        print("Neponel")
                else:
                    print("Tev nav paradu")

            elif action == "4": # Trade
                print("Taisit trade")
                print("Jusu ipasumi:")
                counter = 1
                for item in player.properties:
                    if item.houses == 0:
                        print(f"{counter} - {item.name}")
                        counter += 1
                    
                sel_properties_provide = []
                trade_money_provide = 0
                sel_properties_request = []
                if player.properties:
                    input1 = input(f"Izvelaties pozicijas, ko piedavasiet! (no 1 lidz {len(player.properties)}) vienu no otra ipasumus atdaliet ar space!(Ipasumus ar majam nedrikst tradot, tos nerada). Ja negribi piedavat ipasumus, tad raksti 0. Raksiti cancel, lai atceltu")
                    if input1 == "cancel":
                        print("Trade atcelts")
                        return
                    else:
                        indexes = input1.split(' ')
                        for index in indexes:
                            if int(index) >= 1 and int(index) <= len(player.properties):
                                if player.properties[int(index)-1].houses > 0:
                                    print("Es tak tev teicu, ka nedrikst!")
                                elif int(index) == 0:
                                    pass
                                else:
                                    sel_properties_provide.append(player.properties[int(index)-1])
                else:
                    print(f"{player.name} nav ipasumu, ar ko taisit trade!")

                print("Cik naudas piedavasi?")

                norm_sum = False
                while not norm_sum:
                    trade_money_provide = int(input("Naudas summa: "))
                    try:
                        if trade_money_provide < 0:
                            print("Nauda nevar but mazaka par 0!")
                        elif trade_money_provide > player.money:
                            print("Tev nav tik daudz naudas!")
                        else:
                            norm_sum = True
                    except ValueError:
                        print("Neponel. Ludzu ievadi skaitli!")

                print(f"Jusu piedavatie ipasumi: ")
                for i, prop in enumerate(sel_properties_provide):
                    print(f"{i + 1} - {prop.name}")
                print(f"+{trade_money_provide} lati")
                trade_player_name = input("Ar kuru gribat taisit trade? ")
                trade_player = self.find_player(trade_player_name)

                sel_properties_request = []
                trade_money_request = 0
                if trade_player:
                    print(f"{trade_player.name} ipasumi (tur, kur nav maju):")
                    counter = 1
                    for item in trade_player.properties:
                        if item.houses == 0:
                            print(f"{counter} - {item.name}")
                            counter += 1
                    if trade_player.properties:
                        input_trades = input(f"Izvelaties pozicijas, ko gribat no {trade_player.name} ipasumiem! (no 1 lidz {len(trade_player.properties)}) vienu no otra ipasumus atdaliet ar space!(Ipasumus ar majam nedrikst tradot. Ja nevajag ielas, tad wtf, ko tu dari? Anyways, ja negribi ipasumus, tad raksti 0. Cancel, lai atceltu trade)")
                        indexes_trades = input_trades.split(' ')
                        if input_trades == "cancel":
                            print("Trade atcelts")
                            return
                        else:
                            for index in indexes_trades:
                                if int(index) >= 1 and int(index) <= len(trade_player.properties):
                                    if trade_player.properties[int(index)-1].houses > 0:
                                        print("Zbal tu")
                                    elif int(index) == 0:
                                        pass
                                    else:
                                        sel_properties_request.append(trade_player.properties[int(index)-1])
                    else:
                        print(f"{trade_player.name} nav ipasumu, ar ko taisit trade!")

                    norm_sum = False
                    while not norm_sum:
                        print("Cik naudas prasisi?")
                        trade_money_request = int(input("Naudas summa: "))
                        if trade_money_request < 0:
                            print("Nauda nevar but mazaka par 0!")
                        elif trade_money_request > player.money:
                            print("Tev nav tik daudz naudas!")
                        else:
                            norm_sum = True
                    if trade_money_request < 0:
                        print("Nauda nevar but mazaka par 0!")
                    elif trade_money_request > trade_player.money:
                        print("Vinam (mby vinai, es hz) nav tik daudz naudas!")

                    print(f"Jusu piedavatie ipasumi: ")
                    for i, prop in enumerate(sel_properties_provide):
                        print(f"{i + 1} - {prop.name}")
                    print(f"+{trade_money_provide} lati")

                    print(f"Jusu pieprasitie ipasumi: ")
                    for i, prop in enumerate(sel_properties_request):
                        print(f"{i + 1} - {prop.name}")
                    print(f"-{trade_money_request} lati")
                    print("Sutit trade? (y/n): ")
                    ans = input()
                    if ans.lower() == 'y':
                        accept_trade = input(f"{trade_player.name}, vai piekritasiet trade? (y/n): ")
                        if accept_trade.lower() == 'y':
                            trade_player.pay(trade_money_request)
                            player.earn(trade_money_request)
                            player.pay(trade_money_provide)
                            trade_player.earn(trade_money_provide)
                            for prop in sel_properties_provide:
                                prop.owner = trade_player
                                trade_player.properties.append(prop)
                                player.properties.remove(prop)
                            for prop in sel_properties_request:
                                prop.owner = player
                                player.properties.append(prop)
                                trade_player.properties.remove(prop)
                            print(f"Trade starp {player.name} un {trade_player.name} ir veikts!")
                        else:
                            print("Trade atcelts. Prikiņ, tu šitik ilgi čakarējies, lai tas neonotku")
                else:
                    print("Spēlētājs nav atrasts.")


    def play_game(self):
        while True:
            if not self.victory:
                self.take_turn()
            else:
                print("Speles beigas!")
                print("GG")
                for player in self.players:
                    if player.alive:
                        print(f"{player.name} uzvareja!")
                break
            # cont = input("Continue playing? (yes/no): ").strip().lower()
            # if cont != 'yes':
            #     break

