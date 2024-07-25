# kaplan-meier-to-distribution

Given a [Kaplan-Meier](https://en.wikipedia.org/wiki/Kaplan%E2%80%93Meier_estimator) survival curve, draw for time of death given survival to date.

Context: I have an agent based model of disease transmission which is initialized with a number of living agents. Since the model can run for several decades, it is necessary to remove agents when they reach their date of non-disease death to appropriately model the population. Drawing from a uniform distribution [0 ... max simulation age] isn't right (would I just keep drawing until I get a date of death in the future?) and drawing from [current age ... max simulation age] isn't correct either. Here I am working backwards from the life table from the CDC to create a function letting me draw for a date of death given the agent's current age (>0 during initialization and 0 for newborns during the simulation).

See `date_of_death.py` for the code.

See `explore.ipynb` for a notebook exploring the code a little.

## Sources

- [Life Table - Wikipedia](https://en.wikipedia.org/wiki/Life_table)
- [National Vital Statistics Reports Volume 54, Number 14 United States Life Tables, 2003](https://www.cdc.gov/nchs/data/nvsr/nvsr54/nvsr54_14.pdf)
- [Table 1. Life table for the total population: United States, 2003](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/NVSR/54_14/)

- [UN World Population Prospects 2024](https://population.un.org/wpp/Download/Standard/Mortality/)
