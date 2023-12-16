import os

def count_user_python_files(root_dir):
    """Counts the number of Python files created by the user."""
    python_file_count = 0
    for r, d, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py') and not is_virtual_env_file(r, file):
                python_file_count += 1
    return python_file_count

def is_virtual_env_file(directory, file):
    """Checks if the file is a virtual environment-related file."""
    virtual_env_files = ['.venv', 'venv', 'conda']
    for venv_file in virtual_env_files:
        if venv_file in directory or venv_file in file:
            return True
    return False

root_directory = '.'  # Root of your project
python_file_count = count_user_python_files(root_directory)
python_version = sys.version.split()[0]
venv_used = 'venv' if 'venv' in root_directory else 'conda' if 'conda' in root_directory else 'None'
description = f"I have created {python_file_count} Python file(s) using Python {python_version}. I am using {venv_used} to manage the virtual environment."
print(description)
