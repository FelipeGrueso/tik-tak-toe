i = input("Enter cells: ")
print("---------")
print("|",i[0],i[1],i[2],"|")
print("|",i[3],i[4],i[5],"|")
print("|",i[6],i[7],i[8],"|")
print("---------")

if abs(i.count("O") - i.count("X")) > 1:
    print("Impossible")


elif i[0]==i[1]==i[2]:
    if i[3]==i[4]==i[5]:
        print("Impossible")
    elif i[6]==i[7]==i[8]:
        print("Impossible")
    else:
        print(i[0], "wins")

        
elif i[3]==i[4]==i[5]:
    if i[6]==i[7]==i[8]:
        print("Impossible")
    elif i[0]==i[1]==i[2]:
        print("Impossible")
    else:
        print(i[3], "wins")

        
elif i[6]==i[7]==i[8]:
    if i[0]==i[1]==i[2]:
        print("Impossible")
    elif i[3]==i[4]==i[5]:
        print("Impossible")   
    else:
        print(i[6], "wins")


elif i[0]==i[3]==i[6]:
    if i[1]==i[4]==i[7] or i[2]==i[5]==i[8]:
        print("Impossible")  
    else:
        print(i[0], "wins")

    
elif i[1]==i[4]==i[7]:
    if i[0]==i[3]==i[6] or i[2]==i[5]==i[8]:
        print("Impossible")
    else:
        print(i[1], "wins")
    

    
elif i[2]==i[5]==i[8]:
    if i[0]==i[3]==i[6] or i[1]==i[4]==i[7]:
        print("Impossible")
    else:
        print(i[2], "wins")

    
    
elif i[0]==i[4]==i[8]:
    print(i[4], "wins")
elif i[2]==i[4]==i[6]:
    print(i[4], "wins")

else:
    if i.count("O") + i.count("X") <9:
        print("Game not finished")

    else:
        print("Draw")



