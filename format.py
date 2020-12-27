import os
import json


def conll2json(source, target):
    with open(source, 'r', encoding='utf-8') as sf, \
            open(target, 'w', encoding='utf-8') as tf:
        word_list = []
        entity_list = []
        count = 0
        for line in sf:
            line = line.rstrip()
            if not line:
                if word_list:
                    text = "".join(word_list)
                    tf.write(json.dumps({
                        "text": text,
                        "labels": entity_list
                    }, ensure_ascii=False) + "\n")
                    word_list = []
                    entity_list = []
                    count = 0
            else:
                word, tag = line.split("\t")
                word_list.append(word)
                if tag.startswith("B"):
                    entity_list.append([count, count + 1, tag[2:]])
                elif tag.startswith("I"):
                    entity_list[-1][1] += 1
                count += 1


def json2conll():
    pass


if __name__ == "__main__":
    conll_path = "data/msra/conll"
    json_path = "data/msra/json"
    datasets = ["train", "dev"]
    for dataset in datasets:
        conll_file = os.path.join(conll_path, f"{dataset}.txt")
        json_file = os.path.join(json_path, f"{dataset}.json")
        conll2json(conll_file, json_file)
