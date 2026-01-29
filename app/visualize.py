import matplotlib.pyplot as plt

def plot_sales(sales, output_path):
    plt.figure()
    plt.plot(sales)
    plt.title("Sales Trend")
    plt.xlabel("Day")
    plt.ylabel("Sales")
    plt.savefig(output_path)
    plt.close()
