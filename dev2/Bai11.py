n = int(input("Nhập kích thước ma trận vuông: "))
ma_tran = []
for i in range(n):
    hang = list(map(int, input(f"Nhập hàng {i + 1}: ").split()))
    ma_tran.append(hang)
la_doi_xung = True
for i in range(n):
    for j in range(i + 1, n):
        if ma_tran[i][j] != ma_tran[j][i]:
            la_doi_xung = False
            break
        if not la_doi_xung:
            break
if la_doi_xung:
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xúng")
