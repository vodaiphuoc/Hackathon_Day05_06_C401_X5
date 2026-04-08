# SPEC — AI Product Hackathon

**Nhóm:** ___
**Track:** VinHomes\
**Problem statement (1 câu):** Sale bất động sản mất nhiều thời gian để tư vấn với khách hàng qua Zalo, tin nhắn nhưng khách có thể không có nhu cầu mua hoặc nhu cầu đi xem để chốt đặt cọc/hợp đồng

---

## 1. AI Product Canvas

|   | Value | Trust | Feasibility |
|---|-------|-------|-------------|
| **Câu hỏi** | User nào? Pain gì? AI giải gì? | Khi AI sai thì sao? User sửa bằng cách nào? | Cost/latency bao nhiêu? Risk chính? |
| **Trả lời** | *User: Saler VinHomes, Pain: có nhiều khách hàng tiếp cận qua zalo, kênh tin nhắn nhưng không có thời gian trả lời, AI: chatbot hỗ trợ thông tin bất động sản cho khách hàng* | *AI: Trả lời tôi xin lỗi và gửi thông tin liên hệ với human agent.* | *Cost: ~$0.024/chat session.  Latency: < 1.5s (dùng OpenAI hoặc Gemini Flash). Risk: AI cam kết nhầm mức giá chưa cập nhật.* |

**Automation hay augmentation?** ☐ Automation · ☑ Augmentation.

**Justify**: Bất động sản là tài sản lớn, khách cần sự tin tưởng từ con người. AI đóng vai trò "tiền trạm" lọc thông tin và soạn bản thảo cho Saler duyệt.

**Learning signal:**

1. User correction đi vào đâu? Cập nhật lại Knowledge Base (RAG).
2. Product thu signal gì để biết. tốt lên hay tệ đi? Tỷ lệ khách hàng để lại số điện thoại/lịch hẹn xem nhà sau khi chat với AI.
3. Data thuộc loại nào? ☐ User-specific · ☑ Domain-specific · ☐ Real-time · ☐ Human-judgment  
Có marginal value không? Có. Model thông thường không biết chính xác mặt bằng căn hộ hoặc chính sách bán hàng mới nhất của VinHomes.

---
## 2. User Stories — 4 paths

### Feature: AI Sales Assistant (Chatbot & Lead Scoring)

**Trigger:** Khách hàng nhắn tin hỏi về dự án qua Zalo hoặc Web Portal.

| Path | Câu hỏi thiết kế | Mô tả |
|------|-------------------|-------|
| **Happy** — AI đúng, tự tin | User thấy gì? Flow kết thúc ra sao? | *AI trả lời đúng giá, gửi đúng mặt bằng căn hộ. Khách hỏi cách đặt cọc, AI xin SĐT và báo ngay cho Saler: "Khách VIP, cần tư vấn ngay".* |
| **Low-confidence** — AI không chắc | System báo "không chắc" bằng cách nào? User quyết thế nào? | *AI phản hồi: "Em cần xác nhận lại kho hàng thực tế, anh đợi chút nhé". Đồng thời gửi thông báo đẩy "Cần hỗ trợ" về điện thoại của Saler.* |
| **Failure** — AI sai | User biết AI sai bằng cách nào? Recover ra sao? | *AI báo giá nhầm dự án. Saler xem lịch sử chat thấy sai -> Nhấn nút "Disable AI" và vào đính chính thông tin trực tiếp với khách.* |
| **Correction** — user sửa | User sửa bằng cách nào? Data đó đi vào đâu? | *Saler nhấn "Update Info" trên câu trả lời sai. Hệ thống cập nhật lại Knowledge Base để AI không lặp lại lỗi cũ trong tương lai.* |

---

## 3. Eval metrics + threshold

**Optimize precision hay recall?** ☑ Precision · ☐ Recall  
**Tại sao?** *Trong BĐS, báo sai pháp lý hoặc giá tiền có thể gây hậu quả pháp lý nghiêm trọng. Thà AI nói "Tôi không rõ" còn hơn trả lời sai.*

| Metric | Threshold | Red flag (dừng khi) |
|--------|-----------|---------------------|
| **Accuracy (Thông tin dự án)** | ≥ 90% | < 75% |
| **Lead Conversion Rate** | ≥ 15% | < 5% |
| **Response Latency** | < 2.0s | > 5.0s |

---

## 4. Top 3 failure modes

| # | Trigger | Hậu quả | Mitigation |
|---|---------|---------|------------|
| 1 | Khách hỏi gộp nhiều chương trình chiết khấu | AI cộng dồn sai tổng giá tiền cuối cùng | Thiết lập AI chỉ đưa ra khoảng giá dự kiến và dẫn link bảng tính chuẩn. |
| 2 | Khách dùng từ địa phương hoặc viết tắt quá nhiều | AI không hiểu và trả lời lạc đề | Dùng LLM mạnh (Gemini Flash/GPT-4o) có khả năng hiểu tiếng Việt vùng miền tốt. |
| 3 | Tài liệu dự án cũ chưa được cập nhật kịp | AI tư vấn chính sách đã hết hiệu lực | Gắn Timestamp vào từng file tài liệu trong RAG, AI phải báo: "Dữ liệu tính đến ngày..." |

---

## 5. ROI 3 kịch bản

| | Conservative | Realistic | Optimistic |
|---|-------------|-----------|------------|
| **Assumption** | 50 khách/ngày, 50% lọc được khách ảo | 200 khách/ngày, 75% lọc được khách ảo | 1000 khách/ngày, AI xử lý 90% hỏi đáp |
| **Cost** | $10/tháng (API cost) | $50/tháng (API cost) | $200/tháng (API cost) |
| **Benefit** | Tiết kiệm 1h/ngày/Saler | Tiết kiệm 4h/ngày, tăng 10% tỷ lệ chốt | Giảm 80% nhân sự trực chat, tăng 25% doanh thu |
| **Net** | ROI Dương (Tiết kiệm thời gian) | ROI Rất tốt (Tăng năng suất) | ROI Đột phá (Mở rộng quy mô) |

**Kill criteria:** Dừng dự án nếu tỷ lệ khách hàng phàn nàn về sự phiền phức của AI > 20% trong 2 tuần liên tục.

---

## 6. Mini AI spec (1 trang)

**Sản phẩm:** **VinHomes Sales-Mate AI**

* **Vấn đề:** Saler tốn quá nhiều thời gian trả lời những câu hỏi cơ bản (vị trí, tiện ích, giá sơ bộ) từ khách hàng chưa có nhu cầu thực tế cao, dẫn đến bỏ lỡ "khách nét".
* **Giải pháp:** Hệ thống Chatbot thông minh sử dụng **RAG (Retrieval-Augmented Generation)** để tra cứu chính xác từ kho dữ liệu dự án (PDF, Excel chính sách bán hàng).
* **Điểm nhấn công nghệ:** * **FastAPI** xử lý logic backend và kết nối API LLM (Gemini/OpenAI).
    * **Vector Database (ChromaDB/FAISS)** để lưu trữ và tìm kiếm thông tin dự án.
    * **Lead Scoring:** AI tự động đánh giá khách hàng dựa trên nội dung chat (Khách hỏi sâu về dòng tiền -> Gán nhãn "Hot").
* **Quy trình:** Chatbot trực 24/7 -> Tư vấn thông tin chuẩn -> Phân loại khách -> Đẩy thông báo cho Saler chốt deal khi khách đạt ngưỡng "nóng".
* **Rủi ro chính:** Sai lệch dữ liệu khi có chính sách mới. Giải quyết bằng cách tạo pipeline cập nhật dữ liệu RAG nhanh chóng.