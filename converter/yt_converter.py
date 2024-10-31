import re
import pytube

youtube_url_pattern = re.compile(r'https://www\.youtube\.com/watch\?v=[a-zA-Z0-9_-]+')

class Converter:
    """
    This module for converting Youtube videos to mp3 (or mp4 in this case)
    """
    def __init__(self, url):
        self.video = pytube.YouTube(url)
        self.name = self.video.title # имя видео
        self.thumbnail = self.video.thumbnail_url # превью видео
        self.stream = '140' # звуковая дорожка
        self.path = 'D:/Programs/VS Code projects/DesktopApps/MyProjects/TgConverter/files' # тестовый репозиторий для видео

    def download(self):
        """Downloading files from Youtube"""
        print(f"Downloading {self.name}...")
        try:
            stream =  self.video.streams.get_by_itag(self.stream)
            return stream.download(output_path=self.path)
        except:
            return "Download was not succsesful, try again later"

    def show_image(self):
        """Returns images (use it on your website)"""
        return self.thumbnail

    @staticmethod
    def finish():
        """Just reminder that your covertion finished"""
        print("Finished!")

    def rename(self, new_name):
        self.name = new_name

if __name__ == '__main__':
    test_video = Converter('https://www.youtube.com/watch?v=4Mw0QJ5Udlw')
    test_video.download()