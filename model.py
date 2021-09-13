from random import sample


class Music(object):
    def __init__(self, title: str, duration: str, is_favorite: str):
        self.title = title
        self.duration = duration
        self.is_favorite = is_favorite


class Album(object):
    def __init__(self, title: str, release: str, author: str):
        self.title = title
        self.release = release
        self.author = author
        self.music_list = []

    def add_music(self, music: Music):
        self.music_list.append(music)


def register_album(albums: list, inputs: dict) -> None:
    """
    Registra quantos albuns o usuário desejar e suas respectivas músicas.
    """
    new_album = Album(inputs['title'], inputs['release'], inputs['author'])
    albums.append(new_album)

    register_music_again = True

    while register_music_again:
        print("\nInsira as informações da música")
        music_title = input("Título: ")
        music_duration = input("Duração (ex: 2:00): ")
        music_is_favorite = input("Favoritar [s/n]: ")
        
        new_music = Music(music_title, music_duration, music_is_favorite)
        new_album.add_music(new_music)

        register_other_music = input("\nRegistrar outra música? [s/n]: ")
        register_other_music.lower()
        
        if register_other_music == 's':
            continue

        elif register_other_music == 'n':
            register_music_again = False


def search_album(albums: list, search_option: int):
    """
    Pesquisa albuns, registrados, pelo título, ano de lançamento ou autor.
    """
    found_albums = []

    if len(albums) > 0:
        if search_option == 1:
            title_search = input("Insira o titulo do álbum >>> ")
            
            for album in albums:
                if title_search == album.title:
                    found_albums.append({
                        'title': album.title,
                        'release': album.release,
                        'author': album.author,
                        'musics': album.music_list
                    })

            if len(found_albums) == 0:
                return False
            
            else:
                return found_albums

        elif search_option == 2:
            release_search = input("Insira o ano de lançamento do álbum >>> ")
            
            for album in albums:
                if release_search == album.release:
                    found_albums.append({
                        'title': album.title,
                        'release': album.release,
                        'author': album.author,
                        'musics': album.music_list
                    })

            if len(found_albums) == 0:
                return False
            
            else:
                return found_albums

        elif search_option == 3:
            author_search = input("Insira o nome do artista/banda >>> ")
            
            for album in albums:
                if author_search == album.author:
                    found_albums.append({
                        'title': album.title,
                        'release': album.release,
                        'author': album.author,
                        'musics': album.music_list
                    })

            if len(found_albums) == 0:
                return False
            
            else:
                return found_albums

        else:
            return -1

    else:
        return 0


def search_music(albums: list, search_option: int):
    """
    Pesquisa músicas, registradas, pelo título ou autor.
    """
    found_musics = []

    if search_option == 1:
        title_search = input("Insira o nome da música >>> ")

        for album in albums:
            if len(album.music_list) > 0:
                for music in album.music_list:
                    if music.title == title_search:
                        found_musics.append({
                            'title': music.title,
                            'duration': music.duration,
                            'is_favorite': music.is_favorite
                        })                   
            else:
                return 0

        if len(found_musics) == 0:
            return False

        else:
            return found_musics

    elif search_option == 2:
        author_search = input("Insira o nome do artista/banda >>> ")

        for album in albums:
            if len(album.music_list) > 0:
                for music in album.music_list:
                    if album.author == author_search:
                        found_musics.append({
                            'title': music.title,
                            'duration': music.duration,
                            'is_favorite': music.is_favorite
                        })
            else:
                return 0

        if len(found_musics) == 0:
            return False    

        else:
            return found_musics

    else:
        return -1


def generate_playlist(albums: list) -> list:
    """
    Gera uma playlist de uma hora de duração com 50% músicas favoritas
    e 50% músicas aleatórias. 
    """
    favorite_musics = []
    not_favorite_musics = []
    added_musics_duration = 0
    counter_duration_playlist = 0    
    playlist = []


    def to_second(duration: str) -> int:
        """
        Converte a duração em string para segundos.
        """
        minute, second = duration.split(":")
        minute = int(minute)
        second = int(second)
        return (minute * 60) + second


    def add_to_playlist(random_music_list: list, playlist_duration: int, limit: int) -> int:
        """
        Adiciona músicas aleatórias à playlist e retorna a duração.
        """
        for music in random_music_list:
            duration_music = to_second(music.duration)

            if (playlist_duration + duration_music) < limit:
                playlist_duration += duration_music
                playlist.append(music)

        return playlist_duration


    def sum_musics_durations(music_list: list) -> int:
        """
        Soma a durações das músicas de uma lista.
        """
        musics_list_duration = 0

        for music in music_list:
            music_duration = to_second(music.duration)
            musics_list_duration += music_duration

        return musics_list_duration


    for album in albums:
        for music in album.music_list:
            if music.is_favorite == 's':
                favorite_musics.append(music)

    for album in albums:
        for music in album.music_list:
            if music.is_favorite == 'n':
                not_favorite_musics.append(music)

    added_musics_duration += sum_musics_durations(favorite_musics)
    added_musics_duration += sum_musics_durations(not_favorite_musics)

    if added_musics_duration <= 3600:
        playlist = favorite_musics + not_favorite_musics
        return playlist

    else:
        random_fav_musics = sample(favorite_musics, len(favorite_musics))
        random_not_fav_musics = sample(not_favorite_musics, len(not_favorite_musics))

        counter_duration_playlist += add_to_playlist(random_fav_musics, counter_duration_playlist, 1800)

        counter_duration_playlist += add_to_playlist(random_not_fav_musics, counter_duration_playlist, 3600)

        return playlist
