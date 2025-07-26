# ===================== 07. FILE HANDLING ==============================
print("==== FILE HANDLING ====")
# === Write to a file (creates new or overwrites if file exists) ===
with open("example.txt", "w") as f:
    f.write("Hello File!\nThis is a new line.")
print("[Write] Wrote to 'example.txt'")
print()

# === Read entire content from a file ===
with open("example.txt", "r") as f:
    content = f.read()
print("[Read] File content:\n", content)
print()

# === Append to the file without overwriting existing content ===
with open("example.txt", "a") as f:
    f.write("\nAppending a new line.")
print("[Append] Appended text to 'example.txt'")
print()

# === Read file line by line using readline() ===
with open("example.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()
print("[Readline] First Line:", line1.strip())
print("[Readline] Second Line:", line2.strip())
print("[Readline] Third Line:", line3.strip())
print("[Readline] Fourth Line:", line4.strip())
print()

# === Read all lines as a list using readlines() ===
with open("example.txt", "r") as f:
    lines = f.readlines()
print("[Readlines] All lines as list:", lines)
print()

# === Write multiple lines using writelines() ===
lines_to_write = ["Line A\n", "Line B\n", "Line C\n"]
with open("example2.txt", "w") as f:
    f.writelines(lines_to_write)
print("[Writelines] Multiple lines written to 'example2.txt'")
print()

# === File exists check before reading (good practice) ===
import os

filename = "example3.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f"[Exists] {filename} content:\n", f.read())
else:
    print(f"[Exists] {filename} does not exist.")
print()
# === Using 'with' ensures file is automatically closed after use ===
