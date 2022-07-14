import subprocess

command_line = f'ffmpeg -i timelapse_video.mp4 -i logo.gif -filter_complex "overlay=W-w-5:H-h-5" -c:a copy watermarked_video.mp4'

pipe = subprocess.Popen(command_line, shell=True, stdout=subprocess.PIPE).stdout
output = pipe.read().decode()
pipe.close()
