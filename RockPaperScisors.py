import random
rps = ["🗻","📄","✂"]
while 1:
    player = int(input("напиши 1 если камень, 2 если бумага , 3 если ножницы")) - 1
    if player > 2 or player < 0 :
        break
    bot = random.randint(0,2)
    print(rps[bot],"X",rps[player])
    if player == bot :
        print("ничья")
    elif player == 0 and bot == 2 :
        print("Ты победил!")
    elif player == 2 and bot == 0:
        print("ты проиграл")
