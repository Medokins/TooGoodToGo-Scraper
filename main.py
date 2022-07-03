from tgtg import TgtgClient
from datetime import datetime
import time
import numpy as np
from menu import Menu, runMenu

with open('data.txt') as f:
    lines = f.readlines()

# search radius
user_radius = 1

#[:-1] to not read in new-line character
user_access_token = lines[0][:-1]
user_refresh_token = lines[1][:-1]
user_id = lines[2][:-1]
user_latitude = np.double(lines[3][:-1])
user_longitude = np.double(lines[4][:-1])

client = TgtgClient(access_token = user_access_token,
                    refresh_token = user_refresh_token,
                    user_id = user_id)

items = client.get_items(
        favorites_only = False,
        latitude = user_latitude,
        longitude = user_longitude,
        radius = user_radius
    )

shops = np.unique([item["store"]["store_name"] for item in items])
favourite_stores = runMenu(shops)

while True:
    items = client.get_items(
        favorites_only = False,
        latitude = user_latitude,
        longitude = user_longitude,
        radius = user_radius
    )
    for item in items:
        shop = item["store"]["store_name"]
        available_items = item["items_available"]
        if available_items != 0:
            now = datetime.now()
            if shop in favourite_stores:
                print(f"There are {available_items} packages at {shop} ({now}), be quick!")
                # here will be code to notify You via email
            else:
                print(f"There are {available_items} packages at {shop} ({now})")
        



    time.sleep(10)