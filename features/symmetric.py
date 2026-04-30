"""
Feature 1: Mã hóa đối xứng (Symmetric Encryption)
Thuật toán: DES, 3DES, AES
"""

from Crypto.Cipher import DES, DES3, AES
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
#  AES — ECB & CBC 
# ─────────────────────────────────────────────

# Kích thước khóa hợp lệ của AES (bytes)
_AES_KEY_SIZES = {"128": 16, "192": 24, "256": 32}


def _aes_select_key_size() -> int | None:
    """Cho người dùng chọn độ dài khóa AES. Trả về số bytes hoặc None nếu back."""
    print(f"\n  {Color.CYAN}Chọn độ dài khóa AES:{Color.RESET}")
    print(f"  {Color.CYAN}[1]{Color.RESET} 128-bit  (16 bytes)")
    print(f"  {Color.CYAN}[2]{Color.RESET} 192-bit  (24 bytes)")
    print(f"  {Color.CYAN}[3]{Color.RESET} 256-bit  (32 bytes)")
    print(f"  {Color.CYAN}[0]{Color.RESET} Quay lại")
    print_separator()

    mapping = {"1": 16, "2": 24, "3": 32}
    while True:
        choice = input(f"  {Color.YELLOW}➜ Lựa chọn: {Color.RESET}").strip()
        if choice == "0":
            return None
        if choice in mapping:
            return mapping[choice]
        print(f"  {Color.RED}⚠ Vui lòng nhập 0–3.{Color.RESET}")


def _aes_input_key(key_size: int) -> bytes | None:
    """
    Hỏi người dùng muốn tự nhập hay tự sinh khóa.
    Trả về bytes khóa hoặc None nếu back.
    """
    print(f"\n  {Color.CYAN}Nhập khóa AES ({key_size * 8}-bit):{Color.RESET}")
    print(f"  {Color.CYAN}[1]{Color.RESET} Tự động sinh khóa ngẫu nhiên")
    print(f"  {Color.CYAN}[2]{Color.RESET} Nhập thủ công (Hex, {key_size * 2} ký tự)")
    print(f"  {Color.CYAN}[0]{Color.RESET} Quay lại")
    print_separator()

    while True:
        choice = input(f"  {Color.YELLOW}➜ Lựa chọn: {Color.RESET}").strip()

        if choice == "0":
            return None

        if choice == "1":
            key = get_random_bytes(key_size)
            print(f"  {Color.GREEN}✔ Khóa sinh ngẫu nhiên:{Color.RESET} {binascii.hexlify(key).decode().upper()}")
            return key

        if choice == "2":
            raw = input(
                f"  {Color.YELLOW}➜ Nhập khóa (Hex, {key_size * 2} ký tự): {Color.RESET}"
            ).strip()
            if len(raw) != key_size * 2:
                _print_error(f"Độ dài không đúng — cần {key_size * 2} ký tự Hex, bạn nhập {len(raw)}.")
                continue
            try:
                key = binascii.unhexlify(raw)
                return key
            except Exception:
                _print_error("Chuỗi Hex không hợp lệ.")
            continue

        print(f"  {Color.RED}⚠ Vui lòng nhập 0–2.{Color.RESET}")


def _aes_encrypt(key: bytes, mode_label: str, mode_const: int):
    """
    Vòng mã hóa AES cho một mode cụ thể.
    mode_label : "ECB" hoặc "CBC"
    mode_const : AES.MODE_ECB hoặc AES.MODE_CBC
    """
    key_hex   = binascii.hexlify(key).decode().upper()
    key_bits  = len(key) * 8

    while True:
        clear_screen()
        print_banner()
        print(f"  {Color.BOLD}🔒 AES-{key_bits} — {mode_label} — Mã hóa{Color.RESET}")
        print_separator()
        print(f"  {Color.CYAN}Khóa ({key_bits}-bit, Hex):{Color.RESET} {key_hex}")
        print_separator()

        plaintext_raw = input(
            f"  {Color.YELLOW}➜ Nhập Plaintext{Color.RESET}"
            f" {Color.CYAN}('back' để quay lại):{Color.RESET} "
        ).strip()

        if plaintext_raw.lower() == "back":
            return

        if not plaintext_raw:
            continue

        try:
            pt_bytes = plaintext_raw.encode("utf-8")

            if mode_const == AES.MODE_CBC:
                iv     = get_random_bytes(AES.block_size)          # IV ngẫu nhiên 16 bytes
                cipher = AES.new(key, AES.MODE_CBC, iv)
                ct     = cipher.encrypt(pad(pt_bytes, AES.block_size))
                iv_hex = binascii.hexlify(iv).decode().upper()
                ct_hex = binascii.hexlify(ct).decode().upper()
                _print_result("IV  (Hex) — lưu lại để giải mã", iv_hex)
                _print_result("Ciphertext (Hex)", ct_hex)
            else:  # ECB
                cipher = AES.new(key, AES.MODE_ECB)
                ct     = cipher.encrypt(pad(pt_bytes, AES.block_size))
                _print_result("Ciphertext (Hex)", binascii.hexlify(ct).decode().upper())

        except Exception as e:
            _print_error(str(e))

        _pause()


def _aes_decrypt(key: bytes, mode_label: str, mode_const: int):
    """
    Vòng giải mã AES cho một mode cụ thể.
    """
    key_hex  = binascii.hexlify(key).decode().upper()
    key_bits = len(key) * 8

    while True:
        clear_screen()
        print_banner()
        print(f"  {Color.BOLD}🔓 AES-{key_bits} — {mode_label} — Giải mã{Color.RESET}")
        print_separator()
        print(f"  {Color.CYAN}Khóa ({key_bits}-bit, Hex):{Color.RESET} {key_hex}")
        print_separator()

        # CBC cần IV; ECB thì không
        iv = None
        if mode_const == AES.MODE_CBC:
            iv_raw = input(
                f"  {Color.YELLOW}➜ Nhập IV (Hex, 32 ký tự){Color.RESET}"
                f" {Color.CYAN}('back' để quay lại):{Color.RESET} "
            ).strip()
            if iv_raw.lower() == "back":
                return
            if len(iv_raw) != 32:
                _print_error(f"IV phải là 32 ký tự Hex (16 bytes), bạn nhập {len(iv_raw)}.")
                _pause()
                continue
            try:
                iv = binascii.unhexlify(iv_raw)
            except Exception:
                _print_error("IV không phải chuỗi Hex hợp lệ.")
                _pause()
                continue

        ct_raw = input(
            f"  {Color.YELLOW}➜ Nhập Ciphertext (Hex){Color.RESET}"
            f" {Color.CYAN}('back' để quay lại):{Color.RESET} "
        ).strip()

        if ct_raw.lower() == "back":
            return
        if not ct_raw:
            continue

        try:
            ct = binascii.unhexlify(ct_raw)

            if mode_const == AES.MODE_CBC:
                cipher = AES.new(key, AES.MODE_CBC, iv)
            else:
                cipher = AES.new(key, AES.MODE_ECB)

            pt = unpad(cipher.decrypt(ct), AES.block_size).decode("utf-8")
            _print_result("Plaintext", pt)

        except ValueError as e:
            _print_error(f"Giải mã thất bại — sai khóa, IV, hoặc dữ liệu bị lỗi. ({e})")
        except Exception as e:
            _print_error(str(e))

        _pause()


def _run_aes():
    """Sub-flow AES: chọn key size → nhập/sinh khóa → chọn mode → encrypt/decrypt."""
    while True:
        clear_screen()
        print_banner()
        print(f"  {Color.BOLD}🔑 AES (Advanced Encryption Standard){Color.RESET}")
        print_separator()

        # B1: Chọn độ dài khóa
        key_size = _aes_select_key_size()
        if key_size is None:
            return  # về symmetric_menu

        # B2: Nhập hoặc sinh khóa
        clear_screen()
        print_banner()
        print(f"  {Color.BOLD}🔑 AES-{key_size * 8}{Color.RESET}")
        print_separator()
        key = _aes_input_key(key_size)
        if key is None:
            continue  # chọn lại key size

        # B3: Chọn mode và thao tác
        while True:
            clear_screen()
            print_banner()
            print(f"  {Color.BOLD}🔑 AES-{key_size * 8} — Chọn chế độ & thao tác{Color.RESET}")
            print_separator()
            print(f"  {Color.CYAN}Khóa hiện tại:{Color.RESET} {binascii.hexlify(key).decode().upper()}")
            print_separator()
            print(f"  {Color.CYAN}[1]{Color.RESET} Mã hóa — ECB")
            print(f"  {Color.CYAN}[2]{Color.RESET} Giải mã — ECB")
            print(f"  {Color.CYAN}[3]{Color.RESET} Mã hóa — CBC")
            print(f"  {Color.CYAN}[4]{Color.RESET} Giải mã — CBC")
            print(f"  {Color.CYAN}[5]{Color.RESET} Đổi khóa / Đổi key size")
            print(f"  {Color.CYAN}[0]{Color.RESET} Quay về Symmetric Menu")
            print_separator()

            choice = input(f"  {Color.YELLOW}➜ Lựa chọn: {Color.RESET}").strip()

            if choice == "1":
                _aes_encrypt(key, "ECB", AES.MODE_ECB)
            elif choice == "2":
                _aes_decrypt(key, "ECB", AES.MODE_ECB)
            elif choice == "3":
                _aes_encrypt(key, "CBC", AES.MODE_CBC)
            elif choice == "4":
                _aes_decrypt(key, "CBC", AES.MODE_CBC)
            elif choice == "5":
                break   # vòng ngoài → chọn lại key size + key
            elif choice == "0":
                return  # về symmetric_menu
            else:
                print(f"\n  {Color.RED}⚠ Lựa chọn không hợp lệ.{Color.RESET}")
                _pause()


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
        print(f"  {Color.CYAN}[3]{Color.RESET} AES (ECB / CBC)")
        print(f"  {Color.CYAN}[0]{Color.RESET} Quay về Main Menu")
        print_separator()

        choice = input(f"  {Color.YELLOW}➜ Chọn thuật toán: {Color.RESET}").strip()

        if choice == "1":
            _run_des()
        elif choice == "2":
            _run_3des()
        elif choice == "3":
            _run_aes()
        elif choice == "0":
            break
        else:
            print(f"\n  {Color.RED}⚠ Lựa chọn không hợp lệ.{Color.RESET}")
            _pause()