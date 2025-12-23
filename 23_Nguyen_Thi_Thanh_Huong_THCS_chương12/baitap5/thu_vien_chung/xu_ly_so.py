def kiem_tra_so_nguyen_to(so):
    """Hàm kiểm tra số nguyên tố (số > 1, chỉ chia hết cho 1 và chính nó)"""
    if so <= 1:
        return False
    for i in range(2, int(so**0.5) + 1): 
        if so % i == 0:
            return False
    return True
