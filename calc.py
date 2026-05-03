# Define arithmetic functions
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error"

# Main calculator loop
def run_calculator():
    while True:
        op = input("Enter op (+,-,*,/) or 'q' to quit: ")
        if op == 'q': break
        
        try:
            n1 = float(input("Num 1: "))
            n2 = float(input("Num 2: "))
            
            if op == '+': print(add(n1, n2))
            elif op == '-': print(sub(n1, n2))
            elif op == '*': print(mul(n1, n2))
            elif op == '/': print(div(n1, n2))
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    run_calculator()
