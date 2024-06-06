from argparse import ArgumentParser
import numpy as np

# Derived from table 1 of "National Vital Statistics Reports Volume 54, Number 14 United States Life Tables, 2003" (see README.md)
cumulative_deaths = [
         0,    687,    733,    767,    792,    811,    829,    844,    859,    872,
       884,    895,    906,    922,    945,    978,   1024,   1081,   1149,   1225,
      1307,   1395,   1489,   1587,   1685,   1781,   1876,   1968,   2060,   2153,
      2248,   2346,   2449,   2556,   2669,   2790,   2920,   3060,   3212,   3377,
      3558,   3755,   3967,   4197,   4445,   4715,   5007,   5322,   5662,   6026,
      6416,   6833,   7281,   7759,   8272,   8819,   9405,  10032,  10707,  11435,
     12226,  13089,  14030,  15051,  16146,  17312,  18552,  19877,  21295,  22816,
     24445,  26179,  28018,  29972,  32058,  34283,  36638,  39108,  41696,  44411,
     47257,  50228,  53306,  56474,  59717,  63019,  66336,  69636,  72887,  76054,
     79102,  81998,  84711,  87212,  89481,  91501,  93266,  94775,  96036,  97065,
     97882, 100000,
]

c = np.array(cumulative_deaths)

def predicted_year_of_death(age, max_year=100):
    # e.g., max_year == 10, 884 deaths are recorded in the first 10 years
    total_deaths = c[max_year+1]
    # account for current age, i.e., agent is already 4 years old, so 792 deaths have already occurred
    already_deceased = c[age]
    # this agent will be one of the deaths in (already_deceased, total_deaths] == [already_deceased+1, total_deaths+1)
    draw = np.random.randint(already_deceased+1, total_deaths+1)
    # find the year of death, e.g., draw == 733, searchsorted("left") will return 2, so the year of death is 1
    yod = np.searchsorted(c, draw, side="left") - 1

    return yod

def predicted_day_of_death(age, max_year=100):
    yod = predicted_year_of_death(age, max_year)
    # the agent will die sometime in the year of death, so we randomly select a day
    doy = np.random.randint(365)    # 0 <= doy < 365
    dod = yod * 365 + doy

    return dod


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-n", "--number", type=int, default=32, help="Number of samples [32]")
    parser.add_argument("-m", "--max_year", type=int, default=100, help="Maximum year to consider [100]")
    args = parser.parse_args()

    for i in range(args.number):
        age = np.random.randint(args.max_year+1)
        yod = predicted_year_of_death(age, args.max_year)
        print(f"Age: {age:3}, Year of Death: {yod:3}")

"""
    counts = np.zeros(101, dtype=np.int32)
    for i in range(1_000_000):
        yod = predicted_year_of_death(0, 100)
        counts[yod] += 1
    for i, e in enumerate(counts):
        print(f"{i:3}: {e:8,}")

    print("\n==========\n")

    counts = np.zeros(101, dtype=np.int32)
    for i in range(101):
        for j in range(100_000):
            yod = predicted_year_of_death(i, 100)
            if yod == i:
                counts[i] += 1
    for i, e in enumerate(counts):
        print(f"{i:3}: {e:7,}")
"""

...
