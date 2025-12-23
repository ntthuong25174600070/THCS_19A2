from du_lieu.danh_sach import sap_xep_tang_dan
from du_lieu.tu_dien import lay_gia_tri

danh_sach = [3, 1, 4, 1, 5]
danh_sach_sap_xep = sap_xep_tang_dan(danh_sach)
print(f"Danh sách gốc: {danh_sach}")
print(f"Danh sách sắp xếp: {danh_sach_sap_xep}")

tu_dien = {"a": 1, "b": 2, "c": 3}
gia_tri = lay_gia_tri(tu_dien, "b")
print(f"Giá trị của khóa 'b': {gia_tri}")