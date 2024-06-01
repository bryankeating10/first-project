"""
Version 3
Completed May 17th, 2024
"""

from operator import add

class Player():
	def __init__(self,name):
		self.name = name
	
	# Data (Full Ring, Short Handed, Heads Up)
	hands = [[0,0],[0,0],[0,0]]
	vpip = [[0,0],[0,0],[0,0]]
	pfr = [[0,0],[0,0],[0,0]]
	threeB = [[0,0],[0,0],[0,0]]
	fourB = [[0,0],[0,0],[0,0]]
	cB = [[0,0],[0,0],[0,0]]
	doubBa = [[0,0],[0,0],[0,0]]
	tripBa = [[0,0],[0,0],[0,0]]
	af = [[0,0],[0,0],[0,0]]
	f2threeB = [[0,0],[0,0],[0,0]]
	f2cB = [[0,0],[0,0],[0,0]]
	f2dBa = [[0,0],[0,0],[0,0]]
	f2tBa = [[0,0],[0,0],[0,0]]
	wtsd = [[0,0],[0,0],[0,0]]

bryan = Player("cam")
sini = Player("sini")
sonny = Player("sonny")
drew = Player("drew")
subasa = Player("subasa")
marsh = Player("marsh")
bg = Player("bg")
pablo = Player("pablo")
pete = Player("pete")
mazz = Player("mazz")
jd = Player("jd")
scotty = Player("scotty")
zay = Player("zay")

def checkForData(dataList,stat):
	try:
		dataList[stat]
		return True
	except KeyError:
		return False

def updateData(playerName,sessionData,playerProfile):
	statList = ["2B","3B","3Ba","4B","AF","CB","F2B","F3","F3B","FC","H","PFR","VPIP","WTSD"]
	tableList = ["full ring","short handed","heads up"]
	for stat in statList:
		if checkForData(sessionData[stat],playerName):
			for inputPosition in range(3):
				table = tableList[inputPosition]
				if checkForData(sessionData[stat][playerName],table):
					if stat == "2B":
						playerProfile.doubBa[inputPosition] = list(map(add,playerProfile.doubBa[inputPosition],sessionData[stat][playerName][table]))
					elif stat == "3B":
						playerProfile.threeB[inputPosition] = list(map(add,playerProfile.threeB[inputPosition],sessionData[stat][playerName][table]))
					elif stat == "3Ba":
						playerProfile.tripBa[inputPosition] = list(map(add,playerProfile.tripBa[inputPosition],sessionData[stat][playerName][table]))
					elif stat == "4B":
						playerProfile.fourB[inputPosition] = list(map(add,playerProfile.fourB[inputPosition],sessionData[stat][playerName][table]))
					elif stat == "AF":
						playerProfile.af[inputPosition] = list(map(add,playerProfile.af[inputPosition],sessionData[stat][playerName][table]))
					elif stat == "CB":
						playerProfile.cB[inputPosition] = list(map(add,playerProfile.cB[inputPosition],sessionData[stat][playerName][table]))
					elif stat == "F2B":
						playerProfile.f2dBa[inputPosition] = list(map(add,playerProfile.f2dBa[inputPosition],sessionData[stat][playerName][table]))
					elif stat == "F3":
						playerProfile.f2threeB[inputPosition] = list(map(add,playerProfile.f2threeB[inputPosition],sessionData[stat][playerName][table]))
					elif stat == "F3B":
						playerProfile.f2tBa[inputPosition] = list(map(add,playerProfile.f2tBa[inputPosition],sessionData[stat][playerName][table]))
					elif stat == "FC":
						playerProfile.f2cB[inputPosition] = list(map(add,playerProfile.f2cB[inputPosition],sessionData[stat][playerName][table]))
					elif stat == "H":
						playerProfile.hands[inputPosition] = list(map(add,playerProfile.hands[inputPosition],sessionData[stat][playerName][table]))
					elif stat == "PFR":
						playerProfile.pfr[inputPosition] = list(map(add,playerProfile.pfr[inputPosition],sessionData[stat][playerName][table]))
					elif stat == "VPIP":
						playerProfile.vpip[inputPosition] = list(map(add,playerProfile.vpip[inputPosition],sessionData[stat][playerName][table]))
					elif stat == "WTSD":
						playerProfile.wtsd[inputPosition] = list(map(add,playerProfile.wtsd[inputPosition],sessionData[stat][playerName][table]))

def standardize_name(gameName, universalName,sessionData,cleanData):
	cleanedSessionData = cleanData
	for stat in sessionData:
		for name in sessionData[stat]:
			if name == gameName:
				storage = sessionData[stat][name]
				cleanedSessionData[stat][universalName] = storage
				
	return cleanedSessionData

def playerList(sessionData):
	names= []
	for stat in sessionData:
		for name in sessionData[stat]:
			if not(name in names):
				names.append(name)
	return(names)

def updateAllNames(orderedGameNames,orderedUniversalNames,sessionData):
	storageData = sessionData
	for i,j in zip(orderedGameNames,orderedUniversalNames):
		print("Game Name %s" % i)
		print("Universal Name %s" % j)
		storageData = standardize_name(i,j,sessionData,storageData)
	print(storageData)
	return storageData