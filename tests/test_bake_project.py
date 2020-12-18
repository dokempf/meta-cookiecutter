import pytest

from . import check_bake, inside_bake


def bake_outer_inner(cookies, outer_context={}, inner_context={}):
    # Configure a cookiecutter
    bake = cookies.bake(extra_context=outer_context)
    check_bake(bake)

    # Now try to configure a project from the generated cookiecutter
    with inside_bake(bake):
        inner = cookies.bake(extra_context=inner_context)
        check_bake(inner)


def test_nogit(cookies):
    bake_outer_inner(
        cookies,
        outer_context={
            'git_setup': 'No',
        }
    )


@pytest.mark.parametrize(
    "remote_url",
    [
        "None",
        "git@github.com:dokempf/test-repo.git",
        "https://github.com/dokempf/test-github-actions-cookiecutter-cpp-project.git",
        "git@gitlab.com:dokempf/test-repo.git",
        "https://gitlab.com/dokempf/test-repo.git",
        "ssh://git@gitlab.dune-project.org:22022/dominic/test-repo.git",
        "https://gitlab.dune-project.org/dominic/test-repo.git"
    ])
def test_git(cookies, remote_url):
    bake_outer_inner(
        cookies,
        inner_context={
            'remote_url': remote_url,
        },
        outer_context={
            'git_setup': 'No',
        }
    )
