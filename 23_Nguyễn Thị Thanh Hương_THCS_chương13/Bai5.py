with open("vanban.txt", "rb") as source:
    with open("copy_vanban.txt", "wb") as target:
        while True:
            data = source.read(1024)
            if not data:
                break
            target.write