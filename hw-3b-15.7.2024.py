n = int(input("Please enter a positive number greater than 0: "));

# וידוא שהמספר חיובי וגדול מ-0
if n <= 0:
    print("A positive number greater than 0 must be entered");
else:
    # לולאה להדפסת המשולש
    for i in range(1, n+1):
        # חישוב מספר הכוכביות בכל שורה
        stars = 2 * i - 1
        # חישוב מספר הרווחים משמאל לכוכביות
        spaces = n - i
        # הדפסת השורה עם רווחים וכוכביות
        print(' ' * spaces + '*' * stars);
