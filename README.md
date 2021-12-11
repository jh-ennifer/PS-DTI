# PS-DTI
Esse projeto contém os arquivos que respondem ao projeto proposto para o PS da DTI.

A aplicação permite que o usário salve álbuns de música, informando o artista e as músicas, e para as músicas é necessário que adicione também a duração e se é favorita ou não.
O código permite também:
- Buscar um determinado álbum por título, ano de lançamento, ou artista;
- Buscar uma determinada música por álbum ou artista;
- Gerar uma playlist em que pelo menos 50% das músicas são favoritas do usuário.

Além disso a aplicação foi desenvolvida utilizando a arquitetura [MVC](https://www.lewagon.com/pt-BR/blog/o-que-e-padrao-mvc).
### Linguagem utilizada
<ul>
    <li>
        <a href="https://docs.python.org/pt-br/3/tutorial/">
            <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
        </a>
    </li>
</ul>

### Requisitos:
📍 Para rodar a aplicação é necessário primeiro ter Python instaldo na máquina.
#### Windows
[Dowload Python](https://www.python.org/downloads/)
#### Linux
- Primeiro verifique se já não está instalado:
```bash
    $ which Python
```
```bash
    $ which Python3
```
- Caso não tenha é possível instalar utilizando o comando:
```bash
    $ sudo apt-get install python3
 ```
 📍 Após a instalação é necessário estar dentro de um diretório que contenha os arquivos denominados: 
 - view.py
 - model.py
 - controler.py
 
 📍 Dentro do diretório indicado basta digitar o comando abaixo no terminal e utilizar a aplicação. O comando é o mesmo tanto para Windows quanto para Linux
 ```bash
     $ python3 view.py
 ```
