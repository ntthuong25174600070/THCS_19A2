import os
os.makedirs("du_lieu/tap_tin", exist_ok=True)
open("du_lieu/f1.txt", "w").close()
open("du_lieu/tap_tin/f2.txt", "w").close()
print(os.listdir("du_lieu"))