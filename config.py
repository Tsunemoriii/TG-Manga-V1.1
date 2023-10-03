import os
import json

env_file = "env.json"
if os.path.exists(env_file):
    with open(env_file) as f:
        env_vars = json.loads(f.read())
else:
    env_vars = dict(os.environ)

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)

REQ_CHANNEL = "https://t.me/+UYVBj-9UFzYyZDQ9"        # channel link for requests
REQ_CHANNEL_ID = -1001912478564     # channel id
FORCE_CHANNEL = "https://t.me/Sonic_Otakus"      # channel link for force sub
FORCE_CHANNEL_ID = -1001514116490   # channel id

DB_URL = "mongodb+srv://utahakane003:utahakane003@cluster0.xyoubmt.mongodb.net/?retryWrites=true&w=majority"     # database url
DB_NAME = "MangaReqDB"    # database name
