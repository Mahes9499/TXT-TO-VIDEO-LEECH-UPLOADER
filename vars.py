

from os import environ

API_ID = int(environ.get("API_ID", "22009162"))
API_HASH = environ.get("API_HASH", "d361b273d231fc05d29c6cf9824b263e")
BOT_TOKEN = environ.get("BOT_TOKEN", "8230832807:AAEzqycDF54z-rDhrWx5_AYsd0JgrheooBY")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "sabka baap")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/+_YpIGPntYJQ5NjJl")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "1793622440"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





