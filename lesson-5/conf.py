import os
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(BASE_PATH, 'storage')

if not os.path.exists(OUT_PATH):
    os.mkdir(OUT_PATH)
