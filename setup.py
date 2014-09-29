from shutil import copy
from os.path import join as path, dirname, abspath, expanduser
from os import remove


tin = path('src', 'bakedbeans', 'tin.template')
# Grab modules from the tin and run them, using the local setup_config.
# We don't attempt to fill in the setup_config template from the tin, because
# there's too much custom stuff needed.
copy(path(tin, 'setup.py'), 'bootstrap.py')
copy(path(tin, 'ez_setup.py'), 'ez_setup.py')
import setup_config, bootstrap
# Now setuptools is ensured to be available.
from setuptools.command.install import install as _install


# http://stackoverflow.com/a/18159969/523612
def make_shortcut(script_dir):
    with open(path(expanduser('~'), 'desktop', 'bakedbeans.bat'), 'w') as bat:
        bat.write('@echo off\n"{}\\bakedbeans.exe" %*\npause'.format(script_dir))


class install(_install):
    def run(self):
        super().run()
        self.execute(
            make_shortcut,
            (self.install_scripts,),
            msg="Creating desktop shortcut"
        )


setup_config.extra_options['cmdclass'] = {'install': install}
bootstrap.do_setup(dirname(abspath(__file__)), setup_config)
remove('ez_setup.py')
remove('bootstrap.py')
