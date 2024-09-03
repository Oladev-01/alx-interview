# 0x04-UTF8 Validation

## Description

This project focuses on implementing a Python function to validate if a given list of integers represents a valid UTF-8 encoding. The UTF-8 encoding is a variable-width character encoding used for electronic communication, where each character can be encoded with 1 to 4 bytes.

## Learning Objectives

- Understanding UTF-8 encoding and its characteristics.
- How to validate UTF-8 encoding in a data stream.
- Working with bitwise operations in Python.

## Requirements

- Python 3.x
- Your code should follow the `pycodestyle` (version 2.8.*).
- You are not allowed to import any external libraries.

## Project Files

### 1. `0-validate_utf8.py`

This is the main Python file containing the `validUTF8` function. The function checks whether the given data set is a valid UTF-8 encoding.

#### Function Prototype

```python
def validUTF8(data: List[int]) -> bool:
```

#### Parameters
- `data`: A list of integers, where each integer represents one byte of data (only the 8 least significant bits are used).

#### Return
- `True`: If the data set represents a valid UTF-8 encoding.
- `False`: Otherwise.

### 2. Example Usage

You can test the function using the following code:

```python
data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False

data = [197, 130, 1]
print(validUTF8(data))  # Output: True
```

## Bitwise Operation Explanation

- **Masking:** The function uses bitwise masks to identify the type of UTF-8 character by checking the leading bits of each byte.
- **Continuation Bytes:** The function checks that the appropriate number of continuation bytes (`10xxxxxx`) follows the leading byte of a multi-byte character.

## Usage

To validate a list of integers for UTF-8 encoding, call the `validUTF8(data)` function with the data list as an argument.

```python
data = [197, 130, 1]
print(validUTF8(data))  # Expected: True
```

## Author

- [Your Name]

## License

This project is licensed under the MIT License. See the LICENSE file for more details.