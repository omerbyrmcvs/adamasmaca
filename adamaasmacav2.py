import os
while True:
	can = 4
	def adamasmaca(can):		
		dort ="""
                 ███████████████████████          
                               ███    ██          
                                ████  ██          
                                  ███ ██          
                                   █████          
                                    ████          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
              ███████████████████████████████
		"""
		uc = """
                 ███████████████████████          
                       ████    ███    ██          
                        ██      ████  ██          
                       ██         ███ ██          
                  ███████          █████          
                 ████████           ████          
                █████████             ██          
                 ████████             ██          
                 ████████             ██          
                  ███████             ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██         
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
              ███████████████████████████████
		"""
		iki = """
                 ███████████████████████          
                       ████    ███    ██          
                        ██      ████  ██          
                       ██         ███ ██          
                  ███████          █████          
                 ████████           ████          
                █████████             ██          
                 ████████             ██          
                 ████████             ██          
                  ███████             ██          
                     ███              ██          
                     ███              ██          
                     ██               ██          
                     ██               ██          
                     ██               ██          
                     ██               ██          
                     ██               ██          
                     ██               ██          
                    ████              ██          
                    ████              ██           
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
                                      ██          
              ███████████████████████████████
		"""
		bir = """
                 ███████████████████████          
                       ████    ███    ██          
                        ██      ████  ██          
                       ██         ███ ██          
                  ███████          █████          
                 ████████           ████          
                █████████             ██          
                 ████████             ██          
                 ████████             ██          
                  ███████             ██          
                   ███████            ██          
                   ███████            ██          
                   ████ ███           ██          
                  ██ ██  ██           ██          
                  ██ ██  ██           ██          
                  ██ ██  █            ██          
                     ██               ██          
                     ██               ██          
                    ████              ██          
                    ████              ██          
                                      ██         
                                      ██
                                      ██    
                                      ██          
                                      ██          
                                      ██          
              ███████████████████████████████
		"""
		sifir = """
                 ███████████████████████          
                       ████    ███    ██          
                        ██      ████  ██          
                       ██         ███ ██          
                  ███████          █████          
                 ████████           ████          
                █████████             ██          
                 ████████             ██          
                 ████████             ██          
                  ███████             ██          
                   ███████            ██          
                   ███████            ██          
                   ████ ███           ██          
                  ██ ██  ██           ██          
                  ██ ██  ██           ██          
                  ██ ██  █            ██          
                     ██               ██          
                     ██               ██          
                    ████              ██          
                    ████              ██            
                   ██ ██              ██          
                █████  ██             ██          
               █████   ████           ██          
                        ███           ██          
                                      ██          
                                      ██          
              ███████████████████████████████
		"""
		adamliste = [sifir,bir,iki,uc,dort]
		return adamliste[can]
	os.system('cls')
	kelimes = input("Kelimeyi Giriniz:")
	kelime = kelimes.lower()
	os.system('cls')

	print(adamasmaca(can))

	kelimelist = []

	deneme = ""

	for i in kelime:
		kelimelist.append(i)

	tahminler = []

	cizgiler = []
	for i in kelime:
		cizgiler.append("_")

	while (not can == 0) and ("_" in cizgiler):

		tahmins = input("Harf:")
		tahmin = tahmins.lower()

		if tahmin in kelime:
			if tahmin in tahminler:
				os.system('cls')
				print("Dostum aynı harfi iki kere yazma")
				can -= 1
				print(f"{can} canın kaldı")
				print(adamasmaca(can))
				

			else:
				tahminler.append(tahmin)

		else:
			can -= 1
			os.system('cls')
			print(f"{can} canın kaldı")
			print(adamasmaca(can))
			

		if tahmin in kelime:
			for x,y in enumerate(kelimelist):
				tekrar = []
				if y == tahmin:
					cizgiler[x] = y
		deneme = ""
		for i in cizgiler:
			deneme += i
			deneme += " "
		print(deneme)

	if can == 0:
		os.system('cls')
		print("Öldün Canım Benim")
		print("Kelime:" + kelime)
		print(adamasmaca(can))
			
	if not "_" in cizgiler:
		os.system('cls')
		print("Kazandın Aferim")
		print(adamasmaca(can))
	input("Tekrar oynamak için entera basın")




