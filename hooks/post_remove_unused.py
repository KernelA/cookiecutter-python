import os

FILES_TO_REMOVE = ["pyproject.toml", "setup.cfg", "pyproject.toml", "setup.py"]

if "{{ cookiecutter.as_package }}" == "no":
    for file in FILES_TO_REMOVE:
        os.remove(file)

if "{{ remove_test_script }}" == "yes":
    os.remove("test_log.py")
