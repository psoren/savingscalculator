from datetime import datetime, timedelta
import locale

# Set locale to use commas as thousands separators
locale.setlocale(locale.LC_ALL, '')

def format_currency(amount):
    # Format the amount with dollar sign, commas, and no cents
    return "${:,.0f}".format(amount)

def parse_money_input(input_str):
    # Remove any commas and "k" if present
    input_str = input_str.replace(",", "").replace("k", "000")

    try:
        return float(input_str)
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid number.")

def get_user_input(prompt):
    while True:
        user_input = input(prompt)

        try:
            return parse_money_input(user_input)
        except ValueError as e:
            print(e)

def calculate_investment(starting_amount, ending_amount, monthly_savings, annual_rate_of_return, birthday, new_job_month=None, new_job_savings=None):
    monthly_rate_of_return = (1 + annual_rate_of_return) ** (1 / 12) - 1

    current_date = datetime(2022, 7, 1)
    investment_value = starting_amount

    # Convert the birthday to a datetime object
    birthday = datetime.strptime(birthday, '%b %d %Y')

    while investment_value < ending_amount:
        if new_job_month and current_date >= datetime.strptime(new_job_month, '%b %Y'):
            monthly_savings = new_job_savings

        investment_value += monthly_savings
        investment_value *= (1 + monthly_rate_of_return)
        current_date += timedelta(days=30)  # Assuming 30 days per month for simplicity

        # Calculate age based on the current date and birthday
        age = current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))

        # Format the date as Month Year
        month_year = current_date.strftime("%B %Y")
        formatted_value = format_currency(investment_value)
        amount_saved = format_currency(monthly_savings)
        print(f"{month_year}: {formatted_value} (Age: {age}, Amount Saved: {amount_saved})")

    return current_date

if __name__ == "__main__":
    birthday = input("Enter your birthday (e.g., Dec 1 1990): ")
    starting_amount = get_user_input("Enter your initial savings amount: ")
    annual_rate_of_return = get_user_input("Enter the annual rate of return on investment (as a decimal): ")
    monthly_savings = get_user_input("Enter your current savings amount per month: ")

    new_job_response = input("Do you have a new job where you can save more per month? (yes or no): ")
    if new_job_response.lower() == 'yes':
        new_job_month = input("Enter the month and year when the new job starts (e.g., July 2022): ")
        new_job_savings = get_user_input("Enter the new savings amount per month: ")
    else:
        new_job_month, new_job_savings = None, None

    house_saving_goal = get_user_input("Enter the amount you want to save for the house: ")

    final_date_reached = calculate_investment(starting_amount, house_saving_goal, monthly_savings, annual_rate_of_return,
                                              birthday, new_job_month, new_job_savings)

    formatted_house_saving_goal = format_currency(house_saving_goal)
    print(f"\nReached {formatted_house_saving_goal} on {final_date_reached.strftime('%B %Y')}.")
