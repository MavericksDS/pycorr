# PyCorr
A simple library to calculate correlation between variables. Currently provides correlation between nominal variables.

Based on statistical methodology like Cramer'V and Tschuprow'T allows to gauge the correlation between categorical variables. Ability to plot the correlation in form of heatmap is also provided.

## Usage example
```
import pandas as pd
from pycorrcat.pycorrcat import plot_corr, corr_matrix

df = pd.DataFrame([('a', 'b'), ('a', 'd'), ('c', 'b'), ('e', 'd')],
                  columns=['dogs', 'cats'])

correlation_matrix = corr_matrix(data, ['dogs', 'cats'])
plot_corr(df, ['dogs','cats'] )
```

## Development setup
Create a virtualenv and install dependencies:
- `pip install -r requirements.dev.txt`
- `pip install -r requirements.txt`
Then install the pre-commit hooks: `pre-commit install` and continue with code change.

### Run `pre-commit` locally to check files

`pre-commit run --all-files`

## Release History

* 0.1.4
    * CHANGE: Changed the documentation (no code change)
* 0.1.3
    * ADD: Ability to pass dataframe to get correlation matrix
    * ADD: Ability to plot the correlation in form of heatmap
* 0.1.2
    * Added as first release
* 0.1.1
    * Test release

## Author and Contributor

Anurag Kumar Mishra – Connect on [github](https://github.com/anuragithub) or drop a [mail](mailto:anuragkm25@outlook.com)

Distributed under the GNU license. See ``LICENSE`` for more information.

Github repo link  [https://github.com/MavericksDS/pycorr](https://github.com/MavericksDS/pycorr)


## Contributing

1. Fork it (<https://github.com/MavericksDS/pycorr>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[pip-url]: https://pypi.org/project/pycorr/
