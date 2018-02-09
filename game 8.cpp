#include <iostream>
using namespace std;

main(){
int coinNum , playerOne , playerTwo;
string playerMove;

cout << "Coin Numbers: " << endl;
cin >> coinNum ;

cout << "P1 MOVE: " << endl;
cin >> playerOne;

while(playerOne >= coinNum || playerOne < 1){

    cout << "Can't take all the coins, or more than them  .. play again!" << endl;
    cout << "P1 MOVE: " << endl;
    cin >> playerOne;
}

playerMove = "one";
coinNum = coinNum - playerOne;

while (coinNum > 0 ){

    cout << "P2 MOVE: " << endl;
    cin >> playerTwo;

    while (playerTwo > 2 * playerOne || playerTwo < 1 ){
        cout << "THE MAX NUMBER OF COINS THAT CAN BE TAKEN ARE TWICE AS MUCH AS THE PREVIOUS ONE" << endl;
        cout << "P2 MOVE: ";
        cin >> playerTwo;
    }
    playerMove = "two";
    coinNum = coinNum - playerTwo;
    if (coinNum <= 0)
        break;

    cout << "P1 MOVE :" << endl;
    cin >> playerOne ;

     while (playerOne > 2 * playerTwo || playerOne < 1 ){
        cout << "THE MAX NUMBER OF COINS THAT CAN BE TAKEN ARE TWICE AS MUCH AS THE PREVIOUS ONE" << endl;
        cout << "P2 MOVE: " << endl;
        cin >> playerTwo;
    }
    playerMove = "one";
    coinNum = coinNum - playerOne;
    if (coinNum <= 0)
        break;
}
if ( playerMove =="one"){
    cout << "P1 IS THE WINNER" << endl;
}
else
    cout << "P2 IS THE WINNER" << endl;
}

