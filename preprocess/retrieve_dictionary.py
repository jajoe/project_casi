dictionary = {}
with open("dictionary.tsv", "r") as f:
    lines = f.readlines()[0].split("\r")
    for line in lines:
        elements = line.split("\t")
        power = elements[0]
        word = elements[2]
        ponderation = elements[5]
        if ponderation == "negative":
            ponderation = -1
        elif ponderation == "positive":
            ponderation = -1
        else:
            ponderation = 0
        if power == "strongsubj":
            ponderation *= 2

        dictionary[word] = ponderation


with open('dictionary.csv', 'w') as f:  
    content = ""
    for k in dictionary.keys():
        content += k + ";" + str(dictionary[k]) + "\n"
    f.write(content)
