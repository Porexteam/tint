import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "10360349"))
API_HASH = getenv("API_HASH", "f3c8cbf70588eef17c12e063794b69c3")
BOT_TOKEN = getenv("BOT_TOKEN", "5605743334:AAGGnd1bkehkD254kQLdx6nDzcYZGjdzyt4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AQA0Mq88xspTlGvHVJtMC7PvrJ60ij9s_qLuXUJGKbKkJBfUn4JbYwNtlgIcElCDa0eItGyfEzJr7m7sd-HPQDCGe15oXRXOWWvBbG73OoxxcYBlbLzIFDHtkki2whL3_H6lFGSWyK1el9hF6vafafWVoMDqVQO6j0mYfRpYZ-_a9A7v-G-GnCRl0Ue7Dw5-Ub3-UmrgpBuVp2iHDxeNII6J62D4M2zxYAbSTzyYs20jaHD-VBLXS0QsQic81At8UbuHGYbVKylyo6_mZOpjbycumUiJCnRDqu8m2x_dH7aNfXpgOE7cNFSDs2h9mnXj29C-ceXrQsn5GLp1yDUBS7bjAAAAAVgjReMA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5707831441").split()))
