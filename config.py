
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1474138123:AAFvvAz62r-Rc7B2add1Y6fwwgxJGUL_pa4")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "3206260"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "fbc8918eed3b68ccfd80283cf53db785")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCEyVB6WRtaUltCBxCI1q5BrV_G-yVfneUUKcyN45jCbY6Kx7xLfObjLpoMSfBTTDfWjBMHU4xBG9yG0JuTKQ78xgpYtRvaMTe5zEgJLkFigmZc7B8rtKy5smpdf_ouCf4it8lgJkFC0GBNHqO4omLhKJLaRzKlHUjyd66TbMcON4BZ9ocnAPh29TGP01j0bW0Qk5HAP-R0B09lKH8A_EUeRpMywYPqw_yRyWkF3HltxdRGh5-BKOWZrBfWJlRCIXcpzhgNWJOORRTERqI6aRX0G9x3jpCKif8Ar50SwRG1I-BRGUDB4ApOaynKrR5xGsObWASm4dTm5Glyz4zxyoXdZS2DfgA")

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Gamy_Gamin:Gamin@cluster0.89qnu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Your database name from mongoDB
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# ID of users that can use the bot commands
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1177233175 1398980025").split())

# Should bot search for document files in channels
DOC_SEARCH = os.environ.get("DOC_SEARCH", "yes").lower()

#Should bot search for Images
PHO_SEARCH = os.environ.get("PHO_SEARCH", "yes").lower()

# Should bot search for video files in channels
VID_SEARCH = os.environ.get("VID_SEARCH", "yes").lower()

# Should bot search for music files in channels
MUSIC_SEARCH = os.environ.get("MUSIC_SEARCH", "no").lower()

#Link of the Channel
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", "")

#Web Site Link
WEB_SITE_URL = os.environ.get("WEB_SITE_URL", "")

#text set when User Request Subtitle
SUB_TEXT = os.environ.get("SUB_TEXT", "𝕊𝕦𝕓𝕥𝕚𝕥𝕝𝕖 ❗️ ")

# Link to File bot url before Array
BOT_URL = os.environ.get("BOT_URL", "https://t.me/irupc_sever_bot?start=")

TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
