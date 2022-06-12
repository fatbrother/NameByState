from msvcrt import getch
import os
import time
import trie
import state

def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')
    return

def loadNameList():
    nameList = trie.TrieTree()
    file = open("nameList.txt", 'r')
    list = file.read().split('\n')
    nameList.extend(list)
    return nameList

def cls():
    if os.system('cls') == 1:
        os.system('clear')
    return

def search(nameList: trie.TrieTree):
    res = ""

    while 1:
        cls()
        print("Name: " + res)
        x = 7 + len(res)
        below = nameList.getBelow(res)
        if below:
            for i in range(min(len(below), 5)):
                print(below[i])
        gotoxy(x, 0)

        c = str(getch(), 'utf-8')
        if c == '\r':
            if res in nameList:
                return res
            else:
                cls()
                print("This name was not found.")
                time.sleep(3)
                res = ""
        elif c == '\b':
            res = res[:-1]            
        else:
            res = res + c

def animate(target: str):
    cls()

    states = {name: state.State(name, target) for name in open("namesbystate/stateName.txt", "r").read().split('\n')}

    for year in range(1910, 2021):
        gotoxy(0, 0)
        nowYear = {}

        total = 0
        for key, value in states.items():
            nowYear[key] = value.population['F'][year - 1910] + value.population['M'][year - 1910]
            total += nowYear[key]

        sortedList = dict(sorted(nowYear.items(), key=lambda item: item[1]))
        nameRank = list(sortedList.keys())
        nameRank.reverse()
        maxValue = states[nameRank[0]].population['F'][year - 1910] + states[nameRank[0]].population['M'][year - 1910]
        maxValue = max(1, maxValue)

        print("Year:", year)
        print("Name:", target, '  Total:', total, "    (male/female)")
        for i in range(9):
            name = nameRank[i]
            print(str(i + 1) + ". " + name + ": ",end = '')
            male = states[name].population['M'][year - 1910]
            female = states[name].population['F'][year - 1910]
            print("▓" * int(50 * (float(male) / float(maxValue))), end = '')
            print("|", end = '')
            print("▓" * int(50 * (float(female) / float(maxValue))), end = '')
            print("  ", male,"/", female, end = '')
            print(" " * 10)
        time.sleep(0.2)    

    return
        

if __name__ == "__main__":
    
    nameList = loadNameList()

    while 1:
        target = search(nameList)
        animate(target)
        print("Enter to continue...")
        if str(getch(), 'utf-8') != '\r':
            break