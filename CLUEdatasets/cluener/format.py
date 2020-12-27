# -*- coding: utf-8 -*-
# @Author  : catnlp
# @FileName: format.py
# @Time    : 2020/7/4 18:14

import json


def get_format(source, target):

    with open(source, 'r', encoding='utf-8') as sf, \
            open(target, 'w', encoding='utf-8') as tf:
        for line in sf:
            line = line.rstrip()
            if not line:
                continue
            line = json.loads(line)
            text = line['text']
            label_format = []
            labels = line['label']
            for label in labels:
                entities = labels[label]
                for entity in entities:
                    poss = entities[entity]
                    for pos in poss:
                        label_format.append([pos[0], pos[1] + 1, label])

            label_format = sorted(label_format, key=lambda i: i[0])
            result = {
                'text': text,
                'label': label_format
            }
            tf.write(json.dumps(result, ensure_ascii=False))
            tf.write("\n")


if __name__ == "__main__":
    source = "dev.json"
    target = "dev_format.json"
    get_format(source, target)
