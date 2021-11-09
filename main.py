import pandas as pd

"""
Data example:
[0]Nature Photonics
[1]1749-4885
[2]1749-4893
[3]OPTICS - SCIE
[4]38.771
[5]Energy & Environmental Science
[6]1754-5692
[7]1754-5706
[8]ENGINEERING, CHEMICAL - SCIE
[9]38.532

Every journal have 5 info placed into rows:
1. Journal name
2. Id 1
3. Id 2
4. Category
5. Impact factor
"""
file_path = "data.txt"

with open(file_path, "r") as file:
    data = file.readlines()

journal_info = []

for i in range(len(data)):
    if i == 0:
        continue
    if i % 5 == 0:
        journal_name = data[i - 5]
        id_one = data[i - 4]
        id_two = data[i - 3]
        category = data[i - 2]
        impact_factor = float(data[i - 1])

        journal_info.append(
            {
                "journal_name": journal_name,
                "id_one": id_one,
                "id_two": id_two,
                "category": category,
                "impact_factor": impact_factor,
            }
        )


df = pd.DataFrame(journal_info)

df["impact_factor"].describe().to_csv("result_IF.csv")
