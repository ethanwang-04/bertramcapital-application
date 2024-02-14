# bertramcapital-application
Ethan Wang's application to Bertram Labs for Summer 2024.

To tackle this challenge, I have developed a CLI program in Python to address the coffee payment challenge, ensuring equitable financial contributions among coworkers over time. The program accounts for the dynamic nature of daily coffee runs, including the possibility of coworkers being occasionally absent.

Assumptions
- Coffee prices are consistent.
- Coworkers typically participate daily with their preferred coffee selections.
- The program can be reset periodically (e.g., monthly) to rebalance payments.
- Real-life scenarios, such as occasional absences of coworkers, are considered.

The program will have the following functionalities:
- Manage coworker profiles and coffee preferences.
- Configure prices for various coffee types.
- Identify the most equitable payer for each day, factoring in absences.
- Maintain a detailed record of contributions and absences.
- Generate reports on payment history and participation.

A simple way to store this information is by using dictionaries in Python.
- Coworkers' names and their coffee preferences are mapped in one dictionary.
- Coffee types and corresponding prices are stored in another dictionary.
- A comprehensive record of financial contributions is maintained, alongside an absence log to track daily participation.

Data persistence is achieved through JSON, enabling the program to maintain state across sessions. This approach ensures continuity in tracking payments and absences, providing a realistic and fair solution to managing coffee expenses.

Instructions to Run the Program
1. Ensure Python is installed on your system.
2. Save the code to a file, for example, coffee_fund.py.
3. Run the program in a terminal or command prompt by navigating to the directory where the file is saved and typing python
    coffee_fund.py.
4. Modify the example usage section of the code to reflect the actual coworkers and their coffee preferences, along with the
    correct prices.

GitHub Repository Contents
1. README.md: Detailed instructions for setup and operation, including an overview of the program's functionality.
2. coffee_fund.py: The main Python script for the coffee fund management system.
3. coffee_fund_state.json (automatically generated): A file to store the program's state, ensuring data continuity between
    sessions.