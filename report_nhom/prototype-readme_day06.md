# Prototype — VINHOMES SALES-MATE 

## Mô tả
** Chat bot hỗ trợ giới thiệu bất động sản Vinhome cho saler tiết kiệm thời gian giới thiệu và tư vấn với khách hàng qua Zalo, tin nhắn **

## Level: Mock prototype
- UI build bằng Cursor/Claude (HTML/CSS/JS)
- 1 flow chính chạy thật với OpenAI API: nhập thông tin theo nhu cầu về bất động sản của khách → nhận gợi ý về thông tin bất động sản tương đương

## Links
- prototype: https://github.com/vodaiphuoc/Hackathon_Day05_06_C401_X5
- Prompt test log: 
- Video demo (backup): 

## Tools
- UI: Cursor/Claude
- AI: OpenAI model gpt-4o-mini
- Prompt: system prompt + Database(thông tin bất động sản)

## Phân công
| Thành viên | Phần | Output |
|-----------|------|--------|
| Phước | Model + Tool + Front prototype1 | model.py +  Front prototype1|
| Nhân | 3->6 spec + fake data| du_lieu_chung_cu_HN_HCM_1000_dong (1).csv + spec.md(3->6) |
| Bân | Backend(database) + Front + Model | rag_service.py database.py + frontend final |
| Đức Lâm |  User stories 4 paths + prompt engineering | system_prompt + spec.md(2. User Stories — 4 paths) |
| Tùng Lâm | fake data + canvas/slide canvas | du_lieu_chung_cu_HN_HCM_1000_dong (1).csv + spec.md(1. AI Product Canvas)  |