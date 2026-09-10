import MonopolyGame

def main():
    print("Welcome to Monopoly!")
    num_players = int(input("Enter number of players: "))
    players = [input(f"Enter name for player {i+1}: ") for i in range(num_players)]
    game = MonopolyGame.MonopolyGame(players)
    game.play_game()

if __name__ == "__main__":
    main()
input()

#TO DO: selling in pardon card for 50Ls, situatuation when player tries to trade properties with houses 
# Cancel trade and 0 property trade if needed