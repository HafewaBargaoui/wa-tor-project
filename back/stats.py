import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Globals to keep the status of the graph objects
fig, ax = None, None
line_fish, line_sharks = None, None
cycles = []
pop_fish = []
pop_sharks = []

def create_plot() -> None:
    """ Creates the plot objects
    """
    # Global objects for the plot
    global fig, ax, line_fish, line_sharks
    plt.ion()
    fig, ax = plt.subplots()

    # Empty "lines"
    line_fish, = ax.plot([], [], label="Fish", color="blue")
    line_sharks, = ax.plot([], [], label="Sharks", color="red")

    # Title and labels
    ax.set_title("Populations over time")
    ax.set_xlabel("Cycles")
    ax.set_ylabel("Population")
    ax.legend()
    plt.show()


def update_plot(nb_cycle: int, nb_fish: int, nb_sharks: int) -> None:
    """ Updating the plot with new data each cycle

    Args:
        nb_cycle (int): cycle number to add to the plot
        nb_fish (int): number of fish to add to the plot
        nb_sharks (int): number of sharks to add to the plot
    """
    # Updating data to be plotted
    cycles.append(nb_cycle)
    pop_fish.append(nb_fish)
    pop_sharks.append(nb_sharks)

    # Updating the plot objects
    line_fish.set_data(cycles, pop_fish)
    line_sharks.set_data(cycles, pop_sharks)

    # Updating the axe limits
    ax.relim()
    ax.autoscale_view()

    # Giving the plot some time to update
    plt.pause(0.001)


def close_plot() -> None:
    """ Closes the plot
    """
    plt.ioff()
    plt.show()
