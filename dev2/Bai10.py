n = int(input("Nhập số hàng: "))
m = int(input("Nhập số cột: "))
ma_tran = []
for i in range(n):
    hang = list(map(int, input(f"Nhập hàng {i+1}z: ").split()))
    ma_tran.append(hang)
tong_lon_nhat = float('-inf')
hang_lon_nhat = -1
for i in range(n):
    tong_hang = 0
    for j in range(m):
        tong_hang += ma_tran[i][j]
    if tong_hang > tong_lon_nhat:
        tong_long_nhat = tong_lon_nhat
        hang_lon_nhat = i
print(f"Hàng {hang_lon_nhat + 1} có tổng lớn nhất: {tong_lon_nhat}")