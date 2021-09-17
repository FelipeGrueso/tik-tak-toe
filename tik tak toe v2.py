i = input("Enter cells: ")
print("---------")
print("|",i[0],i[1],i[2],"|")
print("|",i[3],i[4],i[5],"|")
print("|",i[6],i[7],i[8],"|")
print("---------")

coordenadas = {"['1', '1']": 0, "['1', '2']": 1, "['1', '3']": 2, "['2', '1']": 3, "['2', '2']": 4, "['2', '3']": 5, "['3', '1']": 6, "['3', '2']": 7, "['3', '3']": 8}

while True:
    try:
        k = input("Enter the coordinates: ")
        if int(k[0]) < 4 and int(k[2])< 4:
            k = str(k.split())
        else: 
            print("Coordinates should be from 1 to 3!")
            
        if i[coordenadas[k]] != "X" and i[coordenadas[k]] != "O":
            i = list(i)
            i[coordenadas[k]] = "X"           
           
            print("---------")
            print("|",i[0],i[1],i[2],"|")
            print("|",i[3],i[4],i[5],"|")
            print("|",i[6],i[7],i[8],"|")
            print("---------")
            break

        else:
            print("This cell is occupied! Choose another one!")
        
    except:
        print("You should enter numbers!")
