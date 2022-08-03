import pickle
def load_pickle(path):
    with open(path,'rb') as handle:
        my_dict = pickle.load(handle)
    return my_dict

def save_pickle(path, my_dict):
    with open(path,'wb') as handle:
        pickle.dump(my_dict, handle)