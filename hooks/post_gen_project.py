import os

FILES_TO_REMOVE = ["setup.cfg", "pyproject.toml", "setup.py"]

if "{{ cookiecutter.as_package }}" == "no":
    for file in FILES_TO_REMOVE:
        os.remove(file)

if "{{ cookiecutter.remove_test_script }}" == "yes":
    os.remove("test_log.py")

if "{{ cookiecutter.remove_dockerfile }}" == "yes":
    os.remove("Dockerfile")
