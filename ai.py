coinNum = int(input("Enter coin numbers: "))

fibonacciNum = [1,1 , 2, 3, 5, 8, 13, 21, 34, 55]

move = ""

while(coinNum > 0):

    for i in fibonacciNum:
        for j in fibonacciNum:
            
            if(i + j == coinNum):
                print("AI Move: " + str(i))
                
                
    coinNum = coinNum - i
    move = "ai"

    you = int(input("YOU: "))

    while(you > 2*i or you <= 1 ):

              print("wrong value .. PLAY AGAIN!")
              you = int(input("YOU: "))

    coinNum = coinNum - you
    move = "you"

if (move == "ai"):
            print("YOU LOST ! ")

else:
              print("YOU WON!")
              
                
                
                    
              
                
