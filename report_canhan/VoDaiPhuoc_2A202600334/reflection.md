# Individual reflection — Võ Đại Phước (2A202600334)

## 1. Role
Lên ý tưởng cho đề tài + vibe code + audit code + đóng góp thảo luận

## 2. Đóng góp cụ thể
- Lên ý tưởng idea cho đề tài, mạnh dạn đề xuất chọn track ngoài cho vinhomes, thu thập ý kiến các bạn trong team để hình thành bài toán cụ thể
- audit code cho RAG, vibe code full stack end 2 end với langgraph (nhưng fail để demo vì out date langchain sdk cho Qdrant)
- thảo luận với team để tinh chỉnh system prompt
- chủ động note lại case chắc chắc tính năng sẽ không được hỗ trợ trong mvp

## 3. SPEC mạnh/yếu
- Mạnh nhất: 
    - product canvas: most pain point của người mua sản phẩm trong mô hình kinh doanh
- Yếu nhất: 
    ROI — kịch bản về chi phía chưa clear
    User stories chỉ tập trung vào happy case

## 4. Đóng góp khác
- Defend với các team bạn khác trong lúc hackathon về đề tài

## 5. Điều học được
- Còn thiếu những user stories và usecases mà chỉ khi defend với team khác mới nhận ra
- Chưa truyền đạt được mô hình kinh doanh/idea cho team khác hiểu
- vibe-code nhưng ko fix issue gốc từ đầu, dẫn đến tốn thời gian fix bug trong khi vibe code
- Thử nghiệm RAG retrieve as a tool chậm => ko kịp improve quality của agent
- Có thể bổ sung SKILL.md cho bài toán giúp giải quyết quá trình tư vấn tốt hơn nhưng chưa thử được

## 6. Nếu làm lại
- Vibe code ngay từ đầu với implementation plan giúp demo suôn sẻ hơn
- Bổ sung SKILL, workflow để hỗ trợ bài toán tư vấn tốt hơn
- Mời team khác feedback sớm để kịp audit

## 7. AI giúp gì / AI sai gì
- **Giúp:** tạo MVP nhanh, suggest user stories tạm ổn
- **Sai/mislead:** AI có đề xuât tốt nhưng có thể chưa fix, chọn model rẻ có thể dẫn đến code quality thấp => khả năng fail demo cao
