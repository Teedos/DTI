import pickle
import json 
def load_pickle(path):
    with open(path,'rb') as handle:
        my_dict = pickle.load(handle)
    return my_dict

def save_pickle(path, my_dict):
    with open(path,'wb') as handle:
        pickle.dump(my_dict, handle)

def load_json_dict(path):
    with open(path) as f:
        my_dict = json.load(f)
    return my_dict