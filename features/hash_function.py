"""
Feature 3: Hàm băm (Hash Function)
Thuật toán: MD5, SHA-256
"""

import hashlib
from utils.display import (
    clear_screen, print_banner, print_separator,
    print_result_box, print_success, print_error,
    print_info, ask_try_again, offer_copy, Color
)

# ─── Core logic ───────────────────────────────────────────────

def compute_hash(text: str, algorithm: str) -> dict:
    """
    Tính giá trị hash của text.

    Args:
        text: Chuỗi cần băm
        algorithm: 'md5' hoặc 'sha256'

    Returns:
        dict với keys: hex_digest, byte_length, algo_name
    """
    data = text.encode("utf-8")

    if algorithm == "md5":
        h = hashlib.md5(data)
        algo_name = "MD5"
    elif algorithm == "sha256":
        h = hashlib.sha256(data)
        algo_name = "SHA-256"
    else:
        raise ValueError(f"Thuật toán không được hỗ trợ: {algorithm}")

    hex_digest = h.hexdigest()
    byte_length = len(h.digest())

    return {
        "hex_digest": hex_digest,
        "byte_length": byte_length,
        "bit_length": byte_length * 8,
        "algo_name": algo_name,
    }


def compute_hash_from_file(filepath: str, algorithm: str) -> dict:
    """
    Tính giá trị hash của một file (bonus feature).
    Đọc file theo chunk để xử lý file lớn hiệu quả.
    """
    if algorithm == "md5":
        h = hashlib.md5()
        algo_name = "MD5"
    elif algorithm == "sha256":
        h = hashlib.sha256()
        algo_name = "SHA-256"
    else:
        raise ValueError(f"Thuật toán không được hỗ trợ: {algorithm}")

    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)

    hex_digest = h.hexdigest()
    byte_length = len(h.digest())

    return {
        "hex_digest": hex_digest,
        "byte_length": byte_length,
        "bit_length": byte_length * 8,
        "algo_name": algo_name,
    }

def compare_hashes(hash1: str, hash2: str) -> bool:
    """So sánh hai giá trị hash (case-insensitive)."""
    return hash1.strip().lower() == hash2.strip().lower()

# ─── Sub-menus ────────────────────────────────────────────────

def _algo_menu() -> str | None:
    """Hiển thị menu chọn thuật toán. Trả về 'md5', 'sha256', hoặc None."""
    print(f"\n  {Color.BOLD}Chọn thuật toán:{Color.RESET}")
    print_separator()
    print(f"  {Color.CYAN}[1]{Color.RESET} MD5     (128-bit / 32 ký tự hex)")
    print(f"  {Color.CYAN}[2]{Color.RESET} SHA-256 (256-bit / 64 ký tự hex) ← Khuyến nghị")
    print(f"  {Color.CYAN}[0]{Color.RESET} Quay lại")
    print_separator()

    choice = input(f"  {Color.YELLOW}➜ Chọn: {Color.RESET}").strip()
    if choice == "1":
        return "md5"
    elif choice == "2":
        return "sha256"
    elif choice == "0":
        return None
    else:
        print_error("Lựa chọn không hợp lệ.")
        return None
    

def _do_hash_text(algorithm: str):
    """Luồng: nhập text → tính hash → hiển thị kết quả."""
    while True:
        clear_screen()
        print_banner()
        algo_label = "MD5" if algorithm == "md5" else "SHA-256"
        print(f"  {Color.BOLD}# Hash Function → {algo_label} → Nhập văn bản{Color.RESET}")
        print_separator()

        print_info("Nhập văn bản cần băm (Enter để kết thúc nhập).")
        if algorithm == "md5":
            print_info("Lưu ý: MD5 không còn an toàn về mật mã, chỉ dùng cho mục đích học tập.")
        print()

        text = input(f"  {Color.YELLOW}Plaintext: {Color.RESET}")

        if not text:
            print_error("Văn bản không được để trống.")
            if not ask_try_again():
                break
            continue

        try:
            result = compute_hash(text, algorithm)

            print()
            print_result_box(f"Thuật toán: {result['algo_name']}", "")
            print_result_box("Giá trị Hash (hex)", result["hex_digest"])
            print_info(f"Độ dài: {result['bit_length']} bit ({result['byte_length']} bytes, {len(result['hex_digest'])} ký tự hex)")

            offer_copy(result["hex_digest"])

        except Exception as e:
            print_error(f"Lỗi: {e}")

        if not ask_try_again():
            break