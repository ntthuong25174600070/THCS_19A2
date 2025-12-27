with open('vanban.txt', 'w', encoding='utf-8') as f:
    f.write("Python là một dạng ngôn ngữ lập trình mạnh mẽ, dễ học vầ có nhiều ứng dụng. Nó được sử dụng rộng rãi trong phát triển web, khoa học dữ liệu, trí tuệ nhân tạo, tự động hóa. Cộng đồng Python rất lớn và hỗ trọ tuyệt vời, với nhiều thư viện phong phú để giải quyết mọi vấn đề.")
with open('vanban.txt', 'r', encoding='utf-8') as f:
    content = f.read()
words = content.split()
total_words = len(words)
print(f"Tổng số từ trong tập tin: {total_words}")