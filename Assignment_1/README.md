A simple python calculator to perform basic arithmetic operations: Addition, Subtraction, Multiplication, and Division.

The calculator: 
- Takes two numbers as input
- Lets the user choose one operation
- Displays the result
- Asks if the user wants to perform another calculation or exit

To run

1. Have python installed on your computer, check it with:
python --version

2.Save the calculator code to a file, for example:
calculator.py

3.Run the program:
python calculator.py

To use it
1. enter a number when it asks
2. enter second number as it is prompted
3. select the operation you want to perform
4. exit or type 'yes' to perform another operation

A sample interaction:
Enter the first number: 12
Enter the second number: 3

Select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter your choice (1/2/3/4): 3

--- Result ---
12.0 * 3.0 = 36.0

Would you like to perform another operation? (yes/no): no
see ya bye!

error handling:-
upon entering non numeric value it throws an error asking for a  neumeric value
Error: Please enter valid numeric values.

for division by zero, it shows the error below
Error: Cannot divide by zero.