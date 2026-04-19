Text Summarization Web App

1. Giới thiệu
- Đây là ứng dụng web dùng để tóm tắt văn bản tự động
- Hệ thống được xây dựng bằng Flask (Python backend)
- Áp dụng thuật toán TF-IDF để xác định câu quan trọng
- Hỗ trợ nhập văn bản trực tiếp hoặc upload file

2. Mục tiêu
- Giúp người dùng rút gọn nội dung văn bản dài
- Tiết kiệm thời gian đọc và xử lý thông tin
- Minh họa ứng dụng thực tế của xử lý ngôn ngữ tự nhiên (NLP)

3. Công nghệ sử dụng
- Python
- Flask
- Scikit-learn (TF-IDF)
- NumPy
- python-docx (đọc file .docx)
- HTML/CSS

4. Chức năng chính
- Nhập văn bản trực tiếp từ giao diện
- Upload file định dạng .txt và .docx
- Tóm tắt văn bản tự động
- Hiển thị văn bản gốc và kết quả tóm tắt song song
- Nút làm mới (clear) để xóa dữ liệu cũ
- Giao diện web trực quan, dễ sử dụng

5. Nguyên lý hoạt động
- Bước 1: Nhận dữ liệu từ người dùng (text hoặc file)
- Bước 2: Tách văn bản thành các câu riêng biệt
- Bước 3: Sử dụng TF-IDF để tính trọng số từ trong từng câu
- Bước 4: Tính điểm quan trọng cho mỗi câu dựa trên tổng TF-IDF
- Bước 5: Chọn các câu có điểm cao nhất
- Bước 6: Ghép các câu này lại thành đoạn tóm tắt

6. Cấu trúc thư mục
- app.py: file chính chạy Flask server
- summarizer.py: xử lý thuật toán tóm tắt
- templates/index.html: giao diện web
- static/logo.png: hình ảnh logo
- requirements.txt: danh sách thư viện cần cài

7. Cài đặt và chạy chương trình
- Bước 1: Cài Python (>= 3.8)
- Bước 2: Cài thư viện:
  pip install -r requirements.txt
- Bước 3: Chạy ứng dụng:
  python app.py
- Bước 4: Mở trình duyệt:
  http://127.0.0.1:5000

8. Ưu điểm
- Dễ triển khai, không cần GPU
- Tốc độ xử lý nhanh
- Hoạt động offline
- Phù hợp demo học tập và nghiên cứu cơ bản

9. Hướng phát triển
- Áp dụng mô hình NLP nâng cao (BERT, Transformer)
- Cải thiện tách câu và xử lý tiếng Việt
- Thêm lựa chọn độ dài tóm tắt
- Hỗ trợ nhiều định dạng file hơn (PDF)
- Triển khai lên server để sử dụng online

10. Người làm chính
- Tên sinh viên: Nguyễn Văn Quyền - 1848103028
