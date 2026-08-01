#!/usr/bin/env python3
# =============================================================================
# EXERCISE 02: COMPARE MY COUNTRY
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Human Readable Numbers: Gapminder stores populations as "3.28M" or
#    "1.16B", so every cell is a string. It has to be parsed back into a
#    float before anything can be plotted or compared.
# 2. Two Curves, One Axes: calling plot() twice draws on the same figure, and
#    the label= argument is what plt.legend() later reads to name each curve.
# 3. Tick Formatting (FuncFormatter): raw populations run into the hundreds
#    of millions, so the y axis is relabelled in M units to stay readable
#    without touching the underlying data.
# =============================================================================

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from load_csv import load

COUNTRY = "Morocco"
OTHER = "France"
FIRST_YEAR = 1800
LAST_YEAR = 2050
SUFFIXES = {"k": 1e3, "M": 1e6, "B": 1e9}


def to_number(value) -> float:
    """Convert a Gapminder cell such as "3.28M" into a plain float."""
    text = str(value).strip()
    if text and text[-1] in SUFFIXES:
        return float(text[:-1]) * SUFFIXES[text[-1]]
    return float(text)


def series_of(dataset, country: str, years: list) -> list:
    """Return the population of country for each year of the given list."""
    rows = dataset[dataset["country"] == country]
    if rows.empty:
        raise ValueError(f"{country} is not present in the dataset")
    return [to_number(rows.iloc[0][str(year)]) for year in years]


def millions(value, _position) -> str:
    """Format an axis tick value as a number of millions."""
    return f"{value / 1e6:g}M"


def plot_populations(dataset, first: str, second: str) -> None:
    """Draw the population of two countries between 1800 and 2050."""
    available = {int(column) for column in dataset.columns[1:]}
    years = [year for year in range(FIRST_YEAR, LAST_YEAR + 1)
             if year in available]
    if not years:
        raise ValueError("the dataset covers none of the requested years")

    plt.plot(years, series_of(dataset, first, years), label=first)
    plt.plot(years, series_of(dataset, second, years), label=second)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions))
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc="lower right")
    plt.show()


def main() -> None:
    """Load the population dataset and compare two countries."""
    dataset = load("population_total.csv")
    if dataset is None:
        return
    try:
        plot_populations(dataset, COUNTRY, OTHER)
    except (ValueError, KeyError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
