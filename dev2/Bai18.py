def reverse_dict(d):
    reversed_d = {}
    for key, value in d.items():
        reversed_d[value] = key
    return reversed_d
d = {}
n = int(input("Nhập số cặp key-value: "))
for i in range(n):
    key = input(f"Nhập key {i+1}: ")
    value = int(input(f"Nhập value {i+1}: "))
    d[key] = value
reversed_d = reverse_dict(d)
print("Dictionary đảo ngược:", reversed_d)