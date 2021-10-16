'''________________________________________________________
    Creator: Luis Müdder | https://github.com/luismudder
   _____________________________________________________'''
# importaçoes
from pytube import YouTube, Playlist
from os import remove, rename, path, walk
from time import sleep

# request da playlist
Request_Playlist = open("__DATA__/data.Playlist", "r")
data_Playlist = Request_Playlist.readlines()
PlaylistUrl = str(data_Playlist[0])
Request_Playlist.close()

# ativando o State
charge_State = open("__DATA__/data.State", "w")
charge_State.write("on")
charge_State.close()

# request da pasta
Request_path = open("__DATA__/data.path", "r")
data_path = Request_path.readlines()
download_path = str(data_path[0])
Request_path.close()

# pasta de download
print(f'download in => {download_path}')

# detalhes do download
def process(chunk, file_handle, bytes_remaining):
	print(bytes_remaining)

# caso exista um audio com o mesmo nome
def music_rename(Dir_file, name, n):
	try:
		rename(Dir_file, f'{download_path}/{name}({n}).mp3')
	except:
		try:
			rename(Dir_file, f'{download_path}/{name}({n+1}).mp3')
		except:
			music_rename(Dir_file, name, n+1)

# função de analise
class App:
	def __init__(self):

		# memórias
		self.link_v1 = '1'
		self.link_v2 = '2'
		self.phase = 1

		# função principal
		self.MainFunction()

	# função principal
	def MainFunction(self):

		# variavel que define se o app vai rodar ou fechar
		State = True

		# erros
		try:
			while State:

				# request do state
				Request_State = open("__DATA__/data.State", "r")
				data_State = Request_State.readlines()
				State = str(data_State[0])
				Request_State.close()

				# fechar o app via console.py
				if State == "off":
					return
				
				# limpando a pasta __TEMP__
				for dirpath, dirname, file in walk('__TEMP__'):
					for filename in file:
						Dir_file = path.join(path.realpath(dirpath),filename)
						remove(Dir_file)

				# iniciando a analise
				print(f'{"_"*12}\n__Re:Sys__')

				# preparando a analise
				ProcessedPlaylist = Playlist(PlaylistUrl)

				# request de onde o app parou
				Request_Number = open("__DATA__/data.Number","r")
				data_Number = Request_Number.readlines()
				Request_Number.close()

				# lista de urls da playlist
				Url_List = []

				# 'try' caso tenha removido algum(s) video(s) da playlist ou não tenha mais videos para abaixar
				try:

					# salvando os audios adicionado recemtimente 
					for url in ProcessedPlaylist.video_urls[:int(data_Number[0])]:
						Url_List.append(url)

				# analisando se algum(s) video foi removido
				except IndexError:
					try:
						for url in ProcessedPlaylist.video_urls[:int(data_Number[0])-1]:
							pass
						print('Nothing new')
						sleep(1.5)
						App()

					# video realmente foi removido
					except IndexError:
						print("backing")

						# estabilizando o app(motivo a remoção de um video da playlist)
						Update_data = open("__DATA__/data.Number", "w")
						Update_data.write(f"{int(data_Number[0])-1}")
						Update_data.close()

						sleep(1.5)
						App()

				# pegando da list de urls o primeiro item
				Url_Last = Url_List[int(data_Number[0])-1]

				# iniciando a verificação para ver se os dados são reais
				self.verification(Url_Last, data_Number)

		# reiniciando o app
		except Exception as erro:
			print(erro)

			if error == 'maximum recursion depth exceeded while decoding a JSON object from a unicode string':
				startfile("__init__.pyw")
				return
			sleep(1.5)
			App()

	# função de verificação dos dados
	def verification(self, url, data):
		if self.phase == 1:
			self.link_v1 = url
			self.phase = 2
		elif self.phase == 2:
			self.link_v2 = url
			self.phase = 0
		elif self.phase == 0:

			# caso os dados sejam reais
			if self.link_v1 == self.link_v2:

				# limpando variaveis
				self.phase = 1
				self.link_v1 = '1'
				self.link_v2 = '2'

				# iniciando o download
				final(url, data)

				# voltando para a função principal
				return

			elif self.link_v1 != self.link_v2:
				self.phase = 1
				self.link_v1 = '1'
				self.link_v2 = '2'
				return

# função de download
def final(url, number):

	# erros no download
	try:

		print('pass')

		# preparando video
		Video = YouTube(url, on_progress_callback=process)

		# preparando como audio
		print('Downloading')
		stream = Video.streams.get_by_itag(251)

		# tamanho do audio
		print(stream.filesize)

		# download iniciado
		stream.download("__TEMP__")

		# tratamento do arquivo
		for dirpath, dirname, file in walk('__TEMP__'):
			for filename in file:

				# request do nome do arquivo
				filenameedit = filename[:len(filename)-5]
				Dir_file = path.join(path.realpath(dirpath),filename)

				# erros com o nome do arquivo
				try:

					# salvando como mp3
					rename(Dir_file, f'{download_path}/{filenameedit}.mp3')

				# caso exista um audio com o mesmo nome
				except:
					music_rename(Dir_file,filenameedit, 1)

				# indo para o proximo video da playlist
				Update_data = open("__DATA__/data.Number", "w")
				Update_data.write(f"{int(number[0])+1}")
				Update_data.close()

				# nome do video
				print(f'Download => {str(Video.title)}')

		# voltando para a função principal
		return

	# erros de download
	except Exception as error:
		print(error)
		sleep(1.5)
		final(url, number)

# iniciando a classe principal
App()

# fim
