import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

# Target Group Chat ID (e.g. -100xxxxxxxxxx)
GROUP_CHAT_ID = int(os.getenv("GROUP_CHAT_ID", "0")) if os.getenv("GROUP_CHAT_ID") else None

# Admin Private Chat ID (fallback if bot is not in group yet)
ADMIN_ID = int(os.getenv("ADMIN_ID", "467567653")) if os.getenv("ADMIN_ID", "467567653") else None

# Topic ID (Forum thread)
TOPIC_ID = int(os.getenv("TOPIC_ID", "0")) if os.getenv("TOPIC_ID") else None

# Target Region and Group
TARGET_REGION = os.getenv("TARGET_REGION", "kyiv-region").strip()
TARGET_GROUP = os.getenv("TARGET_GROUP", "GPV5.1").strip()
LOCATION_NAME = os.getenv("LOCATION_NAME", "с. Гора, вул. Басейна, 20").strip()

# Polling Interval
CHECK_INTERVAL_SECONDS = int(os.getenv("CHECK_INTERVAL_SECONDS", "600"))

# Visual Options
SEND_IMAGE_WITH_ALERT = os.getenv("SEND_IMAGE_WITH_ALERT", "true").lower() in ("true", "1", "yes")

# Database Path
DB_PATH = str(BASE_DIR / os.getenv("DB_PATH", "dtek_bot.db"))

# Data URLs
DATA_URL = f"https://raw.githubusercontent.com/Baskerville42/outage-data-ua/main/data/{TARGET_REGION}.json"
# Group file mapping: GPV5.1 -> gpv-5-1.png
group_num = TARGET_GROUP.replace("GPV", "").replace(".", "-").lower()
IMAGE_URL = f"https://raw.githubusercontent.com/Baskerville42/outage-data-ua/main/images/{TARGET_REGION}/gpv-{group_num}.png"
