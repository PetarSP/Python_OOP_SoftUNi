from unittest import result

from spoopify.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, new_album: Album):
        for album in self.albums:
            if album.name == new_album.name:
                return f"Band {self.name} already has {new_album.name} in their library."
        self.albums.append(new_album)
        return f"Band {self.name} has added their newest album {new_album.name}."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.published:
                return f"Album has been published. It cannot be removed."
        for album in self.albums:
            if album.name == album_name:
                self.albums.remove(album_name)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}"
        for album in self.albums:
            result += "\n"
            result += f"{album.details()}"
        return result
