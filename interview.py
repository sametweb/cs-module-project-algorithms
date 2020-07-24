from word2number import w2n

lst = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

for num in lst:
    if num % 3 == 0:
        print(num)

nums = [
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]

for num in nums:
    if w2n.word_to_num(num) % 3 == 0:
        print num