import random
number = random.randint(1, 100)
play = 0
count = 0
highscore = 1000
highscorelist = []
while play == 0:
    count = 0
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            count += 1
        except ValueError :
            print("Not a valid input")
        if number == guess:
            print("You Win!")
            print("You took", count ,"guesses")
            if highscore > count:
                highscore = count
                highscorelist.append(highscore)
                highscorelist.sort()
                print("High Score List", highscorelist)
            else:
                pass
            print("The fewest guesses is", highscore)
            playagain = input("Play Again? (Y/N): ").strip.upper
            if playagain == "Y":
                break
            else:
                play = 99
        elif number > guess:
            print("The number is higher")
        elif number < guess:
            print("The number is smaller")
