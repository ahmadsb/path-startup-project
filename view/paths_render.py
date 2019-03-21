import pandas as pd
from matplotlib.pyplot import imread, imshow, plot, legend, show


def render_paths():
    df = pd.read_hdf("data/data.hdf5", "df")

    objects = df.groupby(['filename', 'objectNum']).size()
    df_by_objs = df.set_index(['filename', 'objectNum']).sort_index()

    bg = imread("data/paths0.png")

    imshow(bg, alpha=0.5)
    sample_objs = objects[objects > 50].sample(10)

    for t, n in sample_objs.iteritems():
        o = df_by_objs.loc[t]
        plot(o.x, o.y, label=n)
    show()
    legend()
