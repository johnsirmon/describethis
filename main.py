import os
import sys
import pkg_resources

#git add . && git commit -m "updating" && git pull origin main && git push origin main
#FAIL git add . && git commit -m "Updated on $(date "+%Y-%m-%d"): $(git diff --name-only)" && git push origin main
#works git add .; git commit -m ("Updated on " + (Get-Date -Format "yyyy-MM-dd") + ": " + $(git diff --name-only)); git push origin main



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

    # Check if virtualenv is being used
    if 'VIRTUAL_ENV' in os.environ:
        virtual_env_manager = 'virtualenv'

    # Check if conda is being used
    elif 'CONDA_DEFAULT_ENV' in os.environ:
        virtual_env_manager = 'conda'

    # Check if pipenv is being used
    elif 'PIPENV_ACTIVE' in os.environ:
        virtual_env_manager = 'pipenv'

    # Check if poetry is being used
    elif 'POETRY_ACTIVE' in os.environ:
        virtual_env_manager = 'poetry'

    # Check if pyenv is being used
    elif 'PYENV_VERSION' in os.environ:
        virtual_env_manager = 'pyenv'

    # Check if pipx is being used
    elif 'PIPX_ACTIVE' in os.environ:
        virtual_env_manager = 'pipx'

    # Check if venv is being used
    elif 'VENV' in os.environ:
        virtual_env_manager = 'venv'

    return virtual_env_manager

def get_non_standard_libraries():
    """Returns a list of non-standard libraries used in the project, excluding pip and setuptools."""
    standard_libs = sys.stdlib_module_names
    common_libs = {'pip', 'setuptools'}  # Common tools to exclude
    installed_libs = {dist.key for dist in pkg_resources.working_set}
    non_standard_libs = (installed_libs - set(standard_libs)) - common_libs
    return non_standard_libs


def format_directory_structure(root_dir, max_depth=1):
    """Formats the directory structure for the root."""
    structure = []
    for root, dirs, files in os.walk(root_dir):
        depth = root.count(os.sep) - root_dir.count(os.sep)
        if depth > max_depth:
            continue
        relative_path = os.path.relpath(root, root_dir)
        if relative_path != '.':
            structure.append(relative_path)
    return ', '.join(structure)

# Main execution
virtual_env_manager = determine_virtual_env_manager()
print(f"The developer is using {virtual_env_manager} to manage the virtual environment.")

root_directory = '.'  # Root of your project
python_file_count = count_user_python_files(root_directory)
python_version = sys.version.split()[0]
non_standard_libs = get_non_standard_libraries()
dir_structure = format_directory_structure(root_directory)

description = f"The developer has created {python_file_count} Python files using Python {python_version}."
if virtual_env_manager is not None:
    description += f" They are using {virtual_env_manager} to manage their virtual environment."
if non_standard_libs:
    description += f" Non-standard libraries used: {', '.join(non_standard_libs)}."
description += f" Directory structure includes: {dir_structure}"

print(description)