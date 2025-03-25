def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    :param price: Original price of the item
    :param discount_percent: Discount percentage to be applied
    :return: Final price after discount if discount is 20% or higher, otherwise the original price
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return original price if discount is less than 20%

# Prompting user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Display result
    if final_price == price:
        print(f"No discount applied. The final price is: ${final_price:.2f}")
    else:
        print(f"Discount applied! The final price after {discount_percent}% discount is: ${final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values for price and discount percentage.")
