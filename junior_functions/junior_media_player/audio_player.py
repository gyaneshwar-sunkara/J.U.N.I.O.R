import vlc
from mutagen.mp3 import MP3
from junior_functions.junior_fundamental_ops.media import file_details

def mp3_meta(path):
    try:
        audio = MP3(path)
        title = audio['TIT2'].text[0].split(' - ')[0]
        lead_performer = audio['TPE1'].text[0]
        album = audio['TALB'].text[0]
        return title, lead_performer, album
    except:
        return file_details(path)
"""
class audio_player:
    player = vlc.MediaPlayer(path)
    
    def play():
        if player.is_playing()
        player.play()

    def volume(command):     # verified
        player.is_playing()
        vol = player.audio_get_volume()
        player.audio_set_volume(vol + 10)
        player.audio_get_mute()
        player.audio_set_mute()
        player.get_time()
        player.get_length()
        player.pause()
        player.play()
        player.stop()
        player.release()

    def play_pause_stop(command):

    def video_player(path):
    def volume():


    def play_pause_stop(command):
    adjust_for_amb
"""
