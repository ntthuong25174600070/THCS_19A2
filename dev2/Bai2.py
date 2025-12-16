s = input("Nhập chuỗi: ")
n = int(input("Nhập n: "))
words = []
current_word = ""
for char in s:
    if char != ' ':
        current_word += char
    else:
        if current_word:
            words.append(current_word)
            current_word = ""
if current_word:
    words.append(current_word)
kq = []
for word in words:
    if len(word) > n:
        kq.append(word)
print("Các từ có độ dài lớn hơn", n, ":", kq)

