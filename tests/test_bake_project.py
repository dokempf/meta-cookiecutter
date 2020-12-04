from contextlib import contextmanager

import os


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def test_project_tree(cookies):
    result = cookies.bake(extra_context={'project_slug': 'test_project'})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'test_project'
    assert result.project.isdir()

    # Now try to configure a project from the generated cookiecutter
    with inside_dir(result.project.dirpath()):
        inner = cookies.bake(extra_context={'project_slug': 'inner_project'})
        assert inner.exit_code == 0
        assert inner.exception is None
        assert inner.project.basename == 'inner_project'
        assert inner.project.isdir()
