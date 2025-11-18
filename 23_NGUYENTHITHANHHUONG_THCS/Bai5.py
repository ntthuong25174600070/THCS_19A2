n = int(input("Nhập n: "))
S1 = n * (n + 1) // 2
S2 = 1 
for i in range(1, n + 1):
    S2 *= i
S3 = 0 
for i in range(1, n + 1):
    S3 += ((-1) ** (i + 1)) / i
S4 = 0
for k in range(0, n + 1):
    S4 += k / (k + 2)
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)