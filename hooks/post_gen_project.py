import os
import shutil

if "{{ cookiecutter.remove_test_script }}" == "yes":
    shutil.rmtree("tests")

if "{{ cookiecutter.remove_dockerfile }}" == "yes":
    os.remove("Dockerfile")
