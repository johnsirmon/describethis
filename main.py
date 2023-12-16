import os
import sys

def count_user_python_files(root_dir):
    """Counts the number of Python files created by the user."""
    def is_virtual_env_file(directory, file):
        """Determines if a .py file is related to a virtual environment or if it's a generated file."""
        virtual_env_files = ['.venv', 'env', 'venv', 'virtualenv', 'conda', 'pipenv', 'poetry', 'pyenv', 'pipx']
        generated_files = ['__init__.py', 'settings.py', 'manage.py']

        file_path = os.path.join(directory, file)

        # Check if the file is related to a virtual environment
        for env_file in virtual_env_files:
            if env_file in file_path:
                return True

        # Check if the file is a generated file
        if file in generated_files:
            return True

        return False

    python_file_count = 0
    for r, d, files in os.walk(root_dir):
        if 'Lib' in r:
            continue
        for file in files:
            if file.endswith('.py') and not is_virtual_env_file(r, file):
                python_file_count += 1
    return python_file_count

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
description = f"The developer has created {python_file_count} Python files using Python {python_version}."
#check if the user is using a virtual environment
if determine_virtual_env_manager() is not None:
    description += f" They are using {virtual_env_manager} to manage their virtual environment."
    
print(description)
