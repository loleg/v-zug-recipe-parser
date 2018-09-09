# coding: utf-8

if __name__ == '__main__':
    import time, os, json
    import xml.etree.ElementTree as ET

    from recipe import Recipe
    recipes = []

    dirlist = [dirs for root, dirs, files in os.walk('recipes')]

    for subdir in dirlist[0]:
        # subdir = dirlist[0][0]

        tree = ET.parse('recipes/%s/recipe.xml' % subdir)
        root = tree.getroot()
        data = Recipe(root, 'en').dict()

        with open('data/%s.json' % subdir, 'w') as outfile:
            json.dump(data, outfile)
