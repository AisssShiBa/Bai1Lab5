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

        if choice in ("1", "2", "3"):
            # TODO: Implement RSA flow
            print_info("Chức năng đang được phát triển bởi thành viên nhóm...")
            input(f"\n  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")
        elif choice == "0":
            break
        else:
            print(f"\n  {Color.RED}⚠ Lựa chọn không hợp lệ.{Color.RESET}")
            input(f"  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")
