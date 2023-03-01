class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album_obj):
        if album_obj not in self.albums:
            self.albums.append(album_obj)
            return f"Band {self.name} has added their newest album {album_obj.name}."

        return f"Band {self.name} already has {album_obj.name} in their library."

    def remove_album(self, album_name):
        try:
            album = next(filter(lambda a: a.name == album_name, self.albums))

            if album.published:
                return "Album has been published. It cannot be removed."

            self.albums.remove(album)
            return f"Album {album_name} has been removed."

        except StopIteration:
            return f"Album {album_name} is not found."

    def details(self):
        album = '\n'.join(a.details() for a in self.albums)
        message = f"Band {self.name}\n{album}"

        return message
