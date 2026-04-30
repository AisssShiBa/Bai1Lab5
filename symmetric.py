from Crypto.Cipher import DES, DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii

class SymmetricCipher:
   
    @staticmethod
    def process_des():
        print("\n" + "="*20 + " THIẾT LẬP DES " + "="*20)
        # Khóa ngẫu nhiên duy nhất cho toàn bộ phiên làm việc này
        key = get_random_bytes(8)
        print(f"[*] Khóa DES ngẫu nhiên (Hex): {binascii.hexlify(key).decode().upper()}")
        print("[*] Lưu ý: Khóa này dùng cho mọi Plaintext bên dưới.")
        
        while True:
            plaintext = input("\nNhập Plaintext DES (gõ 'back' để quay lại): ")
            if plaintext.lower() == 'back': 
                break
            if not plaintext: 
                continue
            
            try:
                # Thực hiện mã hóa
                cipher = DES.new(key, DES.MODE_ECB)
                padded_data = pad(plaintext.encode('utf-8'), DES.block_size)
                ciphertext = cipher.encrypt(padded_data)
                
                # Hiển thị kết quả
                res_hex = binascii.hexlify(ciphertext).decode()
                print(f" >> Kết quả (Ciphertext Hex): {res_hex}")
            except Exception as e:
                print(f"[!] Lỗi trong quá trình mã hóa: {e}")

    @staticmethod
    def process_3des():
        print("\n" + "="*20 + " THIẾT LẬP 3DES " + "="*20)
        # Khóa ngẫu nhiên duy nhất (24 bytes) cho toàn bộ phiên
        key = get_random_bytes(24)
        # Điều chỉnh bit parity để khóa hợp lệ (tránh lỗi suy biến)
        key = DES3.adjust_key_parity(key)
        
        print(f"[*] Khóa 3DES ngẫu nhiên (Hex): {binascii.hexlify(key).decode().upper()}")
        print("[*] Lưu ý: Khóa này dùng cho mọi Plaintext bên dưới.")
        
        while True:
            plaintext = input("\nNhập Plaintext 3DES (gõ 'back' để quay lại): ")
            if plaintext.lower() == 'back': 
                break
            if not plaintext: 
                continue
            
            try:
                # Thực hiện mã hóa
                cipher = DES3.new(key, DES3.MODE_ECB)
                padded_data = pad(plaintext.encode('utf-8'), DES3.block_size)
                ciphertext = cipher.encrypt(padded_data)
                
                # Hiển thị kết quả
                res_hex = binascii.hexlify(ciphertext).decode()
                print(f" >> Kết quả (Ciphertext Hex): {res_hex}")
            except Exception as e:
                print(f"[!] Lỗi trong quá trình mã hóa: {e}")