import matplotlib.pyplot as plt
import numpy as np


def plot_all_dices(random_numbers: np.ndarray):
    fig = plt.figure(dpi=200, figsize=(8, 4))
    ax = plt.gca()
    counts, bins, _ = ax.hist(
        random_numbers.flatten(), bins=2, color="skyblue", edgecolor="black"
    )
    ax.set_title(
        f"Histogram of {random_numbers.shape[0]*random_numbers.shape[1]} dice rolls"
    )
    ax.set_xlabel("Dice roll")
    ax.set_ylabel("Frequency")
    bottom, top = ax.get_ylim()
    height = top - bottom
    c = (bins[1] - bins[0]) / 2
    for n, b in zip(counts, bins):
        if n != 0:
            ax.text(
                x=b + c,
                y=n + height * 0.02,
                s=f"{n:.3g}",
                horizontalalignment="center",
                verticalalignment="center",
            )
    plt.show()


def simulation_1():
    """Simulates a rigged dice roll generator."""
    seed = 42
    np.random.seed(seed)
    random_numbers = np.random.choice(
        a=np.array([0, 1]), size=(10000, 100), p=[0.02, 0.98]
    )
    mean_vector = np.mean(random_numbers, axis=1)
    plot_all_dices(random_numbers)
    fig = plt.figure(dpi=200, figsize=(8, 4))
    ax = plt.gca()
    hist = ax.hist(mean_vector, bins=10, color="skyblue", edgecolor="black")
    ax.set_title("Histogram of the mean of 10 dice rolls")
    ax.set_xlabel("Mean")
    ax.set_ylabel("Frequency")
    plt.show()


if __name__ == "__main__":
    simulation_1()
