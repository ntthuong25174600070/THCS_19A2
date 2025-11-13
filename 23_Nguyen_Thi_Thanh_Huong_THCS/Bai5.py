tien_gui = float(input("Nhập số tiền gửi ban đầu: "))
lai_suat_nam = float(input("Nhập lãi suất hàng năm (%):"))
lai_1_thang = tien_gui * (lai_suat_nam / 100) * (1/12)
lai_2_quy = tien_gui * (lai_suat_nam / 100) * (6/12)
lai_3_nam = tien_gui * (lai_suat_nam / 100) * 3
print("TIền lãi sau 1 tháng:", round(lai_1_thang, 2))
print("Tiền lãi sau 2 quý:", round(lai_2_quy, 2))
print("Tiền lãi sau 3 năm:", round(lai_3_nam, 2))
