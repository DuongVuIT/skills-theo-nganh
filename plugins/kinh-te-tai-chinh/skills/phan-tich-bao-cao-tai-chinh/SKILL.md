---
name: phan-tich-bao-cao-tai-chinh
description: Phân tích báo cáo tài chính doanh nghiệp (bảng cân đối kế toán, kết quả kinh doanh, lưu chuyển tiền tệ): tính và diễn giải các chỉ số thanh khoản, đòn bẩy, hiệu quả hoạt động, khả năng sinh lời, phân tích xu hướng và so sánh cùng ngành. Dùng khi người dùng đưa báo cáo tài chính hoặc số liệu và cần nhận xét sức khoẻ tài chính.
---

# Phân tích báo cáo tài chính

## Mục tiêu
Đưa ra nhận xét có căn cứ số liệu về tình hình tài chính, chỉ ra điểm mạnh, rủi ro và câu hỏi cần làm rõ thêm.

## Đầu vào
- Tốt nhất là 3–5 năm hoặc nhiều quý liên tiếp để thấy xu hướng.
- Hỏi: báo cáo hợp nhất hay riêng lẻ, đã kiểm toán chưa, đơn vị tiền tệ, ngành nghề.
- Nếu dữ liệu là file Excel/PDF, đọc số liệu ra bảng trước và cho người dùng xem lại các dòng chính trước khi tính.

## Quy trình
1. **Chuẩn hoá số liệu**: một bảng các khoản mục chính theo năm. Ghi chú các dòng bất thường (lợi nhuận khác lớn, thay đổi chính sách kế toán, ý kiến kiểm toán ngoại trừ).
2. **Tính chỉ số** (ghi rõ công thức dùng, vì mỗi nơi định nghĩa hơi khác):
   - Thanh khoản: hệ số thanh toán hiện hành, nhanh, tiền mặt
   - Đòn bẩy: Nợ/Vốn chủ sở hữu, Nợ vay/EBITDA, khả năng trả lãi (EBIT/chi phí lãi vay)
   - Hiệu quả: vòng quay hàng tồn kho, số ngày phải thu, số ngày phải trả, chu kỳ chuyển đổi tiền
   - Sinh lời: biên lợi nhuận gộp, biên EBIT, biên lợi nhuận ròng, ROA, ROE (có thể tách ROE theo DuPont)
   - Dòng tiền: dòng tiền từ hoạt động kinh doanh so với lợi nhuận ròng, dòng tiền tự do
3. **Phân tích xu hướng**: tăng trưởng doanh thu, lợi nhuận; chỉ số nào cải thiện, chỉ số nào xấu đi và vì sao.
4. **Dấu hiệu cần lưu ý**: lợi nhuận tăng nhưng dòng tiền kinh doanh âm kéo dài; phải thu hoặc tồn kho tăng nhanh hơn doanh thu; vay ngắn hạn tài trợ tài sản dài hạn; giao dịch bên liên quan lớn.
5. **So sánh**: với doanh nghiệp cùng ngành nếu người dùng có số liệu; không tự bịa trung bình ngành.

## Định dạng đầu ra
1. Tóm tắt 3–5 ý chính
2. Bảng chỉ số theo năm
3. Phân tích từng nhóm
4. Rủi ro và câu hỏi cần làm rõ

## Lưu ý
- Mọi phép tính phải tính lại được từ số liệu đầu vào; với nhiều số liệu, dùng code để tính thay vì tính nhẩm.
- Đây là phân tích tham khảo, không phải khuyến nghị mua bán chứng khoán hay tư vấn đầu tư cá nhân.
