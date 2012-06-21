#! /usr/bin/env python

### Colgate 945 Map - FF to X12

###
### Process FF files in the source directory, getting them ready for mapping/processing in the EDI Out area.
###

def ProcessFF():
	
	os.chdir(DATADIR + SourceDir)
	dirlist = os.listdir(DATADIR + SourceDir)

	while len(dirlist) > 0:
		filename = dirlist.pop(0)
		if filename.split(".")[len(filename.split("."))-1] == SourceType:
			flatfile=open(filename,'r')
			mainsort = []
			linecount = 0
			mainlist = []
			TotalWeight = 0
			trailerflag = "No"
			for line in flatfile:
				fcount = 0
				fielddata = ""
				#read each character in the line
				linecount = linecount + 1
				if line[0] == "H":
					ordernumber = line[34:44].strip()
					itemnumber = line[50:68].strip()
					lotnumber = line[105:125].strip()
					MH10number = line[204:224].strip()
					Weight = float(line[303:314])/1000
					TotalWeight = TotalWeight + (Weight)
					recordtype = "200"
					mainparms = ordernumber, recordtype, itemnumber, lotnumber, MH10number, linecount, Weight
					mainsort.append(mainparms)
					mainlist.append(line)
				elif line[0] == "T":
					ordernumber = line[34:44].strip()
					itemnumber = line[50:68].strip()
					lotnumber = line[105:125].strip()
					MH10number = line[204:224].strip()
					recordtype = "100"				
					mainparms = ordernumber, recordtype, itemnumber, lotnumber, MH10number, linecount, TotalWeight
					mainsort.append(mainparms)
					mainlist.append("X" + line[1:])
					
					recordtype = "300"
					linecount = linecount + 1
					mainparms = ordernumber, recordtype, itemnumber, lotnumber, MH10number, linecount, TotalWeight
					mainsort.append(mainparms)
					mainlist.append(line)

					TotalWeight = 0
					trailerflag = "Yes"
				elif line[0] == "P":
					ordernumber = line[34:44].strip()
					itemnumber = line[50:68].strip()
					lotnumber = line[105:125].strip()
					MH10number = line[204:224].strip()
					recordtype = "150"				
					mainparms = ordernumber, recordtype, itemnumber, lotnumber, MH10number, linecount, TotalWeight
					mainsort.append(mainparms)
					mainlist.append(line)
				else:
					ordernumber = line[34:44].strip()
					itemnumber = line[50:68].strip()
					lotnumber = line[105:125].strip()
					MH10number = line[204:224].strip()
					recordtype = "110"				
					mainparms = ordernumber, recordtype, itemnumber, lotnumber, MH10number, linecount, TotalWeight
					mainsort.append(mainparms)
					mainlist.append(line)
				#end if
			#end for		
			flatfile.close()
			
			if trailerflag == "Yes":

				mainsort.sort()
	
				linecount = 0
				transcount = 0
				recordcount = 0
				LXCount = 0
				itemqtyshipped = 0
				sortline = []
				sortorder = []
				chepoutarray = []
				cheppalletcount = 0
				totalqty = 0
				lastlotnumber = "lastlotxxx"
				lastordernumber = "lastorderxxx"
				lastitemnumber = "lastitemxxx"
				lastMH10number = "lastMH10xxx"
	
				while len(mainsort) > 0:
	
					mainparms = mainsort.pop(0)
					inline = mainlist[mainparms[5] - 1]
					if inline[0] == "X":
						TotalWeight = mainparms[6]
						if TotalWeight == 0:
							TotalWeight = 1
						#end if	
						qtyshipped = 0
						totalqty = 0
						palletcount = 0
						cheppalletcount = 0
						halfchep = 0
						qtrchep = 0
						fullchep = 0
					elif inline[0] == "P":	
						palletqty = long(inline[92:100].strip())
						ChepFlag1 = inline[244:245].strip()
						ChepFlag2 = inline[614:624].strip()
						PalletType = inline[624:634].strip()
						if palletqty > 0:
							if ChepFlag1 == "P" and ChepFlag2 == "2":
								cheppalletcount = cheppalletcount + palletqty
								if PalletType == "1":
									fullchep = fullchep + palletqty
								elif PalletType == "2":
									halfchep = halfchep + palletqty
								elif PalletType == "4":
									qtrchep = qtrchep + palletqty
								#end if
							else:
								palletcount = palletcount + palletqty
							#end if
						#end if
					elif inline[0] == "B":
						ordernumber = mainparms[0]
						itemnumber = mainparms[2]
						logfile.write(timestamp + ": => 940 pass through data missing in " + filename + " for order number/itemnumber " + str(ordernumber) + "/" + str(itemnumber) + "\n")
					elif inline[0] == "H":
						lotnumber = mainparms[3]
						ordernumber = mainparms[0]
						itemnumber = mainparms[2]
						MH10number = mainparms[4]
						if len(mainsort) > 0:
							if mainsort[0][1] == "200":
								nextlotnumber = mainsort[0][3]
								nextordernumber = mainsort[0][0]
								nextitemnumber = mainsort[0][2]
								nextMH10number = mainsort[0][4]
							else:
								nextlotnumber = "nextlotxxx"
								nextordernumber = "nextorderxxx"
								nextitemnumber = "nextitemxxx"
								nextMH10number = "nextMH10xxx"
							#end if
						else:
							nextlotnumber = "nextlotxxx"
							nextordernumber = "nextorderxxx"
							nextitemnumber = "nextitemxxx"
							nextMH10number = "nextMH10xxx"
						#end if
						if ordernumber == nextordernumber and itemnumber == nextitemnumber and lotnumber == nextlotnumber and MH10number == nextMH10number:
							qtyshipped = qtyshipped + long(inline[92:100].strip())
							itemqtyshipped = itemqtyshipped + long(inline[92:100].strip())
						else:
							if ordernumber != lastordernumber:	
								lastordernumber = ordernumber
								LXCount = 0
								transcount = transcount + 1
								Segment = {}
								Segment["Segment"] = "Header"
								Segment["Partner"] = PartnerName 
								Segment["FGType"] = "SW"
								Segment["TSetType"] = "945"
								sortline.append(Segment)
								sortparms = transcount, "100", recordcount
								sortorder.append(sortparms)
								recordcount = recordcount + 1
			
								if len(inline[270:285].strip()) > 0:
									BOLNumber = inline[270:285].strip()
								else:
									BOLNumber = inline[1173:1193].strip()
								#end if		
	
								Segment = {}
								Segment["Segment"] = "W06"
								Segment["W06001001"] = "F"
								Segment["W06002001"] = inline[34:44].strip()
								Segment["W06003001"] = inline[285:289].strip() + inline[290:292].strip() + inline[293:295].strip()
								Segment["W06004001"] = BOLNumber
								#Segment["W06010001"] = inline[1208:1228].strip()
								sortline.append(Segment)
								sortparms = transcount, "200", recordcount
								sortorder.append(sortparms)
								recordcount = recordcount + 1
								
								#Segment = {}
								#Segment["Segment"] = "N1"
								#Segment["N1001001"] = "DE"
								#Segment["N1002001"] = "COLGATE"
								#Segment["N1003001"] = "9"
								#Segment["N1004001"] = "0698712000001"
								#sortline.append(Segment)
								#sortparms = transcount, "200", recordcount
								#sortorder.append(sortparms)
								#recordcount = recordcount + 1
		
								
								if len(inline[664:694].strip()) > 0 or len(inline[694:724].strip()) > 0:
									Segment = {}
									Segment["Segment"] = "N1"
									Segment["N1001001"] = "ST"
									Segment["N1002001"] = inline[664:694].strip()
									if len(inline[694:724].strip()) > 0:
										Segment["N1003001"] = "91"
										Segment["N1004001"] = inline[694:724].strip()
									#end if
									sortline.append(Segment)
									sortparms = transcount, "200", recordcount
									sortorder.append(sortparms)
									recordcount = recordcount + 1
								#end if
								
								
								if len(inline[754:784].strip()) > 0:
									Segment = {}
									Segment["Segment"] = "N9"
									Segment["N9001001"] = "LO"
									Segment["N9002001"] = inline[754:784].strip()
									sortline.append(Segment)
									sortparms = transcount, "200", recordcount
									sortorder.append(sortparms)
									recordcount = recordcount + 1
								#end if
								
								Segment = {}
								Segment["Segment"] = "N9"
								Segment["N9001001"] = "MB"
								Segment["N9002001"] = inline[34:44].strip()
								sortline.append(Segment)
								sortparms = transcount, "200", recordcount
								sortorder.append(sortparms)
								recordcount = recordcount + 1
	
								Segment = {}
								Segment["Segment"] = "W27"
								if len(inline[892:902].strip()) > 0:
									Segment["W27001001"] = inline[892:902].strip()
								else:	
									Segment["W27001001"] = "M"
								#end if	
								if len(inline[260:270].strip()) > 0:
									Segment["W27002001"] = inline[260:270].strip()
								elif len(inline[935:945].strip()) > 0:
									Segment["W27002001"] = inline[935:945].strip()
								else:	
									Segment["W27002001"] = "UNKW"
								#end if	
								#Segment["W27006001"] = inline[260:270].strip()
								trailernumber = inline[1741:1756].strip().replace("~", "-").replace("*", "-").replace(">", "-")
								Segment["W27007001"] = trailernumber
								Segment["W27010001"] = "01"
								sortline.append(Segment)
								sortparms = transcount, "200", recordcount
								sortorder.append(sortparms)
								recordcount = recordcount + 1
	
								if cheppalletcount > 0:
									Segment = {}
									Segment["Segment"] = "W10"
									Segment["W10002001"] = str(long(cheppalletcount))
									Segment["W10003001"] = "5"
									sortline.append(Segment)
									sortparms = transcount, "200", recordcount
									sortorder.append(sortparms)
									recordcount = recordcount + 1
									
									#chep variables
									ChepShipDate = time.strftime("%Y%m%d")
									ChepBOL = BOLNumber
									ChepPO = inline[34:44].strip()
									ChepReceiverCode = inline[694:724].strip()
									ChepShipToName = inline[664:694].strip()
									ChepShipToAddr = inline[959:989].strip()
									ChepShipToCity = inline[1051:1071].strip()
									ChepShipToPC = inline[1076:1086].strip()
									ChepShipToProv = inline[1071:1076].strip()
									ChepGlobalID = "4000187668"
									ChepCustomerID = "7392"
									CountryCode = "CA"
									if inline[1076:1086].strip().isdigit:
										ChepShipToCty = "US"
									else:
										ChepShipToCty = "CA"
									#end if	
								#end if							
								if palletcount > 0:
									Segment = {}
									Segment["Segment"] = "W10"
									Segment["W10002001"] = str(long(palletcount))
									Segment["W10003001"] = "1"
									sortline.append(Segment)
									sortparms = transcount, "200", recordcount
									sortorder.append(sortparms)
									recordcount = recordcount + 1
								#end if
	
								Segment = {}
								Segment["Segment"] = "G62"
								Segment["G62001001"] = "011"
								Segment["G62002001"] = inline[285:289].strip() + inline[290:292].strip() + inline[293:295].strip()
								Segment["G62003001"] = "A"
								Segment["G62004001"] = inline[295:297].strip() + inline[298:300].strip()
								sortline.append(Segment)
								sortparms = transcount, "200", recordcount
								sortorder.append(sortparms)
								recordcount = recordcount + 1
	
							#end if	
							qtyshipped = qtyshipped + long(inline[92:100].strip())
							itemqtyshipped = itemqtyshipped + long(inline[92:100].strip())
							qtyordered = long(inline[81:89].strip()) - (itemqtyshipped - qtyshipped)
							totalqty = totalqty + qtyshipped
							qtyos = qtyordered - qtyshipped
							#if ordernumber == nextordernumber and itemnumber == nextitemnumber and lotnumber != nextlotnumber:
							#	qtyordered = qtyshipped
							#	qtyos = 0
							#end if	
							
							LXCount = LXCount + 1
							Segment = {}
							Segment["Segment"] = "LX"
							Segment["LX001001"] = str(long(LXCount))
							sortline.append(Segment)
							sortparms = transcount, "300", recordcount
							sortorder.append(sortparms)
							recordcount = recordcount + 1
							
							Segment = {}
							Segment["Segment"] = "W12"
							if qtyos == 0:
								Segment["W12001001"] = "CC"
								#Segment["W12004001"] = "0"
							elif qtyos > 0:
								Segment["W12001001"] = "CP"
								#Segment["W12004001"] = str(qtyos)
							elif qtyos < 0:
								Segment["W12001001"] = "CP"
								#Segment["W12004001"] = str(-qtyos)
							#end if
							#Segment["W12002001"] = str(qtyordered)
							Segment["W12003001"] = str(qtyshipped)
							if len(inline[1234:1244].strip()) > 0:
								Segment["W12005001"] = inline[1234:1244].strip()
							else:
								Segment["W12005001"] = "CA"
							#end if
							Segment["W12007001"] = "VN"
							Segment["W12008001"] = inline[50:68].strip()
							Segment["W12009001"] = inline[105:125].strip()
							if len(inline[342:347].strip()) > 0:
								Segment["W12019001"] = inline[342:347].strip()
							#end if	
							sortline.append(Segment)
							sortparms = transcount, "300", recordcount
							sortorder.append(sortparms)
							recordcount = recordcount + 1
	
							if len(inline[1756:1776].strip()) > 0:
								Segment = {}
								Segment["Segment"] = "N9"
								Segment["N9001001"] = "LA"
								Segment["N9002001"] = inline[1756:1776].strip()
								sortline.append(Segment)
								sortparms = transcount, "300", recordcount
								sortorder.append(sortparms)
								recordcount = recordcount + 1
							elif len(inline[204:224].strip()) > 0:
								Segment = {}
								Segment["Segment"] = "N9"
								Segment["N9001001"] = "LA"
								Segment["N9002001"] = inline[204:224].strip()
								sortline.append(Segment)
								sortparms = transcount, "300", recordcount
								sortorder.append(sortparms)
								recordcount = recordcount + 1
							#end if						
	
							qtyshipped =0
	
							if ordernumber != nextordernumber or itemnumber != nextitemnumber:
								itemqtyshipped = 0
							#end if	
						
						#end if
					elif inline[0] == "T":
						Segment = {}
						Segment["Segment"] = "W03"
						Segment["W03001001"] = str(totalqty)
						Segment["W03002001"] = str(long(round(TotalWeight)))
						Segment["W03003001"] = "LB"
						sortline.append(Segment)
						sortparms = transcount, "400", recordcount
						sortorder.append(sortparms)
						recordcount = recordcount + 1
	
	############## start chep					
						if cheppalletcount > 0:
							QtrChepTotal = qtrchep
							HalfChepTotal = halfchep
							FullChepTotal = fullchep
							
							NumberofRecords = 0
							if FullChepTotal > 0:
								NumberofRecords = NumberofRecords + 1
							#end if
							if HalfChepTotal > 0:
								NumberofRecords = NumberofRecords + 1
							#end if
							if QtrChepTotal > 0:
								NumberofRecords = NumberofRecords + 1
							#end if
							
							CreationDate = time.strftime("%Y%m%d")
							ChepSequence = 1
							TotalChepQty = 0
							separator = "+"
							detailseparator = "~"
							#read control file into control list dictionary
							if os.path.exists(PROGDIR + "/DEDI_ChepColgateSequence.dat"):
								chepfile=open(PROGDIR + "/DEDI_ChepColgateSequence.dat",'r')
								for line in chepfile:
									ChepSequence = long(line.strip()) + 1
								#end for
								chepfile.close()
								chepfile=open(PROGDIR + "/DEDI_ChepColgateSequence.dat",'w')
								chepfile.write(str(long(ChepSequence)))
								chepfile.close()
							else:	
								chepfile=open(PROGDIR + "/DEDI_ChepColgateSequence.dat",'w')
								chepfile.write(str(long(ChepSequence)))
								chepfile.close()
							#end
							ChepRecord = InitRecord(14)
							ChepRecord[0] = separator
							ChepRecord[1] = "*****"
							ChepRecord[2] = "FROM"
							ChepRecord[3] = "CHEP-" + CountryCode + ChepGlobalID
							ChepRecord[4] = "RCVD"
							ChepRecord[5] = CreationDate
							ChepRecord[6] = "FREF"
							ChepRecord[7] = str(long(ChepSequence))
							ChepRecord[8] = "NORC"
							ChepRecord[9] = str(long(NumberofRecords))
							ChepRecord[10] = "SEPR"
							ChepRecord[11] = detailseparator
							ChepRecord[12] = "VERS"
							ChepRecord[13] = "1.02"
							ChepRecord[14] = "*****"
							RecordO = []
							i = 0
							while i < len(ChepRecord):
								RecordO.append(ChepRecord[i])
								i = i + 1
							#end while
							chepoutarray.append(RecordO)
							NumberofRecords = 0
							if FullChepTotal > 0:
								ChepQty = FullChepTotal
								ChepPalletType = "4001"
								TotalChepQty = TotalChepQty + FullChepTotal
								NumberofRecords = NumberofRecords + 1									
		
								ChepRecord = InitRecord(31)
								ChepRecord[0] = detailseparator
								ChepRecord[1] = "LI="
								ChepRecord[2] = str(long(NumberofRecords))
								ChepRecord[3] = "1"
								ChepRecord[4] = "CA"
								ChepRecord[5] = "SA"
								ChepRecord[6] = ChepGlobalID
								ChepRecord[7] = "IN"
								ChepRecord[8] = ChepReceiverCode
								ChepRecord[9] = "90"
								ChepRecord[10] = ChepPalletType
								ChepRecord[11] = ChepShipDate
								ChepRecord[12] = ""
								ChepRecord[13] = str(long(ChepQty))
								ChepRecord[14] = ChepCustomerID + str(long(ChepSequence)).zfill(4) + str(long(NumberofRecords)).zfill(5)
								ChepRecord[15] = ChepBOL
								ChepRecord[16] = ChepPO
								ChepRecord[17] = "2"
								ChepRecord[18] = ""
								ChepRecord[19] = ""
								ChepRecord[20] = ""
								ChepRecord[21] = ""
								ChepRecord[22] = ""
								ChepRecord[23] = ChepShipToName
								ChepRecord[24] = ChepShipToAddr
								ChepRecord[25] = ChepShipToCity
								ChepRecord[26] = ChepShipToPC
								ChepRecord[27] = ChepShipToProv
								ChepRecord[28] = ChepShipToCty
								ChepRecord[29] = ""
								ChepRecord[30] = ""
								ChepRecord[31] = "<"
								RecordO = []
								i = 0
								while i < len(ChepRecord):
									RecordO.append(ChepRecord[i])
									i = i + 1
								#end while
								chepoutarray.append(RecordO)
							#end if
							if QtrChepTotal > 0:
								ChepQty = QtrChepTotal
								ChepPalletType = "4004"
								TotalChepQty = TotalChepQty + QtrChepTotal
								NumberofRecords = NumberofRecords + 1									
								ChepRecord = InitRecord(31)
								ChepRecord[0] = detailseparator
								ChepRecord[1] = "LI="
								ChepRecord[2] = str(long(NumberofRecords))
								ChepRecord[3] = "1"
								ChepRecord[4] = "CA"
								ChepRecord[5] = "SA"
								ChepRecord[6] = ChepGlobalID
								ChepRecord[7] = "IN"
								ChepRecord[8] = ChepReceiverCode
								ChepRecord[9] = "90"
								ChepRecord[10] = ChepPalletType
								ChepRecord[11] = ChepShipDate
								ChepRecord[12] = ""
								ChepRecord[13] = str(long(ChepQty))
								ChepRecord[14] = ChepCustomerID + str(long(ChepSequence)).zfill(4) + str(long(NumberofRecords)).zfill(5)
								ChepRecord[15] = ChepBOL
								ChepRecord[16] = ChepPO
								ChepRecord[17] = "2"
								ChepRecord[18] = ""
								ChepRecord[19] = ""
								ChepRecord[20] = ""
								ChepRecord[21] = ""
								ChepRecord[22] = ""
								ChepRecord[23] = ChepShipToName
								ChepRecord[24] = ChepShipToAddr
								ChepRecord[25] = ChepShipToCity
								ChepRecord[26] = ChepShipToPC
								ChepRecord[27] = ChepShipToProv
								ChepRecord[28] = ChepShipToCty
								ChepRecord[29] = ""
								ChepRecord[30] = ""
								ChepRecord[31] = "<"
								RecordO = []
								i = 0
								while i < len(ChepRecord):
									RecordO.append(ChepRecord[i])
									i = i + 1
								#end while
								chepoutarray.append(RecordO)
							#end if
							if HalfChepTotal > 0:
								ChepQty = HalfChepTotal
								ChepPalletType = "4005"
								TotalChepQty = TotalChepQty + HalfChepTotal
								NumberofRecords = NumberofRecords + 1									
								ChepRecord = InitRecord(31)
								ChepRecord[0] = detailseparator
								ChepRecord[1] = "LI="
								ChepRecord[2] = str(long(NumberofRecords))
								ChepRecord[3] = "1"
								ChepRecord[4] = "CA"
								ChepRecord[5] = "SA"
								ChepRecord[6] = ChepGlobalID
								ChepRecord[7] = "IN"
								ChepRecord[8] = ChepReceiverCode
								ChepRecord[9] = "90"
								ChepRecord[10] = ChepPalletType
								ChepRecord[11] = ChepShipDate
								ChepRecord[12] = ""
								ChepRecord[13] = str(long(ChepQty))
								ChepRecord[14] = ChepCustomerID + str(long(ChepSequence)).zfill(4) + str(long(NumberofRecords)).zfill(5)
								ChepRecord[15] = ChepBOL
								ChepRecord[16] = ChepPO
								ChepRecord[17] = "2"
								ChepRecord[18] = ""
								ChepRecord[19] = ""
								ChepRecord[20] = ""
								ChepRecord[21] = ""
								ChepRecord[22] = ""
								ChepRecord[23] = ChepShipToName
								ChepRecord[24] = ChepShipToAddr
								ChepRecord[25] = ChepShipToCity
								ChepRecord[26] = ChepShipToPC
								ChepRecord[27] = ChepShipToProv
								ChepRecord[28] = ChepShipToCty
								ChepRecord[29] = ""
								ChepRecord[30] = ""
								ChepRecord[31] = "<"
								RecordO = []
								i = 0
								while i < len(ChepRecord):
									RecordO.append(ChepRecord[i])
									i = i + 1
								#end while
								chepoutarray.append(RecordO)
							#end if
							
							#trailer record
							ChepRecord = InitRecord(6)
							ChepRecord[0] = separator
							ChepRecord[1] = "*****"
							ChepRecord[2] = "NORC"
							ChepRecord[3] = str(long(NumberofRecords))
							ChepRecord[4] = "SQTY"
							ChepRecord[5] = str(long(TotalChepQty))
							ChepRecord[6] = "EOF"
							RecordO = []
							i = 0
							while i < len(ChepRecord):
								RecordO.append(ChepRecord[i])
								i = i + 1
							#end while
							chepoutarray.append(RecordO)
							
							QtrChepTotal = 0
							HalfChepTotal = 0
							FullChepTotal = 0
						#end if
						
	############## end chep
						
					#end if
				#end while
				# sort and write to file here
				sortorder.sort()
	
				outorder = []
				while len(sortorder) > 0:
					sortparms = sortorder.pop(0)
					outline = sortline[sortparms[2]]
					outorder.append(outline)
				#end while
	
				if len(outorder) > 0:
					i = 1
					filename2 = filename.split(".")[0]
					while i < len(filename.split(".")):
						filename2 = filename2 + "-" + filename.split(".")[i]
						i = i + 1
					#end while
	
					filename2 = filename2 + "." + DestType
					if os.access(EDIOUTDIR + DestDir + "/" + filename2, os.F_OK) == 1:
						filecount = 1
						filename1 = filename2.split(".")[0] + "-" + str(filecount) + "." + filename2.split(".")[1]
						while os.access(EDIOUTDIR + DestDir + "/" + filename1, os.F_OK) == 1:
							filecount = filecount + 1							
							filename1 = filename2.split(".")[0] + "-" + str(filecount) + "." + filename2.split(".")[1]
						#end while
					else:
						filename1 = filename2
					#end if	
					pickle.dump(outorder,open(TEMPDIR + "/" + filename1,'w'))
					os.rename(TEMPDIR + "/" + filename1, EDIOUTDIR + DestDir + "/" + filename1)
				else:
					logfile.write(timestamp + ": => No output data from " + filename + "\n")
				#end if	
	
				if len(chepoutarray) > 0:
					i = 1
					filename2 = filename.split(".")[0]
					while i < len(filename.split(".")):
						filename2 = filename2 + "-" + filename.split(".")[i]
						i = i + 1
					#end while
		
					filename2 = filename2 + "." + ChepDestType
					if os.access(DATADIR + ChepDestDir + "/" + filename2, os.F_OK) == 1:
						filecount = 1
						filename1 = filename2.split(".")[0] + "-" + str(filecount) + "." + filename2.split(".")[1]
						while os.access(DATADIR + ChepDestDir + "/" + filename1, os.F_OK) == 1:
							filecount = filecount + 1							
							filename1 = filename2.split(".")[0] + "-" + str(filecount) + "." + filename2.split(".")[1]
						#end while
					else:
						filename1 = filename2
					#end if	
					
					while len(chepoutarray) > 0:
						outline = chepoutarray.pop(0)
						if len(outline) > 0:
							outrecord = ""
							delimiter = str(outline.pop(0))
							while len(outline) > 0:
								field = str(outline.pop(0))
								outrecord = outrecord + field
								if len(outline) > 0:
									outrecord = outrecord + delimiter
								#end if
							#end while
							outfile=open(TEMPDIR + "/" + filename1,'a')
							outfile.write(outrecord + "\n")
							outfile.close()
						#end if
					#end while
					os.rename(TEMPDIR + "/" + filename1, DATADIR + ChepDestDir + "/" + filename1)
				#end if
		
				#archive edi file
				archivefile = ARCHIVE + SourceDir + "/" + filename
				if os.access(archivefile, os.F_OK) == 1:
					os.rename(filename, archivefile + "." + timestamp)
					logfile.write(timestamp + ": => Archived " + filename + " to " + archivefile + "." + timestamp + "\n")
				else:
					os.rename(filename, archivefile)
					logfile.write(timestamp + ": => Archived " + filename + " to " + archivefile + "\n")
				#End if
			else:
				os.rename(filename, DATADIR + "/fromWMS-ColgateError/" + filename)
			#end if
		#End if	
	#end while
#end of function	

###
### Check to see directory exists in archive and EDI processing areas.
###
def CheckDirs():
	if os.access(EDIINDIR + SourceDir, os.F_OK) != 1:
		os.makedirs(EDIINDIR + SourceDir)
		logfile.write(timestamp + ": =>" +  EDIINDIR + SourceDir + " directory created\n")
	#end if	
	if os.access(ARCHIVE + EDIIN + SourceDir, os.F_OK) != 1:
		os.makedirs(ARCHIVE + EDIIN + SourceDir)
		logfile.write(timestamp + ": =>" +  ARCHIVE + EDIIN + SourceDir + " directory created\n")
	#end if	
	if os.access(ARCHIVE + SourceDir, os.F_OK) != 1:
		os.makedirs(ARCHIVE + SourceDir)
		logfile.write(timestamp + ": =>" +  ARCHIVE + SourceDir + " directory created\n")
	#end if	
	if os.access(EDIOUTDIR + DestDir, os.F_OK) != 1:
		os.makedirs(EDIOUTDIR + DestDir)
		logfile.write(timestamp + ": =>" +  EDIOUTDIR + DestDir + " directory created\n")
	#end if	
	if os.access(ARCHIVE + EDIOUT + DestDir, os.F_OK) != 1:
		os.makedirs(ARCHIVE + EDIOUT + DestDir)
		logfile.write(timestamp + ": =>" +  ARCHIVE + EDIOUT + DestDir + " directory created\n")
	#end if	
	if os.access(TEMPDIR, os.F_OK) != 1:
		os.makedirs(TEMPDIR)
		logfile.write(timestamp + ": =>" +  TEMPDIR + " directory created\n")
	#end if	
	if os.access(DATADIR + SourceDir, os.F_OK) != 1:
		os.makedirs(DATADIR + SourceDir)
		logfile.write(timestamp + ": =>" +  DATADIR + SourceDir + " directory created\n")
	#end if	
	if os.access(DATADIR + ChepDestDir, os.F_OK) != 1:
		os.makedirs(DATADIR + ChepDestDir)
		logfile.write(timestamp + ": =>" + DATADIR + ChepDestDir + " directory created\n")
	#end if	
#end of function

###
### Intitialize a Record Array
###

def InitRecord(fields):
	Record = []
	i = -1
	while i < fields:
		Record.append(" ")
		i = i + 1
	#end while
	return Record
#end function

###
### Check to see if key exist, if so return value, else blank
###

def getkeyvalue(dict,dictkey):
	if dict.has_key(dictkey):
		value = dict[dictkey]
	else:
		value = " "
	#end if
	return value	
#end function

###
### Main Program
###

import time
import os
import os.path
import sys
import string
import pickle

#Define Variables
progname='Map_F2X_COL945'
timestamp=time.strftime("%Y%m%d%H%M%S")
datestamp=time.strftime("%y%m%d")

EDIDIR="/apps/distedi"
DATADIR=EDIDIR + "/data"
ARCHIVE=EDIDIR + "/archive"
EDIMONITOR=EDIDIR + "/edimonitor"
FLAGDIR=EDIDIR + "/ediflags"
PROGDIR=EDIDIR+"/programs"
LOGDIR=EDIDIR+"/logs"
EDIIN="/ediin"
EDIOUT="/ediout"
EDIINDIR=EDIDIR+EDIIN
EDIOUTDIR=EDIDIR+EDIOUT
TEMPDIR=EDIOUTDIR + "/temp"
ERRORDIR=EDIINDIR+"/errorlog"
errorlogfile = ERRORDIR + "/" + timestamp + "." + progname
errorlog = LOGDIR + "/" + datestamp + ".EDIErrors"

#open logfile
logfile=open(LOGDIR + "/" + datestamp + "." + progname,'a')

### Process EDI Files

SourceDir="/fromWMS-Colgate"
DestDir="/toColgate"
SourceType="COL945"
DestType="col945"
PartnerName="Colgate"
ChepDestDir = "/toCHEP-Colgate"
ChepDestType="SHP"
CheckDirs()
ProcessFF()

SourceDir="/fromWMS-ColgateTest"
DestDir="/toColgate-Test"
SourceType="COL945"
DestType="col945"
PartnerName="Colgate-Test"
ChepDestDir = "/toCHEP-ColgateTest"
ChepDestType="SHP"
CheckDirs()
ProcessFF()

logfile.close()

sys.exit(0)
