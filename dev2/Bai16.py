def count_frequencies(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
s = input("Nhập chuỗi: ")
freq = count_frequencies(s)
print("Tần suất ký tự:", freq)