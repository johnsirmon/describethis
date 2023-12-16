import os
import sys
import pkg_resources

def count_python_files(root_dir):
    """Counts the number of Python files in the directory."""
    python_file_count = sum([len([f for f in files if f.endswith('.py')]) for r, d, files in os.walk(root_dir)])
    return python_file_count

def check_venv(root_dir):
    """Checks for a virtual environment in the directory."""
    for item in os.listdir(root_dir):
        full_path = os.path.join(root_dir, item)
        if os.path.isdir(full_path) and ('Scripts' in os.listdir(full_path) or 'bin' in os.listdir(full_path)):
            return True, item
    return False, None

def get_non_standard_libraries():
    """Returns a list of non-standard libraries used in the project."""
    standard_libs = sys.stdlib_module_names
    installed_libs = {dist.key for dist in pkg_resources.working_set}
    non_standard_libs = installed_libs - set(standard_libs)
    return non_standard_libs

def format_directory_structure(root_dir):
    """Formats the directory structure for the root."""
    files = []
    dirs = []
    for item in os.listdir(root_dir):
        if os.path.isfile(os.path.join(root_dir, item)):
            files.append(item)
        elif os.path.isdir(os.path.join(root_dir, item)):
            dirs.append(item)
    formatted_files = ', '.join(files)
    formatted_dirs = ', '.join(dirs)
    return formatted_files, formatted_dirs

def format_output(python_file_count, venv, non_standard_libs, python_version, files, dirs):
    """Formats the output for readability."""
    venv_str = 'uses venv to create a virtual environment' if venv else 'does not use virtual environment'
    lib_str = 'does not have any non-standard libraries that have been installed' if not non_standard_libs else f'uses non-standard libraries: {", ".join(non_standard_libs)}'
    files_str = f'The root folder contains the files: {files}'
    dirs_str = f'and the directories are: {dirs}' if dirs else ''
    return f"I have a project I'm working on in VSCode, that uses Python {python_version} and has {python_file_count} Python file(s). {venv_str}. {lib_str}. {files_str} {dirs_str}"

root_directory = '.'  # Root of your project
python_file_count = count_python_files(root_directory)
venv_used, venv_name = check_venv(root_directory)
non_standard_libs = get_non_standard_libraries()
python_version = sys.version.split()[0]
files, dirs = format_directory_structure(root_directory)
description = format_output(python_file_count, venv_used, non_standard_libs, python_version, files, dirs)
print(description)
