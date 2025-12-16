def filter_dict(d, condition_func):
    filtered = {}
    for key, value in d.items():
        if condition_func(value):
            filtered[key] = value
    return filtered
d = {}
n = int(input("Nhập số cặp key-value: "))
for i in range(n):
    key = input(f"Nhập key {i+1}: ")
    value = int(input(f"Nhập value {i+1}: "))
    d[key] = value
def condition(v):
    return v > 50

filtered = filter_dict(d, condition)
print("Các cặp thỏa mãn điều kiện (giá trị > 50):", filtered)