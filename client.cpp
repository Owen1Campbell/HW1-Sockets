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

    // invalid if missing operator or does not end in '='
    if (in[in.length()-1] != '=' || !hasOp)
        return false;

    // check if expression has no second term (ex: 1+=)
    if (in[in.length()-2] == '+' || in[in.length()-2] == '-' || in[in.length()-2] == '*' || in[in.length()-2] == '/') 
        return false;
    return true;
}

float execute(string exp) {
    string pt1, pt2;
    char op;
    float term1, term2;

    int i = 0;
    while (exp[i] != '+' && exp[i] != '-' && exp[i] != '*' && exp[i] != '/') {
        pt1 += exp[i];
        i++;
    }

    term1 = stof(pt1);
    op = exp[i];
    i++;

    while (exp[i] != '=') {
        pt2 += exp[i];
        i++;
    }

    term2 = stof(pt2);

    switch (op) {
        case '+':
            return term1 + term2;
        case '-':
            return term1 - term2;
        case '*':
            return term1 * term2;
        case '/':
            return term1 / term2;
        default:
            cout << "math error :(" << endl;
    }

    return 0;
}

int main() {
    string input;
    cout << "Enter an expression: " << endl;
    cin >> input;
    while(input != "0/0=") 
    {
        if (inputIsValid(input)) {
            cout << "valid" << endl;
            cout << "result is " << execute(input) << endl;
        }
        else
            cout << "Input error. Re-type the math question again." << endl;
            //cout << "Invalid expression, correct format: \"x op y =\" (no whitespace)" << endl;
        cout << "Enter an expression: " << endl;
        cin >> input;
    }
}