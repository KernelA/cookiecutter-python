from setuptools import setup

setup(name="{{cookiecutter.project_slug}}",
      version="{{cookiecutter.project_major_version}}.{{cookiecutter.project_minor_version}}.{{cookiecutter.project_patch_version}}",
      author="{{cookiecutter.author}}",
      author_email= "{{cookiecutter.email}}",
      license="{{cookiecutter.license}}",
      python_requires=">={{cookiecutter.python_min_version}}",
      )
