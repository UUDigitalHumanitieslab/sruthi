__version__ = '0.0.2'
__all__ = ['errors', 'sru', 'client']

from .errors import SruthiError, ServerIncompatibleError, SruError, NoMoreRecordsError  # noqa
from .errors import SruthiWarning, WrongNamespaceWarning # noqa
from .sru import searchretrieve, explain  # noqa
from .client import Client # noqa