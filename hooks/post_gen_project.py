import os

if "{{ cookiecutter.license }}" == "None":
    os.remove("LICENSE.md")
