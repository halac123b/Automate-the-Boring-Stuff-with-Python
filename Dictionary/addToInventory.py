def addToInventory(itemList, inventoryDict):
    for i in range(len(itemList)):
        inventoryDict.setdefault(itemList[i], 0)
        inventoryDict[itemList[i]] += 1
    return inventoryDict

inventoryDict = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inventoryDict = addToInventory(dragonLoot, inventoryDict)
print(inventoryDict)