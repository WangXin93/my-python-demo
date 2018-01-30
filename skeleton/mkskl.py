#!/usr/bin/env python3
import sys
import os

def touch(path):
    assert path, "path can't be empty"
    path = os.path.expanduser(path)
    basedir = os.path.dirname(path)
    # If directory path does't exist
    if not os.path.exists(basedir) and basedir:
        # Make base directory
        os.makedirs(basedir)
    # In case file exists
    with open(path, 'a'):
        # Update mtime incase file exists
        os.utime(path, None)

def build_skeleton(project):
    # Assume project is string like "d1/a1"
    project= project
    # Get base directory "d1"
    projectPath = os.path.dirname(project)
    # Get project name "a1"
    projectName = os.path.basename(project)
    # Make project root
    os.makedirs(project)
    # mkdir bin
    os.makedirs(os.path.join(project, "bin"))
    # mkdir NAME
    os.makedirs(os.path.join(project, projectName))
    # mkdir docs
    os.makedirs(os.path.join(project, "docs"))
    # mkdir tests
    os.makedirs(os.path.join(project, "tests"))
    # touch d1/a1/a1/__init__.py
    touch(os.path.join(project, projectName, "__init__.py"))
    # touch d1/a1/tests/__init__.py
    touch(os.path.join(project, "tests", "__init__.py"))
    # touch d1/a1/setup.py
    touch(os.path.join(project, "setup.py"))
    # touch d1/a1/tests/setup_tests.py
    touch(os.path.join(project, "tests", "setup_tests.py"))
    setup_tests="""from nose.tools import *
def setup_tests():
    print("SETUP!")
"""
    with open(os.path.join(project, "tests", "setup_tests.py"), "w") as f:
        f.write(setup_tests)

    # touch d1/a1/.gitignore
    touch(os.path.join(project, '.gitignore'))
    ignore_contents = """*.pyc
__pychche__
"""
    with open(os.path.join(project, '.gitignore'), 'w') as f:
        f.write(ignore_contents)
    # Print done.
    print(project + " SETUP done!")

if __name__ == "__main__": 
    build_skeleton(sys.argv[1])

