try:
	from .__version__ import __version__
	version_string = ' v{}'.format(__version__)
except ImportError:
	version_string = ''


from shutil import move, copytree, copy, rmtree
from os import makedirs as make_directory, listdir as directory_contents
from os.path import isfile as is_file, isdir as is_directory, join as path
from os.path import dirname, abspath, basename, splitext, exists
from functools import partial


def project_name(filename):
	return splitext(basename(filename))[0]


def location_of(thing):
	return dirname(abspath(thing))


def template_copy(data, source, there):
	class mapping(dict):
		def __missing__(self, key):
			if key == '<': return '{'
			if key == '>': return '}'
			if key.startswith('='):
				# Ruler. The next character indicates the type,
				# and also delimits the specifications for total length.
				ruler_type = key[1]
				ruler_length = sum(
					len(self[piece]) if piece else 1
					for piece in key.split(ruler_type)[1:]
				)
				# reStructuredText allows for rulers made with ':', but that
				# already has special meaning in format specifiers.
				if ruler_type == ';': ruler_type = ':'
				return ruler_type * ruler_length
			if key.startswith('@'): key = key[1:]
			return '{{{}}}'.format(key)

	here, name = location_of(source), basename(source)
	if name.endswith('.template'):
		there = splitext(there)[0]
		print("Debug: template copy from {} to {}".format(source, there))
		with open(source) as infile, open(there, 'w') as outfile:
			for line in infile:
				outfile.write(line.format_map(mapping(data)))
	else:
		# Not a template file; copy normally.
		copy(source, there)


def copy_template_tree(source, there, data):
	"""Interface to shutil.copytree. Interpolates into .template files
	as they are found, removing .template filename extensions from the copies,
	and gracefully handles an already-existing destination folder."""
	def do_copy(s, t):
		copytree(s, t, copy_function=partial(template_copy, data))

	if exists(there):
		# Dump everything into the existing directory, one piece at a time.
		for item in directory_contents(source):
			item, target = path(source, item), path(there, item)
			if is_directory(item):
				do_copy(item, target)
			else:
				template_copy(data, item, target)
	else:
		do_copy(source, there)


def new_project_folder(here, source, data):
	"""Create a new bakedbeans project folder."""
	def finalize():
		copy_template_tree(path(here, 'tin'), project_root, data)
		# Ensure top-level package.
		with open(path(src_folder, '__init__.py'), 'a'):
			pass
		# TODO: git stuff

	there = location_of(source)
	if is_file(source):
		name = project_name(source)
		# Fail fast if the project folder couldn't be made.
		project_root = path(there, name)
		# TODO: make this sync up with package_dir in setup.py
		src_folder = path(there, name, 'src')
		make_directory(src_folder)
		move(source, src_folder)
		finalize()
	elif is_directory(source):
		# TODO
		print("not implemented yet.")
	else:
		raise OSError("couldn't find file or directory")


def main():
	import sys
	print("Baked Beans{} main script".format(version_string))
	args, here = sys.argv[1:], location_of(__file__)
	print("here: {} args: {}".format(here, args))

	if not is_directory(path(here, 'tin')):
		# First run.
		print("Welcome! Please answer a few quick questions to set up the tin.")

		copy_template_tree(
			path(here, 'tin.template'),
			path(here, 'tin'),
			{} # TODO: prompt user for this information
		)
		# rmtree(path(here, 'tin.template'))

	if args:
		# TODO: fill in the data for the copy
		new_project_folder(here, args[0], {})
	else:
		# interactive mode - TODO
		pass


if __name__ == '__main__':
	main()
