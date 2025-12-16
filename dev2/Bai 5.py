lst = list(map(int, input("Nhập danh sách số nguyên, cách nhau bởi dấu cách: ".split())))
unique_lst = []
for item in lst:
    is_duplicate = False
    for unique in unique_lst:
        if item == unique:
            is_duplicate = True
            break
        if not is_duplicate:
            unique_lst.append(item)
print("Danh sách sau khi loại bỏ trùng lặp:", unique_lst)