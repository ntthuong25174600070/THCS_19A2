def max_key_value(d):
    max_key = None
    max_value = None
    for key, value in d.items():
        if max_value is None or value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value
d = {}
n = int(input("Nhập số cặp key-value: "))
for i in range(n):
    key = input(f"Nhập key {i+1}: ")
    value = int(input(f"Nhập value {i+1}: "))
    d[key] = value
max_key, max_value = max_key_value(d)
print(f"Key có giá trị lớn nhất: {max_key}, Giá trị: {max_value}")