import matplotlib.pyplot as plt
import numpy as np


def simulation_1():
    """Simulates a rigged dice roll generator."""
    seed = 42
    np.random.seed(seed)
    random_numbers = np.random.choice(
        a=np.array([0, 1]), size=(10000, 100), p=[0.2, 0.8]
    )
    mean_vector = np.mean(random_numbers, axis=1)
    fig = plt.figure(dpi=200, figsize=(10, 5))
    ax = plt.gca()
    hist = ax.hist(mean_vector, bins=10, color="skyblue", edgecolor="black")
    ax.set_title("Histogram of the mean of 10 dice rolls")
    ax.set_xlabel("Mean")
    ax.set_ylabel("Frequency")
    plt.show()


if __name__ == "__main__":
    simulation_1()
