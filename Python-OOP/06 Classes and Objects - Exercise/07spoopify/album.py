class Album:

    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = [*songs]

    def add_song(self, song_obj):
        if self.published:
            return "Cannot add songs. Album is published."

        if song_obj.single:
            return f"Cannot add {song_obj.name}. It's a single"

        if song_obj in self.songs:
            return "Song is already in the album."

        self.songs.append(song_obj)
        return f"Song {song_obj.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."
        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
            self.songs.remove(song)
            return f"Removed song {song_name} from album {self.name}."
        except StopIteration:
            return "Song is not in the album."

    def details(self):
        songs = '\n'.join(f"== {s.get_info()}" for s in self.songs)
        message = f"Album {self.name}\n{songs}"
        return message

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."
