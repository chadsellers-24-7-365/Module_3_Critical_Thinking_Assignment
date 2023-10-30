# --- Pseudocode ---
# Start
#
#   Declare Real food_charge
#   Declare Real tip
#   Declare Real sales_tax
#   Declare Real total_price
#
#   REPEAT
#     OUTPUT "Please enter the charge for the food:"
#     INPUT food_charge
#
#     IF food_charge is NOT a valid number
#       OUTPUT "Invalid input. Please enter a numeric value."
#   UNTIL food_charge is a valid number
#
#   // Calculate the tip and sales tax based on percentages
#   tip = food_charge * 0.18
#   sales_tax = food_charge * 0.07
#
#   // Calculate the total price including food charge, tip, and sales tax
#   total_price = food_charge + tip + sales_tax
#
#   // Display the calculated amounts
#   OUTPUT "Charge for the food:", food_charge
#   OUTPUT "Tip (18%):", tip
#   OUTPUT "Sales Tax (7%):", sales_tax
#   OUTPUT "Total Price:", total_price
#
# End

# --- Source Code ---
def main():
    while True:
        try:
            # Ask the user for the charge of the food
            food_charge = float(input("Please enter the charge for the food: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Calculate the tip and sales tax
    tip = food_charge * 0.18
    sales_tax = food_charge * 0.07

    # Calculate the total price
    total_price = food_charge + tip + sales_tax

    # Display the results
    print(f"\nCharge for the food: ${food_charge:.2f}")
    print(f"Tip (18%): ${tip:.2f}")
    print(f"Sales Tax (7%): ${sales_tax:.2f}")
    print(f"Total Price: ${total_price:.2f}")


if __name__ == "__main__":
    main()
