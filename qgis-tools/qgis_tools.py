#!/usr/bin/env python3

import os
import pty

def run(name, script, *args):
    import subprocess
    #pty.spawn([script])
    subprocess.call([script] + list(args))


def scriptfolder(rootfolder):
    """
    """
    return os.path.join(rootfolder, "scripts")

def main(args):
    """
    """
    print(args)
    rootfolder = args.root_folder
    os.chdir(rootfolder)
    if args.code_format:
        format_code(rootfolder)
    if args.prepare_commit:
        prepare_commit(rootfolder)
    if args.make_pizza:
        make_pizza()


def format_code(rootfolder):
    """
    """
    print("Formatting Code")
    scripts = scriptfolder(rootfolder)
    astyle = os.path.join(scripts, "astyle.sh")
    print(scripts)
    print(astyle)
    os.chdir(rootfolder)
    run("Format Code", astyle)


def prepare_commit(rootfolder):
    """
    """
    scripts = scriptfolder(rootfolder)
    prepare = os.path.join(scripts, "prepare-commit.sh")
    os.chdir(rootfolder)
    run("Prepare Commit", prepare)


def make_pizza():
    print("why am i so hungry man")