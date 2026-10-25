---
name: du-toan-xay-dung
description: Lập, bóc tách khối lượng và kiểm tra dự toán công trình xây dựng theo cách làm phổ biến ở Việt Nam. Dùng khi người dùng cần bóc khối lượng từ bản vẽ hoặc mô tả, lập bảng dự toán (vật liệu, nhân công, máy thi công), tổng hợp chi phí xây dựng, hoặc rà soát một bảng dự toán có sẵn để tìm sai sót.
---

# Dự toán xây dựng

## Mục tiêu
Giúp người dùng ra được bảng khối lượng và bảng dự toán rõ ràng, có thể kiểm tra lại từng con số, và chỉ ra chỗ cần kỹ sư dự toán xác nhận.

## Thông tin cần hỏi trước (nếu chưa có)
1. Loại công trình, cấp công trình, địa điểm (tỉnh/thành) — đơn giá vật liệu và nhân công khác nhau theo địa phương.
2. Nguồn vốn: vốn nhà nước hay vốn tư nhân — vốn nhà nước phải tuân thủ quy định quản lý chi phí đầu tư xây dựng.
3. Dữ liệu đầu vào: bản vẽ, thuyết minh, bảng khối lượng mời thầu, hay chỉ là mô tả.
4. Thời điểm lập dự toán (để chọn công bố giá vật liệu, chỉ số giá phù hợp).

## Quy trình
1. **Bóc khối lượng** theo từng hạng mục (móng, khung, tường, hoàn thiện, điện nước...). Mỗi dòng ghi rõ: mã hiệu công việc (nếu có), tên công việc, đơn vị, cách tính (diễn giải kích thước), khối lượng.
2. **Áp đơn giá / định mức**: vật liệu, nhân công, máy thi công. Ghi rõ nguồn đơn giá (công bố giá của Sở Xây dựng, báo giá nhà cung cấp, giá thị trường tự khảo sát).
3. **Tổng hợp chi phí** theo cấu trúc thường dùng:
   - Chi phí trực tiếp (vật liệu + nhân công + máy)
   - Chi phí gián tiếp (chi phí chung, lán trại, một số công việc không xác định được khối lượng từ thiết kế...)
   - Thu nhập chịu thuế tính trước
   - Thuế GTGT
   - Dự phòng (khối lượng phát sinh, trượt giá)
4. **Kiểm tra chéo**: suất vốn đầu tư / chi phí trên m² sàn so với công trình tương tự; khối lượng thép/bê tông trên m² sàn có hợp lý không.

## Khi rà soát dự toán có sẵn
Kiểm tra theo thứ tự và liệt kê lỗi kèm vị trí dòng:
- Sai công thức, sai đơn vị (m² và m³, tấn và kg), cộng trùng hạng mục
- Khối lượng lệch so với diễn giải kích thước
- Áp sai mã định mức hoặc sai đơn giá vùng
- Thiếu hạng mục hay gặp: đào đắp đất, vận chuyển phế thải, cốp pha, chống thấm, công tác hoàn trả mặt bằng
- Tỷ lệ chi phí gián tiếp, dự phòng bất thường

## Định dạng đầu ra
- Bảng khối lượng và bảng dự toán dạng bảng Markdown, hoặc file Excel nếu người dùng cần (có công thức thật, không ghi số chết).
- Cuối bảng có mục **"Giả định và điểm cần xác nhận"**.

## Lưu ý quan trọng
- Định mức, đơn giá và văn bản pháp luật về chi phí xây dựng thay đổi thường xuyên. Khi nêu tên văn bản (nghị định, thông tư), luôn nhắc người dùng kiểm tra văn bản còn hiệu lực không. Không bịa số hiệu văn bản hay mã định mức.
- Dự toán do AI hỗ trợ chỉ là bản nháp; hồ sơ chính thức phải do người có chứng chỉ hành nghề định giá xây dựng kiểm tra và ký.
