# Support, if possible, for a more informative version specification.
try:
	from enum import IntEnum
	status = IntEnum(
		'status',
		'PLANNING PREALPHA ALPHA BETA PRODUCTION MATURE INACTIVE'
	)
except ImportError:
	pass


# The project name. Also assumed to be the name of the single package that the
# project distribution consists of.
name = 'bakedbeans'

# The version number.
version = (0, 0, 1)
# Qualifications for the version number - epoch, pre-release version,
# post-release version and development version number, if applicable.
# Allowable keys: 'epoch', 'dev';
# at most one of 'post', 'rev', 'r';
# and at most one of 'a', 'b', 'c', 'alpha', 'beta', 'rc', 'pre', 'preview'.
# See PEP 440 for more information.
version_qualifiers = {}

# Short-form description of the project. A long-form description should be
# written in DESCRIPTION.rst, in ReStructured Text format with UTF-8 encoding.
description = 'A tool for starting new Python projects on GitHub with setuptools'

# Author details. Adjust as appropriate.
author = 'Karl Knechtel'
author_email = 'zahlman@gmail.com'
author_github = 'zahlman'

# The project's main homepage.
# The default setting assumes you will host the project on Github.
url = 'https://github.com/{}/{}'.format(author_github, name)

# Licensing.
license = 'MIT'
# Items to use in the 'license' classifier. Please make sure this matches
# the short license name.
license_long = ('OSI Approved', 'MIT License')

# How mature is this project?
development_status = status.PLANNING

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

# List run-time dependencies here.  These will be installed by pip when the
# project is installed.
dependencies = []

# XXX
package_data = []

# Console scripts. Mapping from script name to fully qualified function name.
console_scripts = {'bakedbeans': 'bakedbeans.main'}

# GUI scripts. Mapping from script name to fully qualified function name.
gui_scripts = {}
