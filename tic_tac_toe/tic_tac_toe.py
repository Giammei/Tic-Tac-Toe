'''
Tic Tac Toe is a game for two players, X and O, who take turns marking the spaces in a 3x3 grid.
The player who succeds in placing three of their marks in a horizontal, vetical, or diagonal row wins the game.
'''

positons = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

print ("Player 1 insert your name")
player01 = input()
print ("Player 2 insert your name")
player02 = input()

winCondition = False
while winCondition != True :
    print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
    print (player01 + " choose the position: from 0 to 8")
    line = int(input())
    positons[line] = "O";
    
    if positons[0] == positons[1] == positons[2] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player01 + " is the Winner!!")
        break
    elif positons[0] == positons[4] == positons[8] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player01 + " is the Winner!!")
        break
    elif positons[0] == positons[3] == positons[6] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player01 + " is the Winner!!")
        break
    elif positons[1] == positons[4] == positons[7] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player01 + " is the Winner!!")
        break
    elif positons[2] == positons[4] == positons[6] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player01 + " is the Winner!!")
        break
    elif positons[2] == positons[5] == positons[8] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player01 + " is the Winner!!")
        break
    elif positons[3] == positons[4] == positons[5] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player01 + " is the Winner!!")
        break
    elif positons[6] == positons[7] == positons[8] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player01 + " is the Winner!!")
        break   
    
    print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
    print (player02 + " choose the position: from 0 to 8")
    line = int(input())
    positons[line] = 'X';
    
    if positons[0] == positons[1] == positons[2] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player02 + " is the Winner!!")
    elif positons[0] == positons[4] == positons[8] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player02 + " is the Winner!!")
    elif positons[0] == positons[3] == positons[6] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player02 + " is the Winner!!")
    elif positons[1] == positons[4] == positons[7] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player02 + " is the Winner!!")
    elif positons[2] == positons[4] == positons[6] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player02 + " is the Winner!!")
    elif positons[2] == positons[5] == positons[8] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player02 + " is the Winner!!")
    elif positons[3] == positons[4] == positons[5] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player02 + " is the Winner!!")
    elif positons[6] == positons[7] == positons[8] :
        winCondition = True
        print ('|{pos11}|{pos12}|{pos13}|\n|{pos21}|{pos22}|{pos23}|\n|{pos31}|{pos32}|{pos33}|'.format(pos11 = positons[0], pos12 = positons[1], pos13 = positons[2], pos21 = positons[3], pos22 = positons[4], pos23 = positons[5], pos31 = positons[6], pos32 = positons[7], pos33 = positons[8]))
        print (player02 + " is the Winner!!")
