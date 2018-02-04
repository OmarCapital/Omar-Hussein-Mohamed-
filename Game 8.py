coinNum = int(input("Coin Numbers:"))
playerMove = ""

firstMove = int(input("P1 move:"))
while(firstMove>= coinNum):
      print("Can't take all the coins, or more than them  .. play again!")
      firstMove=int(input("P1 move:"))
coinNum = coinNum - firstMove

while(coinNum > 0):
   playerTwo = int(input("p2 move:"))
   while (playerTwo > 2 * firstMove):
      print("The Max number of coins that can be taken are twice as the pervious.. play again!")
      playerTwo = int(input("p2 move:"))
   playerMove = "two"
   coinNum = coinNum - playerTwo


   playerOne = int(input("p1 move:"))
   while (playerOne > 2 * playerTwo):
      print("The Max number of coins that can be taken are twice as the previous.. play again!")
      playerOne = int(input("p2 move:"))
   playerMove = "one"
   coinNum = coinNum - playerOne

if (playerMove == "one"):
  print("P1 IS THE WINNER!")
else:
  print("PS IS THE WINNER!")




      
      
       
   


                  
        
         
