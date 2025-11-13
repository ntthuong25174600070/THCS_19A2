so_kwh = float(input("Nhập số kwh điện tiêu thụ: "))
if so_kwh <= 100:
    tien = so_kwh * 1.678
elif so_kwh <= 200:
    tien = so_kwh * 1.678 + (so_kwh - 100) * 1.734
else:
    tien = 100 * 1.678 + 100 * 1.734 + (so_kwh - 200) * 2.014
print("Tổng số tiền điện phải trả:", tien, "VNĐ")