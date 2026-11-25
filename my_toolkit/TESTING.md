# TESTING.md - گزارش تست‌های خودکار

| شماره | ابزار | ورودی | خروجی مورد انتظار | خروجی واقعی | Pass |
|---|---|---|---|---|---|
| 1 | c2f | 100 | 212.00 F | 212.00 F | ✅ |
| 2 | c2f | abc | ValueError | ValueError | ❌ (Fixed) |
| 3 | c2f | ۱۰۰ | ValueError | ValueError | ❌ (Fixed) |
| 4 | people | 0 | None | None | ✅ |
| 5 | people | -5 | None | None | ✅ |
| 6 | people | abc | None | None | ✅ |
| 7 | c2f | 1e308 | inf | inf | ✅ |
| 8 | c2f | 1,000 | ValueError | ValueError | ❌ (Fixed) |