try:
	from .__version__ import __version__
	version_string = ' v{}'.format(__version__)
except ImportError:
	version_string = ''


def main():
	import sys
	print("Baked Beans{} main script".format(version_string))
	print("args:", sys.argv)


if __name__ == '__main__':
	main()
