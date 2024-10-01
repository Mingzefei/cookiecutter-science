# scr/plot/plot_style.py
import matplotlib.pyplot as plt
import scienceplots

plt.style.use("science")


def set_plot_style(Simplified_Chinese=False):
    """
    Set the plot style for matplotlib.

    Parameters:
    Simplified_Chinese (bool): Whether to use simplified Chinese font for labels and titles. Default is False.

    Returns:
    None
    """
    if Simplified_Chinese:
        plt.style.use(["science", "ieee", "no-latex", "cjk-sc-font"])
    else:
        plt.style.use(["science", "ieee"])


# Usage: in other scripts or notebooks
#
# import matplotlib.pyplot as plt
# from src.plot.plot_style import set_plot_style
# set_plot_style(Simplified_Chinese=True)
