import rawpy


assert rawpy.libraw_version >= (0, 21)
assert rawpy.flags is None or isinstance(rawpy.flags, dict)
assert rawpy.DemosaicAlgorithm.AHD.name == "AHD"
