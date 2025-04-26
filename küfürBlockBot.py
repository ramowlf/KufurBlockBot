import telebot
import re

ramowlf = telebot.TeleBot("Bot token gir")

ramazan_babus = [kendi idni gir]  

ramazanin_yarra = [
    "amk", "aq", "oç", "oçç", "sg", "sktm", "sktir", "sktr", "sik", "sikerim", "sikeyim", "siktir", 
    "piç", "pic", "p1c", "p1ç", "pıc", "puşt", "puşşt", "ibne", "i.bne", "i b n e", "ipne", "ibnelik",
    "orospu", "0r0spu", "or0spu", "0rospu", "orsp", "orspu", "orosp", "orrospu", "oruspu", "0ruspu",
    "am1na", "am1nako", "am1nak", "s1k", "s1kt1r", "s1ker1m", "s1kerm", "s1ktr", "s1kim", "s!k", 
    "s!kt!r", "s!ker!m", "s!kt!m", "s1ktim", "s1keyim", "s1km", "sıkm", "sıkım", "sıktır", "s1kik",
    "4mk", "4mk", "4mına", "4m1na", "4m1n4", "4mın4", "4mk", "4mq", "4q", "4n4n1", "4nanı", "4nası",
    "a.m.k", "s.i.k", "s.i.k.t.i.r", "a.q", "o.ç", "o.r.o.s.p.u", "p.i.ç", "a.m", "a.m.c.ı.k",
    "a m k", "s i k", "s i k t i r", "a q", "o ç", "o r o s p u", "p i ç", "s k t r", "s k m",
    "amına", "amına koyayım", "amına koyim", "amına kodum", "amınakoyim", "amınakoyayım", 
    "amcık", "amcık hoşafı", "amcıklar", "amcıklara", "amcığını", "amcığın", "amcığa", 
    "yarrak", "yarrağını", "yarağını", "yarrağım", "yarağım", "yarrağı", "yarağı", "yaraklar",
    "y4rr4k", "y4r4k", "y4rr4m", "y4r4m", "y@rr@k", "y@r@k", "y@rr@m", "y@r@m",
    "g0t", "göt", "g0tv3r3n", "g0t v3r3n", "götlek", "götverir", "götoş", "götünü", "götüne",
    "d4şş4k", "t4şş4k", "d4şş4ğını", "t4şş4ğını", "daşşak", "taşşak", "daşşağını", "taşşağını",
    "a*k", "a**", "a***k", "s*k", "s**", "s***m", "o*ç", "o**u", "p*ç", "p**", "t*şak", "d*şak",
    "am*", "am**", "am***", "*mına", "*mına koyim", "*siktir", "*nani", "*benin", "*nası",
    "gavat", "g4v4t", "g4v@t", "gav@t", "gavad", "g4v4d", "g4v@d", "gav@d",
    "pezevenk", "pezeveng", "pezav*nk", "pezav*ng", "p*zevenk", "p*zeveng",
    "yavşak", "yawşak", "yawsak", "yav$ak", "y4v$4k", "y@v$@k", "y@vs@k",
    "anan", "anani", "ananı", "ananın", "anana", "anneni", "annene", "annenin", "annen", "ananizi", "ananızı",
    "fuck", "fck", "f*ck", "f*k", "fcuk", "fak", "wtf", "fvck", "shit", "sh*t", "sht", "damn", "d*mn",
    "bastard", "b*stard", "bitch", "b*tch", "btch", "b*tch", "dick", "d*ck", "pussy", "p*ssy", 
    "asshole", "a**hole", "a*shole", "a*s", "ass", "cock", "c*ck", "cok", "c*k", "cock", "c0ck",
    "s i k", "a m", "g ö t", "o ç", "o r o s p u", "y a r r a k", "t a ş ş a k", "a m c ı k",
    "s-i-k", "a-m", "g-ö-t", "o-ç", "o-r-o-s-p-u", "y-a-r-r-a-k", "t-a-ş-ş-a-k", "a-m-c-ı-k",
    "siktr", "sktr", "sktrgit", "siktrol", "skerim", "skeyim", "sikiş", "sikis", "sikem", "siken",
    "sikenin", "sikende", "sikende", "sikilen", "sikilen", "sikitter", "sikleri", "sikleriii", 
    "sikli", "sikilen", "sikilen", "sikilmek", "sikilmi", "sikilmiş", "sikilsin", "sikim", "sikimde", 
    "sikimden", "sikime", "sikimi", "sikimiin", "sikimin", "sikimle", "sikimsonik", "sikimtrak", 
    "sikin", "sikinde", "sikinden", "sikine", "sikini", "sikip", "sikis", "sikisek", "sikisen", 
    "sikish", "sikismis", "sikiş", "sikişen", "sikişme", "sikitiin", "sikiyim", "sikiym", "sikiyorum",
    "sikkim", "sikko", "sikleri", "sikleriii", "sikli", "sikm", "sikmek", "sikmem", "sikmiler", 
    "sikmisligim", "siksem", "sikseydin", "sikseyidin", "siksin", "siksinbaya", "siksinler", "siksiz",
    "siksok", "siksz", "sikt", "sikti", "siktigimin", "siktigiminin", "siktiğim", "siktiğimin", 
    "siktiğiminin", "siktii", "siktiim", "siktiimin", "siktiiminin", "siktiler", "siktim", "siktimm", 
    "siktimin", "siktiminin", "siktir", "siktir et", "siktirgit", "siktirgit", "siktirir", "siktiririm",
    "amcık", "amcıklar", "am", "âm", "ami", "amları", "amcığı", "amcığın", "amcığını", "amcığının", 
    "amcığında", "amcığından", "amı", "amı", "amın", "amın", "amına", "amına", "amını", "amını", 
    "amının", "amının", "amından", "amından", "amımı", "amımı", "amımın", "amımın", "amımda", 
    "amımda", "amımdan", "amımdan", "amıma", "amıma", "yarrak", "yarak", "yarrağı", "yarağı",
    "yarrağım", "yarağım", "yarrağımı", "yarağımı", "yarrağının", "yarağının", "yarrağında", 
    "yarağında", "yarrağından", "yarağından", "çük", "çükü", "göt", "gõt", "got", "kıç", "kıllı", 
    "götü", "götü", "götüne", "götüne", "göte", "göte", "götün", "götün", "götsün", "götsün", 
    "götten", "götten", "götün", "götün", "daşak", "daşşak", "dassak", "daşak", "daşşak", "daşşağım",
    "dassaklarım", "taşşak", "taşak", "taşşağım", "tassaklarım", "bacını", "bacını", "ananı", "ananı",
    "@mk", "@mk", "@mın@", "@mın@k0y1m", "@nani", "@nası", "sıkerım", "sikerım", "s1ker1m", "s1kerım", 
    "amçık", "amçık", "amçığı", "amçığı", "amçığın", "amçığın", "amçığını", "amçığını", "amçığının", 
    "amçığının", "amçığında", "amçığında", "amçığından", "amçığından", "çingene", "çıngene", "ebeni", 
    "ananın", "anasını", "anasını", "karını", "avradını", "avradını", "yedi", "ceddini", "sülaleni", 
    "sülaleni", "soyunu", "zürriyetini", "tenasülünü", "deyyus", "deyyüs", "deyus", "dayus", "dayyus",
    "gerizekalı", "gerızekalı", "gerizekali", "gerzek", "aptal", "dangalak", "salak", "mal", "dallama", 
    "beyinsiz", "ahmak", "serseri", "şerefsiz", "şerfsiz", "karaktersiz", "haysiyetsiz", "ezik", "sürtük", 
    "sürtüğü", "sürtüğün", "sürtüksün", "sürtükün", "kaltak", "kaltağın", "kaltaksın", "kahpe", "fahişe", 
    "fahise", "kevaşe", "kevase", "orospu", "orospuçocuğu", "orospucocugu", "orospuçocuğu", "orospuçocugu",
    "orospucocuğu", "orosbu", "orosbu cocugu", "orosbuçocuğu", "orosbucogugu", "orosbucocu", "orsbucucu",
    "31", "boşalmak", "spermleri", "dölü", "döllü", "kerhane", "kerhane", "kerhanede", "kerhaneye",
    "vajina", "am", "bızır", "bızır", "klitoris", "penis", "yarak", "sıçmak", "sictim", "bok", "bokunu",
    "cenabet", "cif", "çükü", "yalama", "otuz bir", "mastürbasyon", "masturbasyon", "attırma", "attırırım",
    "allahsız", "allahs", "dinsiz", "dinsize", "imansız", "allah", "dini", "dinini", "imanını", "kitabını",
    "amfibi", "amonyak", "amalgam", "angut", "ambar", "ambiyans", "ambalaj", "ambulans", "amerikan",
    "göt", "götveren", "götoğlanı", "götoş", "götlek", "kaşar", "kaşarlanmak", "amip", "amiyane",
    "sikim", "sikime", "sikimi", "sikmek", "sikmis", "siktim", "siktir", "kodum", "kodumun", "kodumun",
    "koduğmun", "koduğumun", "koduğum", "koduumun", "koyarm", "koyayım", "koyiim", "koyiiym", "koyim",
    "koyum", "koyyim",
    "pipi", "çük", "taşşak", "daşşak", "yarrak", "boktan", "boktan", "bokunu", "bokunu", "sokarım",
    "sokayım", "sokam", "sokasım", "sokmak", "sokucam", "sokuyum", "sokucu", "sokuşu", "sokuk",
    "sokuşuk", "sokuyor", "sokan", "sokar", "sokatan", "soktun", "soktunuz", "soktum", "soktuğum",
    "ahlaksız", "ahlaksız", "saksocu", "saxocu", "saxo", "seksi", "sıçar", "sıçtım", "osuruk", "ossuruk",
    "sikis", "sikiş", "siktir", "amcik", "amcık", "amk", "anan", "sikerim", "götveren", "ibne", "orospu",
    "pezevenk", "yarak", "yarrak", "oç", "piç", "göte", "am", "amcığ", "çük", "yarağ", "orspu", "anana",
    "amk", "aq", "sg", "siktir", "yarak", "yarrak", "daşşak", "taşşak", "götünü", "amını", "amına",
    "sikiyim", "sikerim", "siktir", "piç", "ibne", "götveren", "sürtük", "orospu", "pezevenk", "gavat",
    "amcık", "sik", "sikik", "amk", "amına koyim", "amına koduğum", "anasını sikiyim", "aq", "göt",
    "göt", "amk", "ebenin", "sik", "pust", "puşt", "orospunun evladı", "amına kodum", "amk", "ibne",
    "sike", "sikerim", "sikik", "amcık", "şerefsiz", "piç", "yarrak", "götünü", "sikim", "sikiym",
    "amını", "ananın", "amına", "sikeyim", "götüne", "sokam", "göt", "götüne", "amına", "sokayım",
    "amınakoyim", "amk", "siktir", "puşt", "sürtük", "götverene", "amına", "koyarım", "amına koyim",
    "siktir", "amını", "sikerim", "sik", "göt", "amk", "yarrak", "o.ç", "piç", "annesiz", "ananı",
    "sikiyim", "annenizi", "sikim", "anneni", "ananızı", "babanızı"
]

def ramazan_ozturk(ramo):
    mesaj = ramo.lower()
    for kelime in ramazanin_yarra:
        if re.search(rf"\b{re.escape(kelime)}\b", mesaj):
            return True
    return False
       
@ramowlf.message_handler(commands=['kufur_ekle'])
def insta_ramowlf(ramazancik):
    if ramazancik.from_user.id not in ramazan_babus:
        return
    ramo = ramazancik.text.split(' ', 1)[1]
    
    if ramo not in ramazanin_yarra:
        ramazanin_yarra.append(ramo)
        ramowlf.reply_to(ramazancik, f'"{ramo}" eklendi.')
    else:
        ramowlf.reply_to(ramazancik, f'"{ramo}" ekledigin şey zaten var.')

@ramowlf.message_handler(commands=['kufur_sil'])
def telegram_ramowlf(ramazancik):
    if ramazancik.from_user.id not in ramazan_babus:
        return
    ramo = ramazancik.text.split(' ', 1)[1]
    
    if ramo in ramazanin_yarra:
        ramazanin_yarra.remove(ramo)
        ramowlf.reply_to(ramazancik, f'"{ramo}" silindi.')
    else:
        ramowlf.reply_to(ramazancik, f'"{ramo}" zaten yokki')

@ramowlf.message_handler(func=lambda message: True)
def ramazancik(ramazancik):
    if ramazan_ozturk(ramazancik.text):
        ramowlf.delete_message(ramazancik.chat.id, ramazancik.message_id)
        
        sikis_online = f"<a href=\"tg://user?id={ramazancik.from_user.id}\">{ramazancik.from_user.first_name}</a>"
        azdim = f"Merhaba {sikis_online}, Grupta Küfür yasak lütfen argo kullanmadan sohbet edelim."
        ramowlf.send_message(ramazancik.chat.id, azdim, parse_mode='HTML')
    
ramowlf.polling(none_stop=True)