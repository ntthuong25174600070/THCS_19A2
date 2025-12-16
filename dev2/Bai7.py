lst = list(map(int, input("Nhập danh sách số nguyên, cách nhau bởi dấu cách: ").split()))
target = int(input("Nhập giá trị tổng: "))
pairs = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            pairs.append((lst[i], lst[j]))
print("Các cặp số có tổng bằng", target, ":", pairs)