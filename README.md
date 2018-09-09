We got an interesting database of recipes to play with from [V-Zug Home](https://home.vzug.com/en/) at the Open Food Data Hackathon, used in a mobile application to program smart kitchen devices. We took a closer look and investigated ways of combining it with other data sources and tools following [challenge #12](https://hack.opendata.ch/project/223).

In the project repository there is a Jupyter [notebook](https://github.com/loleg/v-zug-recipe-parser/blob/master/explore-vzug-recipes.ipynb) written in Python which explores and visualizes the data, along with a [script](https://github.com/loleg/v-zug-recipe-parser/blob/master/convert.py) to convert the XML files we received into JSON format according to a schema defined in [recipe.py](https://github.com/loleg/v-zug-recipe-parser/blob/master/recipe.py).

We then created this example [Data Package](https://frictionlessdata.io/data-packages/) as a potential starting point for future discussions about developing an open standard.

# Preparation

No special libraries are required to use the parsing script. The conversion script `convert.py` references the [Python Data Analysis](https://pandas.pydata.org/) library for CSV file generation. The Jupyter notebook includes some data analysis using the Pandas, Numpy and Matplotlib libraries. You can find some setup [instructions here](https://forum.schoolofdata.ch/t/14-9-wikidata-zurich-workshop/267/2). The schema of this Data Package was inferred using [Frictionless Data](https://frictionlessdata.io/field-guide/) CLI tools.

# License

The licensing terms of this dataset have not yet been established. If you intend to use these data in a public or commercial product, check with each of the data sources for any specific restrictions.

This Data Package is made available by its maintainers under the [Public Domain Dedication and License v1.0](http://www.opendatacommons.org/licenses/pddl/1.0/), a copy of the full text of which is in [LICENSE.md](LICENSE.md).
