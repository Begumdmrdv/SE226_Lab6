// Question 4

#include <iostream>
using namespace std;

int recursive_sum(int n) {
    if (n == 0)
        return 0;
    return n + recursive_sum(n - 1);
}

// Question 5 

int recursive_sum_helper(int n) {
    if (n == 0)
        return 0;
    return n + recursive_sum_helper(n - 1);
}

int recursive_sum() {
    int n;
    cout << "Enter a number (n): ";
    cin >> n;
    return n + recursive_sum_helper(n - 1);
}

int main() {
    
    cout << "Testing: recursive_sum(n)" << endl;
    int n1;
    cout << "Enter n1: ";
    cin >> n1;
    cout << "Sum from 1 to " << n1 << " = " << recursive_sum(n1) << endl;

    cout << "\nTesting: recursive_sum()" << endl;
    int total = recursive_sum();
    cout << "Sum (overloaded function) = " << total << endl;

    return 0;
}
