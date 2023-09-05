def create_dump_file(file_path, size_in_bytes = 1024 * 1024 * 1024):
    with open(file_path, 'wb') as f:
        f.write(b'\0' * size_in_bytes)

if __name__ == "__main__":
    desired_size_gb = 1
    file_path = f"dump_file.bin"
    create_dump_file(file_path)
    print(f"Dump file '{file_path}' created with size {desired_size_gb} GB.")
