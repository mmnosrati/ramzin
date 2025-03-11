"""
Ramzin Steganography Tool v.1
Author: MohamadMahdi Nosrati (mmnosrati)
GitHub: https://github.com/mmnosrati
Description: A tool to hide and extract secret messages in images using steganography
Last Updated: March 10, 2025
"""

from PIL import Image
import numpy as np
import argparse


def txt2bin(text):
    """Convert a text string to its binary representation.

    Args:
        text (str): The input text string to be converted.

    Returns:
        str: A string of binary digits where each character is represented by 8 bits.

    Example:
        >>> txt2bin("Hi")
        '0100100001101001'
    """
    return ''.join(format(ord(char), '08b') for char in text)


def bin2txt(binary):
    """Convert a binary string back to its text representation.

    Args:
        binary (str): A string of binary digits (0s and 1s).

    Returns:
        str: The decoded text string from the binary input.

    Example:
        >>> bin2txt('0100100001101001')
        'Hi'
    """
    chars = [binary[i:i + 8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if char)


def embed_message(image_path, message, output_path):
    """
    Embed a secret message into an image using LSB steganography.

    Args:
        image_path (str): Path to the input image
        message (str): Message to hide in the image
        output_path (str): Path to save the encoded image

    Raises:
        ValueError: If message is too long for the image
    """
    img = Image.open(image_path)
    img_array = np.array(img)
    # Convert message to binary
    message_binary = txt2bin(message) + '11111111'  # End marker
    if len(message_binary) > img_array.size:
        raise ValueError("Message too long! Use a larger image.")

    encoded_img = img_array.copy()
    message_index = 0
    for i in range(encoded_img.shape[0]):
        for j in range(encoded_img.shape[1]):
            for k in range(encoded_img.shape[2]):
                if message_index < len(message_binary):
                    encoded_img[i, j, k] = (encoded_img[i, j, k] & 0xFE) | int(message_binary[message_index])
                    message_index += 1
                else:
                    break
            if message_index >= len(message_binary):
                break
        if message_index >= len(message_binary):
            break

    Image.fromarray(encoded_img).save(output_path)
    print(f"Message successfully embedded in: {output_path}")


def extract_message(image_path):
    """
    Extract a hidden message from an image.

    Args:
        image_path (str): Path to the encoded image

    Returns:
        str: Extracted message from the image
    """
    img = Image.open(image_path)
    img_array = np.array(img)
    binary_message = ''
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(img_array.shape[2]):
                binary_message += str(img_array[i, j, k] & 1)
                if binary_message[-8:] == '11111111':
                    return bin2txt(binary_message[:-8])
    return bin2txt(binary_message)