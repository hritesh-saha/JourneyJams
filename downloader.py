import os
import yt_dlp
from youtubesearchpython import VideosSearch

def search_videos(query, max_result=10):
    videos_search = VideosSearch(query, limit=max_result)
    try:
        result = videos_search.result()
        #print("Raw Results:", result)  # Debugging purpose
        return result.get("result", [])
    except Exception as e:
        print(f"Error during search: {e}")
        return []
    
def download_audio(video_url, save_path):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'quiet': False  # Show progress
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"Error during download: {e}")


def main():
    search_query = input("Enter YouTube video name to download as Audio: ")
    results = search_videos(search_query)

    if not results:
        print("No results found!\n")
        return

    print("Search Results:\n")
    header = f"| {'S.no'}. | {'title':<70} - {'duration':<5} | {'link':<40} |"
    print("-"*len(header))
    for i, result in enumerate(results, start=1):
        title = result.get("title", "Unknown Title")
        title = title.split(",")[0].split(".")[0].strip()
        duration = result.get("duration", "Unknown Duration")
        link = result.get("link", "Unknown Link")
        print(f"| {i:<4}. | {title:<70} - {duration:<5} | {link:<40} |")
    print("-"*len(header))    
    try:
        choice = int(input("\nEnter the number of the video you want to download: "))
        if (1 <= choice <= len(results)):
            selected_video=results[choice-1]
            save_path=os.path.join(os.getcwd(),"downloads")
            os.makedirs(save_path,exist_ok=True)
            download_audio(selected_video['link'], save_path)
        else:
            print("Invalid choice. Please choose a valid number.")
            
    except Exception as e:
        print(f"Error during choice: {e}")

if __name__ == "__main__":
    main()
