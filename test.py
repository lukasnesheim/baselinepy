# package imports
import matplotlib.pyplot as plt
import seaborn as sns

# function imports
from sklearn.linear_model import LinearRegression

# baseline imports
from baselinepy.logo import add_logo
from baselinepy.mpl import baseline_plot, theme_baseline, add_caption, add_legend, add_title
from baselinepy.theme import load_color

# baseline global defaults
theme_baseline()

# baseline colors
color = load_color()
assert color is not None

# convert penguins dataframe to polars
df = sns.load_dataset("penguins").dropna()

# linear regression: flipper_length_mm, body_mass_g
X = df[["flipper_length_mm"]].to_numpy()
y = df["body_mass_g"].to_numpy()
model = LinearRegression().fit(X, y)
df["predicted_mass"] = model.predict(X)

# plot the linear regression
fig1, ax1 = baseline_plot()
sns.regplot(
    data=df,
    x="flipper_length_mm",
    y="body_mass_g",
    ax=ax1,
    ci=95,
    scatter_kws={
        "s": 30,
        "color": color["london"][4],
        "edgecolor": color["london"][2],
        "linewidths": 1.0
    },
    line_kws={
        "color": color["paris"][3],
        "linewidth": 2.0
    }
)

# add titles
add_title(ax1, "Predicting Mass", "Linear Regression of Body Mass on Flipper Length")

# add captions
add_caption(fig1, ["Charting: Lukas Nesheim", "Data: Seaborn"])

# set axis labels
ax1.set_xlabel("Flipper Length (mm)")
ax1.set_ylabel("Body Mass (g)")

plt.tight_layout()

fig1.savefig("test_regression.png", bbox_inches="tight", pad_inches=0.1, dpi=600)

# add the baseline logo
add_logo("test_regression.png")

# violin plot
fig2, ax2 = baseline_plot()

violin_palette = {
    "Adelie": color["paris"][3],
    "Chinstrap": color["vienna"][3],
    "Gentoo": color["dublin"][3]
}

sns.violinplot(data=df, x="species", y="body_mass_g", hue="species", palette=violin_palette, ax=ax2)

for violin in ax2.collections:
    violin.set_edgecolor(color["london"][2])

for violin in ax2.lines:
    violin.set_color(color["london"][2])

# add titles
add_title(ax2, "Weight Differences", "Body Mass by Species")

# add captions
add_caption(fig2, ["Charting: Lukas Nesheim", "Data: Seaborn"])

# set axis labels
ax2.set_xlabel("Species of Penguin")
ax2.set_ylabel("Body Mass (g)")

plt.tight_layout()

fig2.savefig("test_violin.png", bbox_inches="tight", pad_inches=0.1, dpi=600)

# add the baseline logo
add_logo("test_violin.png")

# legend plot
fig3, ax3 = baseline_plot()

sns.scatterplot(
    data=df,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species"
)

# add legend
add_legend(ax3, title="Test Title", frameon=True)

# add titles
add_title(ax3, "A Billi, A Billi", "Bill Depth by Bill Length")

# add captions
add_caption(fig3, ["Charting: Lukas Nesheim", "Data: Seaborn"])

# set axis labels
ax3.set_xlabel("Bill Length (mm)")
ax3.set_ylabel("Bill Depth (mm)")

plt.tight_layout()

fig3.savefig("test_legend.png", bbox_inches="tight", pad_inches=0.1)

add_logo("test_legend.png")