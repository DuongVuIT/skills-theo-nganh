---
name: tham-dinh-du-an-dau-tu
description: Thẩm định hiệu quả tài chính dự án đầu tư: lập dòng tiền, tính NPV, IRR, thời gian hoàn vốn, chỉ số lợi ích/chi phí, phân tích độ nhạy và kịch bản. Dùng khi người dùng cần đánh giá một dự án, phương án kinh doanh, so sánh các phương án đầu tư hoặc lập phần hiệu quả tài chính cho báo cáo nghiên cứu khả thi.
---

# Thẩm định dự án đầu tư

## Mục tiêu
Cho ra dòng tiền minh bạch và các chỉ tiêu hiệu quả tính đúng, kèm phân tích độ nhạy để người ra quyết định thấy rủi ro.

## Thông tin cần hỏi
- Tổng vốn đầu tư và tiến độ giải ngân; cơ cấu vốn (tự có / vay, lãi suất, thời hạn vay)
- Doanh thu dự kiến: sản lượng, giá bán, công suất theo năm
- Chi phí hoạt động: cố định, biến đổi
- Khấu hao (phương pháp, thời gian), thuế thu nhập doanh nghiệp, ưu đãi thuế nếu có
- Vòng đời dự án, giá trị thanh lý
- Suất chiết khấu (WACC hoặc lãi suất yêu cầu của chủ đầu tư)

Ghi rõ mọi giả định thành một bảng riêng trước khi tính.

## Quy trình
1. Lập bảng dòng tiền theo năm: đầu tư, doanh thu, chi phí, khấu hao, lợi nhuận trước thuế, thuế, lợi nhuận sau thuế, dòng tiền ròng (= LNST + khấu hao − đầu tư − tăng vốn lưu động + thanh lý).
2. Tính chỉ tiêu bằng script đi kèm (không tính nhẩm IRR):
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/tham-dinh-du-an-dau-tu/scripts/chi_tieu_du_an.py" --rate 0.10 --cashflows -1000 200 300 400 500
   ```
   Script in ra NPV, IRR, thời gian hoàn vốn giản đơn và có chiết khấu, tỷ số PI. Dòng tiền năm 0 là số âm (vốn bỏ ra).
3. **Phân tích độ nhạy**: thay đổi từng biến chính (giá bán, sản lượng, chi phí đầu tư, chi phí vận hành, suất chiết khấu) ±10%, ±20% và xem NPV, IRR thay đổi thế nào. Chỉ ra biến nhạy nhất.
4. **Kịch bản**: tốt, cơ sở, xấu.
5. **Kết luận**: dự án có khả thi về tài chính không, với điều kiện gì, rủi ro lớn nhất là gì.

## Lưu ý về phương pháp
- Dòng tiền danh nghĩa đi với suất chiết khấu danh nghĩa; dòng tiền thực đi với suất chiết khấu thực. Không trộn lẫn.
- Dòng tiền đổi dấu nhiều lần có thể có nhiều IRR; khi đó dựa vào NPV.
- So sánh các dự án loại trừ nhau có quy mô khác nhau: ưu tiên NPV, không chỉ nhìn IRR.
- Đây là phân tích hỗ trợ ra quyết định, không phải tư vấn đầu tư cá nhân.
