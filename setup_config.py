project_name = 'bakedbeans'

# The version number.
version = (0, 1, 20)
# Qualifications for the version number - epoch, pre-release version,
# post-release version and development version number, if applicable.
# Allowable keys: 'epoch', 'dev';
# at most one of 'post', 'rev', 'r';
# and at most one of 'a', 'b', 'c', 'alpha', 'beta', 'rc', 'pre', 'preview'.
# See PEP 440 for more information.
version_qualifiers = { }

# Short-form description of the project. A long-form description should be
# written in DESCRIPTION.rst, in ReStructured Text format with UTF-8 encoding.
description = 'A tool for starting new Python projects on GitHub with setuptools.'

# Licensing.
license = 'MIT'
# Items to use in the 'license' classifier. Please make sure this matches
# the short license name.
license_long = ('OSI Approved', 'MIT License')

# How mature is this project? Used to set a 'development status' classifier.
development_status = 'planning'

# What versions of Python are supported.
supported_versions = ['3.2', '3.3', '3.4']

# What does your project relate to?
keywords = 'bakedbeans setuptools development'

# Any other classifiers to add, beyond the ones automatically generated.
# See https://pypi.python.org/pypi?%3Aaction=list_classifiers for classifiers.
# For each classifier, specify a sequence of items to join with ' :: ';
# or use nested sequences to group multiple classifiers (see the documentation
# for setup.make_classifiers).
additional_classifiers = (
	('Intended Audience', 'Developers'),
  ('Topic', ('Software Development', 'Build Tools'))
)

# List run-time dependencies here. These will be installed by pip when the
# project is installed.
dependencies = []

# Console scripts. Mapping from script name to package.module:global.callable.
console_scripts = {'bakedbeans': 'bakedbeans.__main__:main'}

# GUI scripts. Mapping from script name to fully qualified function name.
gui_scripts = { }

# Where packages are stored.
source_dir = 'src'
# Things to include or exclude explicitly when searching for packages.
# See documentation for setuptools.find_packages.
include_packages = ('*',)
exclude_packages = ()

# Author details. Adjust as appropriate.
author = 'Karl Knechtel'
author_email = 'zahlman@gmail.com'

# Modify this if your Github user ID changes or if you aren't hosting the
# project on Github.
url = 'https://github.com/zahlman/bakedbeans'

# Any other setuptools options you need to provide (or explicitly override
# for some reason).
extra_options = { }

# Additional instructions for the MANIFEST.in file, after including every
# file found in the git repository. (You might use this, for example, to
# exclude tests from distribution.)
extra_manifest = ['prune *tests*']

