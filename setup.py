from shutil import copy
from os.path import join as path, dirname, abspath
from os import remove

tin = path('src', 'bakedbeans', 'tin.template')
# Grab modules from the tin and run them, using the local setup_config.
# We don't attempt to fill in the setup_config template from the tin, because
# there's too much custom stuff needed.
copy(path(tin, 'setup.py'), 'bootstrap.py')
copy(path(tin, 'ez_setup.py'), 'ez_setup.py')
import setup_config, bootstrap
bootstrap.do_setup(dirname(abspath(__file__)), setup_config)
remove('ez_setup.py')
remove('bootstrap.py')
