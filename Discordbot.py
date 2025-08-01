import discord
import yfinance as yf

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

Token = "Your Token Here"  
def stock_price(ticker):
    try:
        data = yf.Ticker(ticker)
        hist = data.history(period="1d")
        if hist.empty:
            return None
        return hist["Close"].iloc[-1]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("hello"):
        await message.channel.send("Hola welcome to Mr.GOAT'S server")
        await message.author.send("Hola welcome to Mr.GOAT'S server")

    if message.content.startswith("stockprice"):
        parts = message.content.split(" ")
        if len(parts) == 2:
            ticker = parts[1].upper()
            price = stock_price(ticker)
            if price:
                await message.channel.send(f"Stock price of {ticker} is ${price:.2f}")
            else:
                await message.channel.send(f"Couldn't fetch stock price for {ticker}.")

@client.event
async def on_connect():
    print("Bot connected to the server!")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Welcome to the server {member.name}!")

client.run(Token)
