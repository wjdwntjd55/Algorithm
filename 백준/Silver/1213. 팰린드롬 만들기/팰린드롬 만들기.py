import sys
from collections import Counter

word = input()
word_list = list(word)
word_list.sort()

word_count = Counter(word_list)

odd_alphabet_count = 0
odd_alphabet = ""

for alphabet in word_count:
    if word_count[alphabet] % 2 == 1:
        odd_alphabet_count += 1
        odd_alphabet += alphabet

    if odd_alphabet_count > 1:
        print("I'm Sorry Hansoo")
        sys.exit()

answer = ''

# 한 글자씩 읽어오기
for alphabet in word_count:
    half_count = word_count[alphabet] // 2
    answer += alphabet * half_count
    word_count[alphabet] -= half_count * 2

tmp = answer[::-1]
answer += odd_alphabet
answer += tmp
print(answer)