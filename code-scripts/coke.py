def main():
    amount_due = 50  # total price of the Coke
    accepted_coins = [25, 10, 5]  # only these coins are accepted

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            # user didn’t enter a number
            continue

        # subtract only if the coin is valid
        if coin in accepted_coins:
            amount_due -= coin

    # if amount_due <= 0, Coke is paid (possibly with change)
    print(f"Change Owed: {abs(amount_due)}")


main()


