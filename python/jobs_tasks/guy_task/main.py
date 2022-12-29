""""
Write a program in Python that calculates SHA256 for every 'exe' file in given directory and stores to file - named
after the exe.
* and skips existing sha files
*verifying existing sha also
"""
import hashlib
import os


def compute_sha256(file_name):
    hash_sha256 = hashlib.sha256()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


def file_type_is_exe(file_name):
    if str(file_name).endswith('.exe'):
        return True
    else:
        return False


def exe_file_have_a_has_file(file_name, has_dir_path):
    for file in os.listdir(has_dir_path):
        if file[:-4] == file_name[:-4]:
            return True
    return False


def create_has_dir(dir_path):
    if 'has-dir' not in os.listdir(dir_path):
        os.mkdir('has-dir')


def convert_dir_files_to_has256file(dir_path, has_dir=None):
    if has_dir is None:
        create_has_dir(dir_path)
        has_dir = 'has-dir'
    os.chdir(dir_path)
    for file in os.listdir():
        if file_type_is_exe(file) and not exe_file_have_a_has_file(file, has_dir):
            f = open(has_dir + '\\' + file[0:-3] + 'has', 'x')
            f.write(compute_sha256(file))
