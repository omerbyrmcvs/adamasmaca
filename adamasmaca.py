import os
while True:
	can = 4
	def adamasmaca(can):		
		dort ="""
                 .ooooohmdooooodyoooooyo          
                               -h:    /y          
                                `ss`  /y          
                                  /y. /y          
                                   .y++y          
                                    `+my          
                                      +y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
              :oooooooooooooooooooooooyhoooo-
		"""
		uc = """
                 .ooooohmdooooodyoooooyo          
                       /Nh`    -h:    /y          
                        m.      `ss`  /y          
                       .m         /y. /y          
                  `-:/:/h          .y++y          
                 +s/-./dy           `+my          
                .m`  ``:h             +y          
                 ho-`-`:h             /y          
                 .sydh/dh             /y          
                  `ssdNM/             /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
              :oooooooooooooooooooooooyhoooo-
		"""
		iki = """
                 .ooooohmdooooodyoooooyo          
                       /Nh`    -h:    /y          
                        m.      `ss`  /y          
                       .m         /y. /y          
                  `-:/:/h          .y++y          
                 +s/-./dy           `+my          
                .m`  ``:h             +y          
                 ho-`-`:h             /y          
                 .sydh/dh             /y          
                  `ssdNM/             /y          
                     hds              /y          
                     :m.              /y          
                     :d               /y          
                     /y               /y          
                     od               /y          
                     yM`              /y          
                     yM.              /y          
                    .dN:              /y          
                    soyo              /y          
                   `d./h              /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
                                      /y          
              :oooooooooooooooooooooooyhoooo-
		"""
		bir = """
                 .ooooohmdooooodyoooooyo          
                       /Nh`    -h:    /y          
                        m.      `ss`  /y          
                       .m         /y. /y          
                  `-:/:/h          .y++y          
                 +s/-./dy           `+my          
                .m`  ``:h             +y          
                 ho-`-`:h             /y          
                 .sydh/dh             /y          
                  `ssdNM/             /y          
                   `/hdsh`            /y          
                   `d:m.s+            /y          
                   so:d `m`           /y          
                  .m`/y  h:           /y          
                  so od  y/           /y          
                  +` yM` `            /y          
                     yM.              /y          
                    .dN:              /y          
                    soyo              /y          
                   `d./h              /y          
                                      /y         
                                      /y
                                      /y    
                                      /y          
                                      /y          
                                      /y          
              :oooooooooooooooooooooooyhoooo-
		"""
		sifir = """
                 .ooooohmdooooodyoooooyo          
                       /Nh`    -h:    /y          
                        m.      `ss`  /y          
                       .m         /y. /y          
                  `-:/:/h          .y++y          
                 +s/-./dy           `+my          
                .m`  ``:h             +y          
                 ho-`-`:h             /y          
                 .sydh/dh             /y          
                  `ssdNM/             /y          
                   `/hdsh`            /y          
                   `d:m.s+            /y          
                   so:d `m`           /y          
                  .m`/y  h:           /y          
                  so od  y/           /y          
                  +` yM` `            /y          
                     yM.              /y          
                    .dN:              /y          
                    soyo              /y          
                   `d./h              /y          
                   /h .N              /y          
                `.:h:  N-             /y          
               .+/:-   sy/`           /y          
                        .oy           /y          
                                      /y          
                                      /y          
              :oooooooooooooooooooooooyhoooo-
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




