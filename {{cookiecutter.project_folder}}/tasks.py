from invoke import task

@task
def showdeps(ctx):
    print("Current:")
    ctx.run("poetry show --tree")
    print("Latest:")
    ctx.run("poetry show --latest")


@task
def lint(ctx):
    print("\n-------------------------------")

    ctx.run(f"poetry run ruff check .")
    ctx.run("poetry run ruff format --check .")
    ctx.run(f"poetry run mypy .")


@task
def format(ctx):
    ctx.run(f"poetry run ruff check --fix .")
    ctx.run("poetry run ruff format .")
    ctx.run("poetry run mdformat README.md")


@task
def test(ctx):
    ctx.run("poetry run pytest -v --cov --junitxml=unit-test-report.xml --cov-report=xml")


@task(pre=[lint, test])
def build(ctx):
    ctx.run("poetry build")


@task
def pre_commit(ctx):
    ctx.run("poetry run pre-commit run")
