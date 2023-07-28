import sys
import math

word_dict = dict()
total = 0

line = sys.stdin.readline()

while line != "":
    word, count = line.split()
    count = int(count)
    total += count
    word_dict[word] = count
    line = sys.stdin.readline()

max_word_length = max(len(word) for word in word_dict.keys())

for word, count in word_dict.items():
    percentage = math.floor((count / total) * 100)
    stars = math.ceil(percentage / 5)

    print(f"{word: <{max_word_length + 10}}[{'*' * stars}] {percentage}%")

