try:
	from .__version__ import __version__
	version_string = ' v{}'.format(__version__)
except ImportError:
	version_string = ''


from shutil import move, copytree
from os.path import isfile as is_file, isdir as is_directory, join as path
from os.path import dirname, abspath, basename, splitext


def project_name(filename):
	return splitext(basename(filename))[0]


def location_of(thing):
	return dirname(abspath(thing))


def new_project_folder(here, source):
	"""Create a new bakedbeans project folder."""
	there = location_of(source)
	if is_file(source):
		name = project_name(source)
		# Fail fast if the project folder couldn't be made.
		project_root = path(there, name)
		# TODO: make this sync up with package_dir in setup.py
		package_root = path(there, name, 'src', name)
		copytree(path(here, 'project_template'), path(there, name))
		copytree(path(here, 'package_template'), path(there, name, 'src', name))
		move(source, path(there, name, 'src', name))
		# TODO: git stuff
	elif is_directory(source):
		# TODO
		print("not implemented yet.")
	else:
		raise OSError("couldn't find file or directory")


def update_config_file(path, **updates):
	"""Open the setup_config.py file at the named path and update the options.

	For each specified kwarg, a line is looked up in the file of the form
	<kwarg> = <existing option>
	and the existing option is replaced with the kwarg value (a string)."""
	pass # TODO


def setup_package_in(project_folder, package_name, *module_files):
	"""Make a package folder within the src subdirectory of the project_folder,
	and copy the module_files into it."""
	pass # TODO
	# create a subdirectory, then copy in the package_template files
	# and move in the module_files


def setup_git_repo(project_folder):
	"""Create a new git repo in the project_folder and add/commit everything."""
	pass # TODO




def new_project_from(path):
	"""Given a path to a file or directory, make a new project."""
	pass # TODO
	# if path specifies a file:
	# 	project_folder = new_folder(filename -.py)
	# 	files = [filename]
	# else:
	# 	project_folder = path
	# 	files = [glob *.py in path]
	# setup_project_folder(project_folder)
	# setup_package_in(project_folder, filename, *files)
	# setup_git_repo(project_folder)


def main():
	import sys
	print("Baked Beans{} main script".format(version_string))
	args, here = sys.argv[1:], location_of(__file__)
	print("here: {} args: {}".format(here, args))
	new_project_folder(here, args[0])


if __name__ == '__main__':
	main()
