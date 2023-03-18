from matplotlib import pyplot

def scatter(x,y,save_name):
    fig = pyplot.figure()
    pyplot.scatter(x,y)
    fig.savefig(f'{save_name}.png')