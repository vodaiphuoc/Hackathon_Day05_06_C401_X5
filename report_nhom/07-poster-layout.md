# Poster layout — 1 trang

Poster/slides tóm tắt trưng khi trình bày. Peer nhìn poster/slides trong lúc nghe demo.

---

## Sketch tổng thể

```text
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                 🏙  VINHOMES SALES-MATE AI                      │
│                                                                 │
│   Sales bất động sản mất nhiều thời gian trả lời khách qua      │
│   Zalo/web, nhưng nhiều khách chưa có nhu cầu thật.            │
│   → AI chatbot tư vấn 24/7, lọc lead và đẩy khách nóng cho sale│
│                                                                 │
├────────────────────────────┬────────────────────────────────────┤
│                            │                                    │
│     ❌  BEFORE (hiện tại)   │      ✅  AFTER (với AI)            │
│                            │                                    │
│  ┌──────────┐              │  ┌──────────┐                      │
│  │ Khách hàng│             │  │ Khách hàng│                     │
│  └────┬─────┘              │  └────┬─────┘                      │
│       ↓                    │       ↓                            │
│  Nhắn Zalo / web           │  Nhắn Zalo / web                  │
│       ↓                    │       ↓                            │
│  Sale đọc và tự trả lời    │  AI chatbot trả lời ngay          │
│  từng câu hỏi cơ bản       │  (giá sơ bộ, vị trí, tiện ích)    │
│       ↓                    │       ↓                            │
│  Tốn thời gian lọc khách   │  AI đánh giá lead score           │
│  thật / khách ảo           │  (mức độ quan tâm)                │
│       ↓                    │       ↓                            │
│  Có thể bỏ lỡ khách nóng   │  Lead nóng → báo cho sale ngay    │
│  vì trả lời chậm           │  để chốt lịch xem / đặt cọc       │
│       ↓                    │       ↓                            │
│  Sale xử lý toàn bộ        │  Sale chỉ xử lý case quan trọng   │
│  thủ công                  │  hoặc low-confidence              │
│                            │                                    │
│  📊 6 bước · phản hồi chậm  │  📊 4 bước · < 2 giây             │
│                            │                                    │
├────────────────────────────┴────────────────────────────────────┤
│                                                                 │
│                        💻  LIVE DEMO                             │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                                                         │   │
│   │  ┌─────────────────┐    ┌────────────────────────────┐  │   │
│   │  │ Chat khách hàng │    │  Kết quả AI               │  │   │
│   │  │                 │    │                            │  │   │
│   │  │ "Căn 2PN bên    │    │  • Giá sơ bộ: ...         │  │   │
│   │  │  Ocean Park giá │ →  │  • Tiện ích: ...          │  │   │
│   │  │  bao nhiêu?"    │    │  • Dự án phù hợp: ...     │  │   │
│   │  │                 │    │  • Lead score: HOT        │  │   │
│   │  │ [Gửi]           │    │  • Push cho sales agent   │  │   │
│   │  └─────────────────┘    └────────────────────────────┘  │   │
│   │                                                         │   │
│   │        │   │
│   │                                                         │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│                        📊  IMPACT                                │
│                                                                 │
│   Thời gian phản hồi        vài phút ──→ < 5s                  │
│   Độ chính xác thông tin    mục tiêu ─→ ≥ 90%                  │
│   Lead conversion rate      mục tiêu ─→ ≥ 15%                  │
│   Cost / chat session        — ───────→ ~$0.024                │
│                                                                 │
├──────────────────────────────┬──────────────────────────────────┤
│                              │                                  │
│  ⚠  FAILURE MODES            │  🔄  LEARNING SIGNAL              │
│                              │                                  │
│  1. Chính sách bán hàng cũ   │  User để lại SĐT / lịch hẹn?    │
│     chưa cập nhật            │       ↓                          │
│     → AI tư vấn sai giá      │  Tỷ lệ lead chuyển đổi          │
│                              │       ↓                          │
│  2. Khách hỏi pháp lý khó    │  Sale chỉnh / disable AI        │
│     → AI không được đoán     │       ↓                          │
│     → chuyển human agent     │  Update lại Knowledge Base      │
│                              │                                  │
│  3. Khách dùng từ viết tắt   │  📈 Càng cập nhật RAG tốt hơn    │
│     / địa phương             │  thì AI càng trả lời đúng hơn   │
│     → AI hiểu sai intent     │                                  │
│                              │                                  │
└──────────────────────────────┴──────────────────────────────────┘

Đây là ví dụ cho track Vinmec. Nhóm **thay nội dung** theo product của mình, giữ **cấu trúc 5 phần**.

---

## 5 phần bắt buộc

| # | Phần | Mục đích | Ghi chú |
|---|------|----------|---------|
| 1 | **Tên product + problem statement** | Peer biết ngay product làm gì | 1 câu, font lớn nhất |
| 2 | **Before \| After** | So sánh flow cũ vs flow mới | 2 cột, có flow diagram + số liệu (bước, thời gian) |
| 3 | **Live demo** | Peer thấy product chạy thật | Screenshot UI + QR code hoặc link để peer thử ngay |
| 4 | **Impact** | Chứng minh product có giá trị | Số cụ thể: thời gian, accuracy, cost — trước vs sau |
| 5 | **Failure modes \| Learning signal** | Nhóm hiểu giới hạn + hướng cải thiện | 2 cột: khi AI sai thì sao \| product học gì từ user |

---

## Tips

- Font lớn, đọc được từ 1-2 mét — peer đứng xem
- Ít chữ, nhiều hình — screenshot, diagram, flow > mô tả text
- Dùng Canva template "poster" nếu muốn design nhanh
- Không cần đẹp, cần rõ: peer nhìn 10 giây hiểu product làm gì
- Before/After nên dùng flow diagram thay vì chỉ viết text
- QR code trỏ đến live demo → peer scan thử ngay = ấn tượng hơn

---

## Mở rộng (optional — bonus)

### Before/After chi tiết hơn

Thay vì chỉ mô tả text, show bằng hình:

| | Before (hiện tại) | After (với AI) |
|---|---|---|
| **Screenshot / sketch** | *(ảnh flow cũ)* | *(ảnh flow mới)* |
| **Số bước** | *VD: 7 bước, 10 phút* | *VD: 3 bước, 2 phút* |
| **Pain point chính** | *VD: phải chờ lễ tân* | *VD: AI trả lời ngay* |
| **Ai quyết định** | *VD: lễ tân tra thủ công* | *VD: AI gợi ý, user chọn* |

### QR code đến live demo

In QR code trên poster → peer scan = thử demo ngay trên điện thoại. Ấn tượng hơn nhiều so với chỉ nhìn screenshot.

- Dùng bất kỳ QR generator nào (free) trỏ đến link deploy
- Nếu chưa deploy: QR trỏ đến video recording demo

### Impact dashboard mock

Sketch 1 dashboard nhỏ trên poster, show metric trước và sau:

```
┌─────────────────────────────────┐
│ Thời gian trung bình    10m → 2m │
│ Độ chính xác           — → 85%  │
│ User hài lòng          3/5 → 4/5│
└─────────────────────────────────┘
```

Dùng số thật từ test (nếu có) hoặc ước lượng có cơ sở.

### Câu hỏi mở rộng

- Peer chỉ nhìn poster 10 giây — thông tin nào PHẢI thấy đầu tiên?
- Poster có thể "đứng một mình" (không cần người giải thích) không?
- Nếu phải bỏ 1 phần trên poster, bỏ phần nào? Tại sao?

### Kế hoạch phát triển sản phẩm  ###


### Giai đoạn 1 — Demo / MVP hiện tại
**Mục tiêu:** Chứng minh AI có thể hỗ trợ sales trả lời câu hỏi cơ bản nhanh, đúng ngữ cảnh và biết chuyển cho người thật khi không chắc.

**Hiện tại demo chỉ gồm 3 chức năng chính:**
1. **Chatbot trả lời các câu hỏi phổ biến**: giá sơ bộ, vị trí, tiện ích, loại căn hộ  
2. **Dùng RAG để truy xuất dữ liệu** từ tài liệu dự án  
3. **Khi AI không chắc, chuyển sang human agent**

**Giá trị của giai đoạn demo:**
- Giảm tải cho sales ở các câu hỏi lặp lại
- Cho thấy khả năng truy xuất thông tin đúng từ tài liệu dự án
- Tăng độ an toàn vì AI không cố trả lời khi thiếu chắc chắn

**Giả sử trong giai đoạn demo xảy ra các tình huống sau:**
- **Nếu khách chỉ hỏi thông tin cơ bản** → AI có thể tự trả lời ngay
- **Nếu khách hỏi ngoài dữ liệu hoặc quá mơ hồ** → AI chuyển cho human agent
- **Nếu tài liệu RAG chưa đủ tốt** → câu trả lời có thể thiếu, từ đó nhóm biết cần cải thiện knowledge base
- **Nếu khách muốn nói chuyện trực tiếp** → hệ thống ưu tiên handoff sang sales để giữ trải nghiệm tin cậy

---

### Giai đoạn 2 — Mở rộng thu hút khách hàng mới
**Mục tiêu:** Không chỉ trả lời khách đến sẵn, mà còn **chủ động tạo thêm lead đầu vào**.

**Tính năng phát triển thêm:**
1. **Chủ động đăng bài Facebook, Zalo**
   - AI hỗ trợ tạo nội dung giới thiệu dự án, tiện ích, ưu đãi
   - Lên lịch đăng bài theo chiến dịch bán hàng
   - Tối ưu nội dung theo từng nhóm khách hàng mục tiêu

2. **Tự động trả lời bình luận / inbox cơ bản**
   - Trả lời nhanh các câu hỏi phổ biến dưới bài đăng
   - Gợi ý khách để lại số điện thoại hoặc nhắn tin riêng
   - Chuyển lead quan tâm cao về cho sales

**Giả sử xảy ra các tình huống sau:**
- **Nếu bài đăng thu hút nhiều bình luận cùng lúc** → AI giúp phản hồi nhanh, tránh bỏ sót khách
- **Nếu khách chỉ tương tác xã giao hoặc spam** → AI lọc để sales không mất thời gian
- **Nếu khách hỏi sâu hơn mức AI được phép trả lời** → chuyển inbox hoặc human agent
- **Nếu nội dung đăng bài không hiệu quả** → đo lại reach, comment, số lead tạo ra để tối ưu nội dung

**Kỳ vọng đầu ra:**
- Tăng lượng người dùng mới đi vào funnel
- Tăng số lead đến từ social media
- Giảm thời gian sales phải trực comment/inbox thủ công

---

### Giai đoạn 3 — Nâng cấp năng lực tư vấn chuyên sâu
**Mục tiêu:** Mở rộng chatbot từ trả lời thông tin cơ bản sang **hỗ trợ tư vấn tài chính và pháp lý ở mức an toàn**.

**Tính năng phát triển thêm:**
1. **Hoàn thiện chiến lược tư vấn tài chính**
   - Gợi ý mức giá phù hợp theo ngân sách khách hàng
   - Hỗ trợ giải thích phương án vay, trả góp, dòng tiền cơ bản
   - So sánh sơ bộ các lựa chọn căn hộ theo khả năng chi trả

2. **Hoàn thiện chiến lược tư vấn pháp lý**
   - Giải thích các khái niệm pháp lý phổ biến bằng ngôn ngữ dễ hiểu
   - Chỉ trả lời trong phạm vi tài liệu đã được xác minh
   - Với câu hỏi nhạy cảm hoặc chưa rõ, bắt buộc chuyển human agent

**Giả sử xảy ra các tình huống sau:**
- **Nếu khách hỏi về vay mua nhà** → AI hỗ trợ tư vấn sơ bộ theo kịch bản chuẩn
- **Nếu khách hỏi pháp lý phức tạp** → AI không kết luận thay chuyên viên, chỉ dẫn nguồn và chuyển người thật
- **Nếu chính sách thay đổi** → cần cập nhật lại knowledge base ngay để tránh tư vấn lỗi thời
- **Nếu AI trả lời nhầm trong nhóm chủ đề nhạy cảm** → phải có cơ chế log lỗi, sửa và giới hạn phạm vi trả lời

**Điều kiện để triển khai an toàn:**
- Tài liệu tài chính/pháp lý phải được kiểm duyệt
- Có rule rõ ràng: AI chỉ tư vấn sơ bộ, không cam kết thay con người
- Có cơ chế fallback mạnh hơn cho các câu hỏi rủi ro cao

---

### Giai đoạn 4 — Trải nghiệm trực quan bằng ảnh và video
**Mục tiêu:** Giúp khách hàng **hiểu sản phẩm toàn diện hơn**, không chỉ qua text.

**Tính năng phát triển thêm:**
1. **Xây dựng và tích hợp thư viện ảnh/video căn hộ, chung cư**
   - Ảnh mặt bằng, nội thất mẫu, tiện ích, khuôn viên
   - Video walkthrough căn hộ, khu đô thị, tiện ích nội khu
   - Nội dung media gắn với từng dự án và từng loại căn hộ

2. **AI trả lời kèm media phù hợp**
   - Khi khách hỏi về căn hộ 2PN → trả ngay ảnh mặt bằng hoặc video liên quan
   - Khi khách hỏi về tiện ích → gửi hình ảnh thực tế, video khu vực
   - Khi khách hỏi về trải nghiệm sống → AI gợi ý nội dung trực quan thay vì chỉ mô tả bằng chữ

**Giả sử xảy ra các tình huống sau:**
- **Nếu khách chưa hình dung rõ sản phẩm** → ảnh/video giúp tăng độ hiểu và tăng hứng thú
- **Nếu khách do dự vì thiếu niềm tin** → media thực tế giúp tăng thuyết phục
- **Nếu dự án có nhiều loại căn** → AI có thể chọn đúng bộ media tương ứng
- **Nếu media cũ hoặc sai** → cần quản lý version để tránh gửi nhầm tài sản truyền thông

**Kỳ vọng đầu ra:**
- Tăng mức độ quan tâm của khách hàng
- Tăng tỷ lệ khách đồng ý đi xem thực tế
- Giúp sales tư vấn hiệu quả hơn vì khách đã hiểu trước sản phẩm

---

### Giai đoạn 5 — Hệ thống AI Sales Assistant hoàn chỉnh
**Mục tiêu:** Kết nối toàn bộ hành trình từ **thu hút khách hàng → tư vấn → nuôi dưỡng lead → hỗ trợ sales chốt deal**.

**Bức tranh sản phẩm tương lai:**
- AI chủ động tạo lead từ Facebook, Zalo
- AI trả lời câu hỏi cơ bản 24/7
- AI hỗ trợ tư vấn tài chính/pháp lý ở mức sơ bộ và an toàn
- AI gửi ảnh/video phù hợp để tăng hiểu biết về sản phẩm
- AI chuyển khách nóng cho sales đúng thời điểm
- AI học từ các tình huống sai hoặc bị human takeover để cải thiện dần

**Nếu sản phẩm phát triển tốt trong tương lai:**
- Sales tập trung vào khách hàng chất lượng cao thay vì trả lời lặp lại
- Doanh nghiệp có thêm một kênh tư vấn và thu hút khách tự động
- Khách hàng nhận được trải nghiệm nhanh hơn, rõ ràng hơn, trực quan hơn
- Hệ thống có thể mở rộng sang nhiều dự án, nhiều phân khúc, nhiều kênh hơn

---

### Tầm nhìn phát triển
Từ một **demo chatbot trả lời câu hỏi cơ bản bằng RAG**, sản phẩm có thể phát triển thành một **AI Sales Assistant toàn diện** có khả năng:
- thu hút người dùng mới từ social media,
- hỗ trợ tư vấn an toàn hơn về tài chính và pháp lý,
- cung cấp trải nghiệm trực quan bằng ảnh/video,
- và phối hợp với sales trong toàn bộ quy trình bán hàng.