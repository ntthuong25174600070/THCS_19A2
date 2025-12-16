n = int(input("Nhập kích thước ma trận vuông: "))
ma_tran = []
for i in range(n):
    hang = list(map(int, input(f"Nhập hàng {i+1}: ").split()))
    ma_tran.append(hang)
tong = 0
for i in range(n):
    tong = tong + ma_tran[n-i-1][i]
print("Tổng đường chéo phụ:", tong)
