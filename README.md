
# Dump File Creator
This Python script, `main.py`, is a simple utility that allows you to create a binary dump file of a specified size in bytes. This can be useful for various purposes, such as testing disk space allocation or generating large files for testing applications.


## Requirements

Before running the script, make sure you have the following:
- Python 3.x
- Subprocess module (pre-installed with python)




## How to use
Follow these steps to use the script:
- Download the Script: Download the `main.py` script to your local machine.
- Open a terminal or command prompt and navigate to the directory where you saved the script. Then, run the script using the following command:
`python main.py`
- By default, the script creates a dump file of 1 GB in size. You can customize the desired size by changing the desired_size_gb variable in the script. For example, if you want to create a 2 GB dump file, modify the following line:
`desired_size_gb = 2`
- The script will create a binary dump file named dump_file.bin in the same directory as the script. You can change the file_path variable in the script to specify a different file name or path.

- Once the file is created, the script will display a message indicating the file's name and size.

## Script Details

Here's a brief overview of how the script works:

- The `create_dump_file` function is responsible for creating the binary dump file. It takes two parameters: file_path (the path to the output file) and `size_in_bytes` (the desired size of the file in bytes).
- Inside the `create_dump_file function`, the script uses a binary write mode (`'wb'`) to open the file and writes a sequence of null bytes (`b'\0'`) to fill the file to the specified size.
- The `if __name__ == "__main__":` block at the end of the script is the entry point. It sets the desired size in gigabytes, calculates the size in bytes, and then calls the `create_dump_file` function with the specified parameters. Finally, it prints a message indicating the file's creation.
## Disclaimer

Usage at Your Own Risk: This script, main.py, is provided as a utility for creating binary dump files. It is intended for educational and testing purposes. The authors and maintainers of this script are not responsible for any misuse, damage, or loss of data that may occur as a result of its use.

## Acknowledgement

Happy downloading! If you encounter any issues or have suggestions for improvements, feel free to [open an issue](https://github.com/phanitallapudi/Dump-File-Creator/issues) or contribute to the project by creating a pull request.