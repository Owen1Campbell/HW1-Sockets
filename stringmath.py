def isValid(inStr):
    hasOp = False
    i=1
    
    # must begin with number
    if inStr[0].isnumeric() == False:
            return False
        
    while i < len(inStr)-1:
        print(inStr[i])
        if inStr[i] == '+' or inStr[i] == '-' or inStr[i] == '*' or inStr[i] == '/':
            if hasOp:
                return False
            else:
                hasOp = True
                i += 1
                continue

        # check for valid numbers
        if inStr[i].isnumeric() == False:
            return False
        
        i += 1

    # must end in '='
    if inStr[len(inStr)-1] != '=':
        return False

    # invalid if missing operator
    if hasOp == False:
        return False

    # check if expression has no second term (ex: 1+=)
    if inStr[len(inStr)-2] == '+' or inStr[len(inStr)-2] == '-' or inStr[len(inStr)-2] == '*' or inStr[len(inStr)-2] == '/':
        return False
    
    # all conditions met
    return True

inp = input("> ")
while (isValid(inp)):
    print("valid")
    inp = input("> ")
print("Invalid. Exiting...")