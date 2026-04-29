"""
Feature 1: Mã hóa đối xứng (Symmetric Encryption)
Thuật toán: DES, 3DES, AES
"""

from Crypto.Cipher import DES, DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii

from utils.display import (
    clear_screen, print_banner, print_separator,
    print_info, Color
)


# ─────────────────────────────────────────────
#  Helper: in kết quả / lỗi đồng nhất style
# ─────────────────────────────────────────────
def _print_result(label: str, value: str):
    print(f"\n  {Color.GREEN}✔ {label}:{Color.RESET} {value}")

def _print_error(msg: str):
    print(f"\n  {Color.RED}⚠ Lỗi: {msg}{Color.RESET}")

def _pause():
    input(f"\n  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")


# ─────────────────────────────────────────────
#  DES
# ─────────────────────────────────────────────
def _run_des():
    """Sub-flow DES: sinh khóa 1 lần, mã hóa nhiều plaintext."""
    while True:
        clear_screen()
        print_banner()
        print(f"  {Color.BOLD}🔑 DES — ECB Mode{Color.RESET}")
        print_separator()

        # Sinh khóa mới cho mỗi phiên DES
        key = get_random_bytes(8)
        key_hex = binascii.hexlify(key).decode().upper()
        print(f"  {Color.CYAN}Khóa DES (8 bytes, Hex):{Color.RESET} {key_hex}")
        print(f"  {Color.CYAN}Lưu ý:{Color.RESET} Khóa này dùng cho mọi plaintext trong phiên này.")
        print_separator()

        while True:
            plaintext = input(
                f"  {Color.YELLOW}➜ Nhập Plaintext{Color.RESET}"
                f" {Color.CYAN}(Enter để tiếp tục / 'back' để quay lại / 'new' để đổi khóa):{Color.RESET} "
            ).strip()

            if plaintext.lower() == "back":
                return                      # về symmetric_menu
            if plaintext.lower() == "new":
                break                       # vòng ngoài → sinh khóa mới
            if not plaintext:
                continue

            try:
                cipher     = DES.new(key, DES.MODE_ECB)
                ciphertext = cipher.encrypt(pad(plaintext.encode("utf-8"), DES.block_size))
                _print_result("Ciphertext (Hex)", binascii.hexlify(ciphertext).decode().upper())
            except Exception as e:
                _print_error(str(e))


# ─────────────────────────────────────────────
#  3DES
# ─────────────────────────────────────────────
def _run_3des():
    """Sub-flow 3DES: sinh khóa 1 lần, mã hóa nhiều plaintext."""
    while True:
        clear_screen()
        print_banner()
        print(f"  {Color.BOLD}🔑 3DES (Triple DES) — ECB Mode{Color.RESET}")
        print_separator()

        # Sinh khóa mới, điều chỉnh parity để tránh lỗi suy biến
        key = DES3.adjust_key_parity(get_random_bytes(24))
        key_hex = binascii.hexlify(key).decode().upper()
        print(f"  {Color.CYAN}Khóa 3DES (24 bytes, Hex):{Color.RESET} {key_hex}")
        print(f"  {Color.CYAN}Lưu ý:{Color.RESET} Khóa này dùng cho mọi plaintext trong phiên này.")
        print_separator()

        while True:
            plaintext = input(
                f"  {Color.YELLOW}➜ Nhập Plaintext{Color.RESET}"
                f" {Color.CYAN}(Enter để tiếp tục / 'back' để quay lại / 'new' để đổi khóa):{Color.RESET} "
            ).strip()

            if plaintext.lower() == "back":
                return
            if plaintext.lower() == "new":
                break
            if not plaintext:
                continue

            try:
                cipher     = DES3.new(key, DES3.MODE_ECB)
                ciphertext = cipher.encrypt(pad(plaintext.encode("utf-8"), DES3.block_size))
                _print_result("Ciphertext (Hex)", binascii.hexlify(ciphertext).decode().upper())
            except Exception as e:
                _print_error(str(e))


# ─────────────────────────────────────────────
#  Main menu của Feature 1
# ─────────────────────────────────────────────
def symmetric_menu():
    """Menu chính của Feature 1: Symmetric Encryption."""
    while True:
        clear_screen()
        print_banner()
        print(f"  {Color.BOLD}🔐 FEATURE 1: MÃ HÓA ĐỐI XỨNG (Symmetric Encryption){Color.RESET}")
        print_separator()
        print(f"  {Color.CYAN}[1]{Color.RESET} DES")
        print(f"  {Color.CYAN}[2]{Color.RESET} 3DES (Triple DES)")
        print(f"  {Color.CYAN}[3]{Color.RESET} AES (CBC / ECB)")
        print(f"  {Color.CYAN}[0]{Color.RESET} Quay về Main Menu")
        print_separator()

        choice = input(f"  {Color.YELLOW}➜ Chọn thuật toán: {Color.RESET}").strip()

        if choice == "1":
            _run_des()
        elif choice == "2":
            _run_3des()
        elif choice == "3":
            print_info("AES đang được phát triển bởi thành viên nhóm...")
            _pause()
        elif choice == "0":
            break
        else:
            print(f"\n  {Color.RED}⚠ Lựa chọn không hợp lệ.{Color.RESET}")
            _pause()