# run marrytts: $ docker run -it -p 59125:59125 synesthesiam/marytts:5.2 --voice cmu-rms-hsmm

import requests


for x in range(5, 96):
    result = requests.get(f"http://localhost:59125/process?INPUT_TEXT='Attention You+must+rate+this+video+as+{x}'&INPUT_TYPE=TEXT&OUTPUT_TYPE=AUDIO&AUDIO=WAVE_FILE&LOCALE=en_US").content
    with open(f"short_videos_attention_check/audios/{x:02}.wav", "wb") as f:
        f.write(result)

result = requests.get(f"http://localhost:59125/process?INPUT_TEXT='Attention! You+must+report+this+video+as+broken'&INPUT_TYPE=TEXT&OUTPUT_TYPE=AUDIO&AUDIO=WAVE_FILE&LOCALE=en_US").content
with open(f"short_videos_attention_check/audios/broken.wav", "wb") as f:
    f.write(result)
