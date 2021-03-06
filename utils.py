import subprocess
from glob import glob
import os


def create_timelapse_video():
    filenames = []
    frames_per_second = 30
    codec_version = 264

    # years = glob('../../Downloads/Camera app/*')
    # for year in years:
    #     for months in glob(f'{year}/*'):
    #         for day in glob(f'{months}/*'):
    #             for photo in glob(f'{day}/*')[::5]:
    #                 hour = photo.split('_')[-1][0:2]
    #                 if 5 < int(hour) < 17:
    #                     filenames.append(photo)

    years = glob('../../Downloads/Camera app/2020/')
    for year in years:
        for months in glob(f'{year}/*'):
            for day in glob(f'{months}/*'):
                for photo in glob(f'{day}/*')[::5]:
                    hour = photo.split('_')[-1][0:2]
                    if 5 < int(hour) < 17:
                        filenames.append(photo)

    path = os.path.abspath("").replace("\\", "/")
    duration = 0.05

    with open("ffmpeg_input.txt", "wb") as outfile:
        for filename in filenames:
            outfile.write(f"file '{path}/{filename}'\n".encode())
            outfile.write(f"duration {duration}\n".encode())

    command_line = f"ffmpeg -r {frames_per_second} -f concat -safe 0 -i ffmpeg_input.txt -c:v libx{codec_version} -pix_fmt yuv420p {path}\\timelapse_video.mp4"
    print(command_line)
    pipe = subprocess.Popen(command_line, shell=True, stdout=subprocess.PIPE).stdout
    output = pipe.read().decode()
    pipe.close()
    os.remove('./ffmpeg_input.txt')


def add_watermark():
    command_line = f'ffmpeg -i timelapse_video.mp4 -i logo.gif -filter_complex "overlay=W-w-5:H-h-5" -c:a copy watermarked_video.mp4'

    pipe = subprocess.Popen(command_line, shell=True, stdout=subprocess.PIPE).stdout
    output = pipe.read().decode()
    pipe.close()
