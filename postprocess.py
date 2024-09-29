import json
import pdb
import re
from pathlib import Path

import datasets as ds

paths = []
for path in Path("data/interim/enwiki-20240901").glob("*/wiki_*"):
    folder, idx = path.parts[-2], int(path.parts[-1].split("_")[1])
    paths.append((folder, idx, path))
paths = [path for _, _, path in sorted(paths, key=lambda x: (x[0], x[1]))]


def gen():
    for path in paths:
        with open(path) as f:
            for line in f:
                yield json.loads(line)


dataset = ds.Dataset.from_generator(gen, cache_dir="./data/cache")
dataset = dataset.filter(lambda x: x["formulas"])


def remove_math_tags(formula_list):
    for formula in formula_list:
        formula["text"] = re.sub(
            r"<math[^>]*>(.*?)</math>", r"\1", formula["text"], flags=re.DOTALL
        )
    return formula_list


dataset = dataset.map(lambda x: {"formulas": remove_math_tags(x["formulas"])})
dataset = dataset.select_columns(["id", "title", "text", "formulas", "url"])
dataset = dataset.sort("id")

dataset.push_to_hub("s-kat0/enwikimath", max_shard_size="1GB")

pdb.set_trace()
