### Struktur
```
└─┬ root
  |
  ├─┬ ressource
  | |
  | ├─┬ cleaned
  | | ├─ externalRelationship.csv
  | | ├─ linkRelationship.csv
  | | ├─ otherRelationship.csv
  | | └ article.csv
  | |
  | └─┬ data
  |   └ ... // Wikipedia Clickstream-datasets
  |
  ├─┬ src
  | |
  | ├─ FileReader.py
  | └─ FileWriter.py
  |
  └─ .gitignore
```

### Wikipedia-Datasets
https://dumps.wikimedia.org/other/clickstream/
