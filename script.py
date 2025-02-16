from pytube import YouTube

def get_video_url(video_url):
    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(progressive=True, file_extension="mp4").first()
        return video.url  # Returns the direct video download link
    except Exception as e:
        return f"Error: {str(e)}"

print("Python script loaded")  # Debugging message
