[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/dokempf/meta-cookiecutter/CI)](https://github.com/dokempf/meta-cookiecutter/actions?query=workflow%3ACI)

# Meta-cookiecutter - a cookiecutter for cookiecutters!

This is a template repository for the [cookiecutter](https://github.com/cookiecutter/cookiecutter) project
that allows you to quickly set up your own cookiecutters!

This is similar to [cookiecutter-template](https://github.com/eviweb/cookiecutter-template), but
covers some additional aspects that are important for my work:

* Up to date with later versions of cookiecutter
* Automatically adds license selection to the generated cookiecutter
* Slightly different set of configuration values tuned to my needs
# Prerequisites

Meta-cookiecutter only requires [cookiecutter](https://github.com/cookiecutter/cookiecutter) itself, which can be installed with:

```
pip install cookiecutter
```

The versioning of meta-cookiecutter tries to express the compatibility with versions of cookiecutter:
Major and minor version of meta-cookiecutter and cookiecutter should match, where as they may choose
individual versioning for patch releases.

# Create your own cookiecutter

You can simply try meta-cookiecutter by doing:

```
cookiecutter gh:dokempf/meta-cookiecutter
```

Answering all questions on the prompt will create a cookiecutter
that is ready to be customized for your use case.

# Configuration values

Running cookiecutter will query you for the following keys. You may
consider adding some of these to your `.cookiecutterrc` file to provide
personalized default values.

* `project_name` is the human readable name of the Cookiecutter you are writing
* `project_slug` is the slug for the generated cookiecutter
* `full_name` is the cookiecutter's author's full name
* `github_name` is the github account this is published on (currently assuming this to happen)
* `git_setup`: Whether the generated cookiecutter should include a git setup.
