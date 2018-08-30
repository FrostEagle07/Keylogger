# Keylogger
A local keylogger + screenshots taker written in python 

Records all keylogs in Keylogs/Keylogs.txt and take screenshots every 10 seconds if the user is currently typing something, then check if the day has changed and if yes compress all the information recorded in INFOS/.."the current day".. .zip and does this for every day.

How to install all the dependencies needed for the running the .py file:
- sudo pip install -r Requirements.txt

How to make the app running at startup:
- choose whatever folder you want and put the keylogger in it
- Then create a shortcut of the executable and place it in your standard os startup folder
(other solutions might be better to think of, such as running the program as a deamon or add it in the startup by the registry)
