import sys  
import os 
duong_dan_thu_vien = os.path.join(os.path.dirname(__file__), '..', 'thu_vien_chung')
sys.path.append(duong_dan_thu_vien)
import xu_ly_so
so = 7
la_nguyen_to = xu_ly_so.kiem_tra_so_nguyen_to(so)
print(f"Số {so} có phải số nguyên tố? {la_nguyen_to}")
