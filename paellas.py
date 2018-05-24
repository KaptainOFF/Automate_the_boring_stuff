#!/usr/bin/python3


def get_purchase():
    print('=' * 30)
    while True:
        try:
            print("What did you buy?")
            purchase = input(">>")
            print("How much did it cost?")
            price = int(input(">>"))
            return purchase, price
            break
        except ValueError:
            print("Price needs to be a number")


def calculate_price(purchase_data):
    paella = 8.75
    item_price = purchase_data / paella
    return item_price


def main():
    item, item_price = get_purchase()
    num_paellas = calculate_price(item_price)
    if num_paellas < 3:
        print("""Good, {} is a smart purchase. Worth {} paellas.""".format(item, str(num_paellas)))
    else:
        print("""Are you crazy!? This {} is worth {} paellas!""".format(item, num_paellas))
    print('=' * 30)


if __name__ == '__main__':
    main()
