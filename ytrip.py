#!/bin/python3

## Requirements: Install ffmpeg package (sudo apt install ffmpeg) and install yt-dlp pip package (pip install yt_dlp) 

import yt_dlp, argparse, textwrap

def download_audio(yt_url, bitrate, output):
    ydl_opts = {
        'outtmpl': output,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': bitrate,
        
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])

def main(yt_url, bitrate, output):
    print("\nJeroen's Youtube Ripper\n")
    download_audio(yt_url, bitrate, output)

if __name__ == '__main__':  # Start, create variables from arguments and run main

    parser = argparse.ArgumentParser(description="How to use Jeroen's Youtube ripper",formatter_class=argparse.RawDescriptionHelpFormatter,epilog=textwrap.dedent('''Examples:\n
    ## Rip audio from specified URL and write mp3 file generated from video title to ~/Music/ in 128 kbps bitrate:\n
    python3 ytrip.py -u https://www.youtube.com/watch?v=8OAPLk20epo -b 128 -o ~/Music/ \n
    ## Rip audio from specified URL and write to ~/Music/Beethoven - 9th symphony.mp3 in 192 kbps bitrate:\n
    python3 ytrip.py -u https://www.youtube.com/watch?v=8OAPLk20epo -o '~/Music/Beethoven - 9th symphony.mp3' 
    '''))
    parser.add_argument('-b', '--bitrate', type=int, default=192, help='bitrate of generated mp3 file (default = 192)')
    parser.add_argument('-u', '--url', help='Youtube URL')
    parser.add_argument('-o', '--output', help='Specify filename or generate filename by only specifying directory')
    args = parser.parse_args()

    if args.url == None:
        print("No URL specified. Run 'python3 ytrip.py -h' for help")
        quit()
    bitrate = str(args.bitrate)
    if args.output == None:
        print("No output specified. Run 'python3 ytrip.py -h' for help")
        quit()
    elif args.output.endswith('.mp3'):
        output = args.output.strip(".mp3")
    else:
        output = args.output+'/%(title)s'
    main(args.url, bitrate, output)
