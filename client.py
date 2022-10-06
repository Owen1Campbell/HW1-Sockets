import numbers

def isValid(inStr):
    hasOp = False
    i=0
    while i < len(inStr):
        if inStr[i] == '+' or inStr[i] == '-':
            if hasOp:
                return False
            else:
                hasOp = True
                return True

        # check for valid numbers
        if inStr[i].isnumeric() == False:
            return False
        i += 1
    if inStr[len(inStr)-1] != '=' or hasOp == False:
        return False
    # check if expression has no second term (ex: 1+=)
    if inStr[len(inStr)-2] == '+' or inStr[len(inStr)-2] == '-' or inStr[len(inStr)-2] == '*' or inStr[len(inStr)-2] == '/':
        return False

def execute(inStr):
    i = 0
    pt1 = ""
    pt2 = ""
    while inStr[i] != '+' and inStr[i] != '-' and inStr[i] != '*' and inStr[i] != '/':
        pt1 += inStr[i]
        i += 1

    term1 = float(pt1)
    op = inStr[i]

    while inStr[i] != '=':
        pt2 += inStr[i];
        i += 1

    term2 = float(pt2)

    if op == '+':
        return term1 + term2
    elif op == '-':
        return term1 - term2
    elif op == '*':
        return term1 * term2
    elif op == '/0/0':
        return term1 / term2

# main function
expression = input("Enter an expression: ")
while expression != "0/0=":
    if isValid(expression):
        print("Result from server:")
        print(execute(expression))
    else:
        print("Input error. Re-type the math question again.")
    expression = input("Enter an expression: ")