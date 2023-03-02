import matplotlib.pyplot as plt
from sklearn import tree


def save_figure(model, feature_names):
    fig = plt.figure(figsize=(25, 20))
    plt.suptitle(t="Palmer Penguins Species Decision Tree", fontsize="xx-large")
    tree.plot_tree(model,
                   filled=True,
                   feature_names=feature_names)
    fig.savefig("./assets/calculated-penguin-decision-tree.png")
