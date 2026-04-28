# Cryptography Toolkit

CLI App Python — Bài tập môn An toàn thông tin

## Cấu trúc project

```
crypto_toolkit/
├── main.py                  # Entry point, Main Menu
├── requirements.txt
├── features/
│   ├── symmetric.py         # Feature 1: DES, 3DES, AES
│   ├── asymmetric.py        # Feature 2: RSA
│   └── hash_function.py     # Feature 3: MD5, SHA-256
└── utils/
    └── display.py           # Tiện ích UI dùng chung
```

## Cài đặt

```bash
pip install -r requirements.txt
```

## Chạy app

```bash
python main.py
```

## Phân công
| Họ tên                | MSSV       | Phân công                           |
| --------------------- | ---------- | ----------------------------------- |
| Nguyễn Minh Đại Dương | N23DCCN082 | Feature 1                           |
| Nguyễn Quốc Dương     | N23DCCN150 | Feature 1                           |
| Hồ Văn Đức            | N23DCCN147 | Feature 2                           |
| Trần Hoàng Đạt        | N23DCCN145 | Feature 2                           |
| Phạm Đình Hải         | N23DCCN153 | Khởi tạo, set up project, Feature 3 |

## Thư viện sử dụng

- `hashlib` (stdlib) — MD5, SHA-256
- `pycryptodome` — DES, 3DES, AES, RSA
- `pyperclip` (optional) — Copy to clipboard
