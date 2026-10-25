---
name: doi-chieu-so-sach
description: Đối chiếu số liệu kế toán: sổ tiền gửi với sao kê ngân hàng, công nợ phải thu/phải trả với khách hàng và nhà cung cấp, sổ chi tiết với sổ cái, hàng tồn kho sổ sách với kiểm kê. Dùng khi người dùng có hai nguồn số liệu (thường là file Excel/CSV) cần khớp và tìm chênh lệch, hoặc cần lập biên bản đối chiếu công nợ.
---

# Đối chiếu sổ sách

## Mục tiêu
Tìm đúng từng khoản chênh lệch, phân loại nguyên nhân, và đề xuất bút toán điều chỉnh (nếu là lỗi bên mình).

## Quy trình
1. **Đọc hai nguồn dữ liệu** (ví dụ sổ TK 112 và sao kê ngân hàng). Với file Excel/CSV, dùng code (pandas) thay vì đọc mắt. Cho người dùng xem số dòng, tổng phát sinh, số dư đầu và cuối kỳ của mỗi nguồn trước khi đối chiếu.
2. **Kiểm tra số dư đầu kỳ** có khớp không. Nếu không khớp thì chênh lệch đến từ kỳ trước — báo trước khi đi tiếp.
3. **Ghép giao dịch** theo thứ tự ưu tiên:
   - Khớp chính xác: số tiền + ngày + số chứng từ/nội dung
   - Khớp số tiền, ngày lệch vài ngày (giao dịch ghi sổ khác ngày với ngân hàng)
   - Một giao dịch bên này bằng tổng nhiều giao dịch bên kia (thanh toán gộp)
4. **Phân loại phần còn lại**:
   - Có trên sao kê, chưa có trên sổ: phí ngân hàng, lãi tiền gửi, khách chuyển tiền chưa ghi nhận
   - Có trên sổ, chưa có trên sao kê: séc/uỷ nhiệm chi chưa thực hiện, ghi sổ trước
   - Sai số tiền: gõ nhầm, đảo chữ số (chênh lệch chia hết cho 9 là dấu hiệu đảo chữ số)
   - Ghi trùng
5. **Lập bảng điều hoà**: số dư theo sổ → cộng/trừ từng khoản → số dư điều chỉnh, phải bằng số dư theo nguồn kia.
6. **Đề xuất bút toán điều chỉnh** cho các khoản là lỗi hoặc thiếu sót bên mình.

## Biên bản đối chiếu công nợ
Gồm: thông tin hai bên; kỳ đối chiếu; số dư đầu kỳ, phát sinh tăng, phát sinh giảm, số dư cuối kỳ; danh sách hoá đơn/chứng từ còn nợ; chênh lệch (nếu có) và nguyên nhân; xác nhận của hai bên.

## Định dạng đầu ra
- Bảng tóm tắt: số giao dịch khớp, chưa khớp, tổng tiền chênh lệch
- Danh sách chi tiết các khoản chưa khớp kèm phân loại
- Bảng điều hoà và bút toán đề xuất
- Nếu làm trên file, xuất file Excel kết quả có cột trạng thái cho từng dòng

## Lưu ý
Không tự sửa dữ liệu gốc của người dùng; luôn ghi kết quả ra file mới.
