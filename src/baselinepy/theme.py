# package imports
import json

# function imports
from importlib.resources import files

# global variables
_color: dict | None = None
_style: dict | None = None

def load_color() -> dict:
    global _color
    
    if _color is None:
        _color = json.loads((files("baselinepy.resources") / "color.json").read_text())
    
    assert _color is not None, "Failed to load the color.json file."

    return _color

def load_style() -> dict:
    global _style
    
    if _style is None:
        _style = json.loads((files("baselinepy.resources") / "style.json").read_text())
    
    assert _style is not None, "Failed to load the style.json file."

    return _style