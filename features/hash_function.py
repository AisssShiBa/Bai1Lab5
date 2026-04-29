"""
Feature 3: Hàm băm (Hash Function)
Thuật toán: MD5, SHA-256
"""

import hashlib


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
