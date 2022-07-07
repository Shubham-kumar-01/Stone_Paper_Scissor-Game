import random as rand
import main2

c = rand.randint(1, 3)
print("You have to choose rock for 1 , paper for 2 , scissor for 3")
choose = int(input("Your chhosen value is _ _ _ _ =>"))

if choose == 1 and c == 1:
    print("You choose")
    print(main2.a)
    print("Computer choose also rock ")
    print(main2.a)
    print("Match are drawn")
elif choose == 1 and c == 2:
    print("You choose")
    print(main2.a)
    print("Computer choose")
    print(main2.b)
    print("You lose")
elif choose == 1 and c == 3:
    print("You choose")
    print(main2.a)
    print("Computer choose")
    print(main2.c)
    print("You win")
elif choose == 2 and c == 1:
    print("You choose")
    print(main2.b)
    print("Computer choose  ")
    print(main2.a)
    print("You win")
elif choose == 2 and c == 2:
    print("You choose")
    print(main2.b)
    print("Computer choose")
    print(main2.b)
    print("Match drawn")
elif choose == 2 and c == 3:
    print("You choose")
    print(main2.b)
    print("Computer choose")
    print(main2.c)
    print("You loss")
elif choose == 3 and c == 1:
    print("You choose")
    print(main2.c)
    print("Computer choose  ")
    print(main2.a)
    print("You loss")
elif choose == 3 and c == 2:
    print("You choose")
    print(main2.b)
    print("Computer choose")
    print(main2.b)
    print("You won")
elif choose == 3 and c == 3:
    print("You choose")
    print(main2.b)
    print("Computer choose")
    print(c)
    print("match drawn")
else:
    print("You choose invalid no.")
    print("kindly choose between (1-3)")