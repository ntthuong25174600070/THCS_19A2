lst = list(map(int, input("Nhập danh sách số nguyên, cách nhau bởi dấu cách: ").split()))
k = int(input("Nhập k: "))
n = len(lst)
k = k % n 
rotated = lst[-k:] + lst[:-k]
print("Danh sách sau khi dịch chuyển:", rotated)