from invoke import task

SRC = "backend/cai"
TEST_SRC = "backend/tests"


@task
def showdeps(ctx):
    print("Current:")
    ctx.run("poetry show --tree")
    print("Latest:")
    ctx.run("poetry show --latest")


@task
def lint(ctx):
    ctx.run(f"poetry run black {SRC} {TEST_SRC} --check")

    print("\n-------------------------------")

    ctx.run(f"poetry run ruff check {SRC} {TEST_SRC}")


@task
def format(ctx):
    ctx.run(f"poetry run black {SRC} {TEST_SRC}")
    ctx.run(f"poetry run isort {SRC} {TEST_SRC}")
    ctx.run(f"poetry run ruff --fix {SRC} {TEST_SRC}")
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