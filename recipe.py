class Recipe(object):

    def __init__(self, root, lang):
        self.id = root.find('declarations/uid').text

        self.name = root.find('declarations/name/lang[@ref="%s"]' % lang).text

        self.ingredients = {}
        self.ingredient_index = {}
        for e in root.findall('declarations/ingredient-categories/cat'):
            ident = e.attrib["id"]
            unit = e.find('unit/lang[@ref="%s"]' % lang).text
            name = e.find('name/lang[@ref="%s"]' % lang).text
            self.ingredient_index[ident] = {
                "name": name, "unit": unit
            }

        self.categories = {}
        categories = root.find('.//categories')
        self.preparationTime = categories.find('duration[@type="preparation"]').attrib["value"]
        self.cookingTime = categories.find('duration[@type="cooking"]').attrib["value"]

        for e in categories.findall('category'):
            m, major, minor = e.attrib["path"].split("/")
            if not major in self.categories:
                self.categories[major] = []
            self.categories[major].append(minor)

        self.instructions = {}
        for i, grp in enumerate(root.findall('task/group')):
            self.instructions[i] = {
                "title": grp.find('title/lang[@ref="en"]').text,
            }
            msg = grp.find('message/lang[@ref="%s"]' % lang)
            if msg is not None:
                self.instructions[i]["message"] = msg.text.strip()
            if "scope" in grp.attrib:
                self.instructions[i]["scope"] = grp.attrib["scope"]
            for e in grp.findall('ingredient'):
                if not "ingredients" in self.instructions[i]:
                    self.instructions[i]["ingredients"] = []
                ref = e.attrib['ref']
                d = self.ingredient_index[ref]
                amt = e.find('amount')
                if amt is not None:
                    d['amount'] = float(amt.attrib["min"])
                self.instructions[i]["ingredients"].append(d)
                self.ingredients[ref] = d
            for e in grp.findall('*[scope]'):
                a = e.find('oven')
                if a is not None:
                    if not "device" in self.instructions[i]: self.instructions[i]["device"] = []
                    d = {
                        "type": "oven",
                        "duration": a.attrib['duration'],
                        "mode": a.attrib['heating-mode'],
                        "temperature": a.attrib['oven-temperature'],
                    }
                    if a.find('continue') is not None:
                        d["condition"] = a.find('continue').attrib['condition']
                    self.instructions[i]["device"].append(d)
                b = e.find('pause')
                if b is not None:
                    if not "device" in self.instructions[i]: self.instructions[i]["device"] = []
                    self.instructions[i]["device"].append({
                        "type": "pause",
                        "id": b.attrib['id'],
                        "timeout": b.attrib['timeout'],
                    })


    def get_time_seconds(time):
        time.strptime(timeval, "%H:%M:%S").whatever

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            #"yield":
            "categories": self.categories,
            "preparationTime": self.preparationTime,
            "cookingTime": self.cookingTime,
            "ingredients": [ i['name'] for i in self.ingredients.values() ],
            "instructions": self.instructions,
        }
