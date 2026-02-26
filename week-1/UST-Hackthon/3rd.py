import re
from collections import Counter


with open("sample.log", "r") as file:
    lines = file.readlines()

all_words = []

for line in lines:
    words = re.findall(r"\b\w+\b", line.lower())
    all_words.extend(words)


word_counts = Counter(all_words)
total_words = sum(word_counts.values())


rare_words = {
    word for word, count in word_counts.items()
    if count / total_words < 0.01
}
print("Potential Anomalies:\n")

for line in lines:
    words_in_line = re.findall(r"\b\w+\b", line.lower())
    
   
    if any(word in rare_words for word in words_in_line):
        print(line.strip())
