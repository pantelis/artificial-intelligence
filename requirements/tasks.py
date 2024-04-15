# https://gabnotes.org/pip-tools-for-python-dependencies-management/
# Please note that hash generation was removed as we need to install local packages

# tasks.py
from pathlib import Path

from invoke import Context, task

BASE_DIR = Path(__file__).parent.resolve(strict=True)

@task
def split_dependency_constraints(ctx: Context)->None:
    return separate_local_constraints(ctx, 'constraints.txt', 'local_constraints.txt', 'other_constraints.txt')

def separate_local_constraints(ctx:Context, input_file, output_file1, output_file2)->None:
    with ctx.cd(BASE_DIR):
        
        with open(input_file, 'r') as f:
            local_constraints = []
            other_constraints = []
            for line in f:
                if '@ file://' in line:
                    local_constraints.append(line)
                else:
                    other_constraints.append(line)
        with open(output_file1, 'w') as f:
            f.writelines(local_constraints)
        with open(output_file2, 'w') as f:
            f.writelines(other_constraints)
    
        
        
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
    common_args = "--resolver=backtracking"
    if update:
        common_args += " --upgrade"
    with ctx.cd(BASE_DIR):
        
        ctx.run(
            f"pip-compile {common_args}  --index-url https://pypi.nvidia.com/simple --extra-index-url https://pypi.org/simple --trusted-host pypi.nvidia.com --reuse-hashes --output-file requirements.txt docs.requirements.in  --constraint other_constraints.txt requirements.in", 
            pty=True,
            echo=True,
        )
    if sync:
        sync_dependencies(ctx)


@task
def compile_dev_dependencies(
    ctx: Context, *, update: bool = False, sync: bool = False
) -> None:
    common_args = "--resolver=backtracking"
    if update:
        common_args += " --upgrade"
    with ctx.cd(BASE_DIR):
        ctx.run(
            f"pip-compile {common_args} --index-url https://pypi.nvidia.com/simple --extra-index-url https://pypi.org/simple --trusted-host pypi.nvidia.com --reuse-hashes dev.requirements.in", # --generate-hashes --reuse-hashes
            pty=True,
            echo=True,
        )
    if sync:
        sync_dev_dependencies(ctx)

@task
def sync_dependencies(ctx: Context) -> None:
    with ctx.cd(BASE_DIR):
        ctx.run("pip-sync requirements.txt", pty=True, echo=True)
        
@task
def sync_dev_dependencies(ctx: Context) -> None:
    with ctx.cd(BASE_DIR):
        ctx.run("pip-sync requirements-dev.txt", pty=True, echo=True)