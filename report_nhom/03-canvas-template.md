# AI Product Canvas — template

Điền Canvas cho product AI của nhóm. Mỗi ô có câu hỏi guide — trả lời trực tiếp, xóa phần in nghiêng khi điền.
---

Chatbot hỗ trợ tư vấn chuyến bay

## Canvas

|   | Value | Trust | Feasibility |
|---|-------|-------|-------------|
| **Câu hỏi guide** | User nào? Pain gì? AI giải quyết gì mà cách hiện tại không giải được? | Khi AI sai thì user bị ảnh hưởng thế nào? User biết AI sai bằng cách nào? User sửa bằng cách nào? | Cost bao nhiêu/request? Latency bao lâu? Risk chính là gì? |
| **Trả lời** | User: người mua vé, Pain: tìm chuyến bay có giá vé tối ưu nhất tốn 30 phút - 1 tiếng. Aug: chatbot gợi ý, Value: Khi AI đúng, thì tiết kiệm thời gian tìm kiếm | ưu tiên Precision, Khi AI sai thì user có thể bị trễ chuyến, đặt nhầm chuyến, tốn thêm thời gian tìm kiếm. User có thể biết AI sai bằng cách check manual thông tin chuyến bay, nếu sai, bấm report, hoặc bấm vào nút AI response có hữu dụng hay không | Cost per request: nhỏ, với LLM nhỏ, Latency: từ 2s-3s, Risk chính là LLM bị hallucication, không bắt được intent câu hỏi người dùng|

---

## Automation hay augmentation?

☐ Automation — AI làm thay, user không can thiệp
☐ Augmentation — AI gợi ý, user quyết định cuối cùng

=> Augmentation: AI chỉ gợi ý

---

## Learning signal

| # | Câu hỏi | Trả lời |
|---|---------|---------|
| 1 | User correction đi vào đâu? | User correct thu về để cho AI retry|
| 2 | Product thu signal gì để biết tốt lên hay tệ đi? | Cả hai, nếu có rating "hữu ích" chứng tỏ AI recommend tốt, nếu dính "report" button, chứng tỏ sản phẩm tệ đi|
| 3 | Data thuộc loại nào? ☐ User-specific · ☐ Domain-specific · ☐ Real-time · ☐ Human-judgment · ☐ Khác: ___ | User-specific, Domain-specific, Real-time|

**Có marginal value không?** Data có thể hữu ích trong việc tối ưu model ở các version sau để đưa ra recomendation tối ưu hơn, chính xác hơn
___

---

## Cách dùng

1. Điền Value trước — chưa rõ pain thì chưa điền Trust/Feasibility
2. Trust: trả lời 4 câu UX (đúng → sai → không chắc → user sửa)
3. Feasibility: ước lượng cost, không cần chính xác — order of magnitude đủ
4. Learning signal: nghĩ về vòng lặp dài hạn, không chỉ demo ngày mai
5. Đánh [?] cho chỗ chưa biết — Canvas là hypothesis, không phải đáp án

---

*AI Product Canvas — Ngày 5 — VinUni A20 — AI Thực Chiến · 2026*
