import random

# יצירת רשימה ריקה לאחסון הבוליאניים
boolean_list = [];

# הוספת 10 ערכים בוליאניים אקראיים לרשימה
for _ in range(10):
    random_boolean = random.choice([True, False]);
    boolean_list.append(random_boolean);

print(boolean_list);
