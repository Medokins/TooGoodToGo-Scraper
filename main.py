from tgtg import TgtgClient
from datetime import datetime
import time
import numpy as np
import os
from menu import runMenu
from plyer import notification
from notify import pushbullet_notify

with open(os.path.join("settings", "data.txt")) as f:
    lines = f.readlines()

# search radius in kilometers
user_radius = 5
# search frequency (time before checking again in seconds)
refresh_rate = 10
# bonus option to console when package from non-favourite store is available
notify_all = False
# push notifications to phone using pushbullet
notify_phone = True

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

if len(shops) != 0:
    favourite_stores = runMenu(shops)
else:
    print("No shops in Your area at given radius")
    quit()

# save favourites
if len(favourite_stores) > 1:
    favourite_stores_file = open(os.path.join("settings", "favourite_stores.txt"), 'w')
    for store in favourite_stores:
        favourite_stores_file.write(f"{store}\n")
    favourite_stores_file.close()
else:
    saved_favourites = open(os.path.join("settings", "favourite_stores.txt"), 'r')
    favourite_stores = saved_favourites.read().splitlines()
    saved_favourites.close()

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
                if notify_phone:
                    pushbullet_notify("ToGoodToGo", f"There is a package waiting at {shop}")
                print(f"There are {available_items} packages at {shop} ({now}), be quick!")
                notification.notify(
                    title = "You've got a package to save!",
                    message = f"There is a package avaiable at {shop}",
                    app_icon = "tgtg.ico",
                    timeout = 10,
                )
            elif notify_all:
                print(f"There are {available_items} packages at {shop} ({now})")

    time.sleep(refresh_rate)
