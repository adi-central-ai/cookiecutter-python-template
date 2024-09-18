from invoke import task

SRC = "."
TEST_SRC = "tests/"


@task
def showdeps(ctx):
    print("Current:")
    ctx.run("poetry show --tree")
    print("Latest:")
    ctx.run("poetry show --latest")


@task
def lint(ctx):
    print("\n-------------------------------")

    ctx.run(f"poetry run ruff check {TEST_SRC}")
    ctx.run(f"poetry run mypy {TEST_SRC}")


@task
def format(ctx):
    ctx.run(f"poetry run ruff --fix {TEST_SRC}")
    ctx.run("poetry run mdformat README.md")


@task
def test(ctx):
    ctx.run("poetry run pytest -v --cov")


@task(pre=[lint, test])
def build(ctx):
    ctx.run("poetry build")


@task
def pre_commit(ctx):
    ctx.run("poetry run pre-commit run")
