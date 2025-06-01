import time
import os
import random
import sys

def matrix_effect():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    for _ in range(25):
        line = "".join(random.choice(chars) for _ in range(80))
        print(line, flush=True)
        time.sleep(0.05)

def fake_encryption():
    fake_files = ['C:\\Users\\You\\Documents\\resume.docx', 
                  'D:\\Photos\\family.jpg',
                  'C:\\System\\windows32.dll',
                  'C:\\Game\\GTA5\\savegame.dat']
    
    for file in fake_files:
        print(f"[ENCRYPTING] {file}", flush=True)
        time.sleep(1)
    print("\nAll files have been encrypted.", flush=True)
    time.sleep(2)

def countdown():
    print("\nSystem will crash in...", flush=True)
    for i in range(5, 0, -1):
        print(f"{i}...", flush=True)
        time.sleep(1)

def reveal():
    print("\n💥 BOOM! 💥\n", flush=True)
    time.sleep(1)
    print("💀 Just kidding. This is a simulation.", flush=True)
    print("✅ No files were harmed. You're good 😄\n", flush=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    clear()
    print("🔒 Initializing system access...", flush=True)
    time.sleep(2)

    matrix_effect()
    fake_encryption()
    countdown()
    reveal()

    # Keep terminal open so user can see reveal
    print("Press Enter to exit...")
    input()

except Exception as e:
    print(f"An error occurred: {e}", flush=True)
