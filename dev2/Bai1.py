s = input("Nhập chuỗi: ")
chu_cai = 0
chu_so = 0
dac_biet = 0
for c in s:
    if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
        chu_cai += 1
    elif '0' <= c <= '9':
        chu_so += 1
    else:
        dac_biet += 1
        print("chữ cái:", chu_cai)
        print("Chữ số:", chu_so)
        print("ký tự đặc biệt:", dac_biet)