square =[[1,2,3],[4,5,6],[7,8,9]]
winpatten=({1,2,3},{4,5,6}, {7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7})
step=[1,2,3,4,5,6,7,8,9]
player="o"
result = "|"
for i in square:
    for j in i:
        result = result + str(j)+ "|"
    print(f"{result}")
    result = "|"
'''
if the list contain [1,2,3], [4,5,6], [7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7], then the player win
'''
o=set()
x=set()


while len(step) != 0:
    mark = input(f"Player {player}, Enter the number for position:")
    if player =="o":
        o.add(int(mark))
#        player = "x"
    else:
        x.add(int(mark))
#        player = "o"

    for i in square:
        for j in i:
#            print(i)
#            print(j)
#            print(int(mark))
            if j == int(mark):
                i[i.index(int(mark))] = player
                result = result + str(mark)+ "|"
            else:
                result = result + str(j)+ "|"
        result = "|"

    if player =="o":
        player = "x"
    else:
        player = "o"

    for i in square:
        for j in i:
            result = result + str(j)+ "|"
        print(f"{result}")
        result = "|"

    step.remove(int(mark))
    #o.sort()
    #x.sort()
    for win in winpatten:
        if win.issubset(o):
            print(f"O win " + str(win))
            quit()
        elif win.issubset(x):
            print(f"x win " + str(win))
            quit()
    
    


#square = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
#i=1
#result = "|"
#for key in square:
#    if i <=3:
#        result = result + str(key) + "|"
#        i= i+1
#    else:
#        print(f"{result}")
#        result = "|"
#        i = 1