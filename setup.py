from setuptools import setup
from os import path
import setup_config as config


development_status_names = [
	'1 - Planning',
	'2 - Pre-Alpha',
	'3 - Alpha',
	'4 - Beta',
	'5 - Production/Stable',
	'6 - Mature',
	'7 - Inactive'
]


def make_classifiers_gen(breadcrumb, *options):
	prefix = ' :: '.join(breadcrumb)
	for option in options:
		if option is None:
			yield prefix
		# Since strings are iterable, they need to be handled separately.
		elif isinstance(option, str):
			yield prefix + ' :: ' + option
		else:
			try:
				i = iter(option)
				n = next(i)
			except TypeError: # Not a sequence.
				yield '{} :: {}'.format(prefix, option)
			except StopIteration:
				raise ValueError("Empty sequences not permitted")
			else:
				yield from make_classifiers_gen(breadcrumb + (n,), *i)


def make_classifiers(breadcrumb, *options):
	return list(make_classifiers_gen(breadcrumb, *options))


def make_version(*args, **kwargs):
	result = '.'.join(str(a) for a in args)
	if 'epoch' in kwargs:
		result = '{}!{}'.format(kwargs['epoch'], result)
	def single_key(normalize, *names):
		canonical = names[0]
		found = False
		for name in names:
			if name in kwargs:
				if found:
					raise ValueError("please specify only one of {}".format(names))
				found = True
				if normalize and name != canonical:
					kwargs[canonical] = kwargs[name]
					del kwargs[name]
	single_key(True, 'c', 'rc', 'preview', 'pre')
	single_key(True, 'b', 'beta')
	single_key(True, 'a', 'alpha')
	single_key(False, 'a', 'b', 'c')
	single_key(True, 'post', 'r', 'rev')
	for segment in ('a', 'b', 'c', 'post', 'dev'):
		if segment in kwargs:
			result = '{}.{}{}'.format(result, segment, kwargs[segment])
	return result


here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
	long_description = f.read()

options = {
	'name': config.name,
	'version': make_version(*config.version, **config.version_qualifiers),
	'description': config.description,
	'long_description': long_description,
	'url': config.url,
	'author': config.author,
	'author_email': config.author_email,
	'license': config.license,
	'classifiers': make_classifiers(
		('Development Status', development_status_names[config.development_status - 1])
	) + make_classifiers(
		(), *config.additional_classifiers
	) + make_classifiers(
		('License',), config.license_long
	) + make_classifiers(
		('Programming Language', 'Python'), *config.supported_versions
	),
	'keywords': config.keywords,
	'packages': ['src'],
	'install_requires': config.dependencies
}

options['package_data'] = {
	'src': config.package_data + [
		'../DESCRIPTION.rst', '../setup_config.py'
	]
}

# TODO: look for a 'data' directory and set up data_files if appropriate
# Although 'package_data' is the preferred approach, in some case you may
# need to place data files outside of your packages.
# see http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
# In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
# data_files=[('my_data', ['data/data_file'])],

entry_points = {}
for script_type in ('console_scripts', 'gui_scripts'):
	entry_points[script_type] = [
		'{}={}'.format(k, ':'.join(v.rpartition('.')[::2]))
		for k, v in getattr(config, script_type, {}).items()
	]

if entry_points:
	options['entry_points'] = entry_points

# Finally ready.
setup(**options)
