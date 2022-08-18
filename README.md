# Script for creating attention check videos

This repository contains scripts for creating attention check videos used in [GENEA Challenge 2022](https://genea-workshop.github.io/2022/challenge). Please refer the paper [here](https://youngwoo-yoon.github.io/GENEAchallenge2022/) for the details of the attention checks.

## Requirements

* [FFMpeg](https://www.ffmpeg.org/) 4.4.x
* [MaryTTS](http://mary.dfki.de/) 5.2

## Usage

1. Prepare audio files. We used [MaryTTS](http://mary.dfki.de/) to synthesize attention audios.
```bash
$ docker run -it -p 59125:59125 synesthesiam/marytts:5.2 --voice cmu-rms-hsmm
$ python create_attention_audios.py 
```

2. Create attention check videos. There are three different ways of creating attention check videos according to the user study configurations: 1) text overlay for parallel comparisons, 2) text overlay for pairwise comparisons, 3) audio overlay for pairwise comparisons.
```bash
$ python create_attention_videos.py
```
