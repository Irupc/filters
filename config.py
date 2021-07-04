
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1474138123:AAFvvAz62r-Rc7B2add1Y6fwwgxJGUL_pa4")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", 1813445))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "8f45dabd56be5ad1619df16af9eca560")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQBTyd-uQCitlEo9eSDmVh9dcUa1xWaTrWFfWs5QaThn-eblSYOO8IVaS9vygRtOBVkKIjrVbqSmPrNr5IZpvOL9qZJwA-Rc0FVMs5FtpDX5gVnqmJwC7dDgxrHqz1WkEOwiaEfoVyhVXWa7lxEDAoTEKFoUA3nrXADxTmxbI35VBmQktpG5qiDvw5fh0rG1YEFlEpwn55LvgM7UzC6AUG0peYk1BxFuQlmPnga8wsiLpBgq_jhB1FUxUC53gmhqUNfuc8fqvF0aoZRG2Y4wboi8WUj4gm9-fWf4Deu7hdbE4_JOQszDHEp6nkzXsBnFcliW0RY6-sVrs9OSr8Hf7LIGU2K9uQA")

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Gamy_Gamin:Gamy_Gamin@cluster0.89qnu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

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
