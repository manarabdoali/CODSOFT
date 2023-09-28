#include <iostream>

using namespace std;

int main()
{
    float number1,number2;
    char choose;

    cout<<"enter the first number ";
    cin>>number1;
    cout<<"enter the second number ";
    cin>>number2;
    cout<<"enter the operation ";
    cin>>choose;
    if (choose =='+')
        cout<<(number1+number2);
    else if (choose=='-')
        cout<<(number1-number2);
    else if (choose=='/')
        cout<<(number1/number2);
        else
            cout<<(number1*number2);
    return 0;
}
