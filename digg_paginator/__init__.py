__version__ = '0.1.0'
VERSION = tuple(map(int, __version__.split('.')))

from .paginators import ExPaginator, DiggPaginator, QuerySetDiggPaginator
