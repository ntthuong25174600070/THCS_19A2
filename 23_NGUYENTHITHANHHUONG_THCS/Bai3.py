tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
a = tu
b = mau
while b != 0:
    a, b = b, a % b
g = a
tu_gon = tu // g
mau_gon = mau // g
print("Phân số tối giản là:", tu_gon, "/", mau_gon)