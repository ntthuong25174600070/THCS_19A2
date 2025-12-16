nums = list(map(int, input("Nhập danh sách số nguyên, cách nhau bởi dấu cách: ").split()))
if len(nums) < 2:
    print("Danh sách cần ít nhất 2 phần tử.")
else:
    max1 = nums[0]
    max2 = nums[1] if nums[1] < max1 else nums[0]
    if nums[1] > max1:
        max1, max2 = nums[1], nums[0]
    for num in nums[2:]:
        if num > max1:
                max2 = max1
                max1 = num 
        elif num > max2 and num != max1:
                max2 = num 
    print(f"Giá trị lớn thứ 2: {max2}")