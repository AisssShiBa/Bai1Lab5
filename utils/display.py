"""Tiện ích hiển thị dùng chung cho toàn bộ app."""

import os
import platform


class Color:
    """ANSI color codes."""
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BOLD    = "\033[1m"
    RESET   = "\033[0m"


def clear_screen():
    """Xóa màn hình terminal."""
    os.system("cls" if platform.system() == "Windows" else "clear")


def print_banner():
    """In banner chính của app."""
    banner = f"""
{Color.CYAN}{Color.BOLD}
  ╔══════════════════════════════════════════════════╗
  ║            CRYPTOGRAPHY  TOOLKIT                 ║
  ║             Group5: Teafromhand                  ║
  ╚══════════════════════════════════════════════════╝
{Color.RESET}"""
    print(banner)


def print_separator(char="─", length=52):
    """In đường kẻ ngang."""
    print(f"  {Color.BLUE}{char * length}{Color.RESET}")


def print_result_box(label: str, value: str, color: str = Color.GREEN):
    """In kết quả trong khung đẹp."""
    print(f"\n  {Color.BOLD}┌─ {label} {'─' * max(0, 45 - len(label))}┐{Color.RESET}")
    # Wrap dài
    while value:
        chunk = value[:60]
        value = value[60:]
        print(f"  │  {color}{chunk}{Color.RESET}")
    print(f"  {Color.BOLD}└{'─' * 50}┘{Color.RESET}")


def print_success(msg: str):
    print(f"\n  {Color.GREEN}✔ {msg}{Color.RESET}")


def print_error(msg: str):
    print(f"\n  {Color.RED}✘ {msg}{Color.RESET}")


def print_info(msg: str):
    print(f"\n  {Color.CYAN}ℹ {msg}{Color.RESET}")


def ask_try_again() -> bool:
    """
    Hỏi người dùng có muốn thử lại không.
    Trả về True nếu thử lại, False nếu quay về menu.
    """
    print()
    print_separator()
    print(f"  {Color.CYAN}[1]{Color.RESET} Thử lại (Try again)")
    print(f"  {Color.CYAN}[0]{Color.RESET} Quay về menu trước")
    print_separator()
    choice = input(f"  {Color.YELLOW}➜ Chọn: {Color.RESET}").strip()
    return choice == "1"


def copy_to_clipboard(text: str) -> bool:
    """
    Cố gắng copy text vào clipboard.
    Trả về True nếu thành công.
    """
    try:
        import pyperclip
        pyperclip.copy(text)
        return True
    except Exception:
        return False


def offer_copy(result: str):
    """Hỏi người dùng có muốn copy kết quả không."""
    print(f"\n  {Color.YELLOW}[C]{Color.RESET} Sao chép kết quả vào clipboard")
    choice = input(f"  {Color.YELLOW}➜ Nhấn C để copy, hoặc Enter để bỏ qua: {Color.RESET}").strip().upper()
    if choice == "C":
        if copy_to_clipboard(result):
            print_success("Đã sao chép vào clipboard!")
        else:
            print_error("Không thể copy (cần cài pyperclip). Hãy copy thủ công.")
