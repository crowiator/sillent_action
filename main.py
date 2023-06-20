import os

def winner(bidders):
    max = 0
    winner = ""
    for key in bidders:
        if max < bidders[key]:
            max = bidders[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${max}")

def print_logo():
    auction_logo = '''
                             ___________
                             \         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________\\
                             `'-------'`
                           .-------------.
                          /_______________\\
    '''
    print(auction_logo)
    print("Welcome to the secret auction program.")
def main():
    bidders = {}
    run = True
    print_logo()
    while run:
        name = input("What is your name? ")
        bid = int(input("What is your bid? $ "))
        bidders[name] = bid
        choice = input("Are there any other bidders? Typer 'yes' or 'no'.")

        if choice == 'yes':
            run = True
            os.system("clear")
        else:
            run = False
            winner(bidders)
main()

