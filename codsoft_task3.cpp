#include <iostream>

using namespace std;
  string play;
  bool playagian=true;
  char currentplayer='x';
  int row,col,moves;

  void display(char board[3][3])
  {
       for(int i=0;i<3;++i)
      {
          for(int j=0;j<3;++j)
          {
              cout << board[i][j] <<" ";
          }
          cout <<endl;
      }
  }

  bool win(char board[3][3],char currentplayer)
  {
      for(int i=0;i<3;++i)
      {
          if ((board[i][0]==currentplayer) && (board[i][1]==currentplayer) && (board[i][2]==currentplayer))
            return true;
           if ((board[0][i]==currentplayer) && (board[1][i]==currentplayer) && (board[2][i]==currentplayer))
            return true;
           if ((board[0][0]==currentplayer) && (board[1][1]==currentplayer) && (board[2][2]==currentplayer))
             return true;
           if((board[0][2]==currentplayer) && (board[1][1]==currentplayer) && (board[2][0]==currentplayer))
             return true;

      }
      return false;
  }

int main()
{

  while(playagian)
  {  moves=0;
      char board[3][3]={'-','-','-','-','-','-','-','-','-'};
      while (moves < 9)
      {
          cout << " player "<< currentplayer <<" enter your move ( row and col) ";
          cin >> row >> col;
          if ( row <0 || row>=3 || col <0||col >=3 || board[row][col]=='x'|| board[row][col]=='o')
            {cout << " invalid move try again !";
          continue;}
          board [row][col]=currentplayer;

          display(board);
          if (win(board,currentplayer))
          {
              cout <<"player "<<currentplayer<<" win "<<endl;
              break;
          }
             if ( currentplayer=='x')
          {currentplayer='o';
          moves++;}
          else if (currentplayer=='o')
          {currentplayer='x';
          moves++;}
          else
          {
              cout << " invalid ";
              break;
          }

          if (moves==9)
          {
              cout <<"draw!"<<endl;
          }

      }

     cout << "Do you want to play again !: ";
     cin >>play;
     if(play=="yes")
        playagian=true;
     else
        playagian=false;
  }


    return 0;
}
