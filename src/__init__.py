try:
	from .__version__ import __version__
except ImportError:
	pass # development version
__all__ = ['bakedbeans']
