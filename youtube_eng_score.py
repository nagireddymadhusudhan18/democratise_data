import pandas as pd
import configuration
from googleapiclient.discovery import build
import numpy as np

config=configuration

API_KEY = config.API_KEY

country=config.COUNTRY_SLICE
country_list=country.split(',')
print("The engagement score will be calculated for these list of country's =>",country_list)

youtube = build('youtube', 'v3', developerKey=API_KEY)
 
# read by default 1st sheet of an excel file
dataframe_keywords = pd.read_excel('/Users/madhusudhan/desktop/youtube/keywords.xlsx',engine='openpyxl')
 
keywords=(dataframe_keywords.iloc[:, 0])
keywords_random=np.random.choice(keywords, 100, replace=False)
keyword=""

for i in keywords_random:
    keyword=keyword+i+"|"
print("\nAnd for the below 100 random list of keyword's\n\n",keyword)
# Search for videos related to the keyword.

engagement_score_list=[]
for country_ in country_list:
    search_response = youtube.search().list(
        q=keyword,
        type='video',
        part='id',
        regionCode=country_,
        maxResults=100
    ).execute()

    # Calculate the engagement score based on the number of views, likes, and comments.
    total_engagement = 0
    for search_result in search_response.get('items', []):
        video_id = search_result['id']['videoId']
        video_response = youtube.videos().list(
            id=video_id,
            part='statistics'
        ).execute()
        # Get the statistics for the video.
        statistics = video_response['items'][0]['statistics']
        # Calculate the engagement score (you can define your own formula).
        views = int(statistics['viewCount'])
        likes = int(statistics.get('likeCount', 0))
        comments = int(statistics.get('commentCount', 0))
        engagement_score = views + likes + comments
        total_engagement += engagement_score
    engagement_score_list.append(total_engagement)  
ouput_dataframe = pd.DataFrame(list(zip(country_list, engagement_score_list)), columns =['Country', 'Engagement Score']) 
print("\n\n",ouput_dataframe.to_markdown(index=False))


