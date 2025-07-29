# package imports
import numpy as np

# function imports
from matplotlib import rcParams, pyplot as plt
from matplotlib.figure import Figure
from typing import Tuple, Any

# baseline imports
from baselinepy.font import register_montserrat
from baselinepy.theme import load_color, load_style

def add_caption(fig, lines: list[str]):
    style = load_style()
    assert style is not None

    # set the caption
    fig.text(
        0.02,
        -0.02,
        "\n".join(lines),
        fontsize=style["plot"]["font"]["size"]["credit"],
        fontweight=style["plot"]["font"]["weight"]["credit"],
        color=style["plot"]["font"]["color"]["credit"],
        linespacing=1.5
    )

def add_legend(ax, title: str = "", *, loc="best", frameon=False, borderpad=0.8):
    style = load_style()
    assert style is not None

    # set the legend
    legend = ax.legend(title=title, loc=loc, frameon=frameon, borderpad=borderpad)
    
    # style the legend text
    for text in legend.get_texts():
        text.set_fontsize(style["plot"]["font"]["size"]["legend"])
        text.set_color(style["plot"]["font"]["color"]["legend"])
        text.set_fontweight(style["plot"]["font"]["weight"]["legend"])

    # style the legend frame
    if (frame := legend.get_frame()):
        frame.set_facecolor(style["plot"]["legend"]["facecolor"])
        frame.set_edgecolor(style["plot"]["legend"]["edgecolor"])
        frame.set_linewidth(0.8)

def add_title(ax, title: str, subtitle: str):
    style = load_style()
    assert style is not None

    # set the title
    ax.set_title(
        title,
        loc="left",
        pad=20,
        fontsize=style["plot"]["font"]["size"]["title"],
        fontweight=style["plot"]["font"]["weight"]["title"],
        color=style["plot"]["font"]["color"]["title"]
    )

    # set the subtitle
    ax.text(
        0,
        1.02,
        subtitle,
        ha="left",
        transform=ax.transAxes,
        fontsize=style["plot"]["font"]["size"]["subtitle"],
        fontweight=style["plot"]["font"]["weight"]["subtitle"],
        color=style["plot"]["font"]["color"]["subtitle"]
    )

def baseline_plot(*args, flatten: bool = False, **kwargs) -> Tuple[Figure, Any]:
    style = load_style()
    assert style is not None

    # create the subplots
    fig, ax = plt.subplots(*args, **kwargs)

    # flatten the axes for easy iteration
    axes = [*ax.flat] if isinstance(ax, np.ndarray) else [ax]

    for axis in axes:
        # despine the plot
        for spine in axis.spines.values():
            spine.set_visible(False)

        # set grid parameters
        axis.grid(
            True,
            color=style["plot"]["grid"]["color"],
            alpha=style["plot"]["grid"]["alpha"],
            linestyle=style["plot"]["grid"]["linestyle"],
            linewidth=style["plot"]["grid"]["linewidth"]
        )

        # style the x-axis labels
        axis.set_xlabel("",
            fontsize=style["plot"]["font"]["size"]["label"],
            color=style["plot"]["font"]["color"]["label"],
            fontweight=style["plot"]["font"]["weight"]["label"]
        )

        # style the y-axis labels
        axis.set_ylabel("",
            fontsize=style["plot"]["font"]["size"]["label"],
            color=style["plot"]["font"]["color"]["label"],
            fontweight=style["plot"]["font"]["weight"]["label"]
        )

        # weight the x-axis tick labels
        for label in axis.get_xticklabels():
            label.set_fontsize(style["plot"]["font"]["size"]["tick"])
            label.set_color(style["plot"]["font"]["color"]["tick"])
            label.set_fontweight(style["plot"]["font"]["weight"]["tick"])
        
        # weight the y-axis tick labels
        for label in axis.get_yticklabels():
            label.set_fontsize(style["plot"]["font"]["size"]["tick"])
            label.set_color(style["plot"]["font"]["color"]["tick"])
            label.set_fontweight(style["plot"]["font"]["weight"]["tick"])
        
        # set tick parameters
        axis.tick_params(
            axis="both",
            direction="out",
            which="both",
            length=0,
            colors=style["plot"]["font"]["color"]["tick"]
        )

    return fig, axes if flatten else ax

def theme_baseline():
    # register the montserrat font
    register_montserrat()

    # load theme color
    color = load_color()
    assert color is not None

    # load theme style
    style = load_style()
    assert style is not None

    # global settings
    rcParams["font.family"] = style["plot"]["font"]["family"]
    rcParams["font.size"] = style["plot"]["font"]["size"]["body"]
    rcParams["text.color"] = style["plot"]["font"]["color"]["body"]
    rcParams["figure.facecolor"] = color["background"]
    rcParams["axes.facecolor"] = color["background"]
    rcParams["savefig.dpi"] = 600