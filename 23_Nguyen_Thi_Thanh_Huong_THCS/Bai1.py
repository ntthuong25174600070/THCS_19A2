gia_san_pham = float(input("Nhập giá sản phẩm: "))
so_luong_san_pham = int(input("Nhập số lượng mua: "))
tong_chi_phi = gia_san_pham * so_luong_san_pham
thue_vat = tong_chi_phi * 0.1
tong_tien = tong_chi_phi + thue_vat
print("Tổng tiền phải trả:", round(tong_tien, 2), "VNĐ")