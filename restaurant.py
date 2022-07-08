
MENU = {"sandwich": 10, "tea": 7, "salad": 9}

def get_order():
    total = 0
    while True:

        order = input("Order: ").strip()

        if not order:
            break

        if order in MENU:
            total += MENU[order]
            print(f"{order} costs {MENU[order]}, total is {total}")
        else:
            print(f"Sorry, we are fresh out of {order} today")

    print(f"Your total is {total}")

get_order()



