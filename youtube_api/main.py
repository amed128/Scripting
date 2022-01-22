import os

from yt_stats import Yt_stats

YT_API_KEY = os.environ['YT_API_KEY']
YT_CHANNEL_ID = 'UCkXGyz3NGxzCYqJv5I4mEkQ'

yt = Yt_stats(YT_API_KEY, YT_CHANNEL_ID)

# GET A YOUTUBE CHANNEL STATS 
# yt.get_channel_stats()

# DUMP TO A JSON FILE
# yt.dump_channel_stats()

# GET CHANNEL VIDEOS
yt.get_channel_videos()
