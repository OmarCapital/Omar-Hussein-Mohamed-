      
#choosing the coing num
      
      coinNum = int(input("Coin Numbers:"))
      
#plyerMove is just to track who will playe the last move (winner)
      
      playerMove = ""

#player 1 (first move) which should be atleast one and can't be all the coins 

      playerOne = int(input("P1 move:"))
      while(playerOne>= coinNum or playerOne < 1):
            print("Can't take all the coins, or more than them  .. play again!")
            playerOne=int(input("P1 move:"))
      playerMove = "one"
      coinNum = coinNum - playerOne

#this loop will cointinue untile the coins finishes
      
      while(coinNum > 0):
            
#player 2 move (which shouldn't be more than double the pervious move
            
            playerTwo = int(input("p2 move:"))
            while (playerTwo > 2 * playerOne or playerTwo < 1 ):
                  print("The Max number of coins that can be taken are twice as the pervious.. play again!")
                  playerTwo = int(input("p2 move:"))
            playerMove = "two"
            coinNum = coinNum - playerTwo
            if (coinNum <= 0):
                  break
            
#player 1 move (which shouldn't be more than double the pervious move
            
            playerOne = int(input("P1 move:"))
            while(playerOne > 2 * playerTwo or playerOne < 1 ):
                  print("The Max number of coins that can be taken are twice as the pervious.. play again!")
                  playerOne=int(input("P1 move:"))
            playerMove = "one"
            coinNum = coinNum - playerOne
            if (coinNum <= 0):
                  break
           
#determine who wins ( who played the last move and has taken the last coins)
            
      if (playerMove == "one"):
        print("P1 IS THE WINNER!")
      else:
        print("P2 IS THE WINNER!")


      




      
      
       
   


                  
        
         
