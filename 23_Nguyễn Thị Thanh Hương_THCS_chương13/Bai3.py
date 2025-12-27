numbers = [10, 25, 3, 47, 89, 12]
with open('so_nguyen.txt', 'w') as f:
    for num in numbers:
        f.write(str(num) + '\n')
print("Đã ghi danh sách số vào tập tin so_nguyen.txt")
