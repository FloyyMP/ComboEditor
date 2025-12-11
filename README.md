# Combo Editor

A simple command-line tool for managing text files containing email:password combinations.

## Features

- **Extract Lines**: Remove a specified number of lines from the start of a file
- **Merge Files**: Combine multiple text files into one
- **Deduplicate**: Remove exact duplicate email:password combinations
- Preset support for common extraction amounts
- Cross-platform (Windows, macOS, Linux)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/combo-editor.git
cd combo-editor
```

2. Run the tool:
```bash
python main.py
```

## Requirements

- Python 3.6+
- tkinter (usually included with Python)

## Usage

Run `python main.py` and select from the menu:

1. **Extract Lines** - Extract N lines from the beginning of a file and save them separately
2. **Merge Files** - Combine multiple .txt files into one
3. **Deduplicate Lines** - Remove duplicate email:password combinations

## Presets

Edit `presets.json` to customize your extraction presets:
```json
{
  "100k": 100000,
  "250k": 250000,
  "500k": 500000,
}
```

## License

MIT License - see LICENSE file for details
```

## 2. Create a **.gitignore**:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Application specific
*.txt
!requirements.txt
presets.json
```

## 3. Create a **LICENSE** file

If you want MIT License (common for open source):
```
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
