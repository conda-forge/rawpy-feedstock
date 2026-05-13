import numpy as np

import rawpy
from rawpy.enhance import _repair_bad_pixels_bayer2x2


assert rawpy.libraw_version >= (0, 21)
assert rawpy.flags is None or isinstance(rawpy.flags, dict)
assert rawpy.DemosaicAlgorithm.AHD.name == "AHD"

raw = type("Raw", (), {})()
raw.raw_pattern = np.array([[0, 1], [3, 2]], dtype=np.uint8)
raw.raw_image_visible = np.arange(64, dtype=np.uint16).reshape(8, 8)
raw.raw_image_visible[2, 2] = 65535

_repair_bad_pixels_bayer2x2(raw, np.array([[2, 2]]))

assert raw.raw_image_visible[2, 2] != 65535
