import os
os.mkdir("temp_f")
open("temp_f/f.txt", "w").close()
os.rename("temp_f/f.txt", "temp_f/new_f.txt")
os.rename("temp_f/new_f.txt", "new_f.txt")
os.rmdir("temp_f")