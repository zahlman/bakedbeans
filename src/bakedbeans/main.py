try:
	from .__version__ import __version__
	version_string = ' v{}'.format(__version__)
except ImportError:
	version_string = ''


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


def setup_project_folder(project_folder):
	"""Create a new bakedbeans project folder."""
	pass # TODO
	# copy in the project_template files
	# update_config_file(path, name=project_name)


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
	print("args:", sys.argv)


if __name__ == '__main__':
	main()
