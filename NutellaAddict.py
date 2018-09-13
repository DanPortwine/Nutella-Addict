import random
import time
import os
import winsound
from os import listdir
import colorama
from colorama import Fore, Back, Style
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
colorama.init()
blank = ""
pickTiles = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
mineTiles = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
huntTiles = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
grassSounds = ["grass1.wav","grass2.wav","grass3.wav","grass4.wav","grass5.wav"]
forestSounds = ["forest1.wav","forest2.wav","forest3.wav","forest4.wav","forest5.wav"]
stoneSounds = ["stone1.wav","stone2.wav","stone3.wav","stone4.wav"]
waterSounds = ["water1.wav","water2.wav","water3.wav"]
mountainSounds = ["mountain1.wav","mountain2.wav","mountain3.wav"]
def br():
    print("")
def debug():
    print("debug")
def clear():
    print("\n" * 80)
def mapLayoutCellAut(xLength,yLength,landChance,mapLayout,mapLayoutAlt,xyArea):
    for y in range(0,yLength):
        for x in range(0,xLength):
            tileCount = 0
            if mapLayout[x+(y*xLength)] == "░░" or mapLayout[x+(y*xLength)] == "██":
                tileCount = 0
                if x+(y*xLength) > 0:
                    if x+(y*xLength) % xLength != 0:
                        if mapLayout[(x+(y*xLength))-1] == "░░":
                            tileCount += 1
                    else:
                        if mapLayout[(x+(y*xLength)-1)+xLength] == "░░":
                            tileCount += 1
                if x+(y*xLength) < xyArea:
                    if x+(y*xLength) % xLength != xLength -1:
                        if mapLayout[(x+(y*xLength))+1] == "░░":
                            tileCount += 1
                    else:
                        if mapLayout[(x+(y*xLength)+1)-xLength] == "░░":
                            tileCount += 1
                if x+(y*xLength) >= xLength:
                    if mapLayout[(x+(y*xLength))-xLength] == "░░":
                        tileCount += 1
                if x+(y*xLength) < xyArea - xLength:  
                    if mapLayout[(x+(y*xLength))+xLength] == "░░":
                        tileCount += 1
                if x+(y*xLength) > xLength:
                    if x+(y*xLength) % xLength != 0:
                        if mapLayout[((x+(y*xLength))-1)-xLength] == "░░":
                            tileCount += 1
                    else:
                        if mapLayout[x+(y*xLength)-1] == "░░":
                            tileCount += 1
                if x+(y*xLength) > xLength:
                    if x+(y*xLength) % xLength != xLength-1:
                        if mapLayout[x+(y*xLength)+1-xLength] == "░░":
                            tileCount += 1
                    else:
                        if mapLayout[x+(y*xLength)+1-(xLength*2)] == "░░":
                            tileCount += 1
                if x+(y*xLength) < xyArea - xLength:
                    if x+(y*xLength) % xLength != 0:
                        if mapLayout[((x+(y*xLength))-1)+xLength] == "░░":
                            tileCount += 1
                    else:
                        if x+(y*xLength) % xLength != xLength-1:
                            tileCount += 1
                if x+(y*xLength) < xyArea - xLength:
                    if x+(y*xLength) % xLength != xLength-1:
                        if mapLayout[x+(y*xLength)+1+xLength] == "░░":
                            tileCount += 1
                    else:
                        if mapLayout[x+(y*xLength)+1] == "░░":
                            tileCount += 1
            if tileCount > landChance:
                mapLayoutAlt[x+(y*xLength)] = "░░"
            else:
                mapLayoutAlt[x+(y*xLength)] = "██"
def mapLayoutAltCellAut(xLength,yLength,landChance,mapLayout,mapLayoutAlt,xyArea):
    for y in range(0,yLength):
        for x in range(0,xLength):
            tileCount = 0
            if mapLayoutAlt[x+(y*xLength)] == "░░" or mapLayoutAlt[x+(y*xLength)] == "██":
                tileCount = 0
                if x+(y*xLength) > 0:
                    if x+(y*xLength) % xLength != 0:
                        if mapLayoutAlt[(x+(y*xLength))-1] == "░░":
                            tileCount += 1
                    else:
                        if mapLayoutAlt[(x+(y*xLength)-1)+xLength] == "░░":
                            tileCount += 1
                if x+(y*xLength) < xyArea:
                    if x+(y*xLength) % xLength != xLength -1:
                        if mapLayoutAlt[(x+(y*xLength))+1] == "░░":
                            tileCount += 1
                    else:
                        if mapLayoutAlt[(x+(y*xLength)+1)-xLength] == "░░":
                            tileCount += 1
                if x+(y*xLength) >= xLength:
                    if mapLayoutAlt[(x+(y*xLength))-xLength] == "░░":
                        tileCount += 1
                if x+(y*xLength) < xyArea - xLength:  
                    if mapLayoutAlt[(x+(y*xLength))+xLength] == "░░":
                        tileCount += 1
                if x+(y*xLength) > xLength:
                    if x+(y*xLength) % xLength != 0:
                        if mapLayoutAlt[((x+(y*xLength))-1)-xLength] == "░░":
                            tileCount += 1
                    else:
                        if mapLayoutAlt[x+(y*xLength)-1] == "░░":
                            tileCount += 1
                if x+(y*xLength) > xLength:
                    if x+(y*xLength) % xLength != xLength-1:
                        if mapLayoutAlt[x+(y*xLength)+1-xLength] == "░░":
                            tileCount += 1
                    else:
                        if mapLayoutAlt[x+(y*xLength)+1-(xLength*2)] == "░░":
                            tileCount += 1
                if x+(y*xLength) < xyArea - xLength:
                    if x+(y*xLength) % xLength != 0:
                        if mapLayoutAlt[((x+(y*xLength))-1)+xLength] == "░░":
                            tileCount += 1
                    else:
                        if mapLayoutAlt[((x+(y*xLength))-1)+(2*xLength)] == "░░":
                            tileCount += 1
                if x+(y*xLength) < xyArea - xLength:
                    if x+(y*xLength) % xLength != xLength-1:
                        if mapLayoutAlt[x+(y*xLength)+1+xLength] == "░░":
                            tileCount += 1
                    else:
                        if mapLayoutAlt[x+(y*xLength)+1] == "░░":
                            tileCount += 1
            if tileCount > landChance:
                mapLayout[x+(y*xLength)] = "░░"
            else:
                mapLayout[x+(y*xLength)] = "██"
def displayMap(xLength,yLength,mapLayoutFinal):
    if xLength <= maxWidth and yLength <= maxHeight:
        count = 0
        for y in range(0,yLength):
            for x in range(0,xLength):
                tile = mapLayoutFinal[count]
                if tile == "██":
                    print(Fore.BLUE + tile + Style.RESET_ALL,end="")
                elif tile == "■■":
                    print(Fore.WHITE + Back.GREEN + tile + Style.RESET_ALL,end="")
                elif tile == "▒▒":
                    print(Fore.WHITE + Back.BLACK + tile + Style.RESET_ALL,end="")
                elif tile == "░░":
                    print(Fore.BLACK + Back.GREEN + tile + Style.RESET_ALL,end="")
                elif tile == "▓▓":
                    print(Fore.BLACK + Back.GREEN + tile + Style.RESET_ALL,end="")
                count += 1
            br()
        displayTileTypes()
    else:
        time.sleep(0.5)
        print("Your map is too big to display on this window size\n"
              "If you want to see the full map, make one that is less than " + str(maxWidth) + " x " + str(maxHeight) + "\n"
              "Or increase your window size under 'options' from the main menu")
        time.sleep(1)
        input("Hit enter to continue...")
        br()
def displayTileTypes():
    print("Tile types:")
    grass = "░░"
    print(Fore.BLACK + Back.GREEN + grass + Style.RESET_ALL,end="")
    print("  Grassland",end="  |  ")
    stone = "▒▒"
    print(Back.BLACK + Fore.WHITE + stone + Style.RESET_ALL,end="")
    print("  Stone",end="  |  ")
    forest = "▓▓"
    print(Fore.BLACK + Back.GREEN + forest + Style.RESET_ALL,end="")
    print("  Forest",end="  |  ")
    mountain = "■■"
    print(Fore.WHITE + Back.GREEN + mountain + Style.RESET_ALL,end="")
    print("  Mountain",end="  |  ")
    water = "██"
    print(Fore.BLUE + water + Style.RESET_ALL,end="")
    print("  Water\n")
def printMapsTable(maps):
    print("These are the maps you have available:")
    print(" ╔══════╦",end="")
    for i in range(0,34):
        print("═",end="")
    print("╗")   
    #title row
    print(" ║  ID "
          " ║",end="")
    for i in range(0,15):
        print(" ",end="")
    print("Name",end="")
    for i in range(0,15):
        print(" ",end="")
    print("║") 
    #title row bottom border
    print(" ╠══════╬",end="")
    for i in range(0,34):
        print("═",end="")  
    print("╣")
    count = 0
    for i in listdir("maps"):
        count += 1
        maps.append(i)
    count = 1
    sizes = ["B","kB","MB","GB","TB"]
    sizesIndex = 0
    for i in range(0,len(maps)):
        fileSize = float(os.stat("maps/"+maps[i]).st_size)
        sizesIndex = 0
        while fileSize > 1024:
            sizesIndex += 1
            fileSize /= 1024
        fileSize = str(fileSize)[:5]
        fileSize = str(fileSize)+" "+sizes[sizesIndex]
        #print(fileSize)
        if i > 9:
            print(" ║",count,"  ║",maps[i],"("+fileSize+")",end="")
        if i < 10:
            print(" ║",count,"   ║",maps[i],"("+fileSize+")",end="")
        for i in range(0,33 - (len(maps[i]) + len(sizes[sizesIndex]) + 9)):
            print(" ",end="")
        print("║")
        count += 1
    #bottom border
    print(" ╚══════╩",end="")
    for i in range(0,34):
        print("═",end="")
    print("╝\n")
def isBannedChar(string):
    bannedChars = ['\\','/',':','*','?','"','<','>','|']
    for i in string:
        if i in bannedChars:
            return 1
def saveMapToFile(xLength,yLength,mapLayoutFinal):
    saveMap = input("Do you want to save this map to a file to use in-game? (y/n): ")
    winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
    while saveMap != 'y' and saveMap != 'n':
        print("Invalid!")
        saveMap = input("Do you want to save this map to a file to use in-game? (y/n): ")
        winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
    br()
    if saveMap.lower() == "y":
        mapName = input("What do you want to call your map? (no longer than 10 characters): ")
        winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
        while len(mapName) > 10 or len(mapName) == 0 or isBannedChar(mapName) == 1:
            print("Invalid!")
            mapName = input("What do you want to call your map? (no longer than 10 characters): ")
            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
        mapData = []
        mapData.append(str(landChance))
        mapData.append(str(xLength))
        mapData.append(str(yLength))
        for i in mapLayoutFinal:
            if i == "░░":
                mapData.append("1")
            elif i == "▒▒":
                mapData.append("2")
            elif i == "▓▓":
                mapData.append("3")
            elif i == "■■":
                mapData.append("5")
            elif i == "██":
                mapData.append("6")
        file = open("maps/"+mapName+".csv","w")
        for i in range(0,len(mapData)):
            file.write(mapData[i])
            if i != len(mapData)-1:
                file.write(",")
            else:
                file.write("")
        file.close()
def tileGeneration(mapLayout,mapData):
    landCount = 0
    for i in mapLayout:
        if i == "░░":
            landCount += 1
    mapData = []
    for i in range(0,int(landCount * 0.5)):
        mapData.append("░░")
    for i in range(0,int(landCount * 0.2)):
        mapData.append("▒▒")
    for i in range(0,int(landCount * 0.2)):
        mapData.append("▓▓")
    for i in range(0,int(landCount * 0.1)):
        mapData.append("■■")
    for i in range(0,len(mapLayout)):
        if mapLayout[i] == "░░":
            mapLayout[i] = mapData[random.randint(0,len(mapData) - 1)]
def tileGenerationAlt(mapLayoutAlt,mapData):
    landCount = 0
    for i in mapLayoutAlt:
        if i == "░░":
            landCount += 1
    mapData = []
    for i in range(0,int(landCount * 0.6)):
        mapData.append("░░")
    for i in range(0,int(landCount * 0.2)):
        mapData.append("▒▒")
    for i in range(0,int(landCount * 0.2)):
        mapData.append("▓▓")
    for i in range(0,int(landCount * 0.1)):
        mapData.append("■■")
    for i in range(0,len(mapLayout)):
        if mapLayoutAlt[i] == "░░":
            mapLayoutAlt[i] = mapData[random.randint(0,len(mapData) - 1)]
def footstepSound():
    if mapLayoutFinal[playerPos] == "░░":
        grassSound = str("sounds/"+random.choice(grassSounds))
        winsound.PlaySound(grassSound,winsound.SND_ASYNC)
    elif mapLayoutFinal[playerPos] == "▒▒":
        stoneSound = str("sounds/"+random.choice(stoneSounds))
        winsound.PlaySound(stoneSound,winsound.SND_ASYNC)
    elif mapLayoutFinal[playerPos] == "▓▓":
        forestSound = str("sounds/"+random.choice(forestSounds))
        winsound.PlaySound(forestSound,winsound.SND_ASYNC)
    elif mapLayoutFinal[playerPos] == "■■":
        mountainSound = str("sounds/"+random.choice(mountainSounds))
        winsound.PlaySound(mountainSound,winsound.SND_ASYNC)
    elif mapLayoutFinal[playerPos] == "██":
        waterSound = str("sounds/"+random.choice(waterSounds))
        winsound.PlaySound(waterSound,winsound.SND_ASYNC)
def setColour(tile):
    if tile == "██":
        print(Fore.BLUE + tile + Style.RESET_ALL, end="")
    elif tile == "■■":
        print(Fore.WHITE + Back.GREEN + tile + Style.RESET_ALL, end="")
    elif tile == "▒▒":
        print(Fore.WHITE + Back.BLACK + tile + Style.RESET_ALL, end="")
    elif tile == "░░":
        print(Fore.BLACK + Back.GREEN + tile + Style.RESET_ALL, end="")
    elif tile == "▓▓":
        print(Fore.BLACK + Back.GREEN + tile + Style.RESET_ALL, end="")
def setColourEnd(tile):
    if tile == "██":
        print(Fore.BLUE + tile + Style.RESET_ALL)
    elif tile == "■■":
        print(Fore.WHITE + Back.GREEN + tile + Style.RESET_ALL)
    elif tile == "▒▒":
        print(Fore.WHITE + Back.BLACK + tile + Style.RESET_ALL)
    elif tile == "░░":
        print(Fore.BLACK + Back.GREEN + tile + Style.RESET_ALL)
    elif tile == "▓▓":
        print(Fore.BLACK + Back.GREEN + tile + Style.RESET_ALL)
def setTitle(line):
    for i in line:
        if i == "█":
            print(Fore.GREEN + Style.BRIGHT + i + Style.RESET_ALL, end="")
        elif i == "╗" or i == "║" or i == "╚" or i == "═" or i == "╔" or i == "╝":
            print(Fore.MAGENTA + Style.BRIGHT + i + Style.RESET_ALL, end="")
        else:
            print(" ", end="")
    print("")
def saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread):
    file = open("saves/"+mapName.strip(".csv")+".txt","w")
    file.write(mapName+",")
    file.write(str(playerPos)+",")
    file.write(str(health)+",")
    file.write(str(hunger)+",")
    file.write(str(thirst)+",")
    file.write(str(jarPos)+",")
    file.write(str(boat)+",")
    file.write(str(rope)+",")
    file.write(str(breadstick)+",")
    file.write(str(nutellaJar)+",")
    file.write(str(jarFound)+",")
    file.write(str(spear)+",")
    file.write(str(axe)+",")
    file.write(str(picaxe)+",")
    file.write(str(rod)+",")
    file.write(str(bow)+",")
    file.write(str(digTool)+",")
    file.write(str(arrows)+",")
    file.write(str(spearheads)+",")
    file.write(str(arrowheads)+",")
    file.write(str(digheads)+",")
    file.write(str(axeheads)+",")
    file.write(str(picheads)+",")
    file.write(str(trig)+",")
    file.write(str(stones)+",")
    file.write(str(rocks)+",")
    file.write(str(logs)+",")
    file.write(str(sticks)+",")
    file.write(str(clay)+",")
    file.write(str(fibres)+",")
    file.write(str(fish)+",")
    file.write(str(water)+",")
    file.write(str(feathers)+",")
    file.write(str(meat)+",")
    file.write(str(hazelnuts)+",")
    file.write(str(berries)+",")
    file.write(str(wheat)+",")
    file.write(str(bucket)+",")
    file.write(str(sugar)+",")
    file.write(str(juice)+",")
    file.write(str(bread))
    file.close()
def saveGeneral(gamesCompleted,hasSetSize,shape):
    file = open("saves/general.txt","w")
    file.write(str(gamesCompleted)+",")
    file.write(str(hasSetSize)+",")
    file.write(str(shape))
    file.close()
def isInteger(string):
    integers = ['0','1','2','3','4','5','6','7','8','9']
    for i in string:
        if str(i) not in integers:
            return 0
def setSize(choice):
    global maxWidth
    global maxHeight
    global shape
    if choice == 0:
        print("These are the sizes you can choose:\n"
              " 1 - 120 x 30\n"
              " 2 - 120 x 40\n"
              " 3 - 120 x 60\n"
              " 4 - 200 x 30\n"
              " 5 - 200 x 40\n"
              " 6 - 200 x 60\n"
              " 7 - 300 x 50\n"
              " 8 - 300 x 60\n"
              " 9 - 300 x 100\n"
              " 0 - Return")
        shapePrev = shape
        shape = input("Enter your desired size: ")
        winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
        while shape != "1" and shape != "2" and shape != "3" and shape != "4" and shape != "5" and shape != "6" and shape != "7" and shape != "8" and shape != "9" and shape != "0":
            shape = input("Enter your desired size: ")
            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
    else:
        shape = str(choice)
    if shape == "0":
        shape = shapePrev
        saveGeneral(gamesCompleted,hasSetSize,shape)
        pass
    elif shape == "1":
        os.system("mode con cols=120 lines=30")
        maxWidth = 59
        maxHeight = 25
    elif shape == "2":
        os.system("mode con cols=120 lines=40")
        maxWidth = 59
        maxHeight = 35
    elif shape == "3":
        os.system("mode con cols=120 lines=60")
        maxWidth = 59
        maxHeight = 55
    elif shape == "4":
        os.system("mode con cols=200 lines=30")
        maxWidth = 99
        maxHeight = 25
    elif shape == "5":
        os.system("mode con cols=200 lines=40")
        maxWidth = 99
        maxHeight = 35
    elif shape == "6":
        os.system("mode con cols=200 lines=60")
        maxWidth = 99
        maxHeight = 55
    elif shape == "7":
        os.system("mode con cols=300 lines=30")
        maxWidth = 149
        maxHeight = 25
    elif shape == "8":
        os.system("mode con cols=300 lines=40")
        maxWidth = 149
        maxHeight = 35
    elif shape == "9":
        os.system("mode con cols=300 lines=60")
        maxWidth = 149
        maxHeight = 55
def showTitle(maxWidth):
    spaces = int(maxWidth + 1) - 54
    line1 = " " * spaces + "███╗   ██╗██╗   ██╗████████╗███████╗██╗     ██╗      █████╗      █████╗ ██████╗ ██████╗ ██╗ ██████╗████████╗"
    line2 = " " * spaces + "████╗  ██║██║   ██║╚══██╔══╝██╔════╝██║     ██║     ██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝"
    line3 = " " * spaces + "██╔██╗ ██║██║   ██║   ██║   █████╗  ██║     ██║     ███████║    ███████║██║  ██║██║  ██║██║██║        ██║   "
    line4 = " " * spaces + "██║╚██╗██║██║   ██║   ██║   ██╔══╝  ██║     ██║     ██╔══██║    ██╔══██║██║  ██║██║  ██║██║██║        ██║   "
    line5 = " " * spaces + "██║ ╚████║╚██████╔╝   ██║   ███████╗███████╗███████╗██║  ██║    ██║  ██║██████╔╝██████╔╝██║╚██████╗   ██║   "
    line6 = " " * spaces + "╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝ ╚═════╝   ╚═╝   "
    setTitle(line1)
    time.sleep(0.05)
    setTitle(line2)
    time.sleep(0.05)
    setTitle(line3)
    time.sleep(0.05)
    setTitle(line4)
    time.sleep(0.05)
    setTitle(line5)
    time.sleep(0.05)
    setTitle(line6)
    time.sleep(0.05)
def showControls(loc):
    clear()
    time.sleep(0.5)
    print("\nControls (recommended to use the numpad):\n"
          "  7 - Left Up    8 - Up       9 - Right Up\n\n"
          "  4 - Left                    6 - Right\n\n"
          "  1 - Left Down  2 - Down     3 - Right Down\n\n\n"
          "  c - Controls   i - Inventory   q - Quit\n"
          "  l - Use Trig Point   f - Food/Drink\n"
          "  p - Pick up on tile   m - Mine tile   h - Hunt on tile\n\n")
    time.sleep(2)
    print("Instructions:\n"
          " The aim of the game is to find the jar and craft a jar of Nutella\n"
          " The jar spawns on a random tile\n"
          " Using a Trig Point will show you how far away the jar is from that Trig Point's position\n"
          " You can craft various items to aid you in your quest\n"
          " A boat allows you to travel across water\n"
          " A rope allows you to travel over mountains\n"
          " Each time you move, you use 1 hunger and 1 thirst\n"
          " If your hunger or thirst is below 5, you start losing health each move\n"
          " If your hunger and thirst are both above 50, you start recovering health\n"
          " If your health reaches 0, you die and the map is reset\n"
          " The tile you are on and the surrounding 5x5 square of tiles are shown after every move\n"
          " You must hit 'enter' after typing your move number in order to make the move\n"
          " You progress in a map is automatically saved each time you move\n"
          " The map is reset once you complete a game in it\n\n")
    time.sleep(3)
    displayTileTypes()
    time.sleep(2)
    input("Hit enter to return to the " + loc + "...")
def credits():
    for i in range(0, 110):
        if i == 5:
            print("    Developer: DubWine")
        elif i == 10:
            print("    With special thanks to:")
        elif i == 13:
            print("        FlubbaJubba")
        elif i == 15:
            print("        Professor")
        elif i == 20:
            print("    Libraries used:")
        elif i == 23:
            print("        time")
        elif i == 25:
            print("        random")
        elif i == 28:
            print("        os")
        elif i == 31:
            print("        listdir")
        elif i == 34:
            print("        winsound")
        elif i == 37:
            print("        colorama")
        elif i == 40:
            print("        smtplib")
        elif i == 43:
            print("        MIMEMultipart")
        elif i == 46:
            print("        MIMEText")
        else:
            br()
        time.sleep(0.2)
def showSurroundings():
    #middle rows
    if playerPos > (2 * xLength) - 1 and playerPos < xyArea - (2 * xLength):
        #left column
        if playerPos % xLength == 0:
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(3*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(3*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+(2*xLength)]
            setColourEnd(tile)
        #left inner column
        elif playerPos % xLength == 1:
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(3*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+(2*xLength)]
            setColourEnd(tile)
        #right column
        elif playerPos % xLength == xLength - 1:
            tile = mapLayoutFinal[playerPos-2-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(3*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(3*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
        #right inner column
        elif playerPos % xLength == xLength - 2:
            tile = mapLayoutFinal[playerPos-2-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(3*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
        #middle columns
        else:
            tile = mapLayoutFinal[playerPos-2-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+(2*xLength)]
            setColourEnd(tile)
    #top row
    elif playerPos < xLength:
        print("XXXXXXXXXX\nXXXXXXXXXX")
        #left column
        if playerPos % xLength == 0:
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(3*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(3*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+(2*xLength)]
            setColourEnd(tile)
        #left inner coloumn
        elif playerPos % xLength == 1:
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(3*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+(2*xLength)]
            setColourEnd(tile)
        #right column
        elif playerPos % xLength == xLength - 1:
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
        #right inner columns
        elif playerPos % xLength == xLength - 2:
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
        #middle columns
        else:
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+(2*xLength)]
            setColourEnd(tile)
    #top row inner
    elif playerPos < (2 * xLength) and playerPos >= xLength:
        #left column
        print("XXXXXXXXXX")
        if playerPos % xLength == 0:
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(3*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(3*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+(2*xLength)]
            setColourEnd(tile)
        #left inner column
        elif playerPos % xLength == 1:
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(3*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+(2*xLength)]
            setColourEnd(tile)
        #right column
        elif playerPos % xLength == xLength - 1:
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
        #right inner column
        elif playerPos % xLength == xLength - 2:
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
        #middle columns
        else:
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+(2*xLength)]
            setColourEnd(tile)
    #bottom row
    elif playerPos >= xyArea - xLength:
        #left coloumn
        if playerPos % xLength == 0:
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
        #left inner column
        elif playerPos % xLength == 1:
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
        #right column
        elif playerPos % xLength == xLength - 1:
            tile = mapLayoutFinal[playerPos-2-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(3*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(3*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
        #right inner column
        elif playerPos % xLength == xLength - 2:
            tile = mapLayoutFinal[playerPos-2-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-(2*xLength)]
            setColour(tile)
            tiel = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(3*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
        #middle columns
        else:
            tile = mapLayoutFinal[playerPos-2-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
        print("XXXXXXXXXX\nXXXXXXXXXX")
    #bottom row inner
    elif playerPos >= xyArea - (2*xLength) and playerPos <= xyArea - xLength:
        #left column
        if playerPos % xLength == 0:
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
        #left inner column
        elif playerPos % xLength == 1:
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
        #right column
        elif playerPos % xLength == xLength - 1:
            tile = mapLayoutFinal[playerPos-2-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(3*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(3*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
        #right inner column
        elif playerPos % xLength == xLength - 2:
            tile = mapLayoutFinal[playerPos-2-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(3*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
        #middle columns
        else:
            tile = mapLayoutFinal[playerPos-2-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-(2*xLength)]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-(2*xLength)]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1-xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2-xLength]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2]
            setColourEnd(tile)
            tile = mapLayoutFinal[playerPos-2+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos-1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+1+xLength]
            setColour(tile)
            tile = mapLayoutFinal[playerPos+2+xLength]
            setColourEnd(tile)
        print("XXXXXXXXXX")
file = open("saves/general.txt","r")
for line in file:
    data = line.split(",")
gamesCompleted = int(data[0])
hasSetSize = int(data[1])
shape = int(data[2])
file.close()
if hasSetSize == 0:
    setSize(0)
    hasSetSize = 1
    time.sleep(1)
    saveGeneral(gamesCompleted,hasSetSize,shape)
else:
    setSize(shape)
print("V2.0 - Alpha")
winsound.PlaySound("sounds/creditsShort.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
#time.sleep(1)
clear()
for i in range(0,(maxHeight+5)+20):
    if i == 10:
        showTitle(maxWidth)
    elif i == int((maxHeight+5)*0.6) + 6:
        time.sleep(1)
    else:
        br()
    time.sleep(0.1)
loadBar = "█"
hang = []
for i in range(0, random.randint(2, 5)):
    hang.append(random.randint(50, (maxWidth - 1) * 2))
for i in range(0, (maxWidth + 1) * 2):
    if i in hang:
        time.sleep(random.uniform(0, 0.3))
    else:
        time.sleep(random.uniform(0, 0.3 / maxWidth))
    print(Fore.GREEN + loadBar + Style.RESET_ALL, end="")
time.sleep(0.5)
#main menu
while True:
    clear()
    time.sleep(0.5)
    mainMenu = input("Main menu:\n"
                         " 1 - Begin game\n"
                         " 2 - Map creator\n"
                         " 3 - Instructions\n"
                         " 4 - Options\n"
                         " 5 - Support/feedback\n"
                         " 6 - Exit\n"
                         "Enter the option you want to do: ")
    winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
    while mainMenu != "1" and mainMenu != "2" and mainMenu != "3" and mainMenu != "4" and mainMenu != "5" and mainMenu != "6":
        print("Invalid!")
        mainMenu = input("Enter the option you want to do: ")
        winsound.PlaySound("sounds/click.wav",winsound.SND_ASYNC)
    if mainMenu == '6':
        saveGeneral(gamesCompleted,hasSetSize,shape)
        break
    clear()
    mainMenu = int(mainMenu)
    if mainMenu == 1:
        gameCompleted = 0
        finishGame = 0
        dead = 0
        time.sleep(0.5)
        while True:
            maps = []
            mapLayoutFinal = []
            time.sleep(0.5)
            printMapsTable(maps)
            mapToLoad = input("Enter the ID of the map you want to load (0 to Return): ")
            winsound.PlaySound("sounds/click.wav",winsound.SND_ASYNC)
            mapIDs = []
            for i in range(0,len(os.listdir("maps"))+1):
                mapIDs.append(str(i))
            while mapToLoad not in mapIDs:
                print("Invalid!")
                mapToLoad = input("Enter the ID of the map you want to load (0 to Return): ")
                winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
            mapToLoad = int(mapToLoad)
            if mapToLoad == 0:
                break
            clear()
            time.sleep(0.5)
            global mapName
            mapName = maps[mapToLoad - 1]
            file = open("maps/"+mapName,"r")
            br()
            for line in file:
                data = line.split(",")
                landChance = int(data[0])
                xLength = int(data[1])
                yLength = int(data[2])
                xyArea = xLength * yLength
                for i in range(3,len(data)):
                    if data[i] == "1":
                        mapLayoutFinal.append("░░")
                    elif data[i] == "2":
                        mapLayoutFinal.append("▒▒")
                    elif data[i] == "3":
                        mapLayoutFinal.append("▓▓")
                    elif data[i] == "5":
                        mapLayoutFinal.append("■■")
                    elif data[i] == "6":
                        mapLayoutFinal.append("██")
            file.close()
            time.sleep(0.5)
            if xLength <= maxWidth and yLength <= maxHeight:
                displayMap(xLength,yLength,mapLayoutFinal)
            else:
                print("Your map is too big to display on this window size\n"
                      "If you want to see the full map, make one that is less than " + str(maxWidth) + " x " + str(maxHeight) + "\n"
                      "Or increase your window size under 'options' from the main menu")
            time.sleep(0.5)
            input("Hit enter to begin game...")
            time.sleep(0.5)
            landTilesPositions = []
            for i in range(0, len(mapLayoutFinal)):
                if mapLayoutFinal[i] != "██" and mapLayoutFinal[i] != "■■" and mapLayoutFinal[i] != "╠╣":
                    landTilesPositions.append(i)
            saveFound = 0
            for i in os.listdir("saves"):
                if str(i) == str(mapName.strip(".csv")+".txt"):
                    file = open("saves/"+i,"r")
                    for line in file:
                        data = line.split(",")
                    playerPos = int(data[1])
                    health = int(data[2])
                    hunger = int(data[3])
                    thirst = int(data[4])
                    jarPos = int(data[5])
                    boat = int(data[6])
                    rope = int(data[7])
                    breadstick = int(data[8])
                    nutellaJar = int(data[9])
                    jarFound = int(data[10])
                    spear = int(data[11])
                    axe = int(data[12])
                    picaxe = int(data[13])
                    rod = int(data[14])
                    bow = int(data[15])
                    digTool = int(data[16])
                    arrows = int(data[17])
                    spearheads = int(data[18])
                    arrowheads = int(data[19])
                    digheads = int(data[20])
                    axeheads = int(data[21])
                    picheads = int(data[22])
                    trig = int(data[23])
                    stones = int(data[24])
                    rocks = int(data[25])
                    logs = int(data[26])
                    sticks = int(data[27])
                    clay = int(data[28])
                    fibres = int(data[29])
                    fish = int(data[30])
                    water = int(data[31])
                    feathers = int(data[32])
                    meat = int(data[33])
                    hazelnuts = int(data[34])
                    berries = int(data[35])
                    wheat = int(data[36])
                    bucket = int(data[37])
                    sugar = int(data[38])
                    juice = int(data[39])
                    bread = int(data[40])
                    saveFound = 1
                    clear()
                    time.sleep(0.5)
                    print("Your quest continues")
                    file.close()
                    break
            if saveFound == 0:
                playerPos = random.choice(landTilesPositions)
                health = 100
                hunger = 50
                thirst = 50
                jarPos = random.randint(0,len(mapLayoutFinal)-1)
                boat = 0
                rope = 0
                breadstick = 0
                nutellaJar = 0
                jarFound = 0
                spear = 0
                axe = 0
                picaxe = 0
                rod = 0
                bow = 0
                digTool = 0
                arrows = 0
                spearheads = 0
                arrowheads = 0
                digheads = 0
                axeheads = 0
                picheads = 0
                trig = 0
                stones = 0
                rocks = 0
                logs = 0
                sticks = 0
                clay = 0
                fibres = 0
                fish = 0
                water = 0
                feathers = 0
                meat = 0
                hazelnuts = 0
                berries = 0
                wheat = 0
                bucket = 0
                sugar = 0
                juice = 0
                bread = 0
                clear()
                time.sleep(0.5)
                print("Your quest has begun")
            time.sleep(1)
            while True:
                if playerPos == jarPos and jarFound == 0:
                    time.sleep(1.5)
                    winsound.PlaySound("sounds/pickupSpecial.wav",winsound.SND_ASYNC)
                    print("You have found the jar")
                    jarFound = 1
                    time.sleep(2)
                if finishGame == 1:
                    if dead == 0:
                        confirm = input("Confirm:\n"
                                        " 1 - Complete the game and reset the map\n"
                                        " 2 - Return to game and complete later\n"
                                        "Enter your choice: ")
                        winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                        while confirm != "1" and confirm != "2":
                            print("Invalid!")
                            time.sleep(0.5)
                            confirm = input("Enter your choice: ")
                            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                        if confirm == "1":
                            gameCompleted = 1
                            gamesCompleted += 1
                            for i in os.listdir("saves"):
                                if i == str(mapName.strip(".csv") + ".txt"):
                                    os.remove("saves/"+i)
                            time.sleep(2)
                            print("You open the jar of Nutella")
                            winsound.PlaySound("sounds/openNutella.wav", winsound.SND_ASYNC)
                            time.sleep(1)
                            print("You dunk the breadstick in the Nutella")
                            time.sleep(1)
                            print("You eat the Nutella covered breadstick")
                            for i in range(0,2):
                                winsound.PlaySound("sounds/biteBreadstick.wav", winsound.SND_ASYNC)
                                time.sleep(4)
                            time.sleep(1)
                            print("You have completed your quest and ascend to the land of Nutella")
                            winsound.PlaySound("sounds/ascension.wav", winsound.SND_ASYNC)
                            time.sleep(9)
                            clear()
                            winsound.PlaySound("sounds/creditsShort.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
                            credits()
                            break
                        elif confirm == "2":
                            print("Returning to game...")
                            time.sleep(0.5)
                            clear()
                            time.sleep(0.5)
                    elif dead == 1:
                        gameCompleted = 1
                        for i in os.listdir("saves"):
                            if i == str(mapName.strip(".csv") + ".txt"):
                                os.remove("saves/"+i)
                        time.sleep(2)
                        print("You failed to survive!")
                        time.sleep(3)
                        clear()
                        time.sleep(0.5)
                        print("That is rather dissapointing!")
                        time.sleep(3)
                        clear()
                        time.sleep(0.5)
                        print("Better luck next time!")
                        time.sleep(3)
                        clear()
                        winsound.PlaySound("sounds/creditsShort.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
                        credits()
                        break
                hungerMsg = ""
                if hunger < 20 and hunger >= 5:
                    hungerMsg = "You are hungry!"
                elif hunger < 5:
                    hungerMsg = "You are starving!"
                thirstMsg = ""
                if thirst < 20 and thirst >= 5:
                    thirstMsg = "You are thirsty!"
                elif thirst < 5:
                    thirstMsg = "You are dehydrated!"
                print("Health: "+str(health)+"/100")
                print("Hunger: "+str(hunger)+"/100  "+hungerMsg)
                print("Thirst: "+str(thirst)+"/100  "+thirstMsg)
                showSurroundings()
                footstepSound()
                saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                move = input(": ")
                while move != "1" and move != "2" and move != "3" and move != "4" and move != "6" and move != "7" and move != "8" and move != "9" and move.lower() != "c" and move.lower() != "q" and move.lower() != "i" and move.lower() != "p" and move.lower() != "m" and move.lower() != "l" and move.lower() != "f" and move.lower() != "h":
                    clear()
                    print("Invalid!")
                    time.sleep(0.5)
                    clear()
                    hungerMsg = ""
                    if hunger < 20 and hunger >= 5:
                        hungerMsg = "You are hungry!"
                    elif hunger < 5:
                        hungerMsg = "You are starving!"
                    thirstMsg = ""
                    if thirst < 20 and thirst >= 5:
                        thirstMsg = "You are thirsty!"
                    elif thirst < 5:
                        thirstMsg = "You are dehydrated!"
                    print("Health: " + str(health) + "/100")
                    print("Hunger: " + str(hunger) + "/100  " + hungerMsg)
                    print("Thirst: " + str(thirst) + "/100  " + thirstMsg)
                    showSurroundings()
                    time.sleep(0.5)
                    move = input(": ")
                if move.lower() == "q":
                    gameCompleted = 1
                    break
                elif move.lower() == "c":
                    showControls("your game")
                elif move.lower() == "i":
                    clear()
                    time.sleep(0.5)
                    invMenu = "1"
                    while invMenu != "4":
                        saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                        if nutellaJar == 0:
                            invMenu = input("Inventory:\n"
                                            " 1 - Crafting\n"
                                            " 2 - Inventory\n"
                                            " 3 - Return to game\n"
                                            "Enter your choice: ")
                            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                            while invMenu != "1" and invMenu != "2" and invMenu != "3":
                                print("Invalid!")
                                invMenu = input("Enter your choice: ")
                                winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                        else:
                            invMenu = input("Inventory:\n"
                                            " 1 - Crafting\n"
                                            " 2 - Inventory\n"
                                            " 3 - Return to game\n"
                                            " 4 - Finish the game\n"
                                            "Enter your choice:")
                            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                            while invMenu != "1" and invMenu != "2" and invMenu != "3" and invMenu != "4":
                                print("Invalid!")
                                invMenu = input("Enter your choice: ")
                                winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                        if invMenu == "1":
                            clear()
                            time.sleep(0.5)
                            category = input("Crafting categories:\n"
                                             " 1 - Tools\n"
                                             " 2 - Items\n"
                                             " 3 - Food/Drink\n"
                                             " 4 - Return\n"
                                             "Enter your choice: ")
                            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                            while category != "1" and category != "2" and category != "3" and category != "4":
                                print("Invalid!")
                                category = input("Enter your choice: ")
                                winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                            if category == "1":
                                item = "1"
                                while item != "11":
                                    saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                                    clear()
                                    time.sleep(0.5)
                                    item = input("Tools:\n"
                                                 " 1 - 1 Axe ("+str(axe)+")  =  1 Stick ("+str(sticks)+") + 1 Axehead ("+str(axeheads)+")\n"
                                                 " 2 - 1 Boat ("+str(boat)+")  =  20 Logs ("+str(logs)+") + 30 Sticks ("+str(sticks)+")\n"
                                                 " 3 - 1 Bow ("+str(bow)+")  =  1 Log ("+str(logs)+") + 40 Fibres ("+str(fibres)+")\n"
                                                 " 4 - 1 Breadstick ("+str(breadstick)+")  =  15 Wheat ("+str(wheat)+")\n"
                                                 " 5 - 1 Bucket ("+str(bucket)+")  =  5 Clay ("+str(clay)+")\n"
                                                 " 6 - 1 Digging tool ("+str(digTool)+")  =  1 Stick ("+str(sticks)+") + 1 Dighead ("+str(digheads)+")\n"
                                                 " 7 - 1 Fishing rod ("+str(rod)+")  =  1 Stick ("+str(sticks)+") + 10 Fibres ("+str(fibres)+")\n"
                                                 " 8 - 1 Picaxe ("+str(picaxe)+")  =  1 Stick ("+str(sticks)+") + 1 Pichead ("+str(picheads)+")\n"
                                                 " 9 - 1 Rope ("+str(rope)+")  =  60 Fibres ("+str(fibres)+")\n"
                                                 " 10 - 1 Spear ("+str(spear)+")  =  1 Stick ("+str(sticks)+") + 1 Spearhead ("+str(spearheads)+")\n"
                                                 " 11 - Return\n"
                                                 "Enter your choice: ")
                                    winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                                    if item == "11":
                                        pass
                                    elif item == "1":
                                        if sticks >= 1 and axeheads >= 1:
                                            if axe != 1:
                                                print("You just crafted an Axe, use it to mine forest to gather Logs!")
                                                axe = 1
                                                sticks -= 1
                                                axeheads -= 1
                                            else:
                                                print("You already have an Axe!")
                                        else:
                                            print("You don't have enough resources!")
                                    elif item == "2":
                                        if logs >= 20 and sticks >= 30:
                                            if boat != 1:
                                                print("You just crafted a Boat, use it to travel on water!")
                                                boat = 1
                                                logs -= 20
                                                sticks -= 30
                                            else:
                                                print("You already have a Boat!")
                                        else:
                                            print("You don't have enough resources")
                                    elif item == "3":
                                        if logs >= 1 and fibres >= 40:
                                            if bow != 1:
                                                print("You just crafted a Bow, use it to hunt!")
                                                bow = 1
                                                logs -= 1
                                                fibres -= 40
                                            else:
                                                print("You already have a Bow!")
                                        else:
                                            print("You don't have enough resources")
                                    elif item == "4":
                                        if wheat >= 15:
                                            if breadstick != 1:
                                                print("You just crafted a Breadstick, use it to complete the game!")
                                                breadstick = 1
                                                wheat -= 15
                                            else:
                                                print("You already have a Breadstick!")
                                        else:
                                            print("You don't have enough resources")
                                    elif item == "5":
                                        if clay >= 5:
                                            if bucket != 1:
                                                print("You just crafted a Bucket, use it to collect water!")
                                                bucket = 1
                                                clay -= 5
                                            else:
                                                print("You already have a Bucket!")
                                        else:
                                            print("You don't have enough resources")
                                    elif item == "6":
                                        if sticks >= 1 and digheads >= 1:
                                            if digTool != 1:
                                                print("You just crafted a Digging tool, use it to mine grassland to gather Clay!")
                                                digTool = 1
                                                sticks -= 1
                                                digheads -= 1
                                            else:
                                                print("You already have a Digging tool!")
                                        else:
                                            print("You don't have enough resources")
                                    elif item == "7":
                                        if sticks >= 1 and fibres >= 10:
                                            if rod != 1:
                                                print("You just crafted a Fishing rod, use it to gather fish!")
                                                rod = 1
                                                sticks -= 1
                                                fibres -= 10
                                            else:
                                                print("You already have a Fishing rod!")
                                        else:
                                            print("You don't have enough resources")
                                    elif item == "8":
                                        if sticks >= 1 and picheads >= 1:
                                            if picaxe != 1:
                                                print("You just crafted a Picaxe, use it to mine stone to gather Rocks!")
                                                picaxe = 1
                                                sticks -= 1
                                                picheads -= 1
                                            else:
                                                print("You already have a Picaxe!")
                                        else:
                                            print("You don't have enough resources")
                                    elif item == "9":
                                        if fibres >= 60:
                                            if rope != 1:
                                                print("You just crafted a Rope, use it to travel over mountains!")
                                                rope = 1
                                                fibres -= 60
                                            else:
                                                print("You already have a Rope!")
                                        else:
                                            print("You don't have enough resources")
                                    elif item == "10":
                                        if sticks >= 1 and spearheads >= 1:
                                            if spear != 1:
                                                print("You just crafted a Spear, use it to hunt!")
                                                spear = 1
                                                sticks -= 1
                                                spearheads -= 1
                                            else:
                                                print("You already have a Spear!")
                                        else:
                                            print("You don't have enough resources")
                                    else:
                                        print("Invalid!")
                                    time.sleep(2)
                            elif category == "2":
                                item = "1"
                                while item != "8":
                                    saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                                    clear()
                                    time.sleep(0.5)
                                    item = input("Items:\n"
                                                 " 1 - 5 Arrowheads ("+str(arrowheads)+")  =  2 Stones ("+str(stones)+")\n"
                                                 " 2 - 1 Arrow ("+str(arrows)+")  =  1 Stick ("+str(sticks)+") + 2 Feathers ("+str(feathers)+") + 1 Arrowhead ("+str(arrowheads)+")\n"
                                                 " 3 - 1 Axehead ("+str(axeheads)+")  =  2 Stones ("+str(stones)+")\n"
                                                 " 4 - 1 Dighead ("+str(digheads)+")  =  2 Stones ("+str(stones)+")\n"
                                                 " 5 - 1 Pichead ("+str(picheads)+")  =  2 Stones ("+str(stones)+")\n"
                                                 " 6 - 1 Spearhead ("+str(spearheads)+")  =  2 Stones ("+str(stones)+")\n"
                                                 " 7 - 1 Trig Point ("+str(trig)+")  =  5 Rocks ("+str(rocks)+") + 10 Stones ("+str(stones)+")\n"
                                                 " 8 - Return\n"
                                                 "Enter your choice: ")
                                    winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                                    if item == "8":
                                        pass
                                    elif item == "1":
                                        if stones >= 1:
                                            print("You just crafted 5 Arrowheads, use them to craft Arrows!")
                                            arrowheads += 5
                                            stones -= 1
                                        else:
                                            print("You don't have enough resources!")
                                    elif item == "2":
                                        if sticks >= 1 and feathers >= 2 and arrowheads >= 1:
                                            print("You just crafted an Arrow, use it to hunt with a Bow!")
                                            arrows += 1
                                            sticks -= 1
                                            feathers -= 2
                                            arrowheads -= 1
                                        else:
                                            print("You don't have enough resources!")
                                    elif item == "3":
                                        if stones >= 2:
                                            print("You just crafted an Axehead, use it to craft an Axe!")
                                            axeheads += 1
                                            stones -= 2
                                        else:
                                            print("You don't have enough resources!")
                                    elif item == "4":
                                        if stones >= 2:
                                            print("You just crafted a Dighead, use it to craft a Digging tool!")
                                            digheads += 1
                                            stones -= 2
                                        else:
                                            print("You don't have enough resources!")
                                    elif item == "5":
                                        if stones >= 2:
                                            print("You just crafted a Pichead, use it to craft a Picaxe!")
                                            picheads += 1
                                            stones -= 2
                                        else:
                                            print("You don't have enough resources!")
                                    elif item == "6":
                                        if stones >= 2:
                                            print("You just crafted a Spearhead, use it to craft a Spear!")
                                            spearheads += 1
                                            stones -= 2
                                        else:
                                            print("You don't have enough resources!")
                                    elif item == "7":
                                        if rocks >= 5 and stones >= 10:
                                            print("You just crafted a Trig Point, use it to help locate the Jar!")
                                            trig += 1
                                            rocks -= 5
                                            stones -= 10
                                        else:
                                            print("You don't have enough resources!")
                                    else:
                                        print("Invalid!")
                                    time.sleep(1)
                            elif category == "3":
                                item = "1"
                                while item != "5":
                                    saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                                    clear()
                                    time.sleep(0.5)
                                    item = input("Food/Drink:\n"
                                                 " 1 - 1 Jar of Nutella ("+str(nutellaJar)+")  =  10 hazelnuts ("+str(hazelnuts)+") + 100 Sugar ("+str(sugar)+") + 1 Jar ("+str(jarFound)+")\n"
                                                 " 2 - 1 Breadstick ("+str(breadstick)+")  =  15 Wheat ("+str(wheat)+")\n"
                                                 " 3 - 1 Bread ("+str(bread)+")  =  5 Wheat ("+str(wheat)+")\n"
                                                 " 4 - 1 Juice ("+str(juice)+")  =  2 Berries ("+str(berries)+") + 5 Water ("+str(water)+")\n"
                                                 " 5 - Return\n"
                                                 "Enter your choice: ")
                                    winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                                    if item == "5":
                                        pass
                                    elif item == "1":
                                        if nutellaJar == 0:
                                            if hazelnuts >= 10 and sugar >= 100 and jarFound == 1:
                                                print("You just crafted the Jar of Nutella, use it to complete the game!")
                                                nutellaJar = 1
                                                hazelnuts -= 10
                                                sugar -= 100
                                                jarFound = 0
                                            else:
                                                print("You don't have enough resources!")
                                        else:
                                            print("You already have the Jar of Nutella!")
                                    elif item == "2":
                                        if breadstick == 0:
                                            if wheat >= 15:
                                                print("You just crafted the Breadstick, use it to complete the game!")
                                                breadstick = 1
                                                wheat -= 15
                                            else:
                                                print("You don't have enough resources!")
                                        else:
                                            print("You already have the Breadstick")
                                    elif item == "3":
                                        if wheat >= 5:
                                            print("You just crafted a Bread, use it to sate your appetite!")
                                            bread += 1
                                            wheat -= 5
                                        else:
                                            print("You don't have enough resources!")
                                    elif item == "4":
                                        if berries >= 2 and water >= 5:
                                            print("You just crafted a Juice, use it to quench your thirst and sate your appetite!")
                                            juice += 1
                                            berries -= 2
                                            water -= 5
                                        else:
                                            print("You don't have enough resources!")
                                    else:
                                        print("Invalid!")
                                    time.sleep(1)
                            clear()
                            time.sleep(0.5)
                        elif invMenu == "2":
                            clear()
                            time.sleep(0.5)
                            category = input("Inventory categories:\n"
                                             " 1 - Tools\n"
                                             " 2 - Items\n"
                                             " 3 - Food/Drink\n"
                                             " 4 - Return\n"
                                             "Enter your choice: ")
                            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                            while category != "1" and category != "2" and category != "3" and category != "4":
                                print("Invalid!")
                                category = input("Enter your choice: ")
                                winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                            if category == "1":
                                clear()
                                time.sleep(0.5)
                                print("Tools:\n"
                                      " Axe: "+str(axe)+"\n"
                                      " Boat: "+str(boat)+"\n"
                                      " Bow: "+str(bow)+"\n"
                                      " Breadstick: "+str(breadstick)+"\n"
                                      " Bucket: "+str(bucket)+"\n"
                                      " Digging tool: "+str(digTool)+"\n"
                                      " Fishing rod: "+str(rod)+"\n"
                                      " Picaxe: "+str(picaxe)+"\n"
                                      " Rope: "+str(rope)+"\n"
                                      " Spear: "+str(spear)+"\n")
                            elif category == "2":
                                clear()
                                time.sleep(0.5)
                                print("Items:\n"
                                      " Arrowheads: "+str(arrowheads)+"\n"
                                      " Arrows: "+str(arrows)+"\n"
                                      " Axeheads: "+str(axeheads)+"\n"
                                      " Clay: "+str(clay)+"\n"
                                      " Digheads: "+str(digheads)+"\n"
                                      " Feathers: "+str(feathers)+"\n"
                                      " Fibres: "+str(fibres)+"\n"
                                      " Logs: "+str(logs)+"\n"
                                      " Picheads: "+str(picheads)+"\n"
                                      " Rocks: " + str(rocks)+"\n"
                                      " Spearheads: "+str(spearheads)+"\n"
                                      " Sticks: "+str(sticks)+"\n"
                                      " Stones: "+str(stones)+"\n"
                                      " Trig Points: "+str(trig)+"\n")
                            elif category == "3":
                                clear()
                                time.sleep(0.5)
                                print("Food/Drink:\n"
                                      " Berries: "+str(berries)+"\n"
                                      " Bread: "+str(bread)+"\n"
                                      " Fish: "+str(fish)+"\n"
                                      " Hazelnuts: "+str(hazelnuts)+"\n"
                                      " Juice: "+str(juice)+"\n"
                                      " Meat: " + str(meat) + "\n"
                                      " Sugar: " + str(sugar) + "\n"
                                      " Water: " + str(water) + "\n"
                                      " Wheat: " + str(wheat) + "\n")
                            if category != "4":
                                input("Hit enter to continue...")
                            clear()
                            time.sleep(0.5)
                        elif invMenu == "3":
                            clear()
                            time.sleep(0.5)
                            break
                        elif invMenu == "4" and nutellaJar == 1:
                            finishGame = 1
                            clear()
                            time.sleep(0.5)
                            break
                elif move.lower() == "l":
                    if trig >= 1:
                        if mapLayoutFinal[playerPos] == "■■":
                            playerX = int(playerPos % xLength)
                            playerY = int(playerPos / xLength)
                            jarX = int(jarPos % xLength)
                            jarY = int(jarPos / xLength)
                            if playerX > jarX:
                                diffX = jarX - playerX
                            elif playerX < jarX:
                                diffX = playerX - jarX
                            else:
                                diffX = 0
                            if playerY > jarY:
                                diffY = playerY - jarY
                            elif playerY < jarY:
                                diffY = jarY - playerY
                            else:
                                diffY = 0
                            print("The jar is this distance from this Trig Point: ("+str(diffX)+","+str(diffY)+")")
                            trig -= 1
                            saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                            time.sleep(1)
                        else:
                            print("You must be on a mountain to use a Trig Point!")
                    else:
                        print("You need to craft a Trig Point!")
                    time.sleep(1)
                elif move.lower() == "p":
                    clear()
                    time.sleep(0.5)
                    if playerPos not in pickTiles:
                        del pickTiles[0]
                        pickTiles.append(playerPos)
                        tile = mapLayoutFinal[playerPos]
                        if tile == "░░" or tile == "▒▒" or tile == "▓▓" or tile == "██":
                            if tile == "░░":
                                print("Collecting...")
                                time.sleep(random.uniform(1, 2))
                                amount = random.randint(1,9)
                                if amount != 0:
                                    if fibres + amount <= 9999:
                                        print("You collected " + str(amount) + " Fibres")
                                        fibres += amount
                                    elif fibres == 9999:
                                        print("Your storage for Fibres is full!")
                                    else:
                                        print("You collected " + str(9999 - fibres) + " Fibres")
                                        fibres = 9999
                                berryChance = random.randint(0,3)
                                if berryChance == 2:
                                    amount = random.randint(1,4)
                                    if amount != 0:
                                        if berries + amount <= 9999:
                                            print("You collected " + str(amount) + " Berries")
                                            berries += amount
                                        elif berries == 9999:
                                            print("Your storage for Berries is full!")
                                        else:
                                            print("You collected " + str(9999 - berries) + " Berries")
                                            berries = 9999
                                wheatChance = random.randint(0,5)
                                if wheatChance == 2:
                                    amount = random.randint(0,2)
                                    if amount != 0:
                                        if wheat + amount <= 9999:
                                            print("You collected " + str(amount) + " Wheat")
                                            wheat += amount
                                        elif wheat == 9999:
                                            print("Your storage for Wheat is full!")
                                        else:
                                            print("You collected " + str(9999 - wheat) + " Wheat")
                                            wheat = 9999
                                sugarChance = random.randint(0,6)
                                if sugarChance == 2:
                                    amount = random.randint(0,10)
                                    if amount != 0:
                                        if sugar + amount <= 9999:
                                            print("You collected " + str(amount) + " Sugar")
                                            sugar += amount
                                        elif sugar == 9999:
                                            print("Your storage for Sugar is full!")
                                        else:
                                            print("You collected " + str(9999 - sugar) + " Sugar")
                                            sugar = 9999
                            elif tile == "▒▒":
                                print("Collecting...")
                                time.sleep(random.uniform(1, 2))
                                amount = random.randint(1,7)
                                if amount != 0:
                                    if stones + amount <= 999:
                                        print("You collected " + str(amount) + " Stones")
                                        stones += amount
                                    elif stones == 999:
                                        print("Your storage for Stones is full!")
                                    else:
                                        print("You collected " + str(999 - stones) + " Stones")
                                        stones = 9999
                            elif tile == "▓▓":
                                print("Collecting...")
                                time.sleep(random.uniform(1, 2))
                                amount = random.randint(1,8)
                                if amount != 0:
                                    if sticks + amount <= 999:
                                        print("You collected " + str(amount) + " Sticks")
                                        sticks += amount
                                    elif sticks == 999:
                                        print("Your storage for Sticks is full!")
                                    else:
                                        print("You collected " + str(999 - sticks) + " Sticks")
                                        sticks = 999
                                nutChance = random.randint(0,5)
                                if nutChance == 2:
                                    amount = random.randint(0,4)
                                    if amount != 0:
                                        if hazelnuts + amount <= 9999:
                                            print("You collected " + str(amount) + " Hazelnuts")
                                            hazelnuts += amount
                                        elif hazelnuts == 9999:
                                            print("Your storage for Hazelnuts is full!")
                                        else:
                                            print("You collected " + str(9999 - hazelnuts) + " Hazelnuts")
                                            hazelnuts = 9999
                            elif tile == "██" and bucket == 1:
                                print("Collecting...")
                                time.sleep(random.uniform(1, 2))
                                amount = random.randint(2,7)
                                if amount != 0:
                                    if water + amount <= 999:
                                        print("You collected " + str(amount) + " Water")
                                        water += amount
                                    elif water == 999:
                                        print("Your storage for Water is full!")
                                    else:
                                        print("You collected " + str(999 - water) + " Water")
                                        water = 999
                            else:
                                print("You don't have the required item to pick this tile!")
                            saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                        else:
                            print("Can't pick up on this tile!")
                    else:
                        print("You recently picked from this tile!")
                    time.sleep(2)
                    clear()
                elif move.lower() == "m":
                    clear()
                    time.sleep(0.5)
                    if playerPos not in mineTiles:
                        del mineTiles[0]
                        mineTiles.append(playerPos)
                        tile = mapLayoutFinal[playerPos]
                        if tile == "░░" or tile == "▒▒" or tile == "▓▓" or tile == "██":
                            if tile == "░░" and digTool == 1:
                                amount = random.randint(1,6)
                                if amount != 0:
                                    if clay + amount <= 9999:
                                        print("You collected " + str(amount) + " Clay")
                                        clay += amount
                                    elif clay == 9999:
                                        print("Your storage for Clay is full!")
                                    else:
                                        print("You collected " + str(9999 - clay) + " Clay")
                                        clay = 9999
                            elif tile == "▒▒" and picaxe == 1:
                                print("Collecting...")
                                time.sleep(random.uniform(1, 2))
                                amount = random.randint(1, 6)
                                if amount != 0:
                                    if rocks + amount <= 999:
                                        print("You collected " + str(amount) + " Rocks")
                                        rocks += amount
                                    elif rocks == 999:
                                        print("Your storage for Rocks is full!")
                                    else:
                                        print("You collected " + str(999 - rocks) + " Rocks")
                                        rocks = 999
                            elif tile == "▓▓" and axe == 1:
                                print("Collecting...")
                                time.sleep(random.uniform(1, 2))
                                amount = random.randint(1,3)
                                if amount != 0:
                                    if logs + amount <= 999:
                                        print("You collected " + str(amount) + " Logs")
                                        logs += amount
                                    elif logs == 999:
                                        print("Your storage for Logs is full!")
                                    else:
                                        print("You collected " + str(999 - logs) + " Logs")
                                        logs = 999
                            elif tile == "██" and rod == 1:
                                print("Collecting...")
                                time.sleep(random.uniform(1, 2))
                                amount = random.randint(1,3)
                                if amount != 0:
                                    if fish + amount <= 9999:
                                        print("You collected " + str(amount) + " Fish")
                                        fish += amount
                                    elif fish == 9999:
                                        print("Your storage for Fish is full!")
                                    else:
                                        print("You collected " + str(9999 - fish) + " Fish")
                                        fish = 9999
                            else:
                                print("You don't have the required item to mine this tile!")
                            saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                        else:
                            print("You can't mine on this tile!")
                    else:
                        print("You recently mined on this tile!")
                    time.sleep(2)
                    clear()
                elif move.lower() == "h":
                    time.sleep(0.5)
                    clear()
                    miss = 0
                    weapon = input("Weapon:\n"
                                   " 1 - Bare hand - Chase for Turkey\n"
                                   " 2 - Bow ("+str(bow)+") - Used for Grey Squirrel, Turkey\n"
                                   " 3 - Spear ("+str(spear)+") - Used for Deer, Wolf\n"
                                   " 4 - Return to game\n"
                                   "Enter your choice: ")
                    winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                    while weapon != "1" and weapon != "2" and weapon != "3" and weapon != "4":
                        print("Invalid!")
                        weapon = input("Enter your choice: ")
                        winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                    if weapon == "4":
                        time.sleep(0.5)
                        break
                    elif weapon == "1":
                        clear()
                        if playerPos not in huntTiles:
                            del huntTiles[0]
                            huntTiles.append(playerPos)
                            if mapLayoutFinal[playerPos] == "░░" or mapLayoutFinal[playerPos] == "▓▓":
                                print("Hunting...")
                                time.sleep(random.uniform(1,2))
                                turkeyChance = random.randint(0,4)
                                if turkeyChance == 2:
                                    print("You hunted a Turkey!")
                                    amount = random.randint(1,6)
                                    if amount != 0:
                                        if feathers + amount <= 9999:
                                            print("You collected " + str(amount) + " Feathers")
                                            feathers += amount
                                        elif feathers == 9999:
                                            print("Your storage for Feathers is full!")
                                        else:
                                            print("You collected " + str(9999 - feathers) + " Feathers")
                                            feathers = 9999
                                    amount = random.randint(1,4)
                                    if amount != 0:
                                        if meat + amount <= 9999:
                                            print("You collected " + str(amount) + " Meat")
                                            meat += amount
                                        elif meat == 9999:
                                            print("Your storage for Meat is full!")
                                        else:
                                            print("You collected " + str(9999 - meat) + " Meat")
                                            meat = 9999
                                    saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                                else:
                                    print("The Turkey got away!")
                            else:
                                print("There are no Turkeys on this tile type!")
                        else:
                            print("You recently hunted on this tile!")
                    elif weapon == "2":
                        if bow == 0:
                            print("You don't have a Bow!")
                            time.sleep(1)
                        elif bow == 1:
                            if arrows > 0:
                                clear()
                                if playerPos not in huntTiles:
                                    del huntTiles[0]
                                    huntTiles.append(playerPos)
                                    if mapLayoutFinal[playerPos] == "░░":
                                        print("Hunting...")
                                        time.sleep(random.uniform(1,2))
                                        turkeyChance = random.randint(0,5)
                                        if turkeyChance == 2:
                                            arrows -= 1
                                            print("You hunted a Turkey!")
                                            amount = random.randint(1,6)
                                            if amount != 0:
                                                if feathers + amount <= 9999:
                                                    print("You collected " + str(amount) + " Feathers")
                                                    feathers += amount
                                                elif feathers == 9999:
                                                    print("Your storage for Feathers is full!")
                                                else:
                                                    print("You collected " + str(9999 - feathers) + " Feathers")
                                                    feathers = 9999
                                            amount = random.randint(1,4)
                                            if amount != 0:
                                                if meat + amount <= 9999:
                                                    print("You collected " + str(amount) + " Meat")
                                                    meat += amount
                                                elif meat == 9999:
                                                    print("Your storage for Meat is full!")
                                                else:
                                                    print("You collected " + str(9999 - meat) + " Meat")
                                                    meat = 9999
                                            saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                                        else:
                                            miss = 1
                                    elif mapLayoutFinal[playerPos] == "▓▓":
                                        print("Hunting...")
                                        time.sleep(random.uniform(1,2))
                                        squirrelChance = random.randint(0,5)
                                        if squirrelChance == 2:
                                            print("You hunted a Grey Squirrel!")
                                            amount = random.randint(1,3)
                                            if amount != 0:
                                                if meat + amount <= 9999:
                                                    print("You collected " + str(amount) + " Meat")
                                                    meat += amount
                                                elif meat == 9999:
                                                    print("Your storage for Meat is full!")
                                                else:
                                                    print("You collected " + str(9999 - meat) + " Meat")
                                                    meat = 9999
                                            saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                                        else:
                                            miss = 1
                                    else:
                                        print("There are no animals on this tile type!")
                                else:
                                    print("You recently hunted on this tile!")
                            else:
                                print("You don't have any Arrows!")
                    elif weapon == "3":
                        if spear == 0:
                            print("You don't have a Spear!")
                            time.sleep(1)
                        elif spear == 1:
                            clear()
                            if playerPos not in huntTiles:
                                del huntTiles[0]
                                huntTiles.append(playerPos)
                                if mapLayoutFinal[playerPos] == "░░":
                                    print("Hunting...")
                                    time.sleep(random.uniform(1,2))
                                    wolfChance = random.randint(0,5)
                                    if wolfChance == 2:
                                        print("You hunted a Wolf!")
                                        damage = random.randint(0,5)
                                        if damage != 0:
                                            health -= damage
                                            print("You lost "+str(damage)+" Health in the fight!")
                                        amount = random.randint(2,12)
                                        if amount != 0:
                                            if meat + amount <= 9999:
                                                print("You collected " + str(amount) + " Meat")
                                                meat += amount
                                            elif meat == 9999:
                                                print("Your storage for Meat is full!")
                                            else:
                                                print("You collected " + str(9999 - meat) + " Meat")
                                                meat = 9999
                                        saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                                    else:
                                        miss = 1
                                elif mapLayoutFinal[playerPos] == "▓▓":
                                    print("Hunting...")
                                    time.sleep(random.uniform(1,2))
                                    deerChance = random.randint(0,3)
                                    if deerChance == 2:
                                        print("You hunted a Deer!")
                                        amount = random.randint(2,8)
                                        if amount != 0:
                                            if meat + amount <= 9999:
                                                print("You collected " + str(amount) + " Meat")
                                                meat += amount
                                            elif meat == 9999:
                                                print("Your storage for Meat is full!")
                                            else:
                                                print("You collected " + str(9999 - meat) + " Meat")
                                                meat = 9999
                                        wolfChance = random.randint(0,15)
                                        if wolfChance == 2:
                                            print("You hunted a Wolf!")
                                            damage = random.randint(0,5)
                                            if damage != 0:
                                                health -= damage
                                                print("You lost " + str(damage) + " Health in the fight!")
                                            amount = random.randint(2,12)
                                            if amount != 0:
                                                if meat + amount <= 9999:
                                                    print("You collected " + str(amount) + " Meat")
                                                    meat += amount
                                                elif meat == 9999:
                                                    print("Your storage for Meat is full!")
                                                else:
                                                    print("You collected " + str(9999 - meat) + " Meat")
                                                    meat = 9999
                                        saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                                    else:
                                        miss = 1
                                else:
                                    print("There are no animals on this tile type!")
                            else:
                                print("You recently hunted on this tile!")
                    else:
                        print("Invalid!")
                    if miss == 1:
                        print("Your scent scared off all of the animals!")
                    time.sleep(2)
                    clear()
                    time.sleep(0.5)
                elif move.lower() == "f":
                    food = "1"
                    clear()
                    time.sleep(0.5)
                    while food != "8":
                        clear()
                        food = input("Hunger: " + str(hunger) + "/100\n"
                                     "Thirst: " + str(thirst) + "/100\n\n"
                                     "Food:\n"
                                     " 1 - Berries ("+str(berries)+") - Replenish 5 hunger and 1 thirst\n"
                                     " 2 - Bread ("+str(bread)+") - Replenish 8 hunger\n"
                                     " 3 - Fish ("+str(fish)+") - Replenish 5 hunger\n"
                                     " 4 - Hazelnuts ("+str(hazelnuts)+") - Replenish 2 hunger\n"
                                     " 5 - Juice ("+str(juice)+") - Replenish 5 hunger and 5 thirst\n"
                                     " 6 - Meat ("+str(meat)+") - Replenish 10 hunger\n"
                                     " 7 - Water ("+str(water)+") - Replenish 10 thirst\n"
                                     " 8 - Return to game\n"
                                     "Enter your choice: ")
                        winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                        while food != "1" and food != "2" and food != "3" and food != "4" and food != "5" and food != "6" and food != "7" and food != "8":
                            print("Invalid!")
                            food = input("Enter your choice: ")
                            winsound.PlaySound("sounds/click.wav",winsound.SND_ASYNC)
                        if food == "8":
                            time.sleep(0.5)
                            pass
                        elif food == "1":
                            if berries > 0:
                                if hunger + 5 < 100 and thirst + 1 < 100:
                                    hunger += 5
                                    thirst += 1
                                    berries -= 1
                                elif hunger == 100 and thirst == 100:
                                    print("You are fully sated and hydrated")
                                    time.sleep(1)
                                elif hunger + 5 >= 100 and thirst + 1 < 100:
                                    hunger = 100
                                    thirst += 1
                                    berries -= 1
                                elif hunger + 5 >= 100 and thirst == 100:
                                    hunger = 100
                                    berries -=1
                                elif hunger + 5 < 100 and thirst + 1 >= 100:
                                    thirst = 100
                                    hunger += 5
                                    berries -= 1
                                elif hunger == 100 and thirst + 1 >= 100:
                                    thirst = 100
                                    berries -= 1
                                saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                            else:
                                print("You don't have any Berries!")
                                time.sleep(1)
                        elif food == "2":
                            if bread > 0:
                                if hunger + 8 < 100:
                                    hunger += 8
                                    bread -= 1
                                elif hunger == 100:
                                    print("You are fully sated!")
                                    time.sleep(1)
                                elif hunger + 8 >= 100:
                                    hunger = 100
                                    bread -= 1
                                saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                            else:
                                print("You don't have any Bread!")
                                time.sleep(1)
                        elif food == "3":
                            if fish > 0:
                                if hunger + 5 < 100:
                                    hunger += 5
                                    fish -= 1
                                elif hunger == 100:
                                    print("You are fully sated!")
                                    time.sleep(1)
                                elif hunger + 2 >= 100:
                                    hunger = 100
                                    fish -= 1
                                saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                            else:
                                print("You don't have any Fish")
                                time.sleep(1)
                        elif food == "4":
                            if hazelnuts > 0:
                                if hunger + 2 < 100:
                                    hunger += 2
                                    hazelnuts -= 1
                                elif hunger == 100:
                                    print("You are fully sated!")
                                    time.sleep(1)
                                elif hunger + 10 >= 100:
                                    hunger = 100
                                    hazelnuts -= 1
                                saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                            else:
                                print("You don't have any Hazelnuts!")
                                time.sleep(1)
                        elif food == "5":
                            if juice > 0:
                                if hunger + 5 < 100 and thirst + 5 < 100:
                                    hunger += 5
                                    thirst += 5
                                    juice -= 1
                                elif hunger == 100 and thirst == 100:
                                    print("You are fully sated and hydrated")
                                    time.sleep(1)
                                elif hunger + 5 >= 100 and thirst + 5 < 100:
                                    hunger = 100
                                    thirst += 5
                                    juice -= 1
                                elif hunger + 5 >= 100 and thirst == 100:
                                    hunger = 100
                                    juice -=1
                                elif hunger + 5 < 100 and thirst + 5 >= 100:
                                    thirst = 100
                                    hunger += 5
                                    juice -= 1
                                elif hunger == 100 and thirst + 5 >= 100:
                                    thirst = 100
                                    juice -= 1
                                saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                            else:
                                print("You don't have any Juice!")
                                time.sleep(1)
                        elif food == "6":
                            if meat > 0:
                                if hunger + 10 < 100:
                                    hunger += 10
                                    meat -= 1
                                elif hunger == 100:
                                    print("You are fully sated!")
                                    time.sleep(1)
                                elif hunger + 10 >= 100:
                                    hunger = 100
                                    meat -= 1
                                saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                            else:
                                print("You don't have any Meat!")
                                time.sleep(1)
                        elif food == "7":
                            if water > 0:
                                if thirst + 10 < 100:
                                    thirst += 10
                                    water -= 1
                                elif thirst == 100:
                                    print("You are fully hydrated!")
                                    time.sleep(1)
                                elif thirst + 10 >= 100:
                                    thirst = 100
                                    water -= 1
                                saveMap(mapName,playerPos,health,hunger,thirst,jarPos,boat,rope,breadstick,nutellaJar,jarFound,spear,axe,picaxe,rod,bow,digTool,arrows,spearheads,arrowheads,digheads,axeheads,picheads,trig,stones,rocks,logs,sticks,clay,fibres,fish,water,feathers,meat,hazelnuts,berries,wheat,bucket,sugar,juice,bread)
                            else:
                                print("You don't have any Water!")
                                time.sleep(1)
                        else:
                            print("Invalid!")
                            time.sleep(0.5)
                elif move == "6":
                    if playerPos % xLength == xLength - 1:
                        playerPosCheck = playerPos + 1 - xLength
                    else:
                        playerPosCheck = playerPos + 1
                elif move == "4":
                    if playerPos % xLength == 0:
                        playerPosCheck = playerPos - 1 +xLength
                    else:
                        playerPosCheck = playerPos - 1
                elif move == "8":
                    if playerPos < xLength:
                        time.sleep(0.1)
                        print("You are at the top of the world and can't move any higher!")
                        time.sleep(1.5)
                    else:
                        playerPosCheck = playerPos - xLength
                elif move == "2":
                    if playerPos > xyArea - xLength:
                        time.sleep(0.1)
                        print("You are at the bottom of the world and can't move any lower!")
                        time.sleep(1.5)
                    else:
                        playerPosCheck = playerPos + xLength
                elif move == "9":
                    if playerPos < xLength:
                        time.sleep(0.1)
                        print("You are at the top of the world and can't move any higher!")
                        time.sleep(1.5)
                    else:
                        playerPosCheck = playerPos + 1 - xLength
                elif move == "3":
                    if playerPos > xyArea - xLength:
                        time.sleep(0.1)
                        print("You are at the bottom of the world and can't move any lower!")
                        time.sleep(1.5)
                    else:
                        playerPosCheck = playerPos + 1 + xLength
                elif move == "7":
                    if playerPos < xLength:
                        time.sleep(0.1)
                        print("You are at the top of the world and can't move any higher!")
                        time.sleep(1)
                    else:
                        playerPosCheck = playerPos - 1 - xLength
                elif move == "1":
                    if playerPos > xyArea - xLength:
                        time.sleep(0.1)
                        print("You are at the bottom of the world and can't move any lower!")
                        time.sleep(1.5)
                    else:
                        playerPosCheck = playerPos - 1 + xLength
                if move == "1" or move == "2" or move == "3" or move == "4" or move == "6" or move == "7" or move == "8" or move == "9":
                    if mapLayoutFinal[playerPosCheck] == "██" and boat == 0:
                        time.sleep(0.1)
                        print("You can't move to this tile!")
                        time.sleep(0.5)
                        print("Craft a boat to travel on water")
                        time.sleep(1.5)
                    elif mapLayoutFinal[playerPosCheck] == "■■" and rope == 0:
                        time.sleep(0.1)
                        print("You can't move to this tile!")
                        time.sleep(0.5)
                        print("Craft a rope to travel over mountains")
                        time.sleep(1.5)
                    elif mapLayoutFinal[playerPosCheck] != "██" or mapLayoutFinal[playerPosCheck] != "■■":
                        playerPos = playerPosCheck
                        del pickTiles[0]
                        pickTiles.append(1)
                        del mineTiles[0]
                        mineTiles.append(1)
                        if hunger > 0:
                            hunger -= 1
                        if hunger < 5:
                            health -= 1
                        if thirst > 0:
                            thirst -= 1
                        if thirst < 5:
                            health -= 1
                        if health <= 0:
                            finishGame = 1
                            dead = 1
                        if health < 100 and health != 100 and hunger > 50 and thirst > 50:
                            health += 1
                clear()
            if gameCompleted == 1:
                break
    # map creator
    elif mainMenu == 2:
        mapLayout = []
        mapLayoutAlt = []
        mapLayoutFinal = []
        mapData = []
        time.sleep(0.5)
        print("Generate map:\n"
              "Map types:\n"
              " 1 - lots of land, not much water\n"
              " 2 - balanced land and water\n"
              " 3 - not much land, lots of water\n"
              " 0 - Return")
        landChance = input("Enter a map type: ")
        winsound.PlaySound("sounds/click.wav",winsound.SND_ASYNC)
        while landChance != '1' and landChance != '2' and landChance != '3' and landChance != '0':
            print("Invalid!")
            landChance = input("Enter a map type: ")
            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
        landChance = int(landChance) + 1
        time.sleep(0.5)
        br()
        if landChance > 1 and landChance < 5:
            mapData.append(landChance)
            print("The map must be at least 10 tiles wide and at least 5 tiles tall but can be as big as you want\n"
                  "To view a preview of your map, it must be less than " + str(maxWidth) + " tiles wide and less than " + str(maxHeight) + " tall\n"
                  "Large maps can take a very long time to load and display so keep them small unless you have a powerful computer")
            time.sleep(0.5)
            xLength = input(" Enter your desired width: ")
            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
            while  xLength == "" or isInteger(xLength) == 0 or int(xLength) < 10:
                print("Invalid!")
                xLength = input(" Enter your desired width: ")
                winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
            yLength = input(" Enter your desired height: ")
            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
            while  yLength == "" or isInteger(yLength) == 0 or int(yLength) < 5:
                print("Invalid!")
                yLength = input(" Enter your desired width: ")
                winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
            xLength = int(xLength)
            yLength = int(yLength)
            xyArea = xLength * yLength
            br()
            start = time.time()
            for i in range(0, (int(xyArea * 0.4))):
                mapData.append(1)
            for i in range(0, (int(xyArea * 0.6))):
                mapData.append(0)
            for i in range(len(mapData), xyArea):
                mapData.append(0)
            for i in range(0, xyArea):
                mapLayout.append(mapData[random.randint(0, xyArea - 1)])
            for i in range(len(mapLayout)):
                if mapLayout[i] == 1:
                    mapLayout[i] = "░░"
                if mapLayout[i] == 0:
                    mapLayout[i] = "██"
            for i in mapLayout:
                mapLayoutAlt.append(i)
            if landChance == 2:
                mapLayoutCellAut(xLength, yLength, 2, mapLayout, mapLayoutAlt, xyArea)
                mapLayoutAltCellAut(xLength, yLength, 3, mapLayout, mapLayoutAlt, xyArea)
                mapLayoutCellAut(xLength, yLength, 2, mapLayout, mapLayoutAlt, xyArea)
                mapLayoutAltCellAut(xLength, yLength, 6, mapLayout, mapLayoutAlt, xyArea)
                mapLayoutCellAut(xLength, yLength, 2, mapLayout, mapLayoutAlt, xyArea)
                tileGenerationAlt(mapLayoutAlt, mapData)
                for i in mapLayoutAlt:
                    mapLayoutFinal.append(i)
            elif landChance == 3:
                mapLayoutCellAut(xLength, yLength, 3, mapLayout, mapLayoutAlt, xyArea)
                mapLayoutAltCellAut(xLength, yLength, 2, mapLayout, mapLayoutAlt, xyArea)
                mapLayoutCellAut(xLength, yLength, 2, mapLayout, mapLayoutAlt, xyArea)
                mapLayoutAltCellAut(xLength, yLength, 6, mapLayout, mapLayoutAlt, xyArea)
                mapLayoutCellAut(xLength, yLength, 2, mapLayout, mapLayoutAlt, xyArea)
                tileGeneration(mapLayout, mapData)
                for i in mapLayout:
                    mapLayoutFinal.append(i)
            elif landChance == 4:
                mapLayoutCellAut(xLength, yLength, 3, mapLayout, mapLayoutAlt, xyArea)
                mapLayoutAltCellAut(xLength, yLength, 5, mapLayout, mapLayoutAlt, xyArea)
                mapLayoutCellAut(xLength, yLength, 2, mapLayout, mapLayoutAlt, xyArea)
                mapLayoutAltCellAut(xLength, yLength, 4, mapLayout, mapLayoutAlt, xyArea)
                tileGenerationAlt(mapLayout, mapData)
                for i in mapLayout:
                    mapLayoutFinal.append(i)
            displayMap(xLength, yLength, mapLayoutFinal)
            time.sleep(0.5)
            end = time.time()
            if xLength > maxWidth or yLength > maxHeight:
                print("Time taken to generate map: " + str((end - start)-2.5) + " seconds")
            else:
                print("Time taken to generate map: " + str(end - start) + " seconds")
            time.sleep(0.5)
            saveMapToFile(xLength,yLength,mapLayoutFinal)
    elif mainMenu == 3:
        showControls("the main menu")
    elif mainMenu == 4:
        clear()
        time.sleep(0.5)
        setSize(0)
        saveGeneral(gamesCompleted,hasSetSize,shape)
    elif mainMenu == 5:
        clear()
        time.sleep(0.5)
        print("Please be as descriptive as you can if you are reporting a bug/glitch\n"
              "Please do not use any swearing; be polite and supportive")
        time.sleep(1)
        name = input(" Enter your name: ")
        winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
        while name == "":
            print("Required!")
            time.sleep(0.5)
            name = input(" Enter your name: ")
            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
        time.sleep(0.5)
        email = input(" Enter your email (optional - used to respond to you): ")
        winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
        if email != "":
            confirmEmail = input(" Confirm your email: ")
            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
            while email != confirmEmail:
                time.sleep(0.5)
                print("Emails did not match!")
                email = input(" Enter your email: ")
                winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
                if email != "":
                    confirmEmail = input(" Confirm your email: ")
                    winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
        time.sleep(0.5)
        message = input(" Enter your message: ")
        winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
        while message == "":
            print("Required!")
            time.sleep(0.5)
            message = input(" Enter your message: ")
            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
        if email != "":
            message = "Their email is: "+email+"\n\n"+message
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login('nutella.addict.game@gmail.com',"h&gV67LK)(D2Gb?'sd")
            msg = MIMEMultipart()
            msg["From"] = 'nutella.addict.game@gmail.com'
            msg["To"] = 'dubwine.dev@gmail.com'
            msg["Subject"] = ("Feedback from "+name)
            msg.attach(MIMEText(message, "plain"))
            text = msg.as_string()
            confirm = input("\nConfirm:\n"
                            " 1 - Send feedback\n"
                            " 2 - Cancel\n"
                            "Enter your choice: ")
            winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
            while confirm != '1' and confirm != '2':
                print("Invalid!")
                confirm = input("Enter your choice: ")
                winsound.PlaySound("sounds/click.wav", winsound.SND_ASYNC)
            if confirm == '1':
                server.sendmail('nutella.addict.game@gmail.com','dubwine.dev@gmail.com',text)
                time.sleep(0.5)
                print("Sent")
                time.sleep(2)
        except:
            time.sleep(1)
            br()
            print("Could not connect to server, check your internet settings and try again")
            time.sleep(0.5)
            input("Hit enter to return to main menu...")
    saveGeneral(gamesCompleted,hasSetSize,shape)