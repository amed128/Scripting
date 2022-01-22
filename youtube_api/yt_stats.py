import requests, json


class Yt_stats:

    def __init__(self, api_key, yt_channel_id):
        self.api_key = api_key
        self.yt_channel_id = yt_channel_id
        self.channel_stats = None
        self.channel_videos = None

    def get_channel_stats(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.yt_channel_id}&key={self.api_key}'

        json_url =  requests.get(url)
        data = json.loads(json_url.text)

        try:
            data = data['items'][0]['statistics']
        except:
            data = None

        self.channel_stats = data

        print(data)

    def dump_channel_stats(self):
        if self.channel_stats is None:
            return
        
        file_name = 'dump_channel_stats_2.json'
        with open(file_name, 'w') as f:
            json.dump(self.channel_stats, f, indent=1)

        print("Stats dumped in json file")

    def get_channel_videos(self, limit=None):
        url = f'https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.yt_channel_id}&part=id&order=date'

        if limit is not None and isinstance(limit, int):
            url += "&maxResults" + str(limit)

        print(url)
        
        json_url =  requests.get(url)
        data = json.loads(json_url.text)
