import controller

control = controller.Controller()


def main():
    """
    Responsável pelas interações com o usuário.
    """
    print("\n\
        \r[1] Cadastrar Álbum;\n\
        \r[2] Pesquisar Álbum;\n\
        \r[3] Pesquisar Música;\n\
        \r[4] Gerar Playlist;\n\
        \r[5] Sair.\
    ")

    option = int(input(">>> "))

    while 0 < option <= 5:
        if option == 1:
            register_album_again = True
            
            while register_album_again:
                print("\nInsira os dados do álbum:")
                album_title = input('Título >>> ')
                album_release = input('Lançamento >>> ')
                album_author = input('Autor >>> ')

                control.register_album({
                    'title': album_title,
                    'release': album_release,
                    'author': album_author
                })

                register_other_album = input("\nRegistrar outro álbum? [s/n]: ")
                register_other_album.lower()
                
                if register_other_album == 's':
                    continue

                elif register_other_album == 'n':
                    register_album_again = False
        
        elif option == 2:
            print("\n[1] Pesquisar álbum por título;")
            print("[2] Pesquisar álbum pelo lançamento;")
            print("[3] Pesquisar álbum pelo artista/banda.")

            search_option = int(input(">>> "))

            search_result = control.search_album(search_option)

            if search_result == -1:
                print("\n[!] Opção inválida.")
            
            if search_result == 0:
                print("\n[!] Não há registros.")

            elif search_result == False:
                print("\n[!] Álbum não encontrado.")

            elif type(search_result) == list:
                for album in search_result:
                    print("\n[*] Álbum encontrado.")
                    print("\n+--------- Informações do álbum ----------")
                    print("|")
                    print(f"| Título: {album['title']}")
                    print(f"| Lançamento: {album['release']}")
                    print(f"| Autor: {album['author']}")
                    print("|")
                    for music in album['musics']:
                        print(f"|> {music.title}")
                    print("|")
                    print("+" + "-" * 41)

        elif option == 3:
            print("\n[1] Pesquisar música por título;")
            print("[2] Pesquisar música por artista/banda.")

            search_option = int(input(">>> "))

            search_result = control.search_music(search_option)

            if search_result == -1:
                print("\n[!] Opção inválida.")

            elif search_result == False:
                print("\n[!] Música não encontrada.")

            elif type(search_result) == list:
                for music in search_result:
                    print("\n[*] Música encontrada.")
                    print("\n+--------- Informações da música ----------")
                    print("|")
                    print(f"| Título: {music['title']}")
                    print(f"| Duração: {music['duration']}")
                    if music['is_favorite'] == 's':
                        print(f"| Favorita: Sim")
                    else:
                        print(f"| Favorita: Não")
                    print("|")
                    print("+" + "-" * 41)

        elif option == 4:
            playlist = control.generate_playlist()
            for music in playlist:
                    print("\n+--------- Musica ----------")
                    print("|")
                    print(f"| Título: {music.title}")
                    print(f"| Duração: {music.duration}")
                    if music.is_favorite == 's':
                        print(f"| Favorita: Sim")
                    else:
                        print(f"| Favorita: Não")
                    print("|")
                    print("+" + "-" * 27)
                    
        elif option == 5:
            exit()

        print("\n\
            \r[1] Cadastrar Álbum;\n\
            \r[2] Pesquisar Álbum;\n\
            \r[3] Pesquisar Música;\n\
            \r[4] Gerar Playlist;\n\
            \r[5] Sair.\
        ")

        option = int(input(">>> "))

    else:
        print("\n[!] Esta opção não existe.")


if __name__ == '__main__':
    main()
