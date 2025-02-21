def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
    else:
        final_price = price
    return final_price

# Prompting the user for input
    original_price = float(input("2000:"))
    discount_percent = float(input("20%:"))

    final_price = calculate_discount(original_price, discount_percent)
    
    if final_price == original_price:
        print("No discount applied. The original price is:", original_price)
    else:
        print,("The final price after applying the discount is:", final_price)
