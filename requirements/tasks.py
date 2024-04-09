# https://gabnotes.org/pip-tools-for-python-dependencies-management/
# tasks.py
from pathlib import Path

from invoke import Context, task

BASE_DIR = Path(__file__).parent.resolve(strict=True)

@task
def update_dependencies(ctx: Context, *, sync: bool = True) -> None:
    return compile_dependencies(ctx, update=True, sync=sync)


@task
def update_dev_dependencies(ctx: Context, *, sync: bool = True) -> None:
    return compile_dev_dependencies(ctx, update=True, sync=sync)

@task
def compile_dependencies(
    ctx: Context, *, update: bool = False, sync: bool = False
) -> None:
    common_args = "-q --allow-unsafe --resolver=backtracking"
    if update:
        common_args += " --upgrade"
    with ctx.cd(BASE_DIR):
        ctx.run(
            f"pip-compile {common_args} --generate-hashes requirements.in",
            pty=True,
            echo=True,
        )
        ctx.run(
            f"pip-compile {common_args} --strip-extras -o constraints.txt requirements.in",
            pty=True,
            echo=True,
        )
    if sync:
        sync_dependencies(ctx)


@task
def compile_dev_dependencies(
    ctx: Context, *, update: bool = False, sync: bool = False
) -> None:
    common_args = "-q --allow-unsafe --resolver=backtracking"
    if update:
        common_args += " --upgrade"
    with ctx.cd(BASE_DIR):
        ctx.run(
            f"pip-compile {common_args} --generate-hashes requirements-dev.in",
            pty=True,
            echo=True,
        )
    if sync:
        sync_dependencies(ctx)

@task
def sync_dependencies(ctx: Context) -> None:
    with ctx.cd(BASE_DIR):
        ctx.run("pip-sync requirements.txt requirements-dev.txt", pty=True, echo=True)