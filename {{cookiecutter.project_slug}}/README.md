# Welcome to {{ cookiecutter.project_name }}!

This repository is a template repository (a cookiecutter) that allows you to quickly
set up new projects.

# Features

* Very simple, configurable setup of a fully functional project
* Based on an established tool: [Cookiecutter](https://github.com/cookiecutter/cookiecutter) has >13k stars on Github!

# Prerequisites

In order to use {{ cookiecutter.project_name }} you need the following software installed:

* Python `>= 3.6`
* [Cookiecutter](https://github.com/cookiecutter/cookiecutter) e.g. by doing `pip install cookiecutter`.
{%- if cookiecutter.git_setup == "Yes" %}
* Git `>= 1.8.2`
{%- endif %}

# Using {{ cookiecutter.project_name }}

Simply run the cookiecutter command line interface:

```
cookiecutter gh:{{ cookiecutter.github_name }}/{{ cookiecutter.project_slug }}
```

This will start an interactive prompt that will configure and generate your project.
{%- if cookiecutter.git_setup == "Yes" %}
One of the prompts will ask you for a remote repository URL, so you should head to
the Git hosting service of your choice and add a new empty repository e.g. [on Github](https://github.com/new).
{%- endif %}

# Configuration

This cookiecutter accepts the following configuration options:

* `project_name`: The human-readable name of the project, defaults to `My C++ Project`
{%- if cookiecutter.git_setup == "Yes" %}
* `remote_url`: The remote URL for the newly created repository. This is not only used
  to add it as a remote to the Git repository, but also to enable integration with some
  services. Defaults to `None` although we strongly advise you to specify it.
{%- endif %}
* `project_slug`: This will be the name of the generated directory.
{%- if cookiecutter.git_setup == "Yes" -%}
By default, it is deduced from the specified remote URL and the given project name.
{%- endif %}
* `full_name`: Author name, defaults to `Your Name`
* `license` adds a license file to the repository. It can be chosen from [MIT](https://opensource.org/licenses/MIT) (default), [BSD-2](https://opensource.org/licenses/BSD-2-Clause), [GPL-3.0](https://opensource.org/licenses/GPL-3.0), [LGPL-3.0](https://opensource.org/licenses/LGPL-3.0) or it can be omitted.

If you are using `{{ cookiecutter.project_slug }}` a lot, you can customize your default values
by providing a `.cookiecutterrc` file in your home directory, for more details see the
[cookiecutter documentation](https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html).

# Issues

Please report any issues you might have with template using [the Github issue
tracker](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_slug}})
