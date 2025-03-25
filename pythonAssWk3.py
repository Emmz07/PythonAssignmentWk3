
# Prompting user for input

price = float(input("Enter the original price of the item: ")) # Original price of the item
discount_percent = float(input("Enter the discount percentage: ")) # Discount percentage to be applied


# Calculates the final price after applying a discount.

def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price & print(f"A discount of ${discount_amount} was applied. And the final price is: ${final_price}") # Display result
    else:
        return price & print(f"No discount applied. The final price is: ${price}") # Return original price if discount is less than 20%

   
 # Calculate the final price

final_price = calculate_discount(price, discount_percent)
