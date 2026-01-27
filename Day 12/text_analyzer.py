print("Text Analyzer")
print("---------------------")

text = input("Enter your text: ")

char_count = len(text)
word_count = len(text.split())
upper_count = 0
lower_count = 0
digit_count = 0

for ch in text:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
    elif ch.isdigit():
        digit_count += 1

print("\nAnalysis Result")
print("---------------------")
print("Total Characters:", char_count)
print("Total Words:", word_count)
print("Uppercase Letters:", upper_count)
print("Lowercase Letters:", lower_count)
print("Digits:", digit_count)
