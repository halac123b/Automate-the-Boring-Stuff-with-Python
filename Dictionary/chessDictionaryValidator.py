def isValidChessBoard(boardDict):
	black = {"total": 0, "king": 0, "pawn": 0}
	white = {"total": 0, "king": 0, "pawn": 0}
	for key in boardDict.keys():
		if boardDict[key][0] == "b":
			black["total"] += 1
		elif boardDict[key][0] == "w":
			white["pawn"] += 1
		if boardDict[key] == "bking":
			black["king"] += 1
		elif boardDict[key] == "wking":
			white["king"] += 1
		elif boardDict[key] == "bpawn":
			black["pawn"] += 1
		elif boardDict[key] == "wpawn":
			black["pawn"] += 1
		if int(key[0]) not in range(1, 9) or key[1] > "h" or key[1] < "a":
			return "Invalid coordinate of turn"

	if black["total"] > 16:
		return "Too many black one"
	elif white["total"] > 16:
		return "Too many white one"
	elif black["king"] != 1:
		return "Black king number not valid"
	elif white["king"] != 1:
		return "White king number not valid"
	elif black["pawn"] > 16:
		return "Too many black pawns"
	elif white["pawn"] > 16:
		return "Too many white pawns"

print(isValidChessBoard({'1h': 'bking', '6c':
'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '4d': "bking"}))
