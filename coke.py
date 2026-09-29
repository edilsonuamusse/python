def main():

    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        if is_valid_coin(coin):
            amount_due -= coin

    change = -amount_due
    print(f"Change Owed: {change}")


def is_valid_coin(coin):

    accepted_coins = (5, 10, 25)
    return coin in accepted_coins


if __name__ == "__main__":
    main()
