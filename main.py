"""
 * This bot is made by u/Evillja aka Evil. If you're willing to use this code for anything, you have to ask me for it.
"""



import praw
import os
import sys
import time
import openai
import random

client_id     = ""
client_secret = ""
username      = ""
password      = ""
user_agent = f"User-Agent: linux:com.{username}s.runner:v1.0 (by /u/{username}s)"
reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret,
                     username = username,
                     password = password,
                     user_agent = user_agent)

notReplyOrder = ['[removed]', '[deleted]', '', ' ', None]
begin = time.monotonic()-2401
admins = ["anancilikyapma","asim-abi","apklidomaltan","lokumisadog2","bulgurlusikerten","evillja","furkantopal","rohunder","enginargaming","floodlar-com"]
goodbot = "çok teşekkürler :3"
badbot = "Eksikliğimi nyancat#6010 dc'ine yazabilirsin. Ayrıca allahını sikeyim"
subreddit = reddit.subreddit("herseycokguzelolacak")

def getFlood(floodname):
    floodname = floodname.lower().replace("/","")
    flood = ""

    if not os.path.exists("floodlar\\{}.flood".format(floodname)): 
        return "< *Flood bulunamadı. Komutlardan nasıl ekleneceğini öğrenebilirsiniz* >"

    with open("floodlar\\{}.flood".format(floodname),"r",encoding='utf-8') as f:
        tempflood = f.readlines()
        for line in tempflood:
            flood += line

    return flood

def getRandomFlood():
    fname = ""

    with open("defter.nm","r",encoding='utf-8') as f:
        floodes = f.readlines()
        floods = []

        for flood in floodes:
            floods.append(flood.strip())

        for flod in floods:

            if flod == "" or flod == "\n" or flod == " ":

                floods.remove(flod)
        fname = random.choice(floods)


    return fname
def checkReply():
    replied = []
    if not os.path.exists("replied"): return []
    with open("replied","r",encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            replied.append(line.strip())
    return replied
def setReplied(item):
    with open("replied","a+",encoding='utf-8') as f:
        f.write(item+"\n")
def setPredef(kw,fname):
    # ŞİMDİLİK MEVCUT DEĞİL
    pass
def addFlood(fname,flood):
    fname = fname.lower()
    if os.path.exists("floodlar\\{}.flood".format(fname)) or os.path.exists("tmpfloodlar\\{}.flood".format(fname)):
        return "< *Flood zaten var. Bir yanlışlık olduğunu düşünüyorsan nyancat#6010 dc'ine yazabilirsin* >"

    if len(flood) > 8000:
        return "< *Floodunuzun uzunluğu 8000 karakterden fazla. Allah mısın amına koyim o flood ne* >"

    if "*" in fname or "/" in fname or "\\" in fname:
        return "< *Flood adı *, \\, / içeremez* >"

    if len(fname) > 50: return "< *Flood adı 50 karakterden fazla olamaz* >"

    with open("tmpfloodlar\\{}.flood".format(fname),"a+",encoding='utf-8') as f:
        f.write(flood)

    return "< *Floodunuz onay sürecine alındı bu 5 dakikadan 1 güne kadar alabilir* >"
def addQFlood(fname,flood):
    fname = fname.lower()
    if os.path.exists("floodlar\\{}.flood".format(fname)) or os.path.exists("tmpfloodlar\\{}.flood".format(fname)):
        return "< *QFlood zaten var. Bir yanlışlık olduğunu düşünüyorsan nyancat#6010 dc'ine yazabilirsin* >"

    if len(flood) > 8000:
        return "< *QFloodunuzun uzunluğu 8000 karakterden fazla. Allah mısın amına koyim o flood ne* >"

    if "*" in fname or "/" in fname or "\\" in fname:
        return "< *QFlood adı *, \\, / içeremez* >"

    if len(fname) > 50: return "< *QFlood adı 50 karakterden fazla olamaz* >"

    with open("tmpfloodlar\\{}.flood".format(fname),"a+",encoding='utf-8') as f:
        f.write(flood)

    return "< *QFloodunuz onay sürecine alındı bu 5 dakikadan 1 güne kadar alabilir* >"

def moveFlood(fname):
    fname = fname.lower()
    if not os.path.exists("tmpfloodlar\\{}.flood".format(fname)): return "< *Bu flood ya zaten onaylanmış ya da başka bir admin tarafından reddedilmiş* >"

    os.rename("tmpfloodlar\\{}.flood".format(fname),"floodlar\\{}.flood".format(fname))

    with open("defter.nm","a+",encoding='utf-8') as f:
        f.write("/{}\n".format(fname))

    return "< *Flood onaylandı. sum ile çağırabilirsiniz veya beni etiketlediğinizde rastgele denk gelebilir* >"

def removeFlood(fname):

    fname = fname.strip()

    if not os.path.exists("floodlar\\{}.flood".format(fname)): return "< *Bu flood zaten kaldırıldı.* >"

    try:
    	os.remove("floodlar\\{}.flood".format(fname))
    except:
        print("",end="")

    with open("defter.nm","r",encoding='utf-8') as f:
        floodes = f.readlines()
        floods = []

        for flood in floodes:
            floods.append(flood.replace("/","").strip())

        popno = 0
        for flod in floods:
            if flod == fname:
                floods.pop(popno)
            popno += 1

    os.remove("defter.nm")

    with open("defter.nm","a+",encoding='utf-8') as f:

        for flood in floods:
            f.write("/{}\n".format(flood))

    return "< *Flood kaldırıldı.* >"

def changeFlood(fname,flood):

    if not os.path.exists("floodlar\\{}.flood".format(fname)): return "< *Bu flood zaten kaldırıldı.* >"

    if len(flood) > 8000:
        return "< *Floodunuzun uzunluğu 8000 karakterden fazla. Allah mısın amına koyim o flood ne* >"

    if "*" in fname: return "< *Flood adında yıldız bulunamaz* >"

    os.remove("floodlar\\{}.flood".format(fname))

    with open("floodlar\\{}.flood".format(fname),"w",encoding='utf-8') as f:
        f.write(flood)

    return "< *Flood değiştirildi.* >"

def ara(keywords):

    with open("defter.nm","r",encoding='utf-8') as f:
        floodes = f.readlines()
        floods = []

        for flood in floodes:
            floods.append(flood.replace("/","").strip())

        found = []
        for flood in floods:
            fnd = True

            for keyword in keywords:

                if not keyword in flood.lower():
                    fnd = False

            if fnd:
                found.append(flood)

        return found

imabot = "\n\n< *Ben bir botum. Bu yazıyı silmek için !remove* >\n\n< *Komutlara göz atmak için u/floodator help* >"
revel = 0
bots = ["kerbal_galactic","indirbeni","koyunkirpan","savevideo"]
approved = ["goktugh"]
print("!!! Başlatıldı")
nowtime = time.time()
while True:

    try:
        time.sleep(1)
        revel += 1

        for item in list(reddit.inbox.unread(limit=10))[::-1]:
            imabot = "\n\n< *Ben bir botum. Bu yazıyı silmek için !remove* >\n\n< *Komutlara göz atmak için u/floodator help* >"
            time.sleep(7)
            item.mark_read()
            content = item.body.replace("u/floodator ","").split("u/{} ".format(username))
            content = " ".join(content)
            text = content

            print("+  >>>",text[1:25].strip() if text[0] == " " else text[0:24].strip())
            if item.author.name.lower() == "floodator": continue
            if item.author.name.lower() in bots: continue

            if item.author.name.lower() in admins: 
                item.upvote()

            if text == "[deleted]" or text == "[removed]" or text == "[Removed by Reddit]": continue

            if reddit.redditor(item.author.name).created_utc > time.time() - 60 * 60 * 24 * 30 * 2:

                if not item.author.name.lower() in admins or not item.author.name.lower() in approved:

                    print("*  >>> AMK NEWİ TESPİT EDİLDİ:",item.author.name.lower())
                    continue

            if "add" in text.lower()[0:15]:
                print("",end="")

            else:
                text = text.lower()

            if text == "!remove":
                if not item.author.name.lower() in admins:
                    if not item.parent().parent().author.name.lower() == item.author.name.lower():
                        print("*  >>> YETKİSİZ REMOVE GİRİŞİMİ",item.author.name.lower())
                        continue

                try: 
                    item.parent().delete()
                    print("*  >>> BİR YAZI {} TARAFINDAN SİLİNDİ".format(item.author.name.lower()))
                    continue

                except: continue

            if text == " good bot" or text == "good bot":
                print("*  >>> GOOD BOT BİLDİRİMİ")
                item.reply(body=goodbot + imabot)
                item.upvote()
                continue

            if text == " bad bot" or text == "bad bot":
                print("*  >>> BAD BOT BİLDİRİMİ")
                item.reply(body=badbot + imabot)
                item.downvote()
                continue

            if text == " help" or text == "help":
                print("*  >>> KOMUTLAR LİSTELENDİ")
                item.reply(body=getFlood("help")+imabot)
                continue

            if item.body.strip().lower() == "u/floodator" or item.body.strip().lower() == "u/floodator ":
                cf = getRandomFlood()
                print("*  >>> BİR FLOOD ATILDI (R),",cf[1:])
                currentFlood = str(getFlood(cf))

                if len(currentFlood) > 9700:
                    imabot = ""
                item.reply(body=currentFlood+imabot)
                del currentFlood
                continue
            if text == "red" or text == " red":

                if not item.author.name.lower() in admins:

                    print("*  >>> YETKİSİZ RED GİRİŞİMİ")
                    continue
                litem = item
                if item.parent().author.name.lower() == "floodator":
                    item = item.parent()

                exFlood = " ".join(item.parent().body.strip().split("u/{} ".format(username)))
                if not "add" in exFlood:
                    item.reply(body="< *Parent yorumda bir add komutu kullanılmamış.* >"+imabot)
                    continue

                shsh = exFlood.split("add ")[1].split(" ")[0]
                print("!  >>> BİR FLOOD REDDEDİLDİ: {}".format(shsh))
                try:
                    os.remove("tmpfloodlar\\{}.flood".format(shsh))
                    litem.reply(body="< *Flood reddedildi* >"+imabot)
                except: litem.reply(body="< *Bu flood ya zaten kabul edilmiş yada reddedilmiş* >"+imabot)

                continue

            if text.startswith(" qadd ") or text.startswith("qadd "):

                try:
                    shsh = text.split("qadd ")[1].split(" ")
                    flod = ""
                    fllist = []
                    fitem = item
                    item = item.parent()
                    no = 0
                    while type(item) != praw.models.reddit.submission.Submission:
                        if no == 0:
                            prefixN = "\n\n"
                        else:
                            prefixN = ""
                        fllist.append(prefixN+item.author.name.lower()+":\n\n"+item.body)
                        no += 1
                        item = item.parent()
                    fllist.reverse()
                    for fl in fllist:
                        flod += fl
                    flodname = shsh[0].lower()
                    cevap = addQFlood(flodname,flod)

                except Exception as e:
                    fitem.reply(body="< *Flood adını kontrol edin* >" + imabot)
                    continue

                fitem.reply(body=cevap+imabot)
                print(35*"*"+"\n!  >>> BİR QFLOOD KAYDEDİLME GİRİŞİMİ OLDU: {}\n".format(shsh[0])+cevap+"\n"+35*"*")
                del cevap,flod,shsh
                continue

            if text.startswith(" add ") or text.startswith("add "):

                try:
                    shsh = text.split("add ")[1].split(" ")
                    flod = " ".join(shsh[1:])
                    flodname = shsh[0].lower()
                    cevap = addFlood(flodname,flod)

                except Exception as e:
                    item.reply(body="< *Flood adını kontrol edin* >" + imabot)
                    continue

                item.reply(body=cevap+imabot)
                print(35*"*"+"\n!  >>> BİR FLOOD KAYDEDİLME GİRİŞİMİ OLDU: {}\n".format(shsh[0])+cevap+"\n"+35*"*")
                del cevap,flod,shsh
                continue
            if text.startswith(" onay") or text.startswith("onay"):
                mode = "add"
                cevap = "< *Flood onaylandı. sum ile çağırabilirsiniz veya beni etiketlediğinizde rastgele denk gelebilir* >"
                if not item.author.name.lower() in admins: continue

                if item.parent().author.name.lower() == "floodator":

                    item = item.parent()

                exFlood = " ".join(item.parent().body.strip().split("u/{} ".format(username)))

                if not mode+" " in exFlood:

                    mode = "qadd"
                if not mode+" " in exFlood:
                    item.reply("< *Bir add/qadd yorumu bulunamadı* >"+imabot)
                shsh = exFlood.split(mode+" ")[1].split(" ")[0]
                try:
                    cevap = moveFlood(shsh)
                    print("!  >>> BİR FLOOD ONAYLANDI: {}".format(shsh))
                except:
                    cevap = "< *Böyle bir flood yok* >"
                item.reply(body=cevap+imabot)
                del shsh,exFlood,mode,cevap
                continue

            if text.startswith(" sil") or text.startswith("sil"):

                fnamesx = []
                if item.author.name.lower() not in admins:

                    print("-  >>> YETKİSİZ SİLME GİRİŞİMİ: BAŞARISIZ")
                    continue

                with open("defter.nm","r",encoding='utf-8') as f:

                    floods = f.readlines()

                    for flood in floods:

                        flood = flood.strip().replace("/","")

                        if flood == "" or flood == " ": continue

                        with open("floodlar\\{}.flood".format(flood),"r",encoding='utf-8') as xread:
                            cFlood = xread.read()
                            exf = " ".join(item.parent().body.replace("\n\n< *Ben bir botum. Bu yazıyı silmek için !remove* >\n\n< *Flood eklemek için u/floodator add (floodismi) (yazı)* >","").split(" "))

                            if cFlood == exf and flood != "":

                                fnamesx.append(flood)
                                continue
                print("!  >>> {} FLOOD(LAR) {} TARAFINDAN SİLİNMİŞ ".format(len(fnamesx),item.author.name.lower()))

                for fn in fnamesx:

                    cevap = removeFlood(fn)

                item.reply(body=cevap+imabot)
                del cevap,fnamesx,floods,cFlood,exf
                continue

            if text.startswith(" değiştir") or text.startswith("değiştir"):

                if item.author.name.lower() not in admins:

                    print("-  >>> YETKİSİZ DEĞİŞTİRME GİRİŞİMİ: BAŞARISIZ")
                    item.reply(body="< *Değiştirmek için yetkin yok* >"+imabot)
                    continue

                os.remove("floodlar\\{}.flood".format(text.split("değiştir ")[1]))

                if type(item.parent()) == praw.models.reddit.submission.Submission:

                    txt = " ".join(item.parent().selftext.split(" "))

                else:

                    txt = " ".join(item.parent().body.split(" "))

                with open("floodlar\\{}.flood".format(text.split("değiştir ")[1]),"w",encoding='utf-8') as f:

                    f.write(txt)

                print("!  >>> {} FLOODU {} TARAFINDAN DEĞİŞTİRİLDİ".format(text.split("değiştir ")[1],item.author.name.lower()))
                item.reply(body="< *"+text.split("değiştir ")[1] + " Floodu parent ile değiştirildi.* >"+imabot)
                del txt
                continue

            if text.startswith(" sumparent") or text.startswith("sumparent"):

                print("*  >>> BİR FLOOD ATILDI (parent):",end=" ")
                print(text.split("sumparent ")[1])

                if len(getFlood(text.split("sumparent ")[1].split(" ")[0])) > 9700:

                    imabot = ""
                getnflock = getFlood(text.split("sumparent ")[1].split(" ")[0])
                if getnflock == "< *Flood bulunamadı. eklemek için u/floodator add (floodismi) (flood)* >":
                    item = item
                else:
                    item = item.parent()
                item.reply(body=getnflock+imabot)
                continue

            if text.startswith(" sum ") or text.startswith("sum "):

                print("*  >>> BİR FLOOD ATILDI:",end=" ")
                print(text.split("sum ")[1])

                if len(getFlood(text.split("sum ")[1].split(" ")[0])) > 9700:

                    imabot = ""

                item.reply(body=getFlood(text.split("sum ")[1].split(" ")[0])+imabot)
                continue

            if text.startswith(" ara ") or text.startswith("ara "):

                keywords = text.split("ara ")[1].split(" ")

                if keywords == [""]: continue

                kwstring = ""

                for kw in keywords:

                    kwstring += kw+" "

                print("*  >>>",kwstring+"ARANDI") #parent3
                floods = ara(keywords)
                floodno = 1
                floodmsg = ""

                for flood in floods:

                    if floodno == 10:

                        break

                    floodmsg += "{}: {}\n\n".format(floodno,flood)
                    floodno += 1

                if len(floods) < 1:

                    item.reply(body="< *Arama kriterlerine uygun flood bulunamadı.* >"+imabot)
                    continue

                msgja = "1"

                if len(floods) > 1:

                    msgja += "-"+str(len(floods))

                item.reply(body=floodmsg+f"< *.{msgja} yazarak bir floodu atmamı sağlayabilirsin, flood ara komutunu girdiğin yoruma gidecek* >"+imabot)
                continue

            if text.startswith(".") or text.startswith(" ."):

                if not item.parent().body.strip().lower().startswith("1:"): continue

                if not item.parent().author.name.lower() == "floodator": continue

                if not item.parent().parent().author.name.lower() == item.author.name.lower(): continue

                secenekler = item.parent().body
                secenekler = secenekler.split("< *.1")[0]

                try:

                    if int(text.split(".")[1]) > len(secenekler) and (text.split(".")[1]) < 1: continue

                except: continue

                no = 0
                secilFlood = secenekler.replace(": ","").split("\n\n")
                secilFlood.pop(-1)

                for secenek in secilFlood:

                    secilFlood[no] = secilFlood[no][1:]
                    no += 1

                secilen = secilFlood[int(text.split(".")[1]) - 1]

                if len(getFlood(secilen)) > 9700:

                    imabot = ""

                item.parent().parent().parent().reply(body=getFlood(secilen)+imabot)
                print("*  >>> ARAMA KOMUTUNDAN SONRA {} SEÇİLDİ".format(secilen))
                continue

            if text.startswith(" hizliekle") or text.startswith("hizliekle"):

                if item.author.name.lower() not in admins:

                    print("-  >>> YETKİSİZ HIZLI EKLEME GİRİŞİMİ: BAŞARISIZ")
                    item.reply(body="< *Hızlı eklemek için yetkin yok* >"+imabot)
                    continue

                if type(item.parent()) == praw.models.reddit.submission.Submission:

                    cFlood = item.parent().selftext

                else:

                    cFlood = item.parent().body.replace("u/floodator ","").split("u/{} ".format(username))
                    cFlood = " ".join(cFlood)

                if len(cFlood) > 10000:

                    print("!  >>> HIZLI EKLENMEYE ÇALIŞILAN FLOOD 10K KARAKTERDEN FAZLA")
                    item.reply(body="< *Hızlı eklemek için 10K karakterden fazla flood giremezsin* >"+imabot)
                    continue
                if len(text.split("hizliekle"[1])) > 50:

                    item.reply(body="< *Flood adı 50 karakterden fazla olamaz* >"+imabot)

                with open("floodlar\\{}.flood".format(text.split("hizliekle ")[1]),"w",encoding='utf-8') as f:

                    f.write(cFlood)

                with open("defter.nm","a",encoding='utf-8') as f:

                    f.write("/{}\n".format(text.split("hizliekle ")[1]))

                print("!  >>> BİR FLOOD HIZLI EKLENDİ: {}".format(text.split("hizliekle ")[1]))
                item.reply(body="< *{} Başarıyla eklendi.* >".format(text.split("hizliekle ")[1])+imabot)
                continue

            print("!  >>> YORUM ESGEÇİLDİ")
            continue
        canComment = False
        itemno = 0
        for item in list(subreddit.new(limit=3))[::-1]:
            ttime = time.time()-7
            if ttime <= nowtime:
                nowtime = time.time()
            else:
                break
            if item in checkReply():
                canComment = False
                break
            itemno += 1
            canComment = True
        if canComment == True and itemno >= 3:
            iList = []
            for item in list(subreddit.new(limit=5))[::-1]:
                setReplied(item.id)
                iList.append(item)
            nowitem = random.choice(iList)
            fname = getRandomFlood()
            currentFlood = str(getFlood(fname))
           
            imabot = "\n\n< *Ben bir botum. Bu yazıyı silmek için !remove* >\n\n< *Komutlara göz atmak için u/floodator help* >"
            if len(currentFlood) > 9700:
                imabot = ""
            item.reply(body=currentFlood+imabot)
            print("/  >>> POST:",item.title[0:35],"\n/  >>> FLOOD:",fname[1:])
    except Exception as e:

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
            

