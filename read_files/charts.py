import matplotlib.pyplot as plt

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig(f'./imgs/pie_by_continent_final.png')
    plt.close()


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

if __name__ == '__main__':
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]