import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = "28542531"
# -------------------------------------------------------------
API_HASH = "9f4889cd2437d72ede20428c07a909be"

BOT_TOKEN = getenv("BOT_TOKEN", "5663640542:AAG5QT3aXxyTlD7jId6okRvEpvoQ91DNqm4")
OWNER_USERNAME = getenv("OWNER_USERNAME", "shaeep43")
BOT_USERNAME = getenv("BOT_USERNAME", "Iro_x_music_bot")
BOT_NAME = getenv("BOT_NAME", "iro ꭙ ᴍᴜꜱɪᴄ")
ASSUSERNAME = getenv("ASSUSERNAME", "PIKKU_DP_WORLD")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://pikachu:randi@cluster0.tndvlel.mongodb.net/?retryWrites=true&w=majority")
#MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://String:iro@string.bfl5lcm.mongodb.net/?retryWrites=true&w=majority&appName=String")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001772857132"))
OWNER_ID = int(getenv("OWNER_ID", 6045293810))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HRKU-AAWXXwOoG2StptJ5_yDFO3-n-IQSrRQoikIFR24nxs3g_____wpd9s0tZzoJ")
#HEROKU_API_KEY = getenv("HRKU-1e980a6d-beb2-4fd7-8f13-7921cef9c27b")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/IR-O/pvt",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-YukkiMusic-08-30")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/iro_bot_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/iro_x_support")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
#STRING1 = getenv("STRING_SESSION", "BQDEFKsAgiokuBQL9u39ZqrvaCaQO3LKSggOy37pSrHZT5zVqgjq142NHplMweczk3QX9d7zyZtJRnkbAf68dI1UwZL6Zt8E-easqg2itztgxj1x9va6IZsqNUh9L6g8vo56oMeRC9zQ2B3ZIKQUAr-SQmbwKy4yaoZNV2dLrOa0CUC_F1gDWEcLdk-hdoUsQIfEeKVpVKJz8Qgj9YEd8YNgHjbt-TFE5WGcLhV12kjkCw8PCsx1sbALnoNk22TVrhc8HJQRuB5gdJxJeer8a1B4JBrSso6B84LPI0SjAHgu-xCiDI8Mi3h4YhM4c5EN-ajrSJZczpCYkp633E6eYan31cr2FgAAAAHmorCNAA")
STRING1 = getenv("STRING_SESSION", "BQE07uIALglWIh3JmCC_u9DcOwYwQSRE5oaeMS0YS4NEfWNYCzag3RujpsM8mOF_27mluMFiZt2QqzzEjlWt3l9unGwCGExrRimbB8FY9qLy3l4yxXdzyYmFh2t3Mj6S3ZYiwrh2fopCMLJdVG4OfcSqURmL7vJU3jJaPSYQM6MDqKE7rctTLy-5qsIsEnZFrb2VXLdKi_ZfiEW2xLL8aDXLGM_xdRgDtkT1vHlFmhUjIuRz-4GCvaChFVq9v0lVzaBHL5XsxFBIaWna5m8bFf_rS4brbNqKsW0qGi_xm0cc4wwi5eMfbKK2LxaKYnHowdMsV4RjT6xNrQo9pEOXsKhDho9t7QAAAAGxC4UDAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/7c8a61882e4d9f5cf8f58.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/00360393a15daf7fc4e9d.jpg")
PLAYLIST_IMG_URL = "https://telegra.ph/file/79547e01862628bb85df0.jpg"
STATS_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/79547e01862628bb85df0.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
        
