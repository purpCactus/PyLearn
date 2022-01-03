from moviepy import editor

video = editor.VideoFileClip('Rage Against.mp4')
video.audio.write_audiofile('Rage Against.mp3')
