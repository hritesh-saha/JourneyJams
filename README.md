![github](https://img.shields.io/badge/GitHub-000000.svg?style=for-the-badge&logo=GitHub&logoColor=white)
![markdown](https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white)

# JourneyJams

**JourneyJams** is a simple tool to download YouTube videos as `.webm` audio files, designed to provide you with a seamless way to enjoy music or podcasts during road trips. With just a few steps, you can convert and save your favorite YouTube videos as audio files, perfect for offline listening during your travels.

## Features
- Download YouTube videos as `.webm` audio files for offline listening.
- Search YouTube for videos and pick the one to download directly.
- Lightweight, simple terminal interface with a focused user experience.

## Requirements
- Python 3.6+
- `yt-dlp` library for video downloading.
- `youtubesearchpython` for searching YouTube videos.

## Installation

### Clone the repository:
```bash
git clone https://github.com/hritesh-saha/JourneyJams.git
cd JourneyJams
```

Install the necessary dependencies:
```bash
pip install -r requirements.txt
```

Run the program:
```bash
python downloader.py
```

## Run From Terminal:
To directly run the program, execute the shell script:

```bash
bash Jams.sh
```
## Usage

1. **Enter the video name or keywords** to search for a YouTube video.
   
2. The program will **display the top search results** with video details like the title, duration, and link.

3. **Choose the video** you want to download by entering its corresponding number from the search results.

4. The video will be **downloaded as a `.webm` file** to a directory named `downloads` in the current working directory.

## Docker Image
You can pull the image from Docker Hub:
```bash
docker pull hriteshsaha4/journey-jams:latest
```
Once the image is pulled, run the container using this command:
```bash
docker run -it hriteshsaha4/journey-jams:latest
```
This will start the container and give you an interactive terminal. Once inside the container, run the following command to start the Python downloader script:
```bash
python downloader.py
```
This command will execute the `downloader.py` script inside the container.
<br>
<br>
<p align="center"><a href="https://github.com/hritesh-saha/JourneyJams/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=BSD-3-Clause&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a></p>
