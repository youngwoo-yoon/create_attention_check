"""
create attention check videos of all videos in 'short_videos' folder
`corrupt_mp4` script is tested on ffmpeg 4.4.x (not working on ffmpeg 3.4.x)
"""

import glob
import os
import random
from pathlib import Path

import ffmpeg

all_files = glob.glob('short_videos/upper_body/**/*_cut.mp4', recursive=True)
attn_number = list(range(5, 96))
exclude_list = [13, 14, 15, 16, 17, 18, 19, 30, 40, 50, 60, 70, 80, 90]
attn_number = [e for e in attn_number if e not in exclude_list]

for file in sorted(all_files, reverse=True):
    print(file)
    output_path = file.replace('short_videos/', 'short_videos_attention_check/')
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    input_duration = float(ffmpeg.probe(str(file))['streams'][0]['duration'])

    # video overlay
    overlay_duration = 5.0
    start_time = random.uniform(2.0, max(2.0, input_duration - overlay_duration))
    end_time = start_time + overlay_duration

    for test_type in ['slider', 'pairwise']:
        if test_type == 'slider':
            if '_muted_' not in file:
                continue
            selected_attn_number = random.choice(attn_number)
            text1 = f'Attention! You must rate'
            text2 = f'this video as {selected_attn_number}'
            text_out_path = output_path.replace('.mp4', f'_text_attn_check_{selected_attn_number:02d}.mp4')
        else:
            if '_muted_' in file:
                continue
            text1 = f'Attention! You must report'
            text2 = f'this video as broken'
            text_out_path = output_path.replace('.mp4', f'_text_attn_check_pairwise.mp4')
        cmd = f'python ./scripts/corrupt_mp4.py -i "{file}" -o "{text_out_path}" -t1 "{text1}" -t2 "{text2}" -tr {start_time}:{end_time}'
        print(cmd)
        os.system(cmd)

    # audio overlay
    if '_muted_' not in file:
        for test_type in ['pairwise']:
            if test_type == 'slider':
                selected_attn_number = random.choice(attn_number)
                audio_path = f'short_videos_attention_check/audios/{selected_attn_number:02d}.wav'
                audio_out_path = output_path.replace('.mp4', f'_audio_attn_check_{selected_attn_number:02d}.mp4')
            else:
                audio_path = f'short_videos_attention_check/audios/broken.wav'
                audio_out_path = output_path.replace('.mp4', f'_audio_attn_check_pairwise.mp4')
            overlay_duration = float(ffmpeg.probe(str(audio_path))['streams'][0]['duration'])
            start_time = random.uniform(2.0, max(2.0, input_duration - overlay_duration))
            end_time = start_time + overlay_duration
            cmd = f'python ./scripts/corrupt_mp4.py -i "{file}" -o "{audio_out_path}" -a "{audio_path}" -ar {start_time}:{end_time}'
            print(cmd)
            os.system(cmd)
