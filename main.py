"""
╔══════════════════════════════════════════╗
║         CRYPTOGRAPHY TOOLKIT             ║
║         CLI App - Python                 ║
╚══════════════════════════════════════════╝
"""

import sys
from utils.display import clear_screen, print_banner, print_separator, Color


def main_menu():
    """Hiển thị main menu và điều hướng."""
    while True:
        clear_screen()
        print_banner()

        print(f"{Color.BOLD}  MAIN MENU{Color.RESET}")
        print_separator()
        print(f"  {Color.CYAN}[1]{Color.RESET} 🔐  Mã hóa đối xứng    (Symmetric Encryption)")
        print(f"  {Color.CYAN}[2]{Color.RESET} 🔑  Mã hóa bất đối xứng (Asymmetric Encryption)")
        print(f"  {Color.CYAN}[3]{Color.RESET} #   Hàm băm              (Hash Function)")
        print_separator()
        print(f"  {Color.RED}[0]{Color.RESET}     Thoát")
        print_separator()

        choice = input(f"\n  {Color.YELLOW}➜ Chọn chức năng: {Color.RESET}").strip()

        if choice == "1":
            from features.symmetric import symmetric_menu
            symmetric_menu()
        elif choice == "2":
            from features.asymmetric import asymmetric_menu
            asymmetric_menu()
        elif choice == "3":
            from features.hash_function import hash_menu
            hash_menu()
        elif choice == "0":
            print(f"\n  {Color.GREEN}Cảm ơn đã sử dụng Crypto Toolkit. Tạm biệt!{Color.RESET}\n")
            sys.exit(0)
        else:
            input(f"\n  {Color.RED}⚠ Lựa chọn không hợp lệ. Nhấn Enter để thử lại...{Color.RESET}")


if __name__ == "__main__":
    main_menu()
