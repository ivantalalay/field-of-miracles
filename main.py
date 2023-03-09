#20.02.2023
secret_word=input("Введите слово для игры:")
print("\033[2J")
win=False
all_letters=list()
true_letters=list()
points=[0,0,0]
counter=0
while win==False:
    letter=input("Введите букву:")
    all_letters.append(letter)
    if letter in secret_word:
        print("Это буква есть в слове")
        points[counter]+=1       
        true_letters.append(letter)
    elif letter in all_letters:
        print("Эта буква уже была использована")
    else:
        print("Это буквы нет в слове")
    win=True
    for symbol in secret_word:
        if symbol in true_letters:
            print(symbol, end="")
        else:
            print("*", end="")
            win=False
    if counter==0:
        print("\nХодил 1 игрок")
        counter=+1
    elif counter==1:
        print("\nХодил 2 игрок")
        counter=+2
    elif counter==2:
        print("\nХодил 3 игрок")
        counter=0
print("Игрок 1 заработал", points[0], "Игрок 2 заработал:", points[0],"Игрок 3 заработал:", points[0])
