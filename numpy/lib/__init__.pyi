import math as math
from typing import Any

from numpy._pytesttester import PytestTester

from numpy import (
    ndenumerate as ndenumerate,
    ndindex as ndindex,
)

from numpy.version import version

from numpy.lib import (
    format as format,
    mixins as mixins,
    scimath as scimath,
    stride_tricks as stride_tricks,
)

from numpy.lib._version import (
    NumpyVersion as NumpyVersion,
)

from numpy.lib.arrayterator import (
    Arrayterator as Arrayterator,
)

from numpy.lib.index_tricks import (
    ravel_multi_index as ravel_multi_index,
    unravel_index as unravel_index,
    mgrid as mgrid,
    ogrid as ogrid,
    r_ as r_,
    c_ as c_,
    s_ as s_,
    index_exp as index_exp,
    ix_ as ix_,
    fill_diagonal as fill_diagonal,
    diag_indices as diag_indices,
    diag_indices_from as diag_indices_from,
)

from numpy.lib.npyio import (
    savetxt as savetxt,
    loadtxt as loadtxt,
    genfromtxt as genfromtxt,
    recfromtxt as recfromtxt,
    recfromcsv as recfromcsv,
    load as load,
    save as save,
    savez as savez,
    savez_compressed as savez_compressed,
    packbits as packbits,
    unpackbits as unpackbits,
    fromregex as fromregex,
    DataSource as DataSource,
)

from numpy.lib.polynomial import (
    poly as poly,
    roots as roots,
    polyint as polyint,
    polyder as polyder,
    polyadd as polyadd,
    polysub as polysub,
    polymul as polymul,
    polydiv as polydiv,
    polyval as polyval,
    polyfit as polyfit,
    poly1d as poly1d,
)

from numpy.core.multiarray import (
    add_docstring as add_docstring,
    tracemalloc_domain as tracemalloc_domain,
)

from numpy.core.function_base import (
    add_newdoc as add_newdoc,
)

__all__: list[str]
__path__: list[str]
test: PytestTester

__version__ = version
emath = scimath
