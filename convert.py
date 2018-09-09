# coding: utf-8

if __name__ == '__main__':
    import time, os, json
    import xml.etree.ElementTree as ET

    from recipe import Recipe
    recipes = []

    dirlist = [dirs for root, dirs, files in os.walk('recipes')]

    import pandas as pd
    df = pd.DataFrame(columns=['name', 'ingredients', 'instructions', 'skill', 'duration'])

    for subdir in dirlist[0]:
        # subdir = dirlist[0][0]

        tree = ET.parse('recipes/%s/recipe.xml' % subdir)
        root = tree.getroot()
        data = Recipe(root, 'en').dict()

        with open('convert/%s.json' % subdir, 'w') as outfile:
            json.dump(data, outfile)

        df = df.append({
            'name':          data['name'],
            'ingredients':   len(data['ingredients']),
            'instructions':  len(data['instructions']),
            'skill':         data['categories']['cooking-skill'][0],
            'duration':      data['categories']['duration'][0],
        }, ignore_index=True)

    df.to_csv("data/sample.csv", sep=',', encoding='utf-8', index=False)
