
with open('san_pham.txt', 'w', encoding='utf-8') as f:
    f.write("ID, Tên sản phẩm, Giá\n")
    f.write("1, Laptop, 1200\n")
    f.write("2, Chuột máy tính, 25\n")
    f.write("3, Bàn phím, 75\n")
product_id = input("Nhập ID sản phẩm cần cập nhật: ")
new_price = input("Nhập giá mới: ")
updated_lines = []
with open('san_pham.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith(product_id + ','):
            parts = line.strip().split(',')
            parts[2] = new_price
            updated_lines.append(','.join(parts) + '\n')
        else:
            updated_lines.append(line)
with open('san_pham.txt', 'w', encoding='utf-8') as f:
    f.writelines(updated_lines)
print("Đã cập nhật giá sản phẩm!")