import os

API_ID = API_ID = 29226750

API_HASH = os.environ.get("API_HASH", "e2772ee6aba52f15e72ac9684c38f54c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7279986102:AAHbVV6DaE0z9tDgdFdmbMc04Mt8O_6IGR8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7024606962))

LOG = -1002239498714

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7024606962").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


