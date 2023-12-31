from datetime import datetime, timedelta
import locale

# Set locale to use commas as thousands separators
locale.setlocale(locale.LC_ALL, '')

MAX_AGE = 35

def print_welcome_message():
    # Fancy ASCII art for user interaction
    print("╔════════════════════════════════════════════════╗")
    print("║   🏠 Welcome to House Savings Calculator! 🏠   ║")
    print("╚════════════════════════════════════════════════╝")


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

def parse_birthday_input(input_str):
    # Try parsing the date using both the month abbreviation and full month name
    try:
        return datetime.strptime(input_str, '%b %d %Y')
    except ValueError:
        try:
            return datetime.strptime(input_str, '%B %d %Y')
        except ValueError:
            raise ValueError("Invalid date format. Please enter a date in the format 'Dec 1 1990' or 'December 1 1990'.")

def get_user_input(prompt, parser_func):
    while True:
        user_input = input(f"👉 {prompt}: ")

        try:
            return parser_func(user_input)
        except ValueError as e:
            print(e)

def calculate_investment(starting_amount, ending_amount, monthly_savings, annual_rate_of_return, birthday, new_job_month=None, new_job_savings=None):
    monthly_rate_of_return = (1 + annual_rate_of_return) ** (1 / 12) - 1

    current_date = datetime(2022, 7, 1)
    investment_value = starting_amount

    # Convert the birthday to a datetime object
    if not isinstance(birthday, str):
        birthday = birthday.strftime('%b %d %Y')

    birthday = datetime.strptime(birthday, '%b %d %Y')

    print("\n📅 Starting your house savings journey... 🚀\n")

    while investment_value < ending_amount:
        if new_job_month and current_date >= datetime.strptime(new_job_month, '%b %Y'):
            monthly_savings = new_job_savings

        investment_value += monthly_savings
        investment_value *= (1 + monthly_rate_of_return)
        current_date += timedelta(days=30)  # Assuming 30 days per month for simplicity

        # Calculate age based on the current date and birthday
        age = current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))
        if age >= MAX_AGE:
            print("\n🎉 Congratulations! 🎉")
            print(f"You've reached the maximum age of {MAX_AGE} years. You'll never get a house at this rate.\n")
            break

        # Format the date as Month Year
        month_year = current_date.strftime("%B %Y")
        formatted_value = format_currency(investment_value)
        amount_saved = format_currency(monthly_savings)

        # Fancy ASCII art for amount saved per month
        print(f"📅 {month_year}: {formatted_value} (Age: {age}, Amount Saved: {amount_saved})")
        print("   ┏━━━━━━━━━┓")
        print("   ┃  💰 💰  ┃")
        print("   ┃  💰 💰  ┃")
        print("   ┗━━━━━━━━━┛\n")

    return current_date

if __name__ == "__main__":
    print_welcome_message()
    birthday = get_user_input("Enter your birthday (e.g., Dec 1 1990): ", parse_birthday_input)
    starting_amount = get_user_input("Enter your initial savings amount: ", parse_money_input)
    annual_rate_of_return = get_user_input("Enter the annual rate of return on investment (as a decimal): ", parse_money_input)
    monthly_savings = get_user_input("Enter your current savings amount per month: ", parse_money_input)

    new_job_response = input("Do you have a new job where you can save more per month? (yes or no): ")
    if new_job_response.lower() == 'yes':
        new_job_month = input("Enter the month and year when the new job starts (e.g., July 2022): ")
        new_job_savings = get_user_input("Enter the new savings amount per month: ", parse_money_input)
    else:
        new_job_month, new_job_savings = None, None

    house_saving_goal = get_user_input("Enter the amount you want to save for the house: ", parse_money_input)

    final_date_reached = calculate_investment(starting_amount, house_saving_goal, monthly_savings, annual_rate_of_return,
                                              birthday, new_job_month, new_job_savings)

    formatted_house_saving_goal = format_currency(house_saving_goal)
    print(f"\nReached {formatted_house_saving_goal} on {final_date_reached.strftime('%B %Y')}.")
