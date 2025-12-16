def quy_trinh_tuple(t):
    chan_list = []
    le_list = []
    sum_chan = 0
    sum_le = 0
    for num in t:
        if num % 2 == 0:
            chan_list.append(num)
            sum_chan += num
        else:
            le_list.append(num)
            sum_le += num
    chan_tuple = tuple(chan_list)
    le_tuple = tuple(le_list)
    return chan_tuple, le_tuple, sum_chan, sum_le
nums = list(map(int, input("Nhập tuple số nguyên: ").split()))
t = tuple(nums)
chan_tuple, le_tuple, sum_chan, sum_le = quy_trinh_tuple(t)
print(f"tuple Chẵn: {chan_tuple}, tổng: {sum_chan}")
print(f"tuple lẻ: {le_tuple}, tổng: {sum_le}")
