```markdown
# 🔧 Combo Editor

A fast, user-friendly command-line tool for processing large text files containing email:password combinations.

![Version](https://img.shields.io/badge/version-1.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

## ✨ Features

### 📋 Extract Lines
Extract a specific number of lines from the beginning of a file and save them to a new file. The original file is automatically updated with the remaining lines.

- Use custom amounts or quick presets
- Original file is automatically trimmed
- Perfect for splitting large datasets

### 🔗 Merge Files
Combine multiple text files into a single file with ease.

- Select multiple files at once
- Preserves all line content
- Shows real-time progress and stats

### 🧹 Deduplicate Lines
Remove exact duplicate email:password combinations from your files.

- Detects `email:password` format
- Only removes exact duplicates (same email AND same password)
- Preserves non-combo lines
- Case-insensitive email matching

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- tkinter (included with most Python installations)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/combo-editor.git

# Navigate to the directory
cd combo-editor

# Run the tool
python main.py
```

## 📖 Usage

Run the tool and select from the interactive menu:

```
╔═══════════════════════════════════════╗
║                                       ║
║          COMBO EDITOR V1.0            ║
║                                       ║
╚═══════════════════════════════════════╝

┌───────────────────────────────────────┐
│  [1] Extract Lines                    │
│  [2] Merge Files                      │
│  [3] Deduplicate Lines                │
│  [4] Exit                             │
└───────────────────────────────────────┘
```

### 1. Extract Lines

1. Select your text file using the file picker
2. Choose a preset or enter a custom amount
3. Enter an output filename
4. Done! The extracted lines are saved and the original file is updated

**Example:**
```
Original file: 1,000,000 lines
Extract: 100,000 lines
Result: 
  - new_file.txt (100,000 lines)
  - original.txt (900,000 lines remaining)
```

### 2. Merge Files

1. Select 2 or more text files
2. Enter an output filename
3. All files are combined into one

**Example:**
```
file1.txt: 50,000 lines
file2.txt: 75,000 lines
file3.txt: 25,000 lines
Result: merged.txt (150,000 lines)
```

### 3. Deduplicate Lines

1. Select your text file
2. Enter an output filename
3. All exact duplicate email:password combos are removed

**Example:**
```
Input:
  user@example.com:password123
  test@site.com:pass456
  user@example.com:password123  ← duplicate
  user@example.com:different789  ← NOT duplicate (different password)

Output:
  user@example.com:password123
  test@site.com:pass456
  user@example.com:different789
```

## ⚙️ Configuration

### Presets

Edit `presets.json` to customize your extraction presets:

```json
{
  "test": 5000,
  "100k": 100000,
  "500k": 500000,
  "1kk": 1000000
}
```

Add as many presets as you need with any name and line count.

## 🖥️ Platform Support

- ✅ Windows
- ✅ macOS
- ✅ Linux

The tool automatically opens the output folder when processing is complete, using the appropriate file manager for your OS.

## 🎯 Performance

- Handles large files efficiently
- UTF-8 and Latin-1 encoding support
- Real-time progress indicators
- Processing time displayed for all operations

## 📝 File Format

The tool works best with text files containing `email:password` combinations:

```
user1@domain.com:password123
user2@domain.com:mypass456
user3@domain.com:secret789
```

Non-combo lines are preserved as-is during deduplication.

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and legitimate security research purposes only. Always ensure you have proper authorization before processing any data.

## 🛠️ Troubleshooting

**File picker doesn't appear on top?**
- The tool uses `topmost` attribute to bring dialogs to front
- Try Alt+Tab to find the dialog window

**Encoding errors?**
- The tool automatically tries Latin-1 if UTF-8 fails
- Most common text encodings are supported

**Large file processing is slow?**
- Processing time scales with file size
- The tool shows real-time progress indicators
- Consider splitting very large files (10M+ lines)

## 📬 Contact

For questions or support, please open an issue on GitHub.

---

Made with ❤️ for the data processing community
```
