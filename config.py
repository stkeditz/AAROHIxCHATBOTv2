from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 27353035))
API_HASH = getenv("API_HASH", "cf2a75861140ceb746c7796e07cbde9e")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "5465943450"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "LOVE_FEELINGS_WILL1")
UPDATE_CHNL = getenv("UPDATE_CHNL", "alonegroup121")
OWNER_USERNAME = getenv("OWNER_USERNAME", "dil_sagar_121")

