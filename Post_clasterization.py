#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import json

# with open('wall_la.json', encoding='utf-8') as json_file:
#     data = json.load(json_file)

def get_important_posts_id(data):

    clear_data = []
    for i in range(len(data)):
        if data[i]['text'] != '':
            clear_data.append(data[i])

    texts = []
    ids = []
    for i in range(len(clear_data)):
        texts.append((clear_data[i]['text']))
        ids.append((clear_data[i]['id']))

    texts_df = pd.DataFrame(texts)

    id_df = pd.DataFrame(ids)

    posts_df = pd.concat([texts_df, id_df], ignore_index=True, axis=1)
    posts_df['claster'] = 0

    posts_df[0] = posts_df[0].str.lower()

    keywords = ['внимание','помогите', 'репост']

    for index, row in posts_df.iterrows():
        for word in keywords:
            if word in row[0]:
                posts_df.at[index, 'claster'] = 1

    for i, row in posts_df.iterrows():
        if row['claster'] == 0:
             posts_df = posts_df.drop([i])


    posts_df = posts_df.drop(columns={'claster',0})

    posts_df = posts_df.rename(columns={1: "id"})

    output = posts_df.to_dict()
    output = output['id']

    output = output.values()

    return list(output)


