# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount
    else:
        return price

def main():
    # Prompt the user to enter the original price and discount percentage
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)
    
    # Print the final price
    print(f"The final price after applying the discount is: ${final_price:.2f}")

if __name__ == "__main__":
    main()
