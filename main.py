import os
import sys

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
            return venv_file
    return None


def determine_virtual_env_manager():
    """Determines what the developer is using to manage the Python virtual environment."""
    virtual_env_manager = None
    if 'VIRTUAL_ENV' in os.environ:
        virtual_env_manager = 'virtualenv'
    elif 'CONDA_DEFAULT_ENV' in os.environ:
        virtual_env_manager = 'conda'
    elif 'PIPENV_ACTIVE' in os.environ:
        virtual_env_manager = 'pipenv'
    elif 'POETRY_ACTIVE' in os.environ:
        virtual_env_manager = 'poetry'
    elif 'PYENV_VERSION' in os.environ:
        virtual_env_manager = 'pyenv'
    elif 'PIPX_ACTIVE' in os.environ:
        virtual_env_manager = 'pipx'
    elif 'VENV' in os.environ:
        virtual_env_manager = 'venv'
    return virtual_env_manager

virtual_env_manager = determine_virtual_env_manager()
print(f"The developer is using {virtual_env_manager} to manage the virtual environment.")





root_directory = '.'  # Root of your project
python_file_count = count_user_python_files(root_directory)
python_version = sys.version.split()[0]
venv_used = is_virtual_env_file(root_directory, '') or 'None'
description = f"I have created {python_file_count} Python file(s) using Python {python_version}. I am using {venv_used} to manage the virtual environment."
print(description)
