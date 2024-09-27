
# 0x07 - Rotate 2D Matrix

## Description

This project implements a function to rotate a 2D matrix (square matrix) 90 degrees clockwise. The matrix is represented as a list of lists in Python. The rotation is done in place, meaning that no additional matrix is used, and the original matrix is modified directly.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/0x07-rotate_2d_matrix.git
   ```

2. Navigate to the project directory:
   ```bash
   cd 0x07-rotate_2d_matrix
   ```

3. You can run the code directly in a Python environment or integrate it into your existing projects.

## Usage

To use the rotation function, import it into your Python script and call it with a square matrix as an argument.

```python
from rotate_2d_matrix import rotate_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix)

print(matrix)
# Output: 
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
```

## Example

### Input

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

### Output

After calling the rotation function, the matrix will be modified to:

```python
[
    [4, 1],
    [5, 2],
    [6, 3]
]
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
