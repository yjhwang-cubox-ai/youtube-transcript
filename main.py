from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

video_id = '25Nmnve8hi8&t'

transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko'])

formatter = TextFormatter()

json_formatted = formatter.format_transcript(transcript)

# Now we can write it out to a file.
with open('stock.txt', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)