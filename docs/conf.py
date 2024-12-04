# Docs: https://mcss.mosra.cz/documentation/python/
# Run this file with `<mcss_clone_path>/documentation/python.py ./docs/conf.py`

from pathlib import Path

PROJECT_TITLE = "pyslang"
INPUT_MODULES = ['pyslang']

PYBIND11_COMPATIBILITY = True

OUTPUT = str((Path(__file__).parent.parent / "build/docs").absolute())
OUTPUT_STUBS = str((Path(__file__).parent.parent / "build/stubs").absolute())
