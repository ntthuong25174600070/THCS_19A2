s = input("Nhập chuỗi: ")
kq = " "
khoang_trong = False
for c in s:
    if c != " ":
        kq += c
        khoang_trong = False
    else:
        if not khoang_trong:
            kq += " "
            khoang_trong = True
print(kq)