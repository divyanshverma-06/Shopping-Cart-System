
PRODUCTS = {
    "Pen": 10,
    "Notebook": 50,
    "Bag": 500,
}

GST_RATE = 0.18            # 18% GST
DISCOUNT_RATE = 0.10       # 10% discount
DISCOUNT_THRESHOLD = 500   # discount if subtotal is more than 500




def find_product(name):
    name = name.strip().lower()
    for product in PRODUCTS:
        if product.lower() == name:
            return product
    return None


def format_amount(value):
    value = round(value, 2)
    return str(int(value)) if value == int(value) else f"{value:.2f}"


def calculate_subtotal(cart):
    return sum(PRODUCTS[item] * qty for item, qty in cart.items())



def view_products():
    print("Available products:")
    for name, price in PRODUCTS.items():
        print(f"  {name} - Rs.{price}")


def add_to_cart(cart, name, quantity_text):
    product = find_product(name)
    if product is None:
        print("Invalid product. Available: " + ", ".join(PRODUCTS))
        return False

    try:
        quantity = int(quantity_text)
    except ValueError:
        print("Quantity must be a whole number.")
        return False

    if quantity < 1:
        print("Quantity must be at least 1.")
        return False

    cart[product] = cart.get(product, 0) + quantity
    print(f"{product} x{quantity} added | Cart subtotal: "
          f"{format_amount(calculate_subtotal(cart))}")
    return True


def remove_from_cart(cart, name):
    product = find_product(name)
    if product is None:
        print("Invalid product. Available: " + ", ".join(PRODUCTS))
        return False

    if product not in cart:
        print(f"{product} is not in the cart.")
        return False

    del cart[product]
    print(f"{product} removed. Cart: " + cart_summary(cart))
    return True


def cart_summary(cart):
    if not cart:
        return "empty"
    parts = [f"{item} x{qty} = {format_amount(PRODUCTS[item] * qty)}"
             for item, qty in cart.items()]
    return ", ".join(parts)


def view_cart(cart):
    if not cart:
        print("Cart is empty.")
        return
    print("Your cart:")
    for item, qty in cart.items():
        print(f"  {item} x{qty} @ Rs.{PRODUCTS[item]} = "
              f"Rs.{format_amount(PRODUCTS[item] * qty)}")
    print(f"  Subtotal: {format_amount(calculate_subtotal(cart))}")


def calculate_bill(cart):
    subtotal = calculate_subtotal(cart)
    discount = subtotal * DISCOUNT_RATE if subtotal > DISCOUNT_THRESHOLD else 0
    gst = (subtotal - discount) * GST_RATE
    grand_total = subtotal - discount + gst
    return subtotal, discount, gst, grand_total


def checkout(cart):
    if not cart:
        print("Cart is empty. Add items before checkout.")
        return False
    subtotal, discount, gst, grand_total = calculate_bill(cart)
    print("----- FINAL BILL -----")
    for item, qty in cart.items():
        print(f"{item} x{qty} = {format_amount(PRODUCTS[item] * qty)}")
    print(f"Subtotal: {format_amount(subtotal)} | "
          f"Discount: {format_amount(discount)} | "
          f"GST: {format_amount(gst)}")
    print(f"Grand Total: {format_amount(grand_total)}")
    print("----------------------")
    return True



def show_menu():
    print("\n===== SHOPPING CART =====")
    print("1. View products")
    print("2. Add to cart")
    print("3. Remove from cart")
    print("4. View cart")
    print("5. Checkout")
    print("6. Exit")


def main():
    cart = {}  # {product_name: quantity}
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            view_products()
        elif choice == "2":
            name = input("Add to cart: ")
            qty = input("Quantity: ")
            add_to_cart(cart, name, qty)
        elif choice == "3":
            name = input("Remove from cart: ")
            remove_from_cart(cart, name)
        elif choice == "4":
            view_cart(cart)
        elif choice == "5":
            if checkout(cart):
                cart.clear()  # new order starts after billing
        elif choice == "6":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 6.")


if __name__ == "__main__":
    main()