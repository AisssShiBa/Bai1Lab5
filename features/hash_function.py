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

def _do_hash_file(algorithm: str):
    """Bonus: tính hash của file."""
    while True:
        clear_screen()
        print_banner()
        algo_label = "MD5" if algorithm == "md5" else "SHA-256"
        print(f"  {Color.BOLD}# Hash Function → {algo_label} → Hash từ File{Color.RESET}")
        print_separator()
        print_info("Nhập đường dẫn đến file cần tính hash.")
        print()

        filepath = input(f"  {Color.YELLOW}Đường dẫn file: {Color.RESET}").strip()

        if not filepath:
            print_error("Đường dẫn không được để trống.")
            if not ask_try_again():
                break
            continue

        try:
            result = compute_hash_from_file(filepath, algorithm)

            print()
            print_result_box(f"{result['algo_name']} của file: {filepath}", result["hex_digest"])
            print_info(f"Độ dài: {result['bit_length']} bit")

            offer_copy(result["hex_digest"])

        except FileNotFoundError:
            print_error(f"Không tìm thấy file: {filepath}")
        except PermissionError:
            print_error("Không có quyền đọc file này.")
        except Exception as e:
            print_error(f"Lỗi: {e}")

        if not ask_try_again():
            break

def _do_verify_hash(algorithm: str):
    """Bonus: kiểm tra tính toàn vẹn — so sánh hash của text với hash đã biết."""
    while True:
        clear_screen()
        print_banner()
        algo_label = "MD5" if algorithm == "md5" else "SHA-256"
        print(f"  {Color.BOLD}# Hash Function → {algo_label} → Xác minh Hash{Color.RESET}")
        print_separator()
        print_info("Nhập văn bản gốc và hash đã biết để xác minh tính toàn vẹn.")
        print()

        print(f"{Color.YELLOW}Nhập văn bản (Enter 2 lần để kết thúc):{Color.RESET}")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)

        text = "\r\n".join(lines)

        known_hash = input(f"{Color.YELLOW}Hash cần so sánh: {Color.RESET}").strip()

        if not text or not known_hash:
            print_error("Vui lòng nhập đầy đủ thông tin.")
            if not ask_try_again():
                break
            continue

        try:
            result = compute_hash(text, algorithm)
            computed = result["hex_digest"]

            print()
            print_result_box("Hash tính được", computed)
            print_result_box("Hash cần so sánh", known_hash)

            if compare_hashes(computed, known_hash):
                print_success("✔ KHỚP! Văn bản toàn vẹn, không bị thay đổi.")
            else:
                print_error("✘ KHÔNG KHỚP! Văn bản đã bị thay đổi hoặc hash sai.")

        except Exception as e:
            print_error(f"Lỗi: {e}")

        if not ask_try_again():
            break


def _hash_action_menu(algorithm: str):
    """Menu chọn hành động sau khi đã chọn thuật toán."""
    while True:
        clear_screen()
        print_banner()
        algo_label = "MD5" if algorithm == "md5" else "SHA-256"
        print(f"  {Color.BOLD}# Hash Function → {algo_label}{Color.RESET}")
        print_separator()
        print(f"  {Color.CYAN}[1]{Color.RESET} Hash văn bản (Text)")
        print(f"  {Color.CYAN}[2]{Color.RESET} Hash từ File (Bonus)")
        print(f"  {Color.CYAN}[3]{Color.RESET} Xác minh Hash (Verify Integrity - Bonus)")
        print(f"  {Color.CYAN}[0]{Color.RESET} Quay lại chọn thuật toán")
        print_separator()

        choice = input(f"  {Color.YELLOW}➜ Chọn: {Color.RESET}").strip()

        if choice == "1":
            _do_hash_text(algorithm)
        elif choice == "2":
            _do_hash_file(algorithm)
        elif choice == "3":
            _do_verify_hash(algorithm)
        elif choice == "0":
            break
        else:
            print_error("Lựa chọn không hợp lệ.")
            input(f"  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")


# ─── Entry point ──────────────────────────────────────────────

def hash_menu():
    """Menu chính của Feature 3: Hash Function."""
    while True:
        clear_screen()
        print_banner()
        print(f"  {Color.BOLD}# FEATURE 3: HÀM BĂM (Hash Function){Color.RESET}")
        print_separator()
        print(f"  {Color.CYAN}[1]{Color.RESET} MD5     — 128-bit")
        print(f"  {Color.CYAN}[2]{Color.RESET} SHA-256 — 256-bit  {Color.GREEN}(Khuyến nghị){Color.RESET}")
        print(f"  {Color.CYAN}[0]{Color.RESET} Quay về Main Menu")
        print_separator()

        choice = input(f"  {Color.YELLOW}➜ Chọn thuật toán: {Color.RESET}").strip()

        if choice == "1":
            _hash_action_menu("md5")
        elif choice == "2":
            _hash_action_menu("sha256")
        elif choice == "0":
            break
        else:
            print_error("Lựa chọn không hợp lệ.")
            input(f"  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")
