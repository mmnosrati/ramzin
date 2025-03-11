# Ramzin Steganography Tool v.1
![Steganography](https://img.shields.io/badge/Steganography-Tool-blue)  
![Python](https://img.shields.io/badge/Python-3.8%2B-green)  
![License](https://img.shields.io/badge/License-MIT-orange)  

**Ramzin Steganography Tool v.1** is a Python-based tool designed to hide and extract secret messages within images using the Least Significant Bit (LSB) steganography technique. This tool allows users to embed text messages into images and extract them later, ensuring that the hidden data remains undetectable to the naked eye.

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [How It Works](#how-it-works)
5. [Examples](#examples)

---

## Features
- **Embed Messages**: Hide secret text messages inside images.
- **Extract Messages**: Retrieve hidden messages from encoded images.
- **Simple CLI**: Easy-to-use command-line interface.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Lightweight**: Minimal dependencies and fast execution.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- `Pillow` library (for image processing)
- `numpy` library (for array manipulation)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/mmnosrati/Ramzin-Steganography-Tool.git
   cd Ramzin-Steganography-Tool
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

---

## Usage

### Command-Line Interface
The tool provides a simple command-line interface with the following options:

| Argument | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| `mode`   | Choose between `embed` (to hide a message) or `extract` (to reveal a message). |
| `--img`  | Path to the input image. Required for both `embed` and `extract` modes.     |
| `--out`  | Path to save the output image. Required for `embed` mode.                   |
| `--msg`  | The secret message to hide. Required for `embed` mode.                      |

### Examples

1. **Embedding a Message**:
   ```bash
   python main.py embed --img input_image.png --out output_image.png --msg "This is a secret message!"
   ```
   This command will hide the message `"This is a secret message!"` in `input_image.png` and save the result as `output_image.png`.

2. **Extracting a Message**:
   ```bash
   python main.py extract --img output_image.png
   ```
   This command will extract the hidden message from `output_image.png` and display it in the terminal.

---

## How It Works

### Embedding Process
1. The tool converts the secret message into a binary string.
2. It modifies the least significant bit (LSB) of each pixel's RGB values in the image to store the binary message.
3. An end marker (`11111111`) is added to indicate the end of the message.
4. The modified image is saved as the output file.

### Extraction Process
1. The tool reads the LSB of each pixel's RGB values in the encoded image.
2. It reconstructs the binary message until the end marker (`11111111`) is detected.
3. The binary message is converted back into text and displayed.

---

## Examples

### Example 1: Embedding a Message
```bash
python main.py embed --img cat.png --out secret_cat.png --msg "Meet me at midnight!"
```
- Input Image: `cat.png`
- Output Image: `secret_cat.png`
- Message: `"Meet me at midnight!"`

### Example 2: Extracting a Message
```bash
python main.py extract --img secret_cat.png
```
- Output: `Extracted secret: Meet me at midnight!`
