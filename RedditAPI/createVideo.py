from moviepy.editor import *
from random import random
import os
from pydub import AudioSegment

def createClip(audio_id: int):
    print('[VIDEO] starting MoviePy...')
    audio_duration = AudioSegment.from_file(os.path.join('temp', str(audio_id)+".mp3")).duration_seconds
    random_video_start_point = random() * (400 - audio_duration)

    audio_clip = AudioFileClip(os.path.join('temp', str(audio_id)+".mp3"))

    video_clip = VideoFileClip("minecraft.mp4").subclip(
        random_video_start_point,
        random_video_start_point + audio_duration
    )

    post_image = ImageClip(os.path.join('temp', str(audio_id)+".jpg")).set_duration(audio_duration)

    video_clip = CompositeVideoClip([
        video_clip, 
        post_image.set_position("center")
    ])
    video_clip = video_clip.set_audio(audio_clip)

    video_clip.write_videofile("movie.mp4")