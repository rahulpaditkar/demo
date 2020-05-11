import hashlib
from difflib import SequenceMatcher


def hash_file(filename1, filename2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(filename1, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)
    with open(filename2, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)
    return h1.hexdigest(), h2.hexdigest()


song1, song2 = hash_file("C:\\Users\\Rahul\\PycharmProjects\\kaam\\first.mp3", "C:\\Users\\Rahul\\PycharmProjects\\kaam\\second.mp3")
print(song1 + "\t" + song2)
print("Matching two audio files:",(SequenceMatcher(None, song1, song2).ratio()) * 100 ,"%")