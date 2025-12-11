# Combo Editor

A simple command-line tool for managing text files with email:password combinations.

## Setup

1. **Download Python**
   - Go to [python.org](https://python.org) and download Python 3.6 or newer
   - During installation, check "Add Python to PATH"

2. **Download This Tool**
   - Click the green "Code" button above
   - Click "Download ZIP"
   - Extract the ZIP file to a folder

3. **Run the Tool**
   - Open the folder where you extracted the files
   - Double-click `main.py`
   - OR open Command Prompt/Terminal in the folder and type:
```
     python main.py
```

## What It Does

- **Extract Lines** - Take the first X lines from a file and save them separately
- **Merge Files** - Combine multiple text files into one
- **Deduplicate** - Remove duplicate email:password combinations

## Usage

Just run `main.py` and follow the on-screen menu. It will open file picker windows to help you select files.

## Presets

You can edit `presets.json` to add quick shortcuts for extracting lines:
```json
{
  "small": 5000,
  "medium": 100000,
  "large": 1000000
}
```

That's it! Select an option from the menu and follow the prompts. Join https://discord.gg/floyy for help.
