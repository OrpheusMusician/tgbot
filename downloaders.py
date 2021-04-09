import os
from pytube import YouTube

path = os.path.join(os.getcwd(), 'youtube_vids')
def youtube_downloader(link : str):
	global path

	print('Youtube Downloading!!')

	url = YouTube(link)
	name = url.title + '.mp4'
	name = name.replace('\\', '').replace('/', '').replace('"', '')
	name = name.replace('?', '').replace('*', '').replace(':', '')
	name = name.replace('<', '').replace('>', '').replace('|', '')

	print(name)

	video = url.streams.filter(progressive = True).desc().first()
	video.download(path)

	return name

def tiktok_downloader(link : str):
	global path
	pass