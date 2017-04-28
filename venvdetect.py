#!/usr/bin/env python3

"""Script to detect current working directory virtual environment"""

import argparse
import os

def venv_directories():
    """Retrieve and parse virtual environment directories to look for"""

    venv_dirs_env_var = os.getenv('VENV_DIRS')
    return ','.split(venv_dirs_env_var) if venv_dirs_env_var else ['venv']

def directory_has_activate(dir_path):
    """Determine whether specified directory has the activate bin"""

    return os.path.isfile(os.path.join(dir_path, 'bin', 'activate'))

def current_venv():
    """Get the current virtual environment, if there is currently one activated"""

    current_venv_full = os.getenv('VIRTUAL_ENV')
    return os.path.basename(current_venv_full) if current_venv_full else None

def main():
    """Main function"""

    # give the user the option to add a trailing space
    # this helps with PS1 output
    parser = argparse.ArgumentParser()
    parser.add_argument('--space', help='add a trailing space to output', action='store_true')
    args = parser.parse_args()

    current_virtual_env = current_venv()

    cwd = os.getcwd()
    for venv_dir in venv_directories():
        if directory_has_activate(os.path.join(cwd, venv_dir)):
            if venv_dir != current_virtual_env:
                print('available ({}){}'.format(
                    venv_dir,
                    ' ' if args.space else ''
                ), end='')
            break

if __name__ == '__main__':
    main()
