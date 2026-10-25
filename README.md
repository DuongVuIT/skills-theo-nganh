# Skills theo ngành

Bộ skills tiếng Việt cho Claude, chia theo ngành nghề. Mỗi ngành là một plugin riêng: bạn chỉ cài bộ skills cho lĩnh vực của mình.

| Plugin | Ngành | Skills |
|---|---|---|
| `xay-dung` | Xây dựng | Dự toán xây dựng · Hồ sơ thi công – nghiệm thu · An toàn lao động |
| `kinh-te-tai-chinh` | Kinh tế – Tài chính | Phân tích báo cáo tài chính · Thẩm định dự án đầu tư (NPV, IRR) · Phân tích kinh tế vĩ mô |
| `ke-toan` | Kế toán | Định khoản kế toán · Đối chiếu sổ sách · Rà soát hồ sơ thuế |
| `phap-ly-hanh-chinh` | Pháp lý – Hành chính | Soạn hợp đồng · Rà soát hợp đồng · Soạn công văn |

## Cài đặt (Claude Code)

**Bước 1 — Thêm marketplace** (chỉ cần làm một lần):

```
/plugin marketplace add DuongVuIT/skills-theo-nganh
```

**Bước 2 — Chọn ngành và cài:**

Gõ `/plugin`, vào mục duyệt plugin rồi chọn ngành của bạn. Hoặc cài trực tiếp:

```
/plugin install xay-dung@skills-theo-nganh
/plugin install kinh-te-tai-chinh@skills-theo-nganh
/plugin install ke-toan@skills-theo-nganh
/plugin install phap-ly-hanh-chinh@skills-theo-nganh
```

Có thể cài nhiều ngành cùng lúc. Sau khi cài, khởi động lại Claude Code.

**Bước 3 — Dùng:** cứ hỏi bình thường, ví dụ *"Bóc khối lượng móng băng cho nhà 3 tầng này"* hay *"Định khoản nghiệp vụ mua hàng chưa thanh toán"*. Claude tự chọn skill phù hợp.

Cập nhật khi có phiên bản mới: `/plugin marketplace update skills-theo-nganh`.

## Cấu trúc thư mục

```
.claude-plugin/marketplace.json      # danh sách các plugin (ngành)
plugins/
  <ngành>/
    .claude-plugin/plugin.json       # thông tin plugin
    skills/<tên-skill>/SKILL.md      # nội dung skill
```

## Thêm ngành mới

1. Tạo `plugins/<ten-nganh>/.claude-plugin/plugin.json` (theo mẫu của các ngành hiện có).
2. Thêm skills vào `plugins/<ten-nganh>/skills/<ten-skill>/SKILL.md`. Mỗi file có phần đầu `name` và `description`; `description` cần nêu rõ **khi nào** dùng skill để Claude chọn đúng.
3. Khai báo plugin mới trong `.claude-plugin/marketplace.json`.
4. Kiểm tra: `claude plugin validate .`

Tên plugin và tên skill viết không dấu, chữ thường, nối bằng gạch ngang.

## Lưu ý

Nội dung các skill là công cụ hỗ trợ, không thay thế ý kiến của người có chuyên môn và chứng chỉ hành nghề (kỹ sư định giá, kế toán trưởng, đại lý thuế, luật sư). Quy định pháp luật Việt Nam thay đổi thường xuyên; luôn kiểm tra văn bản còn hiệu lực.
