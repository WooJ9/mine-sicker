#[인벤토리 넘버, 타워넘버, 팩토리 넘버]
# clickList=[None, None, None]
if LMBDown(event):
    if isInInventory():
        clickList[0] = WhatIsInventoryNum()
        if (clickList[0]!=None):
            #인벤토리 순서 바꾸기
            resetClickList()
        if (clickList[1]!=None):
            #타워에서 인벤토리로 이동
            resetClickList()
        if (clickList[2]!=None):
            inventoryAndFactory.addInventory(clickList[0], clickList[2])
            resetClickList()
    if isInFactory():
        if whatIsFactoryNum!=3:
            clickList[2] = whatIsFactoryNum()
            if (clickList[0]!=None):
                inventoryAndFactory.addFactory(inventoryNum, factoryNum)
                resetClickList()
            if (clickList[1]!=None):
                #타워에서 팩토리로 이동
                resetClickList()
            if (clickList[2]!=None):
                #팩토리에서 순서 바꾸기
                resetClickList()
        else:
            inventoryAndFactory.compoundLevelUp()#믹스도 넣어야함 나중에
    if isInStore():
        if whatIsStoreNum!=3:
            store.buy(shelf[whatIsStoreNum()])
        else:
            inventoryAndFactory.reroll()
    if isInTower():
        clickList[1] = whatIsTowerNum()
        if (clickList[0]!=None):
            #인벤토리에서 타워
            resetClickList()
        if (clickList[1]!=None):
            #타워끼리 바꾸기
            resetClickList()
        if (clickList[2]!=None):
            #팩토리에서 타워
            resetClickList()        



###################################################################
def isInInventory():
    mousepositon = mousePosition()
    if :
        return True

def whatIsInventoryNum():
    mousepositon = MousePosition()
    if():
        return 0
    if():
        return 1
    if():
        return 2
    if():
        return 3
    if():
        return 4
    if():
        return 5
    if():
        return 6
    if():
        return 7
    if():
        return 8

def isInFactory():
    mousepositon = mousePosition()
    if ():
        return True

def whatIsFactoryNum():
    mousepositon = mousePosition()
    if():
        return 0
    if():
        return 1
    if():
        return 2
    if():
        return 3#이건 버튼

def isInStore():
    mousepositon = mousePosition()
    if ():
        return True

def whatIsStoreNum():
    mousepositon = mousePosition()
    if():
        return 0
    if():
        return 1
    if():
        return 2
    if():
        return 3#이건 리롤 버튼

def isInTower():
    mousepositon = mousePosition()
    if ():
        return True

def whatIsTowerNum():
    mousepositon = mousePosition()

    if():
        return 0
    if():
        return 1
    if():
        return 2
    if():
        return 3
    if():
        return 4
    if():
        return 5
    
def towerToInventory():
    towerNum = whatIsTowerNum()
    if towerMaster[towerNum].element.price != 0:
        towerMaster[towerNum].element = storeinventory.element.Empty()

    inventoryNum = whatIsInventoryNum()
    


def resetClickList():
    clickList=[None, None, None]