import os

def dump_metadata(folder, pipenv = False, pip_freeze = True):
    """
    Dump the metadata necessary to recreate a python environment.

    If using pipenv, the virtual environment can then be recreated using pipenv install.
    
    Parameters
    ----------

    folder: str
        Folder in which to dump metadata.

    pipenv: boolean, default = True
        Use pipenv to generate Pipfile and Pipfile.lock.
        May be long, but is more precise than pip freeze.
        You need to install pipenv for this to work.

    pip_freeze: boolean, default = False
        Use pip freeze to generate a requirement.txt
    """
    if pip_freeze:
        os.system("cd "+folder+" && pip freeze > requirements.txt")
        print("Pip requirement done.")
    if pipenv:
        os.system("cd "+folder+" &&  pipenv lock")
        print("Locked with pipenv.")

