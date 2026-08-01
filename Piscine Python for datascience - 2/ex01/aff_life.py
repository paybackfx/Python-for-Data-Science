#!/usr/bin/env python3
# =============================================================================
# EXERCISE 01: DRAW MY COUNTRY
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Row Selection (dataset[dataset["country"] == COUNTRY]): comparing a
#    column to a value produces a boolean mask, and indexing the frame with
#    that mask keeps only the rows where the mask is True.
# 2. Wide Format: this dataset stores one column per year, so the years are
#    the column labels. They are cast to int to become a real numeric x axis
#    instead of a sequence of strings.
# 3. A Graph Without Labels Is Noise: the subject requires a title and a
#    legend on each axis, because a curve nobody can read proves nothing.
# =============================================================================

import matplotlib.pyplot as plt

from load_csv import load

COUNTRY = "Morocco"


def plot_life_expectancy(dataset, country: str) -> None:
    """Draw the life expectancy curve of the given country over time."""
    rows = dataset[dataset["country"] == country]
    if rows.empty:
        raise ValueError(f"{country} is not present in the dataset")
    years = [int(column) for column in dataset.columns[1:]]
    values = rows.iloc[0, 1:].astype(float).tolist()

    plt.plot(years, values)
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


def main() -> None:
    """Load the life expectancy dataset and draw the campus country."""
    dataset = load("life_expectancy_years.csv")
    if dataset is None:
        return
    try:
        plot_life_expectancy(dataset, COUNTRY)
    except (ValueError, KeyError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
