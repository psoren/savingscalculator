# House Savings Calculator

This House Savings Calculator is a Python program created with ChatGPT. It helps you estimate how long it will take to save up for a house down payment based on your current savings, monthly contributions, and desired savings goal. The program takes into account different stages of savings, such as the potential for increased monthly savings when you get a new job, and calculates your investment value per month until your house saving goal is reached.

## How to Use

1. Make sure you have Python installed on your system.

2. Clone this repository to your local machine or download the `house_savings_calculator.py` file.

3. Open a terminal or command prompt and navigate to the directory where the `house_savings_calculator.py` file is located.

4. Run the Python script by typing the following command:

   ```bash
   python house_savings_calculator.py
The program will prompt you for the following inputs:

Your birthday (e.g., Dec 1 1990)

Your initial savings amount (e.g., 10,000, 50,000, 250k)

Annual rate of return on investment as a decimal (e.g., 0.10 for 10%)

Your current savings amount per month (e.g., 1000, 5,000, 100k)

If you have a new job where you can save more per month (yes or no)

If you have a new job, the month and year when the new job starts (e.g., July 2023)

If you have a new job, the new savings amount per month (e.g., 2000, 50,000, 80k)

The amount you want to save for the house (e.g., 30000, 500,000, 800k)

The program will then calculate and display the investment value per month until your house saving goal is reached.

## What it's for

The House Savings Calculator is designed to assist individuals in planning their savings journey for a house down payment. By providing your current financial situation and desired savings goal, the program offers a realistic estimate of the time needed to achieve the target amount. It also accounts for possible changes, such as increased savings with a new job, to provide a comprehensive savings projection. The calculator serves as a helpful tool for anyone looking to make informed financial decisions and work towards their dream of owning a home.


## Sample output

```Enter your birthday (e.g., Dec 1 1990): apr 1 1999
Enter your birthday (e.g., Dec 1 1990): apr 1 1999
Enter your initial savings amount: 5k
Enter the annual rate of return on investment (as a decimal): 0.10
Enter your current savings amount per month: 500
Do you have a new job where you can save more per month? (yes or no): yes
Enter the month and year when the new job starts (e.g., July 2022): oct 2022
Enter the new savings amount per month: 800
Enter the amount you want to save for the house: 20k
July 2022: $5,544 (Age: 23, Amount Saved: $500)
August 2022: $6,092 (Age: 23, Amount Saved: $500)
September 2022: $6,645 (Age: 23, Amount Saved: $500)
October 2022: $7,202 (Age: 23, Amount Saved: $500)
November 2022: $8,065 (Age: 23, Amount Saved: $800)
December 2022: $8,936 (Age: 23, Amount Saved: $800)
January 2023: $9,814 (Age: 23, Amount Saved: $800)
February 2023: $10,698 (Age: 23, Amount Saved: $800)
March 2023: $11,590 (Age: 23, Amount Saved: $800)
April 2023: $12,489 (Age: 24, Amount Saved: $800)
May 2023: $13,395 (Age: 24, Amount Saved: $800)
June 2023: $14,308 (Age: 24, Amount Saved: $800)
July 2023: $15,228 (Age: 24, Amount Saved: $800)
August 2023: $16,156 (Age: 24, Amount Saved: $800)
September 2023: $17,092 (Age: 24, Amount Saved: $800)
October 2023: $18,034 (Age: 24, Amount Saved: $800)
November 2023: $18,984 (Age: 24, Amount Saved: $800)
December 2023: $19,942 (Age: 24, Amount Saved: $800)
January 2024: $20,908 (Age: 24, Amount Saved: $800)

Reached $20,000 on January 2024.
```