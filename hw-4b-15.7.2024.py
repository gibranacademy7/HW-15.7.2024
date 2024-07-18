import random

from typing import List  # (תיקון אוטומתי מהפיטון)
# This is imported from the typing module to provide type hinting for variables.
# It specifies that random_numbers is a list that contains integers (int). ( = הסבר שלמדתי מצאט גבט)

random_numbers: List[int] = [];

for _ in range(10):
    random_number = random.randint(1, 100);
    random_numbers.append(random_number);
print(random_numbers);

