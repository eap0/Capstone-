import os
project_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(project_dir,'data')

from .clean_data import clean_data
