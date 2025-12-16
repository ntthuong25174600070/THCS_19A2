lst = list(map(int, input("Nhập danh sách số nguyên, cách nhau bởi dấu cách: ").split()))
chan_sum = 0
le_sum = 0
for num in lst:
    if num % 2 == 0:
        chan_sum += num
    else:
        le_sum += num
print(f"Tổng số chẵn: {chan_sum}")
print(f"Tổng số lẻ: {le_sum}")