"""Data preparation/preprocessing."""

import os 
from ast import literal_eval

import pandas as pd 
# from sklearn.feature_extraction

# NOTE: You may override this if you want :)
DEFAULT_DATA_PATH = os.path.abspath(
    os.path.join(__file__, '..', '..', '..', 'data')
)


def quote_str_to_list(txt):
    try:
        return literal_eval(txt)
    except Exception:
        return ['ERROR PARSING QUOTES']


def load_dfs(which='train', path_data=DEFAULT_DATA_PATH):
    """Loads [post, thread] dfs for one subset (`which`).
    
    Parameters
    ----------
    which : {'train', 'public', 'private'}
        One of the datasets. Only the train one is marked.
    path_data : str
        Which path to use as the base data path.
    """
    
    p_post = os.path.join(path_data, which, 'post.csv')
    p_thread = os.path.join(path_data, which, 'thread.csv')

    post = pd.read_csv(p_post, header=0, encoding='utf-8')
    thread = pd.read_csv(p_thread, header=0, encoding='utf-8')

    # clean up `post` df with proper quotes
    post['quotes'] = post['quotes'].apply(quote_str_to_list)
    post['text'] = post['text'].astype(str)

    return post, thread


def load_label_map(path_data=DEFAULT_DATA_PATH):
    """Loads the label mapping from type to index.
    
    Parameters
    ----------
    path_data : str
        Which path to use as the base data path.
    """

    pt = os.path.join(path_data, 'label_map.csv')
    label_map = pd.read_csv(pt, header=0, encoding='utf-8')
    label_map = label_map.set_index('type_name')['type_id']
    return label_map
