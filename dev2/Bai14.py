def set_operations(A, B):
    diff_A_B = []
    for a in A:
        found = False
        for b in B:
            if a == b:
                found = True
                break
        if not found:
            diff_A_B.append(a)
    diff_B_A = []
    for b in B:
        found = False
        for a in A:
            if b == a:
                found = True
                break
        if not found:
            diff_B_A.append(b)
    intersection = []
    for a in A:
        for b in B:
            if a == b:
                intersection.append(a)
                break
    union = []
    for a in A:
        union.append(a)
    for b in B:
        found = False
        for u in union:
            if b == u:
                found = True
                break
        if not found:
            union.append(b)
    
    return diff_A_B, diff_B_A, intersection, union
A = list(map(int, input("Nhập set A (cách nhau bởi dấu cách): ").split()))
B = list(map(int, input("Nhập set B (cách nhau bởi dấu cách): ").split()))
diff_A_B, diff_B_A, intersection, union = set_operations(A, B)
print(f"Thuộc A không thuộc B: {diff_A_B}")
print(f"Thuộc B không thuộc A: {diff_B_A}")
print(f"Có trong cả A và B: {intersection}")
print(f"Hợp của A và B: {union}")
