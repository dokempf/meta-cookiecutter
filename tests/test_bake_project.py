from . import check_bake, inside_bake


def test_project_tree(cookies):
    bake = cookies.bake(extra_context={'project_slug': 'test_project'})
    check_bake(bake)

    # Now try to configure a project from the generated cookiecutter
    with inside_bake(bake):
        inner = cookies.bake(extra_context={'project_slug': 'inner_project'})
        check_bake(inner)
