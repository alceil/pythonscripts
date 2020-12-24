import instaloader
L=instaloader.Instaloader()
profile = instaloader.Profile.from_username(L.context,'__pythonworld__')
print(profile.biography)