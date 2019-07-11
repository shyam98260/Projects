#include<iostream>
using namespace std;
int fch;

int choice,p=0;

int invalid=0;

char turn = 'x';

int box_Completed[9];

char a[3][3] = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};

int flag=0;



void display()
{
	int start;
	system("cls");
	cout<<"\t\t\t\t______________________\n";
	cout<<"\t\t\t\t|                    |\n";
	cout<<"\t\t\t\t|  TIC TAC TOE GAME  |\n";
	cout<<"\t\t\t\t|____________________|";
	cout<<"\n\n\n\t Player 1 :- [x] \n";
	cout<<"\t Player 2 :- [0] ";
	
	cout<<"\n\n\t\t\t\t     |     |     \n";
	cout<<"\t\t\t\t  "<<a[0][0]<<"  |  "<<a[0][1]<<"  |  "<<a[0][2]<<"  \n";
	cout<<"\t\t\t\t_____|_____|_____\n";
	cout<<"\t\t\t\t     |     |     \n";
	cout<<"\t\t\t\t  "<<a[1][0]<<"  |  "<<a[1][1]<<"  |  "<<a[1][2]<<"  \n";
	cout<<"\t\t\t\t_____|_____|_____\n";
	cout<<"\t\t\t\t     |     |     \n";
	cout<<"\t\t\t\t  "<<a[2][0]<<"  |  "<<a[2][1]<<"  |  "<<a[2][2]<<"  \n";
	cout<<"\t\t\t\t     |     |     \n";	
}






int playerTurn()
{
	if ((a[0][0]=='0' && a[1][1]=='0' && a[2][2]=='0') || (a[1][0]=='0' &&  a[2][0]=='0' && a[0][0]=='0') || (a[0][1]=='0' && a[1][1]=='0' && a[2][1]=='0') || (a[0][2]=='0' && a[1][2]=='0' && a[2][2]=='0') || (a[0][2]=='0' && a[1][1]=='0' && a[2][0]=='0') || (a[0][0]=='0' && a[0][1]=='0' && a[0][2]=='0') || (a[1][0]=='0' && a[1][1]=='0' && a[1][2]=='0') || (a[2][0]=='0' && a[2][1]=='0' && a[2][2]=='0'))
	{
		cout<<"\n\n\t\t\t\t______________________\n";
		cout<<"\t\t\t\t|                    |\n";
		cout<<"\t\t\t\t|  2 nd Player win   |\n";
		cout<<"\t\t\t\t|____________________|";
		cout<<"\n\n\t\t\t\t !!!... Thankyou For Playing This game visit again \n\n";
      flag=1;
		exit(0);
	}
	else if ((a[0][0]=='x' && a[1][1]=='x' && a[2][2]=='x') || (a[1][0]=='x' &&  a[2][0]=='x' && a[0][0]=='x') || (a[0][1]=='x' && a[1][1]=='x' && a[2][1]=='x') || (a[0][2]=='x' && a[1][2]=='x' && a[2][2]=='x') || (a[0][2]=='x' && a[1][1]=='x' && a[2][0]=='x') || (a[0][0]=='x' && a[0][1]=='x' && a[0][2]=='x') || (a[1][0]=='x' && a[1][1]=='x' && a[1][2]=='x') || (a[2][0]=='x' && a[2][1]=='x' && a[2][2]=='x'))
	{
		cout<<"\n\n\t\t\t\t______________________\n";
		cout<<"\t\t\t\t|                    |\n";
		cout<<"\t\t\t\t|  1 st Player win   |\n";
		cout<<"\t\t\t\t|____________________|";
		cout<<"\n\n\t\t\t\t !!!... Thankyou For Playting This game visit again \n\n";
      flag=1;
		exit(0);
	}
	if(invalid = 1)
	{
		system("cls");
		invalid=0;
		display();
	}
	cout<<"\n\n";
	if(turn == 'x')
	{
		cout<<"\t Player 1 [x] Turn :- ";
		cin>>choice;
	}
	else if(turn == '0')
	{
		cout<<"\t Player 2 [0] Turn :- ";
		cin>>choice;
	}
	p = choice;
	for(int i=0;i<9;i++)
	{
		if(p == box_Completed[i])
		{
			if(box_Completed[0]==1 && box_Completed[1]==2 && box_Completed[2]==3 && box_Completed[3]==4 && box_Completed[4]==5 &&  box_Completed[5]==6 &&  box_Completed[6]==7 &&  box_Completed[7]==8 &&  box_Completed[8]==9)
			{
				cout<<"\n No One WIns";
			}
			else
			{
				playerTurn();
			}
		}
	}
	switch(choice)
	{
		case 1:
			a[0][0]=turn;
			box_Completed[0]=1;
			if(turn == 'x')
			{
				turn = '0';
			}
			else
			{
				turn = 'x';
			}
				
			break;
		case 2:
			a[0][1]=turn;
			box_Completed[1]=2;
			if(turn == 'x')
			{
				turn = '0';
			}
			else
			{
				turn = 'x';
			}	
			break;
		case 3:
			a[0][2]=turn;
			box_Completed[2]=3;
			if(turn == 'x')
				turn = '0';
			else
				turn = 'x';
			break;
		case 4:
			a[1][0]=turn;
			box_Completed[3]=4;
			if(turn == 'x')
			{
				turn = '0';
			}
			else
			{
				turn = 'x';
			}
			break;
		case 5:
			a[1][1]=turn;
			box_Completed[4]=5;
			if(turn == 'x')
			{
				turn = '0';
			}
			else
			{
				turn = 'x';
			}	
			break;
		case 6:
			a[1][2]=turn;
			box_Completed[5]=6;
			if(turn == 'x')
				turn = '0';
			else
				turn = 'x';
			break;
		case 7:
			a[2][0]=turn;
			box_Completed[6]=7;
			if(turn == 'x')
			{
				turn = '0';
			}
			else
			{
				turn = 'x';
			}
			break;
		case 8:
			a[2][1]=turn;
			box_Completed[7]=8;
			if(turn == 'x')
			{
				turn = '0';
			}
			else
			{
				turn = 'x';
			}
			break;
		case 9:
			a[2][2]=turn;
			box_Completed[8]=9;
			if(turn == 'x')
			{
				turn = '0';
			}
			else
			{
				turn = 'x';
			}
			break;
		default :
			cout<<"\n Invalid choice \n";
			invalid=1;
			for(int i=0;i<=99999999;i++)
				for(int j=0;i<=99999999;i++)
				{
				}
			getchar();
			playerTurn();
			break;	
	}
	
}

int Tic_Tac_Toe_Game()
{
	for(int i=0;i<9;i++)
	{
		box_Completed[i]=0;
	}
	for(int i=0;i<9;i++)
	{
		display();
		playerTurn();
	}
	display();
	if(flag==0)
	{
	   cout<<"\n\n\t\t\t\t ______________________\n";
		cout<<"\t\t\t\t|                     |\n";
		cout<<"\t\t\t\t| No One Won The Game |\n";
		cout<<"\t\t\t\t|_ ___________________|";
		cout<<"\n\n\t\t\t\t !!!... Thankyou For Playting This game visit again \n\n";
	}
}

