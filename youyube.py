from googleapiclient.discovery import build

API_KEY = 'AIzaSyBUifBNejneMKD3DlpqNl4E--HDITZUQRQ'

def fetch_youtube_videos(query, max_results=5):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    print(response)

    videos = []
    for item in response.get('items', []):
        video_title = item['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        videos.append({'title': video_title, 'url': video_url})
    
    return videos


topic = "loli selling icecream"  
videos = fetch_youtube_videos(topic)

print("Recommended Videos:")
for idx, video in enumerate(videos, start=1):
    print(f"{idx}. {video['title']}: {video['url']}")