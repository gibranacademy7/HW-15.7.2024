import random

word_length = random.randint(5, 20);

# אתחול מחרוזת ריקה כדי לאחסן את המילה האקראית
random_word = ""
for _ in range(word_length):
    random_letter = random.choice(['c', 'b', 'a']);
    random_word += random_letter

print("Random word:", random_word);
