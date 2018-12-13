import numpy as np
import json

dim = 768
max_len = 128
sep = 8727
test = 967
# with open("./data/birth_place_x.jsonl", "r", encoding='utf-8') as f:
with open("../output.jsonl", "r", encoding='utf-8') as f:
    vec = np.empty([sep + test, dim])
    vec2 = np.empty([sep + test, dim])

    for line_index in range(sep + test):
        bb = json.loads(f.readline())
        # line=bb[line_index]["features"]
        line = bb["features"]

        # tokens_vec=np.empty([max_len,dim])
        tokens_vec = [token["layers"][0]["values"] for token in line]
        tokens_vec = np.array(tokens_vec)
        sen_vec = np.sum(tokens_vec, axis=0) / tokens_vec.shape[0]
        vec[line_index] = sen_vec

        tokens_vec2 = [token["layers"][1]["values"] for token in line]
        tokens_vec2 = np.array(tokens_vec2)
        sen_vec2 = np.sum(tokens_vec2, axis=0) / tokens_vec2.shape[0]
        vec2[line_index] = sen_vec2

    np.save('./data/birth_place_trainx.npy', vec[:sep])
    np.save('./data/birth_place_testx.npy', vec[sep:])

    np.save('./data/birth_place_trainx2.npy', vec2[:sep])
    np.save('./data/birth_place_testx2.npy', vec2[sep:])
