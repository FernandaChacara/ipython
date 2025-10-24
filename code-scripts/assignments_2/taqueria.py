# taqueria.py
MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0.0

while True:
    try:
       item = input("Item: ").title()
    except EOFError:
        break

    if not item:
        # Empty input -> re-prompt
        continue

    if item in MENU:
        total += MENU[item]
        print(f"Total: ${total:.2f}")
    # If the item is not in the menu, do nothing (no print or error)

