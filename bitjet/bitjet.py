import mmap

from IPython.html.widgets import DOMWidget
from IPython.utils.traitlets import Int, Unicode, List, Instance, Bytes

import base64

try:
    from numpy import ndarray
except:
    ndarray = None


def b64encode_json(a):
    return {'b64data': base64.b64encode(a)}

class BitWidget(DOMWidget):
    _view_module = Unicode('nbextensions/bitjet/bitjet', sync=True)
    _view_name = Unicode('BitView', sync=True)

    bitwidth = Int(2, sync=True)

    data = (
            Bytes(sync=True, to_json=b64encode_json) |
            Instance(ndarray, sync=True, to_json=b64encode_json)
    )

    blockwidth = Int(4, sync=True)
    blockheight = Int(4, sync=True)
