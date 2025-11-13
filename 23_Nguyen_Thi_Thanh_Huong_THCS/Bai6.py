nam = int(input("Nhập năm: "))
if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(nam, "Là năm nhuận")
else:
    print(nam, "Không phải là năm nhuận")