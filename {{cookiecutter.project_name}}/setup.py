from setuptools import setup

with open("requirements.txt", encoding="utf-8") as file:
      req_list = list(filter(lambda x: len(x) > 0, map(str.strip, file.readlines())))

setup(name="{{cookiecutter.project_slug}}",
      version="{{cookiecutter.project_major_version}}.{{cookiecutter.project_minor_version}}.{{cookiecutter.project_patch_version}}",
      author="{{cookiecutter.author}}",
      author_email= "{{cookiecutter.email}}",
      license="{{cookiecutter.license}}",
      install_requires=req_list,
      py_modules=["main"],
      python_requires=">={{cookiecutter.python_min_version}}",
      )
