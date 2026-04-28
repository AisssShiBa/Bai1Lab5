"""
Feature 1: Mã hóa đối xứng (Symmetric Encryption)
Thuật toán: DES, 3DES, AES
TODO: Implement by teammate
"""

from utils.display import (
    clear_screen, print_banner, print_separator,
    print_info, Color
)


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

        if choice in ("1", "2", "3"):
            # TODO: Implement encryption/decryption sub-flow
            print_info("Chức năng đang được phát triển bởi thành viên nhóm...")
            input(f"\n  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")
        elif choice == "0":
            break
        else:
            print(f"\n  {Color.RED}⚠ Lựa chọn không hợp lệ.{Color.RESET}")
            input(f"  {Color.YELLOW}Nhấn Enter để tiếp tục...{Color.RESET}")
