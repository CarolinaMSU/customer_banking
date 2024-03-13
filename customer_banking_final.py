# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account_final import create_cd_account
from savings_account_final import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Tell me your Savings Balance:"))
    savings_interest = float(input("What is your Savings Interest rate?"))
    savings_months = int(input("How many months have you banked with us?"))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your Interest Earned is: {interest_earned}%")
    print(f"Your updated balance is $ {updated_savings_balance}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Tell me your CD Balance:"))
    cd_interest = float(input("What is your CD Interest rate?"))
    cd_months = int(input("How many months have you banked with us?"))

    # # Call the create_cd_account function and pass the variables from the user.
    updated_cd_account, interest_earned = create_cd_account(cd_balance, cd_interest, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Your Interest Earned is: {cd_interest}%")
    print(f"Your updated balance is $ {updated_cd_account}")

if __name__ == "__main__":()
    # Call the main function.
main()