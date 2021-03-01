from time import sleep
class Dasturlar():
    
    def __init__(self,nomi,imkoniyati,qiyin_daraja):
        sleep(1)
        print("Dastur ishga tushmoqda...")
        self.nomi = nomi
        self.imkoniyati = imkoniyati
        self.qiyin_daraja = qiyin_daraja
   
    def oqi(self):
        print("""
              Dasturning nomi:       {}
              Dasturning imkoniyati: {}
              Dasturning Darajasi:   {}
              """.format(self.nomi,self.imkoniyati,self.qiyin_daraja))

class Adobe_Pro(Dasturlar):
    
    def __init__(self,nomi,imkoniyati,qiyin_daraja,videomontaj):
        self.nomi = nomi
        self.imkoniyati = imkoniyati
        self.qiyin_daraja = qiyin_daraja
        self.videomontaj = videomontaj
    
    def videoMi(self):
        if self.videomontaj == True:
            print("Bu dastur Video montaj qilishga qulay!")
        else:
            print("Bu dastur Video montaj qilishga qulay EMAS!!!\n")

premier1 = Adobe_Pro("Adobe Premier Pro", "Videomontajda professional", "Normal", True)
premier1.oqi()
premier1.videoMi()

after_effects = Adobe_Pro("Adobe After Effects", "Grafikalar qilishda professional", "Yuqori", False)
after_effects.oqi()
after_effects.videoMi()

photoshop_dast = Adobe_Pro("Aobe Photoshop", "Fotolarni tahrirlashda qulay", "Normal", False)
photoshop_dast.oqi()
photoshop_dast.videoMi()

class Dasturchilik(Dasturlar):
    def __init__(self,nomi,imkoniyati,qiyin_daraja):
        super().__init__(nomi,imkoniyati,qiyin_daraja)

c_tili = Dasturchilik("C - Dasturlash tili", "Juda tez ishlaydi va kompayl bo'ladi", "Yuqori")
c_tili.oqi()

python_tili = Dasturchilik("Python", "Juda keng yani botlar yaratishda, suniy ongda, turli dasturlar yaratishda qo'llaniladi", "Normal")
python_tili.oqi()

js = Dasturchilik("Java Script", "WEB dasturlar yaratishda ishlatiladi", "Normal")
js.oqi()

swift = Dasturchilik("Swift", "iOS qurilmalariga dastur yozishda ishlatiladi", "Yuqori")
swift.oqi()

go_tili = Dasturchilik("GO dasturlash tili", "Juda keng, pochti hamma narsa qilsa bo'ladi", "Yuqori")
go_tili.oqi()

java = Dasturchilik("Java", "Dasturlarni backend qismi uchun ishlatiladi", "Normal")
java.oqi()

kotlin = Dasturchilik("Kotlin", "Android qurilmariga dastur va aplicationlar yaratishda qo'llaniladi", "Normal")
kotlin.oqi()

class Otizimlar(Dasturlar):
    
    def __init__(self,nomi,imkoniyati,qiyin_daraja,kopdas_bormi):
        self.nomi = nomi
        self.imkoniyati = imkoniyati
        self.qiyin_daraja = qiyin_daraja
        self.kopdas_bormi = kopdas_bormi
    
    def kopDastBormi(self):
        if self.kopdas_bormi == True:
            print("Bu OS ga ko'p dasturlar topiladi!")
        else:
            print("Bu OS ga ko'p dasturlar topilishi qiyin!!!!\n")

windows_ot = Otizimlar("Windows 10", "Imkoniyati keng", "Oson", True)
windows_ot.oqi()
windows_ot.kopDastBormi()

macOs = Otizimlar("MAC OTizimi", "Ishlatish oson virus tushmaydi", "Oson", False)
macOs.oqi()
macOs.kopDastBormi()

linux_OT = Otizimlar("Linux Kali", "Dasturlashda foydalanish qulay, Hakkerlarning Operatsion tizimi", "Normal",False)
linux_OT.oqi()
linux_OT.kopDastBormi()

android_OT = Otizimlar("Android", "Smartfon,Planshet, Soat va shunga o'xshash qurilmalarda foydlaniladi", "Normal", True)
android_OT.oqi()
android_OT.kopDastBormi()

iOS_OT = Otizimlar("iOS", "Apple kompaniyasining mahsulotlarida qo'llaniladi", "Oson", False)
iOS_OT.oqi()
iOS_OT.kopDastBormi()

nomi = input("O'zingiz Biror Dasturning Nomini Kiriting: ")
imkoniyati = input("Dasturning Imkoniyatlari Qanday: ")      
darajasi = input("Dasturning o'rganishning qiyinlik darajasi qanday: ")  
dastur = Dasturlar(nomi,imkoniyati,darajasi)
dastur.oqi()



























































