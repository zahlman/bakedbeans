try:
	from .__version__ import __version__
except ImportError:
	VERSION_STRING = ''
	DEVELOPMENT_VERSION = True
else:
	VERSION_STRING = ' v{}'.format(__version__)
	DEVELOPMENT_VERSION = False


from shutil import move, copytree, copy, rmtree, get_terminal_size
from os import makedirs as make_directory, listdir as directory_contents
from os.path import isfile as is_file, isdir as is_directory, join as path
from os.path import dirname, abspath, basename, splitext, exists
from functools import partial
import json, codecs
from urllib.request import urlopen as open_url
from textwrap import wrap, dedent


def clean(text):
	return dedent(text).strip('\r\n')


def message(text):
	print(
		*wrap(clean(text), get_terminal_size().columns - 1),
		sep='\n'
	)


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
		name = data['project_name']
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


def prompt_missing_info(data, key, prompt):
	if data.get(key, None) is None:
		print()
		message('Please supply {}.'.format(clean(prompt)))
		data[key] = input('{}: '.format(key.title()))


def get_github_info(data, username):
	try:
		result = json.load(codecs.getreader('utf-8')(open_url(
			'https://api.github.com/users/{}'.format(username)
		)))
	except:
		return # oh well, prompt for it all explicitly.
	for github_name, my_name in (
		('html_url', 'url'),
		('name', 'name'),
		('email', 'email')
	):
		data[my_name] = result.get(github_name, None)


def firstrun(here):
	# First run.
	print("Welcome to Baked Beans!")
	data = {}
	message("""
		To get started, a few pieces of information are needed so they can be
		filled in for each new project you start. If you're already on GitHub,
		you can fill in your user ID and as much information as possible will be
		looked up automatically for you. Or you can leave it blank and enter the
		rest manually.
	""")
	username = input("Enter your GitHub user ID (optional): ")
	if username:
		get_github_info(data, username)
	prompt_missing_info(data, 'name', """
		your full name, as you would like it to appear on projects you publish
	""")
	prompt_missing_info(data, 'url', """
		a base URL for your projects, including http:// or https:// as desired.
		The default project URL for each new project will be of the form
		<base url>/<project name>.
	""")
	prompt_missing_info(data, 'email', """
		an email where you can be reached for project support
	""")

	copy_template_tree(path(here, 'tin.template'), path(here, 'tin'), data)
	if not DEVELOPMENT_VERSION:
		rmtree(path(here, 'tin.template'))

	print("Great! Now, let's set up your first project...")


def main():
	import argparse
	parser = argparse.ArgumentParser(prog='bakedbeans', description='A tool for starting new Python projects hosted on Github, targeting Windows.')
	parser.add_argument('source', nargs='?', help='file or folder to make a new project from')
	parser.add_argument('-d', '--description', help='short project description')
	data = vars(parser.parse_args())

	print("Baked Beans{} main script".format(VERSION_STRING))
	here = location_of(__file__)

	if not is_directory(path(here, 'tin')):
		firstrun(here)

	prompt_missing_info(data, 'source', 'the path to the project folder, or a .py file to create a new project from')
	prompt_missing_info(data, 'description', 'a brief description of the project')
	source = data.pop('source')
	data['project_name'] = project_name(source)
	new_project_folder(here, source, data)
	print("All done!")


if __name__ == '__main__':
	main()
