from project.song import Song


class Album:

    def __init__(self, name, *songs):
        self.name = name
        self.songs = [*songs]
        self.published = False

    def add_song(self, song_ojb: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song_ojb.single:
            return f"Cannot add {song_ojb.name}. It's a single"
        if song_ojb in self.songs:
            return "Song is already in the album."
        self.songs.append(song_ojb)
        return f"Song {song_ojb.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."
        if song_name not in [sng.name for sng in self.songs]:
            return "Song is not in the album."
        [self.songs.remove(sng) for sng in self.songs if sng.name == song_name]
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        list_songs = '\n'.join(f"== {mp3.get_info()}" for mp3 in self.songs)
        return f"Album {self.name}\n{list_songs}"
