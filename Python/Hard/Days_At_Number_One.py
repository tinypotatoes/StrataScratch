"""
Days At Number One
https://platform.stratascratch.com/coding/10173-days-at-number-one?code_type=2

Difficulty: Medium

Find the number of days a US track has stayed in the 1st position for both the US and worldwide rankings on the same day. Output the track name and the number of days in the 1st position. Order your output alphabetically by track name.

If the region 'US' appears in dataset, it should be included in the worldwide ranking.

Tables:
(spotify_daily_rankings_2017_us)
position    int
trackname   varchar
artist      varchar
streams     int
url         varchar
date        datetime

(spotify_worldwide_daily_song_ranking)
id           int
position     int
trackname    varchar
artist       varchar
streams      int
url          varchar
date         datetime
region       varchar
"""
# Import your libraries
import pandas as pd

# Start writing code
spotify_daily_rankings_2017_us.head()

df = spotify_daily_rankings_2017_us.merge(spotify_worldwide_daily_song_ranking, on=["trackname", "date"])
result = df.groupby("trackname").size().reset_index(name="days").sort_values("trackname")

