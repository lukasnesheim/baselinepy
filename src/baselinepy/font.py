# function imports
from importlib.resources import files
from matplotlib import font_manager

def register_montserrat():
    for font in files("baselinepy.resources.fonts.montserrat").iterdir():
        font_manager.fontManager.addfont(str(font))