# Welcome to {{ cookiecutter.project_name }}!

This repository is a template repository (a cookiecutter) that allows you to quickly
set up new projects.

# Prerequisites

In order to use, {{ cookiecutter.project_name }} you need the following software installed:

* [Cookiecutter](https://github.com/cookiecutter/cookiecutter) e.g. by doing `pip install cookiecutter`.

# Using {{ cookiecutter.project_name }}

Simply run the cookiecutter command line interface:

```
cookiecutter gh:{{ cookiecutter.github_name }}/{{ cookiecutter.project_slug }}
```

This will start an interactive prompt that will configure and generate your project.

# Configuration

This cookiecutter accepts the following configuration options:

{% for k, v in cookiecutter.items() if not k.startswith("_") %}
* `{{ k }}`: defaults to `{{ v }}`
{% endfor%}

# Issues

Please report any issues you might have with template using [the Github issue
tracker](https://githab.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_slug}})
