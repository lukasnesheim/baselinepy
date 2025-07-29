# package imports
import json

# function imports
from importlib.resources import files

# global variables
_color: dict | None = None
_style: dict | None = None

def load_color() -> dict | None:
    global _color
    
    if _color is None:
        _color = json.loads((files("baselinepy.resources") / "color.json").read_text())

    return _color

def load_style() -> dict | None:
    global _style

    if _style is None:
        _style = json.loads((files("baselinepy.resources") / "style.json").read_text())

    return _style