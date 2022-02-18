import os
import pandas as pd
import csv
from datetime import date

from src.FileWriter import FileWriter

file = os.path.join(os.path.dirname(__file__), '../ressource/data/clickstream-dewiki-2021-12.tsv')

FileWriter.removeFilesIfExist()
FileWriter.createFilesIfNotExist()

seen = set()
count = 0;

df = pd.read_csv(file, sep='\t', names=["coming_from", "article", "referrer_type", "n"],
                 dtype={"referrer_type": "category"},
                 on_bad_lines="skip",
                 quoting=csv.QUOTE_NONE,
                 skiprows=1234567
                 )

# Boundarie
df = df.iloc[:500000]

df = df.reset_index()

for index, row in df.iterrows():

    count += 1
    if count % 100000 == 0:
        print(count)

    articleData = (str(row['coming_from']), "Article")

    if articleData not in seen:
        FileWriter.write(FileWriter.articleCsv, articleData)
        seen.add(articleData)

    articleData = (str(row['article']), "Article")
    if articleData not in seen:
        FileWriter.write(FileWriter.articleCsv, articleData)
        seen.add(articleData)

    if row['referrer_type'] == "link":
        FileWriter.write(FileWriter.linkRelationshipCsv, (
        str(row['coming_from']), date(year=2020, month=1, day=1), int(row["n"]),
        str(row['article']), "Link"))
    elif row['referrer_type'] == "other":
        FileWriter.write(FileWriter.otherRelationshipCsv,
                         (str(row['coming_from']), date(year=2020, month=1, day=1), int(row["n"]),
                           str(row['article']), "Other"))
    elif row['referrer_type'] == "external":
        FileWriter.write(FileWriter.externalRelationshipCsv, (
        str(row['coming_from']), date(year=2020, month=1, day=1), int(row["n"]),
        str(row['article']), "External"))
