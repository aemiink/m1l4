# İlk Olarak discord kütüphanesini komutumun içine aktarmalıyım.
import discord
# Discord botunu "bot" sınıfı ile oluşturmak isterseniz farklı bir kütüphanenin içindeki fonksiyonu içeri aktarmalısınız.
from discord.ext import commands
# Kendi yazdığımız fonksiyonları içeri aktarmak istiyorsak;
from fonksiyonlar import *


#Ayrıcalık mantığı client sınıfı ile aynı mantıktadır.
intents = discord.Intents.default()
intents.message_content = True

#Bot Sınıfı kullanılarak bot oluşturulması
# commands.Bot() fonksiyonu bir botun özelliklerini belirtmenize yardımcı olur.
# command_prefix='!' --> botun komutları hangi sembolle başlayacak bunu belirtir.
# intents=intents --> botun ayrıcalıkları developer portaldaki gibi olmasını sağlar.
bot = commands.Bot(command_prefix='!', intents=intents)


# @bot.event dekaratörü bot hazır olduğunda konsolda bir mesaj yayınlamaızı sağlayacaktır.
@bot.event
async def on_ready():
    print(f'{bot.user} olarak discorda giriş yaptık!')
    
# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def hello(ctx):
    await ctx.send(f"Merhaba Sevgili {ctx.author.mention}! Nasılsın?")

# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def iyiyim(ctx):
    await ctx.send(f"{ctx.author.mention}! İyi olduğuna sevindim! Senin için ne yapmamı istersin?")

# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def kotuyum(ctx):
    await ctx.send(f"{ctx.author.mention}! Kötü olduğuna üzüldüm :( ! Senin için ne yapmamı istersin?")

# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def Ders(ctx):
    await ctx.send(f"Merhaba Sevgili {ctx.author.mention}! 'Yarın ki Ders Programın: '")
    
# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def Sifre(ctx):
    await ctx.send(f"Merhaba Sevgili {ctx.author.mention}! 20 Haneli Oluşturulan Şifren:{sifre_olusturucu(20)}") 

# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def yazimiturami(ctx):
    await ctx.send(f"Merhaba Sevgili {ctx.author.mention}! Parayı attım Tuttum. Çıkan Sonuç:{yazi_tura()}")
    
# @bot.command() deakratörü bota bir komut verildiğinde fonkisyonu aktifleştirir.
@bot.command()
# fonksiyonu oluşturduktan sonra parantezin icersine ctx adında bir arguman vermelisiniz.
# ctx = context --> içerik
async def emoji(ctx):
    await ctx.send(f"Merhaba Sevgili {ctx.author.mention}! Moduna göre rastgele bir emoji belirledim. Çıkan Sonuç:{emoji_olusturucu()}")
    
bot.run('MTIxMzE3MDQ5NzgxMDg2NjE5Ng.GTOQB5.saPSfq8sZcIDsDnKg-JYG1U3jyMs9WQxHom13c')
    
    




