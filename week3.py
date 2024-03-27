# Define the calculate_discount function
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Return the price after applying the discount
        return price - discount_amount
    else:
        # Return the original price if the discount is less than 20%
        return price

# Example usage:
# Assuming the original price is Ksh.1000 and the discount percentage is 25
final_price = calculate_discount(1000, 25)
print(f"The final price after applying the discount is: {final_price}")

print()

# Prompt the user to enter the original price and the discount percentage
original_price = float(input("Enter the original price of the item you bought from Jumia: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price or the original price if no discount was applied
if discount_percentage >= 20:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount was applied. The original price is: {original_price}")

