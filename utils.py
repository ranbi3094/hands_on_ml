from __future__ import division, print_function, unicode_literals
import config as cg
import numpy as np
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)


def save_fig(chapter_id, fig_id, tight_layout=True, fig_extension="png", resolution=300):
    images_path = os.path.join(cg.PROJECT_ROOT_DIR,  "images", chapter_id)
    if not os.path.exists(images_path):
        os.makedirs(images_path)

    path = os.path.join(images_path, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
