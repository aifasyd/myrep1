def get_price(item):
    if item == "idli":
        return 30
    elif item == "dosa":
        return 50
    elif item == "coffee":
        return 20
    elif item == "vada":
        return 25
    else:
        return 0

def item_cost(item, qty):
    price = get_price(item)
    return price * qty

def calculate_gst(amount, rate=0.05):
    return round(amount * rate, 2)

def generate_bill(subtotal, discount_percent=0):
    discount = subtotal * discount_percent / 100
    amount_after_discount = subtotal - discount
    gst = calculate_gst(amount_after_discount)
    total = amount_after_discount + gst
    return discount, gst, total

def split_bill(total, people):
    each_pays = total // people
    left_over = total % people
    return each_pays, left_over

# ---------------- Main program ----------------
# Works for any items, any quantities, any number of people, any discount

num_items = int(input("How many different items did you order? "))
discount_percent = float(input("Enter discount percent (e.g. 10 for 10%): "))

grand_total = 0

for i in range(num_items):
    item = input("Enter item name: ")
    qty = int(input(f"Enter quantity of {item}: "))

    subtotal = item_cost(item, qty)
    discount, gst, total = generate_bill(subtotal, discount_percent)
    grand_total = grand_total + total

    print(f"\n--- {item} Bill ---")
    print("Subtotal :", subtotal)
    print("Discount :", discount)
    print("GST      :", gst)
    print("Total    :", total)

num_people = int(input("\nEnter number of people splitting the bill: "))
each, extra = split_bill(int(grand_total), num_people)

print("\n--- Per Head Split ---")
print("Grand Total:", grand_total)
print("Each pays:", each, "| Left over:", extra)