# package imports
import numpy as np

# function imports
from baselinepy.font import register_montserrat
from baselinepy.theme import load_color, load_style
from matplotlib import rcParams, pyplot as plt
from matplotlib.figure import Figure
from typing import Tuple, Any

# global variables
_scale: float = 1.0

def add_caption(fig, lines: list[str]):
    style = load_style()["plot"]

    global _scale

    # set the caption
    fig.text(0.02, -0.02, "\n".join(lines), fontsize=_scale * style["font"]["size"]["credit"], fontweight=style["font"]["weight"]["credit"], color=style["font"]["color"]["credit"], linespacing=1.5)

def add_legend(ax, title: str = "", *, loc="best", frameon=False):
    style = load_style()["plot"]

    # set the legend
    legend = ax.legend(title=title, loc=loc, frameon=frameon)
    
    # style the legend
    for text in legend.get_texts():
        text.set_fontweight(style["font"]["weight"]["legend"])
        text.set_color(style["font"]["color"]["legend"])

def add_titles(ax, title: str, subtitle: str):
    style = load_style()["plot"]

    global _scale

    # set the title
    ax.set_title(title, pad=20)

    # set the subtitle
    ax.text(0, 1.02, subtitle, ha="left", transform=ax.transAxes, fontsize=_scale * style["font"]["size"]["subtitle"], fontweight=style["font"]["weight"]["subtitle"], color=style["font"]["color"]["subtitle"])

def baseline_plot(*args, flatten: bool = False, **kwargs) -> Tuple[Figure, Any]:
    style = load_style()["plot"]

    # create the subplots
    fig, ax = plt.subplots(*args, **kwargs)

    # flatten the axes for easy iteration
    axes = [*ax.flat] if isinstance(ax, np.ndarray) else [ax]

    for axis in axes:
        # despine the plot
        for spine in axis.spines.values():
            spine.set_visible(False)

        # weight the x-axis tick labels
        for label in axis.get_xticklabels():
            label.set_fontweight(style["font"]["weight"]["tick"])
        
        # weight the y-axis tick labels
        for label in axis.get_yticklabels():
            label.set_fontweight(style["font"]["weight"]["tick"])

    return fig, axes if flatten else ax

def theme_baseline(scale: float = 1.0):
    assert scale > 0, "'scale' must be a positive number."

    global _scale
    _scale = scale

    # register the montserrat font
    register_montserrat()

    # load theme color
    color = load_color()

    # load theme style
    style = load_style()["plot"]

    # global settings
    rcParams["font.family"] = style["font"]["family"]
    rcParams["font.size"] = _scale * style["font"]["size"]["body"]
    rcParams["text.color"] = style["font"]["color"]["body"]
    rcParams["figure.facecolor"] = color["background"]
    rcParams["axes.facecolor"] = color["background"]
    rcParams["savefig.dpi"] = 600

    # title settings
    rcParams["axes.titlelocation"] = "left"
    rcParams["axes.titlesize"] = _scale * style["font"]["size"]["title"]
    rcParams["axes.titleweight"] = style["font"]["weight"]["title"]
    rcParams["axes.titlecolor"] = style["font"]["color"]["title"]

    # axis labels
    rcParams["axes.labelsize"] = _scale * style["font"]["size"]["label"]
    rcParams["axes.labelcolor"] = style["font"]["color"]["label"]
    rcParams["axes.labelweight"] = style["font"]["weight"]["label"]

    # axis ticks
    rcParams["xtick.labelsize"] = _scale * style["font"]["size"]["tick"]
    rcParams["ytick.labelsize"] = _scale * style["font"]["size"]["tick"]
    rcParams["xtick.color"] = style["font"]["color"]["tick"]
    rcParams["ytick.color"] = style["font"]["color"]["tick"]

    # grid lines
    rcParams["axes.grid"] = True
    rcParams["grid.color"] = style["grid"]["color"]
    rcParams["grid.alpha"] = style["grid"]["alpha"]
    rcParams["grid.linestyle"] = style["grid"]["linestyle"]
    rcParams["grid.linewidth"] = style["grid"]["linewidth"]

    # tick parameters
    rcParams["xtick.direction"] = "out"
    rcParams["ytick.direction"] = "out"
    rcParams["xtick.major.size"] = 0
    rcParams["ytick.major.size"] = 0
    rcParams["xtick.minor.size"] = 0
    rcParams["ytick.minor.size"] = 0

    # legend settings
    rcParams["legend.loc"] = style["legend"]["location"]
    rcParams["legend.frameon"] = style["legend"]["frame"]
    rcParams["legend.facecolor"] = style["legend"]["facecolor"]
    rcParams["legend.edgecolor"] = style["legend"]["edgecolor"]
    rcParams["legend.fontsize"] = _scale * style["font"]["size"]["legend"]
    rcParams["legend.borderpad"] = 0.8