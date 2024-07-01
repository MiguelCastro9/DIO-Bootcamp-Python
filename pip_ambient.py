# pip and virtual environment in python

# pip is python's package manager. 
# it allows us to install, update and remove packages easily. 
# it communicates with PyPI (Python Package Index), which is where most python packages are stored.

# install a package
# pip install package_name

# uninstall a package
# pip uninstall package_name

# list installed packages
# pip list

# update a package
# pip install --upgrade package_name

# virtual environments, like those created by venvs, allow us to maintain dependencies of different projects. 
# this is important to avoid conflicts between package versions.

# example commands:

# python3 -m venv myenv
# source myenv/bin/activate

# a simple example when working with pip and virtual environments:

# project on the machine and we run the 'pip list' command displays 5 dependencies.
# project in the virtual environment and running the 'pip list' command displays 2 dependencies.

# this allows us to have better control over our dependencies in python projects

# we also have pipenv and poetry

# pipenv is a package management tool that combines dependency management with virtual environment creation 
# for your projects and automatically adds/removes packages to packages from the Pipfile as you install and uninstall packages.

# poetry is another dependency management tool for python that allows you to declare libraries 
# that your project depends on and manages (installs/updates/removes) these libraries for you. 
# it also supports packaging and publishing projects to PyPl.