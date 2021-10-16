from os import system, startfile, name
def clear():
	system('cls' if name == 'nt' else 'clear')
	return
def line():
	print('_'*80)
	return
class console():
	def __init__(self):
		try:
			line()
			print("commands:")
			print("	playlist")
			print("	start")
			print("	break")
			print("	download")
			print(" help")
			line()
			command = input("=> ")
			if command == "playlist":
				clear()
				line()
				print('commands:')
				print("	charge")
				print("	show")
				line()
				command = input("=> ")
				if command == "charge":
					clear()
					line()
					print("link paste here")
					command = input("link => ")
					charge = open("__DATA__/data.Playlist","w")
					charge.write(command)
					charge.close()
					charge = open("__DATA__/data.Number","w")
					charge.write('1')
					charge.close()
					console()
				elif command == 'show':
					clear()
					line()
					charge = open("__DATA__/data.Playlist","r")
					url = charge.readline()
					charge.close()
					print(f"playlist:{url}")
					line()
					console()
			elif command == "start":
				startfile("__init__.pyw")
				console()
			elif command == "break":
				charge = open("__DATA__/data.State","w")
				charge.write("off")
				charge.close()
				console()
			elif command == "help":
				clear()
				line()
				print('charge your playlist:')
				print("write 'playlist', after write 'charge' and paste link")
				line()
				print('start:')
				print("write 'start' ")
				line()
				print('stop apllication:')
				print("write 'break'")
				line()
				print("charge your path downlads:")
				print("write 'downloads', after 'charge' and write your new path")
				line()
				print('open downloads:')
				print("write 'downloads', after 'open")
				input(" for back click Enter")
				console()
			elif command == "download":
				clear()
				line()
				print('commands:')
				print('	show')
				print('	charge')
				line()
				command = input("=> ")
				if command == "show":
					Request_path = open("__DATA__/data.path", "r")
					data_path = Request_path.readlines()
					downloads = str(data_path[0])
					Request_path.close()
					startfile(downloads)
					console()
				elif command == "charge":
					clear()
					line()
					print("write your new dirpath(complete):")
					dirpath = input('=> ')
					charge = open("__DATA__/data.Path","w")
					charge.write(dirpath)
					charge.close()
					print(f"your new dir's:{dirpath}")
					console()
			clear()
			console()
		except:
			console()
console()