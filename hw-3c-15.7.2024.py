# קליטת מספר אי-זוגי מהמשתמש
while True:
    num = int(input("Please enter an odd number greater than 0: "));
    if num > 0 and num % 2 != 0:
        break
    else:
        print("The number must be odd and greater than 0. Try again! ");

# לולאה להדפסת המשולש
for i in range(1, num+1):
    # חישוב מספר הכוכביות בכל שורה
    stars = 2 * i - 1
    # חישוב מספר הרווחים משמאל לכוכביות
    spaces = num - i
    # הדפסת השורה עם רווחים וכוכביות
    print(' ' * spaces + '*' * stars);
