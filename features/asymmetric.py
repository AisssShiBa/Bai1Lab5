"""
Feature 2: Mã hóa bất đối xứng (Asymmetric Encryption)
Thuật toán: RSA
TODO: Implement by teammate
"""

from utils.display import (
    clear_screen, print_banner, print_separator,
    print_info, Color
)


def asymmetric_menu():
    """Menu chính của Feature 2: Asymmetric Encryption."""
    while True:
        clear_screen()
        print_banner()
        print(f"  {Color.BOLD}🔑 FEATURE 2: MÃ HÓA BẤT ĐỐI XỨNG (Asymmetric Encryption){Color.RESET}")
        print_separator()
        print(f"  {Color.CYAN}[1]{Color.RESET} Tạo Key Pair (Generate RSA Keys)")
        print(f"  {Color.CYAN}[2]{Color.RESET} Mã hóa (Encrypt với Public Key)")
        print(f"  {Color.CYAN}[3]{Color.RESET} Giải mã (Decrypt với Private Key)")
        print(f"  {Color.CYAN}[0]{Color.RESET} Quay về Main Menu")
        print_separator()

        choice = input(f"  {Color.YELLOW}➜ Chọn: {Color.RESET}").strip()

        if choice == "1":
            public_key, private_key = generate_rsa_keys()
            print_info("Tạo thành công RSA Key Pair!")
            print(f"\n  {Color.GREEN}Public Key:{Color.RESET}\n{public_key.decode()}")
            print(f"\n  {Color.GREEN}Private Key:{Color.RESET}\n{private_key.decode()}")
            input(f"\n  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")
        elif choice == "2":
            pub_key = input(f"  {Color.YELLOW}Nhập Public Key: {Color.RESET}")
            message = input(f"  {Color.YELLOW}Nhập thông điệp cần mã hóa: {Color.RESET}")
            try:
                encrypted = rsa_encrypt(message, pub_key.encode())
                print_info("Mã hóa thành công!")
                print(f"\n  {Color.GREEN}Ciphertext (hex):{Color.RESET}\n{encrypted.hex()}")
            except Exception as e:
                print(f"\n  {Color.RED}Lỗi mã hóa: {e}{Color.RESET}")
            input(f"\n  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")
        elif choice == "3":
            print_info("Chức năng giải mã đang được phát triển...")
            input(f"\n  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")
        elif choice == "0":
            break
        else:
            print(f"\n  {Color.RED}⚠ Lựa chọn không hợp lệ.{Color.RESET}")
            input(f"  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")

# Thêm các hàm RSA và import ngoài menu
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key

def rsa_encrypt(message, public_key):
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    return cipher_rsa.encrypt(message.encode())
