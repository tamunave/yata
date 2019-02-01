from yata.handy import None2Zero
from yata.handy import None2EmptyList


def honorId2Img(i):
    from awards.honors import d

    id = d.get(i)
    if id is None:
        url = None
        print("honor number {}: not in dictionnary".format(i))
    elif not id:
        url = None
        print("honor number {}: value 0".format(i))
    else:
        url = "https://awardimages.torn.com/{}.png".format(id)

    return url


def createAwardsSummary(awards):
    awardsSummary = dict()
    nAwardedTot = 0
    nAwardsTot = 0
    for k, v in awards.items():
        nAwarded = 0
        for l, w in v.items():
            if w["achieve"] == 1:
                nAwarded += 1
        nAwards = len(v)
        awardsSummary[k] = {"nAwarded": nAwarded, "nAwards": nAwards}
        nAwardedTot += nAwarded
        nAwardsTot += nAwards
    awardsSummary["All awards"] = {"nAwarded": nAwardedTot, "nAwards": nAwardsTot}

    return awardsSummary


def createAwards(allAwards, myAwards, typeOfAwards):
    from itertools import chain

    if typeOfAwards == "crimes":

        crimeBridgeMedal2App = {
            "Computer": "Computer crimes",
            "Murder": "Murder",
            "Grand theft auto": "Auto theft",
            "Theft": "Theft",
            "Drug dealing": "Drug deals",
            "Arson": "Fraud crimes"}

        crimeBridgeApp2API = {
            "Computer crimes": "computer_crimes",
            "Illegal products": "selling_illegal_products",
            "Murder": "murder",
            "Auto theft": "auto_theft",
            "Theft": "theft",
            "Drug deals": "drug_deals",
            "Fraud crimes": "fraud_crimes",
            "Other crimes": "other",
            "Total": "total"}

        forComment = {
            "Computer crimes": [9, 0.75],
            "Illegal products": [3, 1.0],
            "Murder": [10, 0.75],
            "Auto theft": [12, 0.7],
            "Theft": [4, 1.0],
            "Drug deals": [8, 0.8],
            "Fraud crimes": [11, 0.95],
            "Other crimes": [2, 1.0],
            "Total": [2, 1.0],
            }

        awards = dict({
            "Illegal products": dict(),
            "Theft": dict(),
            "Auto theft": dict(),
            "Drug deals": dict(),
            "Computer crimes": dict(),
            "Murder": dict(),
            "Fraud crimes": dict(),
            "Other crimes": dict(),
            "Organised crimes": dict(),
            "Busts": dict(),
            "Total": dict()})

        totalNumberOfBusts = None2Zero(myAwards["personalstats"].get("peoplebusted")) + None2Zero(myAwards["personalstats"].get("failedbusts"))

        for k, v in allAwards["honors"].items():
            if v["type"] in [5, 15]:
                vp = v
                vp["awardType"] = "Honor"
                vp["img"] = honorId2Img(int(k))

                if int(k) in [2, 25, 154, 157, 158]:
                    type = "Theft"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["criminalrecord"][crimeBridgeApp2API[type]])
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(forComment[type][0] * (vp["goal"] - vp["current"]) / forComment[type][1], 0)
                    vp["comment"] = ["nerve needed", "arbitrary success rate of {:,.0f}%".format(100 * forComment[type][1])]
                    awards[type]["h_" + k] = vp

                elif int(k) in [6]:
                    type = "Other crimes"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["criminalrecord"][crimeBridgeApp2API[type]])
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(forComment[type][0] * (vp["goal"] - vp["current"]) / forComment[type][1], 0)
                    vp["comment"] = ["nerve needed", "arbitrary success rate of {:,.0f}%".format(100 * forComment[type][1])]
                    awards[type]["h_" + k] = vp

                elif int(k) in [24]:
                    type = "Fraud crimes"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["criminalrecord"][crimeBridgeApp2API[type]])
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(forComment[type][0] * (vp["goal"] - vp["current"]) / forComment[type][1], 0)
                    vp["comment"] = ["nerve needed", "arbitrary success rate of {:,.0f}%".format(100 * forComment[type][1])]
                    awards[type]["h_" + k] = vp

                elif int(k) in [152]:
                    type = "Illegal products"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["criminalrecord"][crimeBridgeApp2API[type]])
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(forComment[type][0] * (vp["goal"] - vp["current"]) / forComment[type][1], 0)
                    vp["comment"] = ["nerve needed", "arbitrary success rate of {:,.0f}%".format(100 * forComment[type][1])]
                    awards[type]["h_" + k] = vp

                elif int(k) in [153]:
                    type = "Drug deals"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["criminalrecord"][crimeBridgeApp2API[type]])
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(forComment[type][0] * (vp["goal"] - vp["current"]) / forComment[type][1], 0)
                    vp["comment"] = ["nerve needed", "arbitrary success rate of {:,.0f}%".format(100 * forComment[type][1])]
                    awards[type]["h_" + k] = vp

                elif int(k) in [155, 161]:
                    type = "Computer crimes"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["criminalrecord"][crimeBridgeApp2API[type]])
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(forComment[type][0] * (vp["goal"] - vp["current"]) / forComment[type][1], 0)
                    vp["comment"] = ["nerve needed", "arbitrary success rate of {:,.0f}%".format(100 * forComment[type][1])]
                    awards[type]["h_" + k] = vp

                elif int(k) in [159]:
                    type = "Murder"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["criminalrecord"][crimeBridgeApp2API[type]])
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(forComment[type][0] * (vp["goal"] - vp["current"]) / forComment[type][1], 0)
                    vp["comment"] = ["nerve needed", "arbitrary success rate of {:,.0f}%".format(100 * forComment[type][1])]
                    awards[type]["h_" + k] = vp

                elif int(k) in [160]:
                    type = "Auto theft"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["criminalrecord"][crimeBridgeApp2API[type]])
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(forComment[type][0] * (vp["goal"] - vp["current"]) / forComment[type][1], 0)
                    vp["comment"] = ["nerve needed", "arbitrary success rate of {:,.0f}%".format(100 * forComment[type][1])]
                    awards[type]["h_" + k] = vp

                elif int(k) in [251]:
                    type = "Total"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["criminalrecord"][crimeBridgeApp2API[type]])
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(forComment[type][0] * (vp["goal"] - vp["current"]) / forComment[type][1], 0)
                    awards[type]["h_" + k] = vp

                elif int(k) in [552]:
                    type = "Organised crimes"
                    vp["goal"] = int(v["description"].split(" ")[2].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("organisedcrimes"))
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [248, 249, 250]:
                    # 248 {'name': 'Bar Breaker', 'description': 'Make 1,000 busts', 'type': 15, 'circulation': 4454, 'rarity': 'Rare', 'goal': 1000, 'awardType': 'Honor'}
                    type = "Busts"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("peoplebusted"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(totalNumberOfBusts, 1))
                    vp["left"] = max(5 * (vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["nerve needed", "current ratio of {:,.2f} people busted / bust".format(ratio)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [252]:
                    # 252 {'name': "Freedom Isn't Free", 'description': 'Make 500 bails from jail', 'type': 15, 'circulation': 2032, 'rarity': 'Extraordinary', 'goal': 500, 'awardType': 'Honor'}
                    type = "Busts"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("peoplebailed"))
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                else:
                    vp["comment"] = ""

        for k, v in allAwards["medals"].items():
            vp = v
            vp["awardType"] = "Medal"
            vp["img"] = k

            if v["type"] == "CRM":
                type = crimeBridgeMedal2App[" ".join(v["description"].split(" ")[2:-1])]
                vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                vp["current"] = None2Zero(myAwards["criminalrecord"][crimeBridgeApp2API[type]])
                vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                vp["left"] = max(forComment[type][0] * (vp["goal"] - vp["current"]) / forComment[type][1], 0)
                vp["comment"] = ["nerve needed", "arbitrary success rate of {:,.0f}%".format(100 * forComment[type][1])]
                awards[type]["m_" + k] = vp

            elif v["type"] == "OTR":
                if int(k) in [30, 31, 32, 33, 105, 106, 107]:
                    type = "Busts"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("peoplebusted"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(totalNumberOfBusts, 1))
                    vp["left"] = max(5 * (vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["nerve needed", "current ratio of {:,.2f} people busted / bust".format(ratio)]
                    awards[type]["m_" + k] = vp

    elif typeOfAwards == "drugs":

        # minutes of CD
        forComment = dict({
            "Cannabis": 75,
            "Ecstasy": 210,
            "Ketamine": 70,
            "LSD": 425,
            "Opium": 215,
            "Shrooms": 209.5,
            "Speed": 301,
            "PCP": 330,
            "Xanax": 420,
            "Vicodin": 300})

        awards = dict({
            "Cannabis": dict(),
            "Ecstasy": dict(),
            "Ketamine": dict(),
            "LSD": dict(),
            "Opium": dict(),
            "Shrooms": dict(),
            "Speed": dict(),
            "PCP": dict(),
            "Xanax": dict(),
            "Vicodin": dict()})

        for k, v in allAwards["honors"].items():
            if v["type"] == 6:
                vp = v
                vp["awardType"] = "Honor"
                vp["img"] = honorId2Img(int(k))

                if int(k) in [26]:
                    type = "Cannabis"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [29, 30, 31, 32, 33, 34, 35, 36, 37, 38]:
                    type = v["description"].split(" ")[-1]
                    vp["goal"] = 50
                    key = type.lower()[:3] + "taken"
                    if key == "ecstaken":
                        key = "exttaken"
                    vp["current"] = None2Zero(myAwards["personalstats"].get(key))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["comment"] = ["hours of CD", "average {:.0f} minutes of CD".format(forComment[type])]
                    vp["left"] = max(forComment[type] * (vp["goal"] - vp["current"]) / 60.0, 0)
                    awards[type]["h_" + k] = vp

                # else:
                #     print(k, v)

    elif typeOfAwards == "attacks":

        awards = dict({
            "Wins": dict(),
            "Defends": dict(),
            "Escapes": dict(),
            "Kill streak": dict(),
            "Critical hits": dict(),
            "Bounties": dict(),
            "Fire rounds": dict(),
            "Other attacks": dict(),
            "Assists": dict(),
            "Finishing hits": dict()})

        totalNumberOfAttacks = None2Zero(myAwards["personalstats"].get("attackswon")) + None2Zero(myAwards["personalstats"].get("attacksstealthed")) + None2Zero(myAwards["personalstats"].get("attackslost")) + \
            None2Zero(myAwards["personalstats"].get("attacksdraw")) + None2Zero(myAwards["personalstats"].get("attacksassisted"))
        totalNumberOfDefends = None2Zero(myAwards["personalstats"].get("defendslost")) + None2Zero(myAwards["personalstats"].get("defendswon")) + \
            None2Zero(myAwards["personalstats"].get("defendsstalemated")) + None2Zero(myAwards["personalstats"].get("theyrunaway"))

        # print("Total number of attacks:", totalNumberOfAttacks)

        for k, v in allAwards["honors"].items():
            if int(v["type"]) in [8, 2, 3]:
                vp = v
                vp["awardType"] = "Honor"
                vp["img"] = honorId2Img(int(k))

                if int(k) in [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]:
                    # 39 {'name': 'Woodland Camo', 'description': 'Win 5 awards', 'type': 3, 'circulation': 205626, 'rarity': 'Very Common', 'awardType': 'Honor', 'achieve': 0}
                    type = "Wins"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("attackswon"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(totalNumberOfAttacks, 1))
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["energy needed", "current ratio of {:,.4f} wins / attack".format(ratio)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [28, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 515]:
                    # 28 {'name': 'Machinist', 'description': 'Achieve 100 finishing hits with mechanical weapons', 'type': 2, 'circulation': 9269, 'rarity': 'Limited', 'awardType': 'Honor', 'achieve': 0}
                    type = "Finishing hits"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    end = " ".join(v["description"].split(" ")[5:])
                    key = end.lower()[:3] + "hits"
                    bridge = {"heahits": "heahits",
                              "mechits": "chahits",
                              "cluhits": "axehits",
                              "temhits": "grehits",
                              "machits": "machits",
                              "pishits": "pishits",
                              "rifhits": "rifhits",
                              "shohits": "shohits",
                              "smghits": "smghits",
                              "piehits": "piehits",
                              "slahits": "slahits",
                              "fishits": "h2hhits"}
                    vp["current"] = None2Zero(myAwards["personalstats"].get(bridge[key]))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(totalNumberOfAttacks, 1))
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["energy needed", "current ratio of {:,.4f} {}/attack".format(ratio, key)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [15, 16, 17]:
                    # 15 {'name': 'Kill Streaker 1', 'description': 'Achieve a best killstreak of 10', 'type': 8, 'circulation': 124231, 'rarity': 'Very Common'}
                    type = "Kill streak"
                    vp["goal"] = int(v["description"].split(" ")[-1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("killstreak"))
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["comment"] = ["best kill streak", ""]
                    vp["left"] = None2Zero(myAwards["personalstats"].get("bestkillstreak"))
                    awards[type]["h_" + k] = vp

                elif int(k) in [20, 227]:
                    # 20 {'name': 'Precision', 'description': 'Achieve 25 critical hits', 'type': 8, 'circulation': 133458, 'rarity': 'Very Common'}
                    type = "Critical hits"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("attackcriticalhits"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(totalNumberOfAttacks, 1))
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["energy needed", "current ratio of {:,.2f} critical hits / attack".format(ratio)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [22, 228]:
                    # 22 {'name': 'Self Defense', 'description': 'Win 50 defends', 'type': 8, 'circulation': 31674, 'rarity': 'Common', 'awardType': 'Honor'}
                    # 228 {'name': '007', 'description': 'Achieve 1,000 attacks and 1,000 defends', 'type': 8, 'circulation': 1710, 'rarity': 'Extraordinary', 'awardType': 'Honor'}
                    type = "Defends"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("defendswon"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(totalNumberOfDefends, 1))
                    vp["left"] = max((vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["defends left", "current ratio of {:,.4f} defends won / defend".format(ratio)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [27]:
                    # 27 {'name': 'Night Walker', 'description': 'Make 100 stealthed attacks', 'type': 8, 'circulation': 50474, 'rarity': 'Common', 'awardType': 'Honor'}
                    type = "Other attacks"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("attacksstealthed"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(None2Zero(myAwards["personalstats"].get("attackswon")), 1))
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["energy needed", "current ratio of {:.2f} stealth/win".format(ratio)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [140, 151]:
                    # 140 {'name': 'Spray And Pray', 'description': 'Fire 2,500 rounds', 'type': 8, 'circulation': 72720, 'rarity': 'Very Common', 'awardType': 'Honor'}
                    type = "Fire rounds"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("roundsfired"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(totalNumberOfAttacks, 1))
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["energy needed", "current ratio of {:,.2f} rounds/attack".format(ratio)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [230, 254, 481, 500, 615]:
                    # 230 {'name': 'Domino Effect', 'description': 'Defeat someone displaying this honor', 'type': 8, 'circulation': 112529, 'rarity': 'Very Common', 'awardType': 'Honor'}
                    # 254 {'name': 'Flatline', 'description': 'Achieve a one hit kill on a target from full life', 'type': 8, 'circulation': 72276, 'rarity': 'Very Common', 'awardType': 'Honor'}
                    # 500 {'name': 'Survivalist', 'description': 'Win an attack with only 1% life remaining', 'type': 8, 'circulation': 5980, 'rarity': 'Limited', 'awardType': 'Honor'}
                    # 481 {'name': 'Semper     Fortis', 'description': 'Defeat someone more powerful than you', 'type': 8, 'circulation': 29809, 'rarity': 'Common', 'awardType': 'Honor'}
                    # 615 {'name': 'Guardian Angel', 'description': 'Defeat someone while they are attacking someone else', 'type': 8, 'circulation': 6228, 'rarity': 'Limited', 'awardType': 'Honor'}
                    type = "Other attacks"
                    vp["goal"] = 1
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [232]:
                    # 232 {'name': 'Bounty Hunter', 'description': 'Collect 250 bounties', 'type': 8, 'circulation': 3942, 'rarity': 'Rare', 'awardType': 'Honor'}
                    type = "Bounties"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("bountiescollected"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["comment"] = ["energy needed", "25e / bounty"]
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]), 0)
                    awards[type]["h_" + k] = vp

                elif int(k) in [236]:
                    # 236 {'name': 'Dead Or Alive', 'description': 'Earn $10,000,000 from bounty hunting', 'type': 8, 'circulation': 12012, 'rarity': 'Uncommon', 'awardType': 'Honor'}
                    type = "Bounties"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", "").replace("$", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("totalbountyreward"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["head"] = "$"
                    ratio = vp["current"] / float(max(None2Zero(myAwards["personalstats"].get("bountiescollected")), 1))
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["energy needed", "current ratio of ${:,.0f} / bounty".format(ratio)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [247]:
                    # 247 {'name': 'Blood Money', 'description': 'Make $1,000,000 from a single mugging', 'type': 8, 'circulation': 32879, 'rarity': 'Common', 'awardType': 'Honor'}
                    type = "Other attacks"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", "").replace("$", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("largestmug"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["head"] = "$"
                    awards[type]["h_" + k] = vp

                elif int(k) in [270]:
                    # 270 {'name': 'Deadlock', 'description': 'Stalemate 100 times', 'type': 8, 'circulation': 5194, 'rarity': 'Rare', 'awardType': 'Honor'}
                    type = "Other attacks"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("attacksdraw")) + None2Zero(myAwards["personalstats"].get("defendsstalemated"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["comment"] = ["energy needed", "without defends"]
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]), 0)
                    awards[type]["h_" + k] = vp

                elif int(k) in [639]:
                    # 639 {'name': 'Double Dragon', 'description': 'Assist in a single attack', 'type': 8, 'circulation': 5413, 'rarity': 'Rare', 'awardType': 'Honor'}
                    type = "Assists"
                    vp["goal"] = 1
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["comment"] = ["energy needed", "25e / assist"]
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]), 0)
                    awards[type]["h_" + k] = vp

                elif int(k) in [490]:
                    # 490 {'name': 'Sidekick', 'description': 'Assist in 250 attacks', 'type': 8, 'circulation': 59, 'rarity': 'Extremely Rare', 'awardType': 'Honor'}
                    type = "Assists"
                    vp["goal"] = int(v["description"].split(" ")[2].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("attacksassisted"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["comment"] = ["energy needed", "25e / assist"]
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]), 0)
                    awards[type]["h_" + k] = vp

                elif int(k) in [517]:
                    # 517 {'name': 'Pressure Point', 'description': 'Achieve 100 one hit kills', 'type': 8, 'circulation': 13351, 'rarity': 'Uncommon', 'awardType': 'Honor'}
                    type = "Other attacks"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("onehitkills"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(totalNumberOfAttacks, 1))
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["energy needed", "current ratio of {:,.2f} one hit kill / attack".format(ratio)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [601]:
                    # 601 {'name': 'Fury', 'description': 'Achieve 10,000 hits', 'type': 8, 'circulation': 8172, 'rarity': 'Limited', 'awardType': 'Honor'}
                    type = "Other attacks"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("attackhits"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(totalNumberOfAttacks, 1))
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["energy needed", "current ratio of {:,.2f} hits / attack".format(ratio)]
                    awards[type]["h_" + k] = vp

                # else:
                #     print(k, v)

        for k, v in allAwards["medals"].items():
            if v["type"] == "ATK":
                vp = v
                vp["awardType"] = "Medal"
                vp["img"] = k

                if int(k) in [174, 175, 176, 177, 178]:
                    # 174 {'name': 'Anti Social', 'description': 'Win 50 attacks', 'type': 'ATK'}
                    type = "Wins"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("attackswon"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(totalNumberOfAttacks, 1))
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["energy needed", "current ratio of {:,.4f} wins / attack".format(ratio)]
                    awards[type]["m_" + k] = vp

                elif int(k) in [179, 180, 181, 182, 183]:
                    # 179 {'name': 'Bouncer', 'description': 'Successfully defend against 50 attacks', 'type': 'ATK', 'awardType': 'Medals'}
                    type = "Defends"
                    vp["goal"] = int(v["description"].split(" ")[-2].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("defendswon"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(totalNumberOfDefends, 1))
                    vp["left"] = max((vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["defends left", "current ratio of {:,.4f} defends won / defend".format(ratio)]
                    awards[type]["m_" + k] = vp

                elif int(k) in [184, 185, 186]:
                    # 184 {'name': 'Close Escape', 'description': 'Successfully escape from 50 foes', 'type': 'ATK', 'awardType': 'Medal'}
                    type = "Escapes"
                    vp["goal"] = int(v["description"].split(" ")[-2].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("yourunaway"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["energy needed", "25e / escape"]
                    awards[type]["m_" + k] = vp

                elif int(k) in [187, 188, 189]:
                    # 187 {'name': 'Ego Smashing', 'description': 'Have 50 enemies escape from you during an attack', 'type': 'ATK', 'awardType': 'Medal'}
                    type = "Escapes"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("theyrunaway"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(totalNumberOfDefends, 1))
                    vp["left"] = max((vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["defends left", "current ratio of {:,.4f} escapes / defend".format(ratio)]
                    awards[type]["m_" + k] = vp

                elif int(k) in [190, 191, 192, 193, 194]:
                    # 190 {'name': 'Strike', 'description': 'Acquire a kill streak of 25', 'type': 'ATK', 'awardType': 'Medal'}
                    type = "Kill streak"
                    vp["goal"] = int(v["description"].split(" ")[-1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("killstreak"))
                    vp["achieve"] = 1 if int(k) in myAwards["medals_awarded"] else min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["comment"] = ["best kill streak", ""]
                    vp["left"] = None2Zero(myAwards["personalstats"].get("bestkillstreak"))
                    awards[type]["m_" + k] = vp

                elif int(k) in [195, 196, 197]:
                    # 195 {'name': 'Boom Headshot', 'description': 'Deal 500 critical hits to enemies during combat', 'type': 'ATK', 'awardType': 'Medal'}
                    type = "Critical hits"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("attackcriticalhits"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(totalNumberOfAttacks, 1))
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["energy needed", "current ratio of {:,.2f} critical hits / attack".format(ratio)]
                    awards[type]["m_" + k] = vp

                elif int(k) in [201, 202, 203]:
                    # 201 {'name': 'Hired Gun', 'description': 'Collect 25 bounties', 'type': 'ATK', 'awardType': 'Medal', 'goal': 25, 'current': 160, 'achieve': 1}
                    type = "Bounties"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("bountiescollected"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["energy needed", "25e / bounty"]
                    awards[type]["m_" + k] = vp

                # else:
                #     print(k, v)

    elif typeOfAwards == "faction":

        awards = dict({
            "Respects": dict(),
            "Chains": dict(),
            "Commitment": dict(),
            "Dirty bomb": dict()})

        for k, v in allAwards["honors"].items():
            if int(v["type"]) in [0, 8, 2]:
                vp = v
                vp["awardType"] = "Honor"
                vp["img"] = honorId2Img(int(k))

                if int(k) in [253, 255, 257, 475, 476]:
                    # 253 {'name': 'Chainer 1', 'description': 'Participate in a 10 length chain', 'type': 8, 'circulation': 39418, 'rarity': 'Common', 'awardType': 'Honor'}
                    type = "Chains"
                    vp["goal"] = 1
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [256, 477, 478]:
                    # 256 {'name': 'Carnage', 'description': 'Make a single hit that earns your faction 10 or more respect', 'type': 8, 'circulation': 19716, 'rarity': 'Uncommon', 'awardType': 'Honor'}
                    type = "Respects"
                    vp["goal"] = 1
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [14, 156, 231]:
                    # 14 {'name': 'Slow Bomb', 'description': 'Use a dirty bomb', 'type': 0, 'circulation': 27, 'rarity': 'Extremely Rare', 'awardType': 'Honor', 'img': None, 'title': 'Slow Bomb [14]: Extremely Rare (27)'}
                    # 231 {'name': 'Discovery', 'description': 'Be in a faction which starts making a dirty bomb', 'type': 0, 'circulation': 4566, 'rarity': 'Rare', 'awardType': 'Honor', 'img': 175241290, 'title': 'Discovery [231]: Rare (4566)'}
                    # 156 {'name': 'RDD', 'description': 'Use a dirty bomb', 'type': 0, 'circulation': 27, 'rarity': 'Extremely Rare', 'awardType': 'Honor', 'img': None, 'title': 'RDD [156]: Extremely Rare (27)'}
                    type = "Dirty bomb"
                    vp["goal"] = 1
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                # else:
                #     print(k, v)

        for k, v in allAwards["medals"].items():
            if v["type"] in ["ATK", "CMT"]:
                vp = v
                vp["awardType"] = "Medal"
                vp["img"] = k

                if int(k) in [215, 216, 217, 218, 219, 220, 221, 222, 223, 224]:
                    # 215 {'name': 'Recruit', 'description': 'Earn 100 respect for your faction', 'type': 'ATK', 'awardType': 'Medal'}
                    type = "Respects"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("respectforfaction"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    totalNumberOfAttacks = None2Zero(myAwards["personalstats"].get("attackswon")) + None2Zero(myAwards["personalstats"].get("attacksstealthed")) + \
                        None2Zero(myAwards["personalstats"].get("attackslost")) + None2Zero(myAwards["personalstats"].get("attacksdraw")) + None2Zero(myAwards["personalstats"].get("attacksassisted"))
                    ratio = vp["current"] / float(max(totalNumberOfAttacks, 1))
                    vp["left"] = max(25 * (vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["energy needed", "current ratio of {:,.2f} respects / attack".format(ratio)]
                    awards[type]["m_" + k] = vp

                elif int(k) in [26, 27, 28, 29, 108, 109, 148, 149, 150, 151]:
                    # 26 {'name': 'Apprentice Faction Member', 'description': 'Serve 100 days in a single faction', 'type': 'CMT', 'awardType': 'Medal'}
                    type = "Commitment"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["faction"].get("days_in_faction"))
                    vp["achieve"] = 1 if int(k) in myAwards["medals_awarded"] else min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max((vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["day left" if vp["left"] == 1 else "days left", ""]
                    awards[type]["m_" + k] = vp

                # else:
                #     print(k, v)

    elif typeOfAwards == "items":

        awards = dict({
            "City": dict(),
            "Medical items": dict(),
            "Other items": dict(),
            "Consume": dict()})

        for k, v in allAwards["honors"].items():
            if int(v["type"]) in [0, 15, 16]:
                vp = v
                vp["awardType"] = "Honor"
                vp["img"] = honorId2Img(int(k))

                if int(k) in [398, 418]:
                    # 398 {'name': 'Anaemic', 'description': 'Fill 1,000 empty blood bags', 'type': 15, 'circulation': 3823, 'rarity': 'Rare', 'awardType': 'Honor', 'goal': 1000, 'current': 0, 'achieve': 0.0}
                    type = "Medical items"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("bloodwithdrawn"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(3 * (vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["hours of CD", "3h CD / blood bag filled"]

                    awards[type]["h_" + k] = vp

                elif int(k) in [367, 406]:
                    # 406 {'name': 'Vampire', 'description': 'Random chance upon using a blood bag', 'type': 15, 'circulation': 10562, 'rarity': 'Limited', 'awardType': 'Honor', 'achieve': 0}
                    # 367 {'name': 'Clotted', 'description': 'Suffer from an acute haemolytic reaction, or be immune to it', 'type': 15, 'circulation': 11247, 'rarity': 'Uncommon', 'awardType': 'Honor', 'achieve': 0}
                    type = "Medical items"
                    vp["goal"] = 1
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [4]:
                    # 4 {'name': "I'm a Real Doctor", 'description': 'Steal 500 medical items', 'type': 15, 'circulation': 24992, 'rarity': 'Common', 'awardType': 'Honor', 'achieve': 0}
                    type = "Medical items"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("medstolen"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max((vp["goal"] - vp["current"]) / (0.5 * 7), 0)
                    vp["comment"] = ["day left" if vp["left"] == 1 else "days left", "as brain surgeon stealing SFAK"]
                    awards[type]["h_" + k] = vp

                elif int(k) in [7]:
                    # 7 {'name': 'Magical Veins', 'description': 'Use 5,000 medical items', 'type': 15, 'circulation': 4686, 'rarity': 'Rare', 'awardType': 'Honor', 'achieve': 0}
                    type = "Medical items"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("medicalitemsused"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(vp["goal"] - vp["current"], 0)
                    vp["comment"] = ["hours of CD", "using 1h CD blood bags"]
                    awards[type]["h_" + k] = vp

                elif int(k) in [1]:
                    # 1 {'name': "I'm Watching You", 'description': 'Find 50 items in the city', 'type': 16, 'circulation': 26943, 'rarity': 'Common', 'awardType': 'Honor', 'achieve': 0}
                    type = "City"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("cityfinds"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(myAwards.get("age"), 1))
                    vp["left"] = max((vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["day left" if vp["left"] == 1 else "days left", "current ratio of {:.2f} finds / day".format(ratio)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [238]:
                    # 238 {'name': 'Optimist', 'description': 'Find 1,000 items in the dump', 'type': 16, 'circulation': 5850, 'rarity': 'Limited', 'awardType': 'Honor', 'achieve': 0}
                    type = "City"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("dumpfinds"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(5 * (vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["energy needed", "for 5e a search"]
                    awards[type]["h_" + k] = vp

                elif int(k) in [271]:
                    # 271 {'name': 'Eco Friendly', 'description': 'Trash 5,000 items', 'type': 16, 'circulation': 14796, 'rarity': 'Uncommon', 'awardType': 'Honor', 'achieve': 0}
                    type = "City"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("itemsdumped"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max((vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["left", ""]
                    awards[type]["h_" + k] = vp

                elif int(k) in [273]:
                    # 273 {'name': 'Bargain Hunter', 'description': 'Win 10 auctions', 'type': 16, 'circulation': 8415, 'rarity': 'Limited', 'awardType': 'Honor', 'achieve': 0}
                    type = "Other items"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("auctionswon"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    awards[type]["h_" + k] = vp

                elif int(k) in [216]:
                    # 216 {'name': 'Silicon Valley', 'description': 'Code 100 viruses', 'type': 0, 'circulation': 3627, 'rarity': 'Rare', 'awardType': 'Honor', 'img': 539384064, 'title': 'Silicon Valley [216]: Rare (3627)'}
                    type = "Other items"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("virusescoded"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(3 * (vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["day left" if vp["left"] == 1 else "days left", "coding simple viruses with IIL block and education"]
                    awards[type]["h_" + k] = vp

                elif int(k) in [527]:
                    # 527 {'name': 'Worth it', 'description': 'Use a stat enhancer', 'type': 16, 'circulation': 698, 'rarity': 'Extraordinary', 'awardType': 'Honor', 'achieve': 0}
                    type = "Consume"
                    vp["goal"] = 1
                    vp["current"] = None2Zero(myAwards["personalstats"].get("statenhancersused"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    awards[type]["h_" + k] = vp

                elif int(k) in [534]:
                    # 534 {'name': 'Alcoholic', 'description': 'Drink 500 bottles of alcohol', 'type': 16, 'circulation': 7842, 'rarity': 'Limited', 'awardType': 'Honor', 'achieve': 0}
                    type = "Consume"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("alcoholused"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(0.5 * (vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["hours of CD", "using 1h CD bootles"]
                    awards[type]["h_" + k] = vp

                elif int(k) in [537]:
                    # 537 {'name': 'Diabetic', 'description': 'Eat 500 bags of candy', 'type': 16, 'circulation': 7948, 'rarity': 'Limited', 'awardType': 'Honor', 'achieve': 0}
                    type = "Consume"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("candyused"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(0.5 * (vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["hours of CD", "using 30min CD sweets"]
                    awards[type]["h_" + k] = vp

                elif int(k) in [538]:
                    # 538 {'name': 'Sodaholic', 'description': 'Drink 500 cans of energy drink', 'type': 16, 'circulation': 898, 'rarity': 'Extraordinary', 'awardType': 'Honor', 'achieve': 0}
                    type = "Consume"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("energydrinkused"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(2 * (vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["hours of CD", "using 2h CD cans"]
                    awards[type]["h_" + k] = vp

                elif int(k) in [539]:
                    # 539 {'name': 'Bibliophile', 'description': 'Read 10 books', 'type': 16, 'circulation': 384, 'rarity': 'Extraordinary', 'awardType': 'Honor', 'achieve': 0}
                    type = "Consume"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("booksread"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(31 * (vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["day left" if vp["left"] == 1 else "days left", "reading 31 days long books"]
                    awards[type]["h_" + k] = vp

                # else:
                #     print(k, v)

        for k, v in allAwards["medals"].items():
            if v["type"] == "OTR":
                vp = v
                vp["awardType"] = "Medal"
                vp["img"] = k

                if int(k) in [204, 205, 206]:
                    # 204 {'name': 'Watchful', 'description': 'Find 10 items in the city', 'type': 'OTR', 'awardType': 'Medal', 'goal': 10, 'current': 0, 'achieve': 0.0}
                    type = "City"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("cityfinds"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(myAwards.get("age"), 1))
                    vp["left"] = max((vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["day left" if vp["left"] == 1 else "days left", "current ratio of {:.2f} finds / day".format(ratio)]
                    awards[type]["m_" + k] = vp

                elif int(k) in [198, 199, 200]:
                    # 198 {'name': 'Pin Cushion', 'description': 'Use 500 medical items', 'type': 'OTR', 'awardType': 'Medal', 'goal': 500, 'current': 0, 'achieve': 0.0}
                    type = "Medical items"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("medicalitemsused"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(vp["goal"] - vp["current"], 0)
                    vp["comment"] = ["hours of CD", "using 1h CD blood bags"]
                    awards[type]["m_" + k] = vp

                # else:
                #     print(k, v)

    elif typeOfAwards == "travel":

        awards = dict({
            "Destinations": dict(),
            "Time": dict()})

        pilot = 0.7 if "+ Access to airstrip" in None2EmptyList(myAwards["property_perks"]) else 1.0

        flightTimes = {
            "mextravel": 26,
            "caytravel": 35,
            "cantravel": 41,
            "hawtravel": 134,
            "lontravel": 159,
            "argtravel": 167,
            "switravel": 175,
            "japtravel": 225,
            "chitravel": 242,
            "dubtravel": 271,
            "soutravel": 297,
            }

        for k, v in allAwards["honors"].items():
            if int(v["type"]) in [7]:
                vp = v
                vp["awardType"] = "Honor"
                vp["img"] = honorId2Img(int(k))

                if int(k) in [11, 165]:
                    # 11 {'name': 'Mile High Club', 'description': 'Travel 100 times', 'type': 7, 'circulation': 31338, 'rarity': 'Common', 'awardType': 'Honor', 'img': 241952085, 'title': 'Mile High Club [11]: Common (31338)'}
                    type = "Time"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("traveltimes"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(myAwards.get("age"), 1))
                    vp["left"] = max((vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["days left", "current ratio of {:.02f} travels / day".format(ratio)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [549, 567]:
                    # 549 {'name': 'Tourist', 'description': 'Spend 7 days in the air', 'type': 7, 'circulation': 16881, 'rarity': 'Uncommon', 'awardType': 'Honor', 'img': 724568067, 'title': 'Tourist [549]: Uncommon (16881)'}
                    type = "Time"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = int(None2Zero(myAwards["personalstats"].get("traveltime")) / (3600 * 24))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(myAwards.get("age"), 1))
                    vp["left"] = max((vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["days left", "current ratio of {:.02f} hours / day".format(ratio)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 272]:
                    # 130 {'name': 'Maradona', 'description': 'Travel to Argentina 50 times', 'type': 7, 'circulation': 10543, 'rarity': 'Limited', 'awardType': 'Honor', 'img': 697523940, 'title': 'Maradona [130]: Limited (10543)'}
                    type = "Destinations"
                    key = v["description"].split(" ")[2].lower()[:3] + "travel"
                    key = "lontravel" if key == "thetravel" else key
                    vp["goal"] = int(v["description"].split(" ")[-2].replace(",", ""))
                    vp["current"] = int(None2Zero(myAwards["personalstats"].get(key)))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(2 * flightTimes[key] * pilot * (vp["goal"] - vp["current"]) / 60., 0)
                    vp["comment"] = ["hours left", "with a one way travel of {:.0f} minutes".format(flightTimes[key] * pilot)]
                    awards[type]["h_" + k] = vp

                # else:
                #     print(k, v)

        for k, v in allAwards["medals"].items():
            if v["type"] == "OTR":
                vp = v
                vp["awardType"] = "Medal"
                vp["img"] = k

                if int(k) in [207, 208, 209]:
                    # 207 {'name': 'Frequent Flyer', 'description': 'Travel abroad 25 times', 'type': 'OTR', 'awardType': 'Medal', 'achieve': 0}
                    type = "Time"
                    vp["goal"] = int(v["description"].split(" ")[2].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("traveltimes"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(myAwards.get("age"), 1))
                    vp["left"] = max((vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["days left", "current ratio of {:.02f} travels / day".format(ratio)]
                    awards[type]["m_" + k] = vp

                # else:
                #     print(k, v)

    elif typeOfAwards == "work":
        from awards.educations import educations

        awards = dict({
            "Bachelors": dict(),
            "Courses": dict(),
            "Working stats": dict(),
            "City jobs": dict()})

        for k, v in allAwards["honors"].items():
            if int(v["type"]) in [0, 4, 15]:
                vp = v
                vp["awardType"] = "Honor"
                vp["img"] = honorId2Img(int(k))

                # get time reduction
                educationTimeReduction = 1.0
                for perk in None2EmptyList(myAwards.get("merit_perks")):
                    start, end = perk.split(" ")[1], " ".join(perk.split(" ")[2:])
                    educationTimeReduction = educationTimeReduction * (1. - float(start.replace("%", "")) / 100.) if end == "Education length" else educationTimeReduction
                for perk in None2EmptyList(myAwards.get("stock_perks")):
                    start, end = perk.split(" ")[1], " ".join(perk.split(" ")[2:])
                    educationTimeReduction = educationTimeReduction * (1. - float(start.replace("%", "")) / 100.) if end == "Education length reduction (WSSB)" else educationTimeReduction
                for perk in None2EmptyList(myAwards.get("job_perks")):
                    start, end = perk.split(" ")[1], " ".join(perk.split(" ")[2:])
                    educationTimeReduction = educationTimeReduction * (1. - float(start.replace("%", "")) / 100.) if end == "Education time" else educationTimeReduction

                if int(k) in [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]:
                    # 53 {'name': 'Biology Bachelor', 'description': 'Complete all classes in Biology', 'type': 4, 'circulation': 28936, 'rarity': 'Common', 'awardType': 'Honor', 'img': None, 'title': 'Biology Bachelor [53]: Common (28936)'}
                    type = "Bachelors"

                    eduBridge = {
                        "Biology": "Biology",
                        "Business": "Commerce",
                        "Combat": "Military Arts and Science",
                        "ICT": "Computer Science",
                        "Defense": "Self Defense",
                        "General": "General Studies",
                        "Fitness": "Health Sciences",
                        "History": "History",
                        "Law": "Law",
                        "Mathematics": "Mathematics",
                        "Psychology": "Psychological Sciences",
                        "Sports": "Sports Science",
                        }

                    eduDic = {
                        "Commerce": list(range(1, 14)),
                        "History": list(range(14, 22)),
                        "Mathematics": list(chain([22], range(24, 34))),
                        "Biology": list(chain(range(34, 43), [127])),
                        "Sports Science": list(chain(range(43, 52), [126])),
                        "Computer Science": list(range(52, 63)),
                        "Psychological Sciences": list(range(63, 70)),
                        "Self Defense": list(range(70, 78)),
                        "Military Arts and Science": list(chain(range(78, 88), [125])),
                        "Law": list(range(88, 103)),
                        "Health Sciences": list(range(103, 112)),
                        "General Studies": list(range(112, 124)),
                        }

                    name = v["name"].split(" ")[0]
                    educationCompleted = None2EmptyList(myAwards.get("education_completed"))
                    numberOfClasses = len(eduDic[eduBridge[name]])
                    numberOfClassesDone = 0
                    timeLeft = 0
                    for v in eduDic[eduBridge[name]]:
                        if int(v) in educationCompleted:
                            numberOfClassesDone += 1
                        else:
                            timeLeft += educations[str(v)]["duration"]
                    vp["goal"] = numberOfClasses
                    vp["current"] = numberOfClassesDone
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else numberOfClassesDone / float(numberOfClasses)
                    vp["left"] = max(educationTimeReduction * timeLeft / (24. * 3600.), 0)
                    vp["comment"] = ["days left", "with {:.0f}% education length reducion".format((1. - educationTimeReduction) * 100.)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [653, 659]:
                    # 653 {'name': 'Smart Alec', 'description': 'Complete 10 education courses', 'type': 4, 'circulation': 150699, 'rarity': 'Very Common', 'awardType': 'Honor', 'img': 872280837, 'title': 'Smart Alec [653]: Very Common (150699)'}
                    type = "Courses"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(len(myAwards.get("education_completed")))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    i = 0
                    timeLeft = 0
                    for a, b in sorted(educations.items(), key=lambda x: x[1]['duration'], reverse=False):
                        if int(a) not in None2EmptyList(myAwards.get("education_completed")):
                            if i >= vp["goal"] - vp["current"]:
                                break
                            i += 1
                            timeLeft += educationTimeReduction * b["duration"]
                    vp["left"] = max(educationTimeReduction * timeLeft / (24. * 3600.), 0)
                    vp["comment"] = ["days left", "taking the shortest courses left with {:.0f}% education length reducion".format((1. - educationTimeReduction) * 100.)]

                    awards[type]["h_" + k] = vp

                elif int(k) in [4]:
                    # 4 {'name': "I'm a Real Doctor", 'description': 'Steal 500 medical items', 'type': 15, 'circulation': 24996, 'rarity': 'Common', 'awardType': 'Honor', 'img': 408554952, 'title': "I'm a Real Doctor [4]: Common (24996)"}
                    type = "City jobs"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("medstolen"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max((vp["goal"] - vp["current"]) / (0.5 * 7), 0)
                    vp["comment"] = ["day left" if vp["left"] == 1 else "days left", "as brain surgeon stealing SFAK"]
                    awards[type]["h_" + k] = vp

                elif int(k) in [23, 267]:
                    # 23 {'name': 'Florence Nightingale', 'description': 'Revive 500 people', 'type': 15, 'circulation': 1053, 'rarity': 'Extraordinary', 'awardType': 'Honor', 'img': None, 'title': 'Florence Nightingale [23]: Extraordinary (1053)'}
                    type = "City jobs"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("revives"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    e = 75
                    for perk in None2EmptyList(myAwards.get("faction_perks")):
                        start, end = " ".join(perk.split(" ")[:-1]), perk.split(" ")[-1]
                        e = float(end) if start == "+ Reduces the energy used while reviving to" else e

                    vp["left"] = max(e * (vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["energy left", "with {:.0f} energy / revive".format(e)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [164]:
                    # 164 {'name': 'Keen', 'description': 'Spy on people while in the army 100 times', 'type': 0, 'circulation': 2066, 'rarity': 'Extraordinary', 'awardType': 'Honor', 'img': None, 'title': 'Keen [164]: Extraordinary (2066)'}
                    type = "City jobs"
                    vp["goal"] = int(v["description"].split(" ")[-2].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("?"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max((vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["days left", "as General in the army"]
                    awards[type]["h_" + k] = vp

                elif int(k) in [220]:
                    # 220 {'name': 'The Affronted', 'description': 'Infuriate all interviewers in starter jobs', 'type': 0, 'circulation': 4630, 'rarity': 'Rare', 'awardType': 'Honor', 'img': 384148528, 'title': 'The Affronted [220]: Rare (4630)'}
                    type = "City jobs"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [525, 530, 533]:
                    # 525 {'name': 'Tireless', 'description': 'Attain 100,000 endurance', 'type': 4, 'circulation': 8731, 'rarity': 'Limited', 'awardType': 'Honor', 'img': None, 'title': 'Tireless [525]: Limited (8731)'}
                    # 530 {'name': 'Talented', 'description': 'Attain 100,000 intelligence', 'type': 4, 'circulation': 11171, 'rarity': 'Uncommon', 'awardType': 'Honor', 'img': None, 'title': 'Talented [530]: Uncommon (11171)'}
                    # 533 {'name': 'Tough', 'description': 'Attain 100,000 manual labour', 'type': 4, 'circulation': 7204, 'rarity': 'Limited', 'awardType': 'Honor', 'img': None, 'title': 'Tough [533]: Limited (7204)'}
                    type = "Working stats"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    key = "_".join(v["description"].split(" ")[2:]).replace("ou", "o")
                    vp["current"] = None2Zero(myAwards.get(key))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max((vp["goal"] - vp["current"]) / 50., 0)
                    vp["comment"] = ["days left", "if daily trains as primary stat"]
                    awards[type]["h_" + k] = vp

                # else:
                #     print(k, v)

    elif typeOfAwards == "gym":

        awards = dict({
            "Memberships": dict(),
            "Defense": dict(),
            "Dexterity": dict(),
            "Speed": dict(),
            "Strength": dict(),
            "Total stats": dict()})

        for k, v in allAwards["honors"].items():
            if int(v["type"]) in [10]:
                vp = v
                vp["awardType"] = "Honor"
                vp["img"] = honorId2Img(int(k))

                if int(k) in [240, 241, 242, 243, 297, 497, 505, 506, 635, 640, 643, 646, 686, 687, 694, 720, 723, 708, 629]:
                    # 240 {'name': 'Behemoth', 'description': 'Gain 1,000,000 defense', 'type': 10, 'circulation': 20913, 'rarity': 'Uncommon', 'awardType': 'Honor', 'img': 362146978, 'title': 'Behemoth [240]: Uncommon (20913)'}
                    type = "zzz".join(v["description"].split(" ")[2:]).title().replace("zzz", " ")
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    key = v["description"].split(" ")[2].lower()
                    vp["current"] = None2Zero(myAwards.get(key)).split(".")[0]
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    awards[type]["h_" + k] = vp
                elif int(k) in [233, 234, 235]:
                    # 233 {'name': 'Bronze Belt', 'description': 'Own all lightweight gym memberships', 'type': 10, 'circulation': 61239, 'rarity': 'Common', 'awardType': 'Honor', 'img': 439667520, 'title': 'Bronze Belt [233]: Common (61239)'}
                    type = "Memberships"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

    elif typeOfAwards == "money":

        awards = dict({
            "Stocks": dict(),
            "Bank": dict(),
            "Estate": dict(),
            "Networth": dict(),
            "Casino": dict(),
            "Other money": dict()})

        for k, v in allAwards["honors"].items():
            if int(v["type"]) in [0, 9, 14, 16]:
                vp = v
                vp["awardType"] = "Honor"
                vp["img"] = honorId2Img(int(k))

                if int(k) in [546]:
                    # 546 {'name': 'Dividend', 'description': 'Receive 100 stock payouts ', 'type': 14, 'circulation': 8295, 'rarity': 'Limited', 'awardType': 'Honor', 'img': 543547927, 'title': 'Dividend [546]: Limited (8295)'}
                    type = "Stocks"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("stockpayouts"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    awards[type]["h_" + k] = vp

                elif int(k) in [3, 19, 546]:
                    # 3 {'name': 'Moneybags', 'description': 'Achieve excellent success in the stock market', 'type': 14, 'circulation': 20747, 'rarity': 'Uncommon', 'awardType': 'Honor', 'img': 234842928, 'title': 'Moneybags [3]: Uncommon (20747)'}
                    # 19 {'name': 'Stock Analyst', 'description': 'Buy and sell shares actively in the stock market', 'type': 14, 'circulation': 2446, 'rarity': 'Rare', 'awardType': 'Honor', 'img': 890959235, 'title': 'Stock Analyst [19]: Rare (2446)'}
                    type = "Stocks"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [10]:
                    # 10 {'name': 'Green, Green Grass', 'description': 'Make an investment in the city bank of over $1,000,000,000', 'type': 14, 'circulation': 21990, 'rarity': 'Uncommon', 'awardType': 'Honor', 'img': 927018892, 'title': 'Green, Green Grass [10]: Uncommon (21990)'}
                    type = "Bank"
                    vp["goal"] = int(v["description"].split(" ")[-1].replace(",", "").replace("$", ""))
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = None2Zero(myAwards["networth"].get("bank"))
                    vp["head"] = "$"
                    awards[type]["h_" + k] = vp

                elif int(k) in [12]:
                    # 12 {'name': 'Pocket Money', 'description': 'Make an investment in the city bank', 'type': 14, 'circulation': 182442, 'rarity': 'Very Common', 'awardType': 'Honor', 'img': 533285823, 'title': 'Pocket Money [12]: Very Common (182442)'}
                    type = "Bank"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [8]:
                    # 8 {'name': 'Loan Shark', 'description': 'Achieve a high credit score with Duke', 'type': 14, 'circulation': 10499, 'rarity': 'Limited', 'awardType': 'Honor', 'img': 602403620, 'title': 'Loan Shark [8]: Limited (10499)'}
                    type = "Other money"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [9, 258]:
                    # 9 {'name': 'Luxury Real Estate', 'description': 'Buy an airstrip for a property', 'type': 0, 'circulation': 22735, 'rarity': 'Common', 'awardType': 'Honor', 'img': 442995373, 'title': 'Luxury Real Estate [9]: Common (22735)'}
                    # 258 {'name': 'The High Life', 'description': 'Own a yacht', 'type': 0, 'circulation': 9173, 'rarity': 'Limited', 'awardType': 'Honor', 'img': 780858042, 'title': 'The High Life [258]: Limited (9173)'}
                    type = "Estate"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [239]:
                    # 239 {'name': 'Middleman', 'description': 'Have 100 customers buy from your bazaar', 'type': 16, 'circulation': 27683, 'rarity': 'Common', 'awardType': 'Honor', 'achieve': 0}
                    type = "Other money"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("bazaarcustomers"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    awards[type]["h_" + k] = vp

                elif int(k) in [268]:
                    # 268 {'name': 'Wholesaler', 'description': 'Sell 1,000 points on the market', 'type': 0, 'circulation': 29688, 'rarity': 'Common', 'awardType': 'Honor', 'img': 517070365, 'title': 'Wholesaler [268]: Common (29688)'}
                    type = "Other money"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("pointssold"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    awards[type]["h_" + k] = vp

                elif int(k) in [237, 269, 275, 276, 326, 327, 338, 427, 431, 437, 513]:
                    # 237 {'name': 'Poker King', 'description': 'Earn a poker score of 10,000,000', 'type': 9, 'circulation': 2267, 'rarity': 'Rare', 'awardType': 'Honor', 'img': '/static/honors/tsimg/NQ5Yy.png', 'title': 'Poker King [237]: Rare (2267)'}
                    type = "Casino"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                # else:
                #     print(k, v)

        for k, v in allAwards["medals"].items():
            if v["type"] == "NTW":
                vp = v
                vp["awardType"] = "Medal"
                vp["img"] = k

                if int(k) in [89, 90, 91, 92, 93, 94, 95, 96, 236, 237, 238, 239, 240, 241]:
                    # 89 {'name': 'Apprentice', 'description': 'Have a recorded networth value of $100,000 for at least 3 days', 'type': 'NTW', 'awardType': 'Medal'}
                    type = "Networth"
                    vp["goal"] = int(v["description"].split(" ")[6].replace(",", "").replace("$", ""))
                    vp["current"] = None2Zero(myAwards["networth"].get("total"))
                    vp["achieve"] = 1 if int(k) in myAwards["medals_awarded"] else min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["head"] = "$"
                    awards[type]["m_" + k] = vp

                # else:
                #     print(k, v)

    elif typeOfAwards == "competitions":

        awards = dict({
            "Elimination": dict(),
            "Other competitions": dict(),
            "Token shop": dict(),
            "TC endurance": dict(),
            "Torn of the dead": dict(),
            "Dog tag": dict()})

        for k, v in allAwards["honors"].items():
            if int(v["type"]) in [13]:
                vp = v
                vp["awardType"] = "Honor"
                vp["img"] = honorId2Img(int(k))

                if int(k) in [213, 222, 330]:
                    # 213 {'name': 'Allure', 'description': 'Participate in the Mr & Ms Torn competition', 'type': 13, 'circulation': 3928, 'rarity': 'Rare', 'awardType': 'Honor', 'img': 576433461, 'title': 'Allure [213]: Rare (3928)'}
                    # 222 {'name': 'Good Friday', 'description': 'Exchange all eggs for a gold one in the Easter egg hunt competition', 'type': 13, 'circulation': 14880, 'rarity': 'Uncommon', 'awardType': 'Honor', 'img': 566217580, 'title': 'Good Friday [222]: Uncommon (14880)'}
                    # 330 {'name': 'Champion', 'description': '', 'type': 13, 'circulation': 106, 'rarity': 'Extremely Rare', 'awardType': 'Honor', 'img': None, 'title': 'Champion [330]: Extremely Rare (106)'}
                    type = "Other competitions"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [263, 306, 311]:
                    # 263 {'name': 'Survivor', 'description': 'Finish the Torn of the Dead competition as a civilian', 'type': 13, 'circulation': 1342, 'rarity': 'Extraordinary', 'awardType': 'Honor', 'img': None, 'title': 'Survivor [263]: Extraordinary (1342)'}
                    # 306 {'name': 'Resistance', 'description': 'Attack 50 zombies in the Torn of the Dead competition', 'type': 13, 'circulation': 3213, 'rarity': 'Rare', 'awardType': 'Honor', 'img': 412574893, 'title': 'Resistance [306]: Rare (3213)'}
                    # 311 {'name': 'Brainz', 'description': 'Infect 50 civilians in the Torn of the Dead competition', 'type': 13, 'circulation': 509, 'rarity': 'Extraordinary', 'awardType': 'Honor', 'img': None, 'title': 'Brainz [311]: Extraordinary (509)'}
                    type = "Torn of the dead"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [214, 224, 225, 278]:
                    # 214 {'name': 'Jack Of All Trades', 'description': 'Complete the 4th stage of the TC endurance challenge', 'type': 13, 'circulation': 12742, 'rarity': 'Uncommon', 'awardType': 'Honor', 'img': 241772067, 'title': 'Jack Of All Trades [214]: Uncommon (12742)'}
                    # 224 {'name': 'Proven Capacity', 'description': 'Complete the 5th stage of the TC endurance challenge', 'type': 13, 'circulation': 6144, 'rarity': 'Limited', 'awardType': 'Honor', 'img': None, 'title': 'Proven Capacity [224]: Limited (6144)'}
                    # 225 {'name': 'Master Of One', 'description': 'Complete the endurance challenge bonus task', 'type': 13, 'circulation': 5286, 'rarity': 'Rare', 'awardType': 'Honor', 'img': None, 'title': 'Master Of One [225]: Rare (5286)'}
                    # 278 {'name': 'Globally Effective', 'description': 'Complete the 6th stage of the TC endurance challenge', 'type': 13, 'circulation': 4941, 'rarity': 'Rare', 'awardType': 'Honor', 'img': None, 'title': 'Globally Effective [278]: Rare (4941)'}
                    type = "TC endurance"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [215, 281, 283, 284, 294, 297, 298, 308, 313, 315, 318, 321]:
                    # 215 {'name': 'Labyrinth', 'description': 'Purchased from the Token Shop', 'type': 13, 'circulation': 4542, 'rarity': 'Rare', 'awardType': 'Honor', 'img': 431217843, 'title': 'Labyrinth [215]: Rare (4542)'}
                    type = "Token shop"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0

                    token = {
                        "Globule": 3,
                        "Retro": 4,
                        "Acute": 4,
                        "Serenity": 5,
                        "Futurity": 6,
                        "Constellations": 7,
                        "Parallel": 8,
                        "Labyrinth": 9,
                        "Glimmer": 10,
                        "Supernova": 12,
                        "Pepperoni": 13,
                        "Electric Dream": 15,
                        }

                    vp["left"] = (1 - vp["achieve"]) * token[v["name"]]
                    vp["comment"] = ["token needed", "cost {} tokens".format(token[v["name"]])]

                    awards[type]["h_" + k] = vp

                elif int(k) in [221, 277]:
                    # 221 {'name': 'KIA', 'description': 'Get 50 or more tags in the Dog Tag competition', 'type': 13, 'circulation': 5513, 'rarity': 'Rare', 'awardType': 'Honor', 'img': 844457156, 'title': 'KIA [221]: Rare (5513)'}
                    # 277 {'name': 'Departure', 'description': 'Get 250 or more tags in the Dog Tag competition', 'type': 13, 'circulation': 1279, 'rarity': 'Extraordinary', 'awardType': 'Honor', 'img': None, 'title': 'Departure [277]: Extraordinary (1279)'}
                    type = "Dog tag"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [226, 280, 279, 212]:
                    # 226 {'name': 'Purple Heart', 'description': 'Achieve 50 attacks against enemy team members in the Elimination competition', 'type': 13, 'circulation': 15101, 'rarity': 'Uncommon', 'awardType': 'Honor', 'img': 783491253, 'title': 'Purple Heart [226]: Uncommon (15101)'}
                    # 280 {'name': 'Supremacy', 'description': 'Finish the Elimination competition within the top 5% of attacking players in your team', 'type': 13, 'circulation': 4491, 'rarity': 'Rare', 'awardType': 'Honor', 'img': 790762265, 'title': 'Supremacy [280]: Rare (4491)'}
                    # 279 {'name': 'Domination', 'description': 'Finish the Elimination competition with your team in 1st place', 'type': 13, 'circulation': 2481, 'rarity': 'Rare', 'awardType': 'Honor', 'img': None, 'title': 'Domination [279]: Rare (2481)'}
                    # 212 {'name': 'Mission Accomplished', 'description': 'Finish the Elimination competition with your team in 1st, 2nd or 3rd', 'type': 13, 'circulation': 28864, 'rarity': 'Common', 'awardType': 'Honor', 'img': 153743487, 'title': 'Mission Accomplished [212]: Common (28864)'}
                    type = "Elimination"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                # else:
                #     print(k, v)

    elif typeOfAwards == "commitment":

        awards = dict({
            "Spouse": dict(),
            "Donator": dict(),
            "Age": dict(),
            "Level": dict(),
            "Rank": dict(),
            "Faction": dict(),
            "Other commitment": dict()})

        for k, v in allAwards["honors"].items():
            if int(v["type"]) in [0, 11, 12]:
                vp = v
                vp["awardType"] = "Honor"
                vp["img"] = honorId2Img(int(k))

                if int(k) in [163, 162, 166]:
                    # 163 {'name': 'Fascination', 'description': 'Stay married for 250 days', 'type': 11, 'circulation': 75114, 'rarity': 'Very Common', 'awardType': 'Honor', 'img': 431464057, 'title': 'Fascination [163]: Very Common (75114)'}
                    # 162 {'name': 'Chasm', 'description': 'Stay married for 750 days', 'type': 11, 'circulation': 48240, 'rarity': 'Common', 'awardType': 'Honor', 'img': 636752583, 'title': 'Chasm [162]: Common (48240)'}
                    # 166 {'name': 'Stairway To Heaven', 'description': 'Stay married for 1,500 days', 'type': 11, 'circulation': 27557, 'rarity': 'Common', 'awardType': 'Honor', 'img': 507297243, 'title': 'Stairway To Heaven [166]: Common (27557)'}
                    type = "Spouse"
                    vp["goal"] = int(v["description"].split(" ")[-2].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["married"].get("duration"))
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max((vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["day left" if vp["left"] == 1 else "days left", ""]
                    awards[type]["h_" + k] = vp

                elif int(k) in [245]:
                    # 245 {'name': 'Couch Potato', 'description': 'Achieve 1,000 hours of activity on Torn', 'type': 11, 'circulation': 8396, 'rarity': 'Limited', 'awardType': 'Honor', 'img': 965199742, 'title': 'Couch Potato [245]: Limited (8396)'}
                    type = "Other commitment"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = int(None2Zero(myAwards["personalstats"].get("useractivity")) / 3600)
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(myAwards.get("age"), 1))
                    vp["left"] = max((vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["day left" if vp["left"] == 1 else "days left", "current ratio of {:.02f} hours / day".format(ratio)]
                    awards[type]["h_" + k] = vp

                elif int(k) in [312]:
                    # 312 {'name': 'Time Traveller', 'description': 'Survive a Torn City restore', 'type': 0, 'circulation': 24165, 'rarity': 'Common', 'awardType': 'Honor', 'img': 834531746, 'title': 'Time Traveller [312]: Common (24165)'}
                    type = "Other commitment"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [3, 19, 546]:
                    type = "Spouse"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [13, 18, 259, 264, 265]:
                    # 18 {'name': 'Another Brick In The Wall', 'description': 'Reach level 10', 'type': 12, 'circulation': 197925, 'rarity': 'Very Common', 'awardType': 'Honor', 'img': 978797305, 'title': 'Another Brick In The Wall [18]: Very Common (197925)'}
                    type = "Level"
                    vp["goal"] = int(v["description"].split(" ")[-1])
                    vp["current"] = None2Zero(myAwards.get("level"))
                    vp["achieve"] = min(1, vp["current"] / float(vp["goal"]))
                    awards[type]["h_" + k] = vp

                # else:
                #     print(k, v)

        for k, v in allAwards["medals"].items():
            if v["type"] in ["CMT", "LVL", "RNK"]:
                vp = v
                vp["awardType"] = "Medal"
                vp["img"] = k

                if int(k) in [74, 75, 76, 77, 78, 79, 80, 110, 111, 112, 113, 114, 115, 116, 156, 157, 158, 159, 160, 161, 162]:
                    # 74 {'name': 'Silver Anniversary', 'description': 'Stay married to a single person for 50 days without divorce', 'type': 'CMT', 'awardType': 'Medal'}
                    type = "Spouse"
                    vp["goal"] = int(v["description"].split(" ")[-4].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["married"].get("duration"))
                    vp["achieve"] = 1 if int(k) in myAwards["medals_awarded"] else min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max((vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["day left" if vp["left"] == 1 else "days left", ""]
                    awards[type]["m_" + k] = vp

                elif int(k) in [210, 211, 212, 213, 214]:
                    # 210 {'name': 'Citizenship', 'description': 'Be a donator for 30 days', 'type': 'CMT', 'awardType': 'Medal'}
                    type = "Donator"
                    vp["goal"] = int(v["description"].split(" ")[-2].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("daysbeendonator"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max((vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["day left" if vp["left"] == 1 else "days left", ""]
                    awards[type]["m_" + k] = vp

                elif int(k) in [225, 226, 227, 228, 229, 230, 231, 232, 234, 235]:
                    # 225 {'name': 'One Year of Service', 'description': 'Live in Torn for one year', 'type': 'CMT', 'awardType': 'Medal'}
                    type = "Age"
                    str2int = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
                    vp["goal"] = str2int[v["description"].split(" ")[-2]]
                    tmp = None2Zero(myAwards.get("age")) / 365.
                    vp["achieve"] = min(1, tmp / float(vp["goal"]))
                    vp["current"] = "{:.2f}".format(tmp)
                    vp["left"] = max(365 * vp["goal"] - None2Zero(myAwards.get("age")), 0)
                    vp["comment"] = ["day left" if vp["left"] == 1 else "days left", ""]
                    awards[type]["m_" + k] = vp

                elif int(k) in [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]:
                    # 34 {'name': 'Level Five', 'description': 'Reach level Five', 'type': 'LVL', 'awardType': 'Medal'}
                    type = "Level"
                    str2int = {"Five": 5, "Ten": 10, "Fifteen": 15, "Twenty": 20, "Twenty Five": 25, "Thirty": 30, "Thirty Five": 35, "Forty": 40, "Forty Five": 45, "Fifty": 50,
                               "Fifty Five": 55, "Sixty": 60, "Sixty Five": 65, "Seventy": 70, "Seventy Five": 75, "Eighty": 80, "Eighty Five": 85, "Ninety": 90, "Ninety Five": 95, "One Hundred": 100}
                    vp["goal"] = str2int[" ".join(v["description"].split(" ")[2:])]
                    vp["current"] = None2Zero(myAwards.get("level"))
                    vp["achieve"] = min(1, vp["current"] / float(vp["goal"]))
                    awards[type]["m_" + k] = vp

                elif int(k) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]:
                    # 1 {'name': 'Beginner', 'description': 'Reach the rank of "Beginner"', 'type': 'RNK', 'awardType': 'Medal'}
                    type = "Rank"
                    # vp["img"] = "https://www.torn.com/images/v2/main/medals/rank_slice.png"
                    # shift = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
                    # vp["shift"] = shift.index(int(k))
                    # vp["init"] = [0, 0]
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in [int(a) for a in myAwards["medals_awarded"]] else 0
                    vp["current"] = 1 if int(k) in [int(a) for a in myAwards["medals_awarded"]] else 0
                    awards[type]["m_" + k] = vp

                elif int(k) in [26, 27, 28, 29, 108, 109, 148, 149, 150, 151]:
                    # 26 {'name': 'Apprentice Faction Member', 'description': 'Serve 100 days in a single faction', 'type': 'CMT', 'awardType': 'Medal'}
                    type = "Faction"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["faction"].get("days_in_faction"))
                    vp["achieve"] = 1 if int(k) in myAwards["medals_awarded"] else min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max((vp["goal"] - vp["current"]), 0)
                    vp["comment"] = ["day left" if vp["left"] == 1 else "days left", ""]
                    awards[type]["m_" + k] = vp

                # else:
                #     print(k, v)

    elif typeOfAwards == "miscellaneous":

        awards = dict({
            "Social": dict(),
            "Refills": dict(),
            "Perks": dict(),
            "Racing": dict(),
            "Other miscellaneous": dict(),
            "Missions": dict(),
            "Maximum": dict(),
            "Events": dict()})

        for k, v in allAwards["honors"].items():
            if int(v["type"]) in [0, 11, 17]:
                vp = v
                vp["awardType"] = "Honor"
                vp["img"] = honorId2Img(int(k))

                if int(k) in [5, 167, 217, 218, 219, 223, 246]:
                    # 5 {'name': 'Journalist', 'description': 'Have an article accepted in the newspaper', 'type': 0, 'circulation': 138, 'rarity': 'Extremely Rare', 'awardType': 'Honor', 'img': None, 'title': 'Journalist [5]: Extremely Rare (138)'}
                    # 167 {'name': 'Velutinous', 'description': 'Have a comic accepted in the newspaper', 'type': 0, 'circulation': 114, 'rarity': 'Extremely Rare', 'awardType': 'Honor', 'img': 363324386, 'title': 'Velutinous [167]: Extremely Rare (114)'}
                    # 217 {'name': "Two's Company", 'description': 'Refer one friend to Torn', 'type': 11, 'circulation': 13121, 'rarity': 'Uncommon', 'awardType': 'Honor', 'img': 438803717, 'title': "Two's Company [217]: Uncommon (13121)"}
                    # 218 {'name': "Three's a Crowd", 'description': 'Refer two friends to Torn', 'type': 11, 'circulation': 5404, 'rarity': 'Rare', 'awardType': 'Honor', 'img': 294488415, 'title': "Three's a Crowd [218]: Rare (5404)"}
                    # 219 {'name': 'Social Butterfly', 'description': 'Refer three friends to Torn', 'type': 11, 'circulation': 3037, 'rarity': 'Rare', 'awardType': 'Honor', 'img': 534607883, 'title': 'Social Butterfly [219]: Rare (3037)'}
                    # 223 {'name': 'The Socialist', 'description': 'Achieve level 5 on facebook Torn', 'type': 11, 'circulation': 16222, 'rarity': 'Uncommon', 'awardType': 'Honor', 'img': 350797134, 'title': 'The Socialist [223]: Uncommon (16222)'}
                    # 246 {'name': 'Pyramid Scheme', 'description': 'Have one of your referrals refer 5 Other players', 'type': 11, 'circulation': 1041, 'rarity': 'Extraordinary', 'awardType': 'Honor', 'img': 536984897, 'title': 'Pyramid Scheme [246]: Extraordinary (1041)'}
                    type = "Social"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [309, 443, 459]:
                    # 309 {'name': 'Christmas in Torn', 'description': 'Login on Christmas Day', 'type': 11, 'circulation': 50473, 'rarity': 'Common', 'awardType': 'Honor', 'img': 959806366, 'title': 'Christmas in Torn [309]: Common (50473)'}
                    # 443 {'name': 'Trick or Treat', 'description': 'Login on Halloween', 'type': 11, 'circulation': 40866, 'rarity': 'Common', 'awardType': 'Honor', 'img': 513488839, 'title': 'Trick or Treat [443]: Common (40866)'}
                    # 459 {'name': 'Torniversary', 'description': 'Login on November 15th', 'type': 11, 'circulation': 41332, 'rarity': 'Common', 'awardType': 'Honor', 'img': 332983521, 'title': 'Torniversary [459]: Common (41332)'}
                    type = "Events"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [316]:
                    # 316 {'name': 'Forgiven', 'description': 'Be truly forgiven for all of your sins', 'type': 11, 'circulation': 5434, 'rarity': 'Rare', 'awardType': 'Honor', 'img': 240827340, 'title': 'Forgiven [316]: Rare (5434)'}
                    type = "Other miscellaneous"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [229]:
                    # 229 {'name': 'Seeker', 'description': 'Achieve 250 total awards', 'type': 0, 'circulation': 5633, 'rarity': 'Limited', 'awardType': 'Honor', 'img': 486362984, 'title': 'Seeker [229]: Limited (5633)'}
                    type = "Other miscellaneous"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = len(myAwards["honors_awarded"]) + len(myAwards["medals_awarded"])
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    awards[type]["h_" + k] = vp

                elif int(k) in [21, 274, 572]:
                    # 21 {'name': 'Driving Elite', 'description': 'Reach racing class A', 'type': 0, 'circulation': 15853, 'rarity': 'Uncommon', 'awardType': 'Honor', 'img': 819611004, 'title': 'Driving Elite [21]: Uncommon (15853)'}
                    # 274 {'name': 'Redline', 'description': 'Win 250 races with a single car', 'type': 0, 'circulation': 3513, 'rarity': 'Rare', 'awardType': 'Honor', 'img': 739693375, 'title': 'Redline [274]: Rare (3513)'}
                    # 572 {'name': 'Motorhead', 'description': 'Reach a racing skill of 10', 'type': 0, 'circulation': 1960, 'rarity': 'Extraordinary', 'awardType': 'Honor', 'img': None, 'title': 'Motorhead [572]: Extraordinary (1960)'}
                    type = "Racing"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [380, 395]:
                    # 380 {'name': 'Ecstatic', 'description': 'Achieve the maximum of 99,999 happiness', 'type': 0, 'circulation': 2153, 'rarity': 'Extraordinary', 'awardType': 'Honor', 'img': 462192588, 'title': 'Ecstatic [380]: Extraordinary (2153)'}
                    # 395 {'name': 'Energetic', 'description': 'Achieve the maximum of 1,000 energy', 'type': 0, 'circulation': 20651, 'rarity': 'Uncommon', 'awardType': 'Honor', 'img': 579593508, 'title': 'Energetic [395]: Uncommon (20651)'}
                    type = "Maximum"
                    vp["goal"] = 1
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [617]:
                    # 617 {'name': '10-Stack', 'description': 'Increase a merit upgrade to its maximum', 'type': 0, 'circulation': 33547, 'rarity': 'Common', 'awardType': 'Honor', 'img': 312084767, 'title': '10-Stack [617]: Common (33547)'}
                    type = "Maximum"
                    vp["goal"] = 10
                    n = 0
                    for _, nMerits in myAwards["merits"].items():
                        n = nMerits if int(nMerits) > n else n
                    vp["current"] = n
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [266, 566]:
                    # 566 {'name': "You've Got Some Nerve", 'description': 'Refill your nerve bar 250 times', 'type': 0, 'circulation': 812, 'rarity': 'Extraordinary', 'awardType': 'Honor', 'img': 572050307, 'title': "You've Got Some Nerve [566]: Extraordinary (812)"}
                    # 266 {'name': 'Energize', 'description': 'Refill your energy bar 250 times', 'type': 0, 'circulation': 10237, 'rarity': 'Limited', 'awardType': 'Honor', 'img': 400884239, 'title': 'Energize [266]: Limited (10237)'}
                    type = "Refills"
                    vp["goal"] = int(v["description"].split(" ")[-2].replace(",", ""))
                    key = "nerverefills" if v["description"].split(" ")[2] == "nerve" else "refills"
                    vp["current"] = None2Zero(myAwards["personalstats"].get(key))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    vp["left"] = max(vp["goal"] - vp["current"], 0)
                    vp["comment"] = ["days left", "with daily refill"]
                    awards[type]["h_" + k] = vp

                elif int(k) in [244, 607, 620]:
                    # 607 {'name': 'Buffed', 'description': 'Achieve 50 personal perks', 'type': 0, 'circulation': 18274, 'rarity': 'Uncommon', 'awardType': 'Honor', 'img': 210452243, 'title': 'Buffed [607]: Uncommon (18274)'}
                    # 244 {'name': 'Web Of Perks', 'description': 'Achieve 100 personal perks', 'type': 0, 'circulation': 7466, 'rarity': 'Limited', 'awardType': 'Honor', 'img': 411243367, 'title': 'Web Of Perks [244]: Limited (7466)'}
                    # 620 {'name': 'OP', 'description': 'Achieve 150 personal perks', 'type': 0, 'circulation': 282, 'rarity': 'Extraordinary', 'awardType': 'Honor', 'img': None, 'title': 'OP [620]: Extraordinary (282)'}
                    type = "Perks"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    n = 0
                    for key_perk, perks in myAwards.items():
                        if key_perk.split("_")[-1] == "perks":
                            n += len(perks)
                    vp["current"] = n
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else min(1, float(vp["current"]) / float(vp["goal"]))
                    awards[type]["h_" + k] = vp

                elif int(k) in [371]:
                    # 371 {'name': 'Protege', 'description': 'Complete the mission Introduction: Duke', 'type': 17, 'circulation': 44516, 'rarity': 'Common', 'awardType': 'Honor', 'img': 668653618, 'title': 'Protege [371]: Common (44516)'}
                    type = "Missions"
                    vp["current"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    vp["achieve"] = 1 if int(k) in myAwards["honors_awarded"] else 0
                    awards[type]["h_" + k] = vp

                elif int(k) in [664]:
                    # "664": {"name": "Mercenary", "description": "Complete 1,000 contracts", "type": 17},
                    type = "Missions"
                    vp["goal"] = int(v["description"].split(" ")[1].replace(",", ""))
                    vp["current"] = None2Zero(myAwards["personalstats"].get("contractscompleted"))
                    vp["achieve"] = min(1, float(vp["current"]) / float(vp["goal"]))
                    ratio = vp["current"] / float(max(myAwards.get("age"), 1))
                    vp["left"] = max((vp["goal"] - vp["current"]) / ratio, 0) if ratio > 0 else "&infin;"
                    vp["comment"] = ["days left", "current ratio of {:.02f} contracts / day".format(ratio)]
                    awards[type]["h_" + k] = vp

                # else:
                #     print(k, v)

    awardsSummary = dict()
    nAwardedTot = 0
    nAwardsTot = 0
    for k, v in awards.items():
        nAwarded = 0
        for l, w in v.items():
            if w["achieve"] == 1:
                nAwarded += 1
        nAwards = len(v)
        awardsSummary[k] = {"nAwarded": nAwarded, "nAwards": nAwards}
        nAwardedTot += nAwarded
        nAwardsTot += nAwards
    awardsSummary["All awards"] = {"nAwarded": nAwardedTot, "nAwards": nAwardsTot}

    return awards, awardsSummary