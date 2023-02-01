from project.album import Album
from project.song import Song


class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album_obj: Album):
        if album_obj not in self.albums:
            self.albums.append(album_obj)
            return f"Band {self.name} has added their newest album {album_obj.name}."
        return f"Band {self.name} already has {album_obj.name} in their library."

    def remove_album(self, album_name):
        if album_name not in [album.name for album in self.albums]:
            return f"Album {album_name} is not found."
        if True in [album.published for album in self.albums if album.name == album_name]:
            return f"Album has been published. It cannot be removed."
        [self.albums.remove(album) for album in self.albums if album.name == album_name]
        return f"Album {album_name} has been removed."

    def details(self):
        details_albums = '\n'.join(album.details() for album in self.albums)
        return f"Band {self.name}\n{details_albums}"

# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
