#include <iostream>
#include "string.h"
using namespace std;

bool inputIsValid(string in) {
    bool hasOp = false;
    for (int i=0; i<in.length() - 1; i++) {
        // check for operators
        if (in[i] == '+' || in[i] == '-' || in[i] == '*' || in[i] == '/') {
            // return false if the input has more than one operator
            if (hasOp)
                return false;
            else 
            {
                hasOp = true;
                continue;
            }
        }

        // check for valid numbers
        if (in[i] < 48 || in[i] > 57) 
            return false;
    }

    if (in[in.length()-1] != '=' || !hasOp)
        return false;

    return true;
}

int main() {
    string input;
    cout << "Enter an expression: " << endl;
    cin >> input;
    while(input != "0/0=") 
    {
        if (inputIsValid(input)) {
            cout << "valid";
        }
        else
            cout << "Input error. Re-type the math question again." << endl;
            //cout << "Invalid expression, correct format: \"x op y =\" (no whitespace)" << endl;
        cout << "Enter an expression: " << endl;
        cin >> input;
    }
}