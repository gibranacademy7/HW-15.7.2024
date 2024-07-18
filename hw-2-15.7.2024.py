import random
def play_game(): # פונקציה play_game מבצעת את הגרלת המספר ומנהלת את המשחק
    random_number = random.randint(1, 20);
    attempts: int = 0;
    while True:
        user_guess = int(input("Guess the number between 1 and 20: "));
        attempts += 1
        if user_guess > random_number:
            print("Your number is too big");
        elif user_guess < random_number:
            print("Your number is too small");
        else:
            print("BINGO");
            break
    return attempts

while True: # בלולאה while True, מתבצע קליטת מספר מהמשתמש והשוואה למספר שהוגרל
    attempts = play_game();
    print(f"Your number of attempts was: {attempts}");
    play_again = input("Do you want to play again? (Yes / No): ").strip().lower(); # בכדי להתעלם מטעויות קשורות לרווחים או אותיות קטנות וגדולות
    if play_again != "YES":
        break;
