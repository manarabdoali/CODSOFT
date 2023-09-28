#include <iostream>
# include <ctime>
using namespace std;
int main()
{  srand(time(0));
    int number= rand();
    int guess;

  for (int i=1;i<100;i++)
       {    cout<<"enter guess number ";

           cin>> guess;

        if(guess==number)
            {cout<<"number of  guess is "<< i;
            break;

            }
            else if(guess<number)
                {cout<<"less than number\n";

             }
            else
                        {cout<<"greater than number\n";

                       }}
    return 0;
}
