# Đưa các import lên đầu file theo chuẩn Python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from utils.display import (
    clear_screen, print_banner, print_separator,
    print_info, Color
)


def read_multiline_input(prompt_msg):
    """Hỗ trợ nhập chuỗi nhiều dòng (dùng để copy-paste các Key PEM format)."""
    print(prompt_msg)
    print(f"  {Color.YELLOW}(Dán đoạn Key vào đây, sau đó nhấn Enter 2 lần để xác nhận){Color.RESET}")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return "\n".join(lines)


def generate_rsa_keys():
    """Tạo cặp khóa RSA 2048 bit."""
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key


def rsa_encrypt(message, public_key_pem):
    """Mã hóa thông điệp bằng Public Key."""
    recipient_key = RSA.import_key(public_key_pem)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    # Trả về bytes
    return cipher_rsa.encrypt(message.encode('utf-8'))


def rsa_decrypt(ciphertext_hex, private_key_pem):
    """Giải mã chuỗi Hex bằng Private Key."""
    private_key = RSA.import_key(private_key_pem)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    # Chuyển chuỗi hex thành bytes rồi mới giải mã
    decrypted_bytes = cipher_rsa.decrypt(bytes.fromhex(ciphertext_hex))
    return decrypted_bytes.decode('utf-8')


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
            print(f"\n  {Color.GREEN}Public Key:{Color.RESET}\n{public_key.decode('utf-8')}")
            print(f"\n  {Color.GREEN}Private Key:{Color.RESET}\n{private_key.decode('utf-8')}")
            input(f"\n  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")

        elif choice == "2":
            # Dùng hàm đọc nhiều dòng thay vì input() thông thường
            pub_key = read_multiline_input(f"\n  {Color.BOLD}Nhập/Dán Public Key:{Color.RESET}")
            message = input(f"  {Color.BOLD}Nhập thông điệp cần mã hóa: {Color.RESET}")
            
            try:
                encrypted = rsa_encrypt(message, pub_key.encode('utf-8'))
                print_info("Mã hóa thành công!")
                print(f"\n  {Color.GREEN}Ciphertext (hex):{Color.RESET}\n{encrypted.hex()}")
                print(f"\n  {Color.YELLOW}(Hãy copy dòng hex phía trên để dùng cho chức năng Giải mã){Color.RESET}")
            except Exception as e:
                print(f"\n  {Color.RED}Lỗi mã hóa: Vui lòng kiểm tra lại Public Key. ({e}){Color.RESET}")
            
            input(f"\n  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")

        elif choice == "3":
            # Chức năng Giải mã đã được thêm vào
            priv_key = read_multiline_input(f"\n  {Color.BOLD}Nhập/Dán Private Key:{Color.RESET}")
            ciphertext = input(f"  {Color.BOLD}Nhập Ciphertext (dạng hex): {Color.RESET}").strip()
            
            try:
                decrypted_message = rsa_decrypt(ciphertext, priv_key.encode('utf-8'))
                print_info("Giải mã thành công!")
                print(f"\n  {Color.GREEN}Plaintext (Thông điệp gốc):{Color.RESET}\n{decrypted_message}")
            except ValueError:
                print(f"\n  {Color.RED}Lỗi giải mã: Ciphertext hoặc Private Key không đúng định dạng/không khớp nhau.{Color.RESET}")
            except Exception as e:
                print(f"\n  {Color.RED}Lỗi giải mã: {e}{Color.RESET}")
                
            input(f"\n  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")

        elif choice == "0":
            break
        else:
            print(f"\n  {Color.RED}⚠ Lựa chọn không hợp lệ.{Color.RESET}")
            input(f"  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")