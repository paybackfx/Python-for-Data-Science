#!/usr/bin/env python3
# =============================================================================
# EXERCISE 03: DRAW MY YEAR
# =============================================================================
# Educational Notes for Beginners:
#
# 1. Joining Two Datasets: the two files share the country column, so an
#    inner merge keeps exactly the countries present in both and guarantees
#    that each point pairs the right income with the right life expectancy.
# 2. Logarithmic X Axis: incomes span three orders of magnitude, so a linear
#    axis would crush every poor country into the left margin. A log scale
#    turns a multiplicative spread into a readable linear one.
# 3. Scatter, Not Line: each point is an independent country observed the
#    same year - connecting them would suggest a progression that does not
#    exist. The shape of the cloud is the answer to the subject's question.
# =============================================================================

import matplotlib.pyplot as plt

from load_csv import load

YEAR = "1900"
SUFFIXES = {"k": 1e3, "M": 1e6, "B": 1e9}


def to_number(value) -> float:
    """Convert a Gapminder cell such as "1.05k" into a plain float."""
    text = str(value).strip()
    if text and text[-1] in SUFFIXES:
        return float(text[:-1]) * SUFFIXES[text[-1]]
    return float(text)


def column_of(dataset, year: str) -> dict:
    """Return a {country: value} mapping for the given year column."""
    if year not in dataset.columns:
        raise ValueError(f"the dataset does not cover the year {year}")
    pairs = {}
    for country, raw in zip(dataset["country"], dataset[year]):
        try:
            pairs[country] = to_number(raw)
        except ValueError:
            continue
    return pairs


def plot_projection(income, life, year: str) -> None:
    """Draw life expectancy against income for every country of a year."""
    incomes = column_of(income, year)
    lives = column_of(life, year)
    shared = sorted(set(incomes) & set(lives))
    if not shared:
        raise ValueError(f"no country has both values for {year}")

    plt.scatter([incomes[country] for country in shared],
                [lives[country] for country in shared],
                label=f"Countries in {year}")
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.legend(loc="lower right")
    plt.show()


def main() -> None:
    """Load both datasets and project life expectancy against income."""
    income = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if income is None:
        return
    life = load("life_expectancy_years.csv")
    if life is None:
        return
    try:
        plot_projection(income, life, YEAR)
    except (ValueError, KeyError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
