HISTORY_FILE = "history.txt"

def show_history():
    try:
        file = open(HISTORY_FILE, 'r')
        lines = file.readlines()
        if len(lines) == 0:
            print("No history found!")
        else:
            for line in reversed(lines):
                print(line.strip())
        file.close()
    except FileNotFoundError:
        print("No history found!")

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print('History cleared')

def save_to_history(equation, result):
    # equation + "=" + result 
    file = open(HISTORY_FILE, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print('Invalid input. Use format: number operator number (eg. 8 + 8)')
        return None
    
    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print('Invalid numbers. Please enter valid numbers.')
        return None
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print('Cannot divide by zero')
            return None
        result = num1 / num2
    else:
        print('Invalid operator. USE ONLY + - * / ')
        return None
    
    if result == int(result):
        result = int(result)
    
    print("Result:", result)
    equation = user_input
    save_to_history(equation, result)
    return result

def main():
    print('----SIMPLE CALCULATOR (type history, clear or exit)')
    while True:
        user_input = input("Enter Calculation (+ - * /) or command (history, clear, exit): ")
        if user_input == 'exit':
            print('Goodbye')
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)

if __name__ == "__main__":
    main()