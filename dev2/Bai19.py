def group_by_score(d):
    grouped = {}
    for name, score in d.items():
        if score in grouped:
            grouped[score].append(name)
        else:
            grouped[score] = [name]
    return grouped
d = {}
n = int(input("Nhập số sinh viên: "))
for i in range(n):
    name = input(f"Nhập tên sinh viên {i+1}: ")
    score = int(input(f"Nhập điểm của {name}: "))
    d[name] = score
grouped = group_by_score(d)
print("Nhóm theo điểm:", grouped)