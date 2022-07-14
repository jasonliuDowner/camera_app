import subprocess

command_line = f'ffmpeg -i test.mp4 -i logo.gif -filter_complex "overlay=W-w-5:H-h-5" -c:a copy watermarked_video.mp4'

# command_line = f"ffmpeg -i timelapse_video.mp4 -i logo.png -filter_complex \
# '[0:v][1:v]overlay=15:10[outv]' -map [outv] -map [0:a] \
# -c:a copy -c:v libx264 -crf 22 -preset veryfast watermarked_video.mp4"

pipe = subprocess.Popen(command_line, shell=True, stdout=subprocess.PIPE).stdout
output = pipe.read().decode()
pipe.close()
