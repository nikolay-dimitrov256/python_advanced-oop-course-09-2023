from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < 4:
                self.photos[index].append(label)
                return f'{label} photo added successfully on page {index + 1} slot {len(page)}'

        return 'No more free slots'

    def display(self):
        separator = '-' * 11
        result = [separator]
        for page in self.photos:
            result.append(' '.join(['[]' for item in page]))
            result.append(separator)

        return '\n'.join(result)


album = PhotoAlbum(3)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
