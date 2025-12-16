def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        return None  
    result = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            sum_val = 0
            for k in range(cols_A):
                sum_val += A[i][k] * B[k][j]
            row.append(sum_val)
        result.append(row)
    return result

rows_A = int(input("Nhập số hàng ma trận A: "))
cols_A = int(input("Nhập số cột ma trận A: "))
A = []
for i in range(rows_A):
    row = list(map(int, input(f"Nhập hàng {i+1} của A: ").split()))
    A.append(row)

rows_B = int(input("Nhập số hàng ma trận B: "))
cols_B = int(input("Nhập số cột ma trận B: "))
B = []
for i in range(rows_B):
    row = list(map(int, input(f"Nhập hàng {i+1} của B: ").split()))
    B.append(row)

result = matrix_multiply(A, B)
if result is None:
    print("Phép nhân không khả thi")
else:
    print("Ma trận tích:")
    for row in result:
        print(row)