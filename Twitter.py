import tweepy #tweepy kütüphanesini kullanacağımız için kütüphaneyi import ediyoruz
import os #Led yakmak ve mp3 çaldırdığımız dosyaları çalıştırmak için kullanacağız
import time #tweet apinin veri çekme aşımına düşmemek için 2 sn de bir tweetleri çekmek için kullanacağız
consumer_key="SetTjt4D3KoBN3avFLmVBpZvE" #Twitter apinizin consumer keyiniz
consumer_secret="HsvtteVP3Fu3x93AkqnnfaJwKBoDlzQQGniYLiNpe5vAfB6zZx" #Twitter apinizin consumer_secret keyiniz
access_token="1629196130-Y9E1lA4sqwrRbpvHNIZL68QEvSsv7AiayKvCwCs"#Apinizin tokeni
access_token_secret="Ngr4hoXQUISUdVqZV3OgXIHwr5sQ6YA2ZQ2G5jk5l0Sno"#Apinin token secreti

giris = tweepy.OAuthHandler(consumer_key, consumer_secret)
giris.set_access_token(access_token, access_token_secret)

api = tweepy.API(giris)

sayac=1
while sayac==1: #Sayaç 1 olduğu sürecek bu işlemi yap diyoruz ve aşağıdaki kodlara geçiyor
    twitler = api.home_timeline() #Her seferinde tweete bakarken zaman tünelinizdeki güncel tweeti çekiyor
    twit=twitler[0].text#Zaman tünelinizdeki son tweeti twit adındaki değişkene atıyor
    print("tweet cekiliyor",twit) #Bunu kontrol için kullandım güncel tweeti görebiliyor mu diye
    time.sleep(2)#Bu işlemleri yaptıktan sonra 2 sn boyunca bekliyor
    if twit=="Calistir":#Bu kısımda eğer son atılan tweet Calistir ise aşağıdaki işlemleri yapmaya başla
        os.system('python LedYak.py')#Ledimizi yakan dosyayı çalıştırıyor
        os.system('python mp3cal.py')#Mp3 ü müzü çalan dosyayı çalıştırıyor
        break#İstediğimiz işlemi yaptığı için döngüden çıkıyor




