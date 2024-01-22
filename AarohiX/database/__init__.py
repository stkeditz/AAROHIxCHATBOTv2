from pymongo import MongoClient

import config

dildb = MongoClient(config.MONGO_URL)
dil = dildb["DilDb"]["Dil"]


from .chats import *
from .users import *
