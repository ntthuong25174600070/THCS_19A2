with open('vanban.txt', 'r', encoding='utf-8') as f:
    content = f.read()
word_freq = {}
words = content.split()
for word in words:
    word = word.lower()
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("Danh sách từ và số lần suất hiện:")
for word, count in word_freq.items():
    print(f"{word}: {count}")