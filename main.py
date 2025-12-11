from tkinter import Tk, filedialog
import os
import json
import subprocess
import platform
import time

PRESETS_FILE = "presets.json"

def clear():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_tk_window():
    """Create a Tk window that appears on top."""
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    root.update()
    return root

def format_file_size(size_bytes):
    """Convert bytes to human-readable format (B, KB, MB, GB, TB)."""
    if size_bytes < 1024:
        return f"{int(size_bytes)} B"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024 ** 3:
        return f"{size_bytes / (1024 ** 2):.2f} MB"
    elif size_bytes < 1024 ** 4:
        return f"{size_bytes / (1024 ** 3):.2f} GB"
    else:
        return f"{size_bytes / (1024 ** 4):.2f} TB"

def open_folder(filepath):
    """Open folder containing the file and select it."""
    system = platform.system()
    
    if system == "Windows":
        abs_path = os.path.abspath(filepath)
        subprocess.Popen(f'explorer /select,"{abs_path}"')
    elif system == "Darwin":
        folder = os.path.dirname(os.path.abspath(filepath))
        subprocess.run(["open", folder])
    else:
        folder = os.path.dirname(os.path.abspath(filepath))
        subprocess.run(["xdg-open", folder])

def load_presets():
    """Load presets from JSON file."""
    if os.path.exists(PRESETS_FILE):
        with open(PRESETS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_presets(presets):
    """Save presets to JSON file."""
    with open(PRESETS_FILE, 'w') as f:
        json.dump(presets, f, indent=2)

def print_banner():
    """Display the application banner."""
    banner = """
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║          COMBO EDITOR V1.0            ║
    ║                                       ║
    ║                                       ║
    ╚═══════════════════════════════════════╝
    """
    print(banner)

def print_menu():
    """Display the main menu."""
    menu = """
    ┌───────────────────────────────────────┐
    │  [1] Extract Lines                    │
    │  [2] Merge Files                      │
    │  [3] Deduplicate Lines                │
    │  [4] Exit                             │
    └───────────────────────────────────────┘
    """
    print(menu)

def read_file(filepath):
    """Read file with automatic encoding detection."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.readlines()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            return f.readlines()

def deduplicate_lines():
    """Remove exact duplicate email:password combinations from a file."""
    clear()
    print_banner()
    
    print("\n→ Deduplicate Lines (email:password exact combo)")
    print("   Remove duplicate email:password lines (same email AND same password)\n")
    
    root = create_tk_window()
    print("→ Opening file picker...")
    input_file = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        parent=root
    )
    root.destroy()
    
    if not input_file:
        print("✗ No file selected\n")
        input("Press Enter to continue...")
        return
    
    clear()
    print_banner()
    print(f"\n→ Loading file: {os.path.basename(input_file)}")
    
    # Read file
    start_time = time.time()
    try:
        print("→ Reading file contents...")
        lines = read_file(input_file)
        print(f"✓ File loaded in {time.time() - start_time:.2f}s")
    except Exception as e:
        print(f"\n✗ Error: {e}\n")
        input("Press Enter to continue...")
        return
    
    print(f"\n┌─ FILE INFO")
    print(f"│ Name: {os.path.basename(input_file)}")
    print(f"│ Original lines: {len(lines):,}")
    print(f"│ Size: {format_file_size(os.path.getsize(input_file))}")
    print(f"└─")
    
    print("\n→ Removing exact duplicate email:password combos...")
    start_dedup = time.time()
    
    seen_combos = set()
    unique_lines = []
    duplicates_found = 0
    combos_total = 0
    non_combo_lines = 0
    
    for line in lines:
        raw = line.rstrip("\n")
        
        if ":" in raw:
            parts = raw.split(":", 1)
            if len(parts) == 2:
                email_part, password_part = parts
                email_clean = email_part.strip()
                password_clean = password_part.strip()
                
                if "@" in email_clean and "." in email_clean:
                    combos_total += 1
                    combo_key = (email_clean.lower(), password_clean)
                    
                    if combo_key not in seen_combos:
                        seen_combos.add(combo_key)
                        unique_lines.append(line)
                    else:
                        duplicates_found += 1
                    continue
        
        non_combo_lines += 1
        unique_lines.append(line)
    
    print(f"✓ Deduplication complete in {time.time() - start_dedup:.2f}s")
    
    if duplicates_found == 0:
        print("\n✓ No exact duplicate email:password combos found!\n")
        input("Press Enter to continue...")
        return
    
    output_name = input("\nOutput filename: ").strip()
    if not output_name.endswith('.txt'):
        output_name += '.txt'
    
    output_file = os.path.join(os.path.dirname(input_file), output_name)
    
    print(f"\n→ Writing deduplicated file: {output_name}...")
    start_write = time.time()
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(unique_lines)
    print(f"✓ File written in {time.time() - start_write:.2f}s")
    
    clear()
    print_banner()
    
    print("\n┌─ DEDUPLICATE COMPLETE (email:password exact combo)")
    print(f"│ Original lines: {len(lines):,}")
    print(f"│ Email:password combos detected: {combos_total:,}")
    print(f"│ Unique email:password combos: {len(seen_combos):,}")
    print(f"│ Non-combo lines passed through: {non_combo_lines:,}")
    print(f"│ Duplicates removed (same email & password): {duplicates_found:,}")
    print(f"│ Output: {output_name}")
    print(f"│ Size: {format_file_size(os.path.getsize(output_file))}")
    print(f"└─\n")
    
    open_folder(output_file)
    input("Press Enter to continue...")

def merge_files():
    """Merge multiple text files into one."""
    clear()
    print_banner()
    
    print("\n→ File Merger")
    print("   Select multiple .txt files to merge\n")
    
    root = create_tk_window()
    print("→ Opening file picker...")
    files = filedialog.askopenfilenames(
        title="Select text files to merge",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        parent=root
    )
    root.destroy()
    
    if not files or len(files) < 2:
        print("✗ Need at least 2 files to merge\n")
        input("Press Enter to continue...")
        return
    
    clear()
    print_banner()
    
    print(f"\n→ Selected {len(files)} files:")
    total_lines = 0
    
    for i, filepath in enumerate(files, 1):
        lines = read_file(filepath)
        print(f"   [{i}] {os.path.basename(filepath)} - {len(lines):,} lines")
        total_lines += len(lines)
    
    print(f"\n   Total: {total_lines:,} lines")
    
    output_name = input("\nOutput filename: ").strip()
    if not output_name.endswith('.txt'):
        output_name += '.txt'
    
    output_file = os.path.join(os.path.dirname(files[0]), output_name)
    
    print("\n→ Starting merge process...")
    start_time = time.time()
    merged_lines = []
    
    for i, filepath in enumerate(files, 1):
        print(f"→ Reading file {i}/{len(files)}: {os.path.basename(filepath)}...")
        merged_lines.extend(read_file(filepath))
    
    print(f"→ Writing merged file: {output_name}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(merged_lines)
    
    print(f"✓ Merge complete in {time.time() - start_time:.2f}s")
    
    clear()
    print_banner()
    
    print("\n┌─ MERGE COMPLETE")
    print(f"│ Files merged: {len(files)}")
    print(f"│ Total lines: {len(merged_lines):,}")
    print(f"│ Output: {output_name}")
    print(f"│ Size: {format_file_size(os.path.getsize(output_file))}")
    print(f"└─\n")
    
    open_folder(output_file)
    input("Press Enter to continue...")

def extract_lines():
    """Extract a specified number of lines from a file."""
    presets = load_presets()
    
    clear()
    print_banner()
    
    print("\n→ Initializing file picker...")
    root = create_tk_window()
    
    print("→ Waiting for file selection...")
    input_file = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        parent=root
    )
    root.destroy()
    
    if not input_file:
        print("✗ No file selected\n")
        input("Press Enter to continue...")
        return
    
    clear()
    print_banner()
    print(f"\n→ Loading file: {os.path.basename(input_file)}")
    
    start_time = time.time()
    try:
        print("→ Reading file contents...")
        lines = read_file(input_file)
        print(f"✓ File loaded in {time.time() - start_time:.2f}s")
    except Exception as e:
        print(f"\n✗ Error: {e}\n")
        input("Press Enter to continue...")
        return
    
    print(f"\n┌─ FILE INFO")
    print(f"│ Name: {os.path.basename(input_file)}")
    print(f"│ Lines: {len(lines):,}")
    print(f"│ Size: {format_file_size(os.path.getsize(input_file))}")
    print(f"└─")
    
    num_lines = None
    if presets:
        print("\n┌─ PRESETS")
        preset_list = list(presets.items())
        for i, (name, preset_lines) in enumerate(preset_list, 1):
            print(f"│ [{i}] {name}: {preset_lines:,} lines")
        print(f"│ [0] Custom amount")
        print(f"└─")
        
        preset_choice = input("\nSelect preset or custom: ").strip()
        
        if preset_choice.isdigit():
            preset_idx = int(preset_choice)
            if 1 <= preset_idx <= len(preset_list):
                num_lines = preset_list[preset_idx - 1][1]
                if num_lines > len(lines):
                    print(f"✗ Preset exceeds file size (max {len(lines):,})")
                    num_lines = None
            elif preset_idx != 0:
                print("✗ Invalid preset")
    
    
    if num_lines is None:
        while True:
            try:
                num_lines = int(input("\nLines to extract: "))
                if num_lines <= 0:
                    print("✗ Must be positive")
                    continue
                if num_lines > len(lines):
                    print(f"✗ Maximum is {len(lines):,} lines")
                    continue
                break
            except ValueError:
                print("✗ Enter a valid number")
    
    output_name = input("Output filename: ").strip()
    if not output_name.endswith('.txt'):
        output_name += '.txt'
    
    output_file = os.path.join(os.path.dirname(input_file), output_name)
    
    print("\n→ Starting extraction process...")
    
    extracted = lines[:num_lines]
    remaining = lines[num_lines:]
    
    print(f"→ Writing extracted lines to {output_name}...")
    start_write = time.time()
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(extracted)
    print(f"✓ Extracted file written in {time.time() - start_write:.2f}s")
    
    print(f"→ Updating original file with {len(remaining):,} remaining lines...")
    start_update = time.time()
    with open(input_file, 'w', encoding='utf-8') as f:
        f.writelines(remaining)
    print(f"✓ Original file updated in {time.time() - start_update:.2f}s")
    
    clear()
    print_banner()
    
    # Success
    print("\n┌─ COMPLETE")
    print(f"│ Extracted: {num_lines:,} lines → {output_name}")
    print(f"│ Remaining: {len(remaining):,} lines")
    print(f"└─\n")
    
    open_folder(output_file)
    input("Press Enter to continue...")

def main():
    """Main application loop."""
    while True:
        clear()
        print_banner()
        print_menu()
        
        choice = input("    Select option: ").strip()
        
        if choice == '1':
            extract_lines()
        elif choice == '2':
            merge_files()
        elif choice == '3':
            deduplicate_lines()
        elif choice == '4':
            clear()
            print_banner()
            print("\n    Goodbye!\n")
            break
        else:
            print("\n    ✗ Invalid option")
            input("    Press Enter to continue...")

if __name__ == "__main__":
    main()