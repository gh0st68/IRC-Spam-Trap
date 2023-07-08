##TWISTED SPAM TRAP BOT## 
## This is a IRC Channel Spam Bot Trap Bot.
## This bot will automatically GLINE any user or bot who joins the two specified channels below. 
## Spam bots do the /list command on your network than join all channels and spam. This will help prevent that, since the spam bots will join the spam trap channels. 
## The bot will set a 30 day GLINE. (NOTE ANYONE WHO JOINS THE CHANNEL THE BOT IS IN THEY WILL BE GLINED, BUT MOST PEOPLE DONT GO SNOOPING TO ALL RANDOM CHANNELS ON A NETWORK)


## TESTED ON INSPIRCD 
## IF IT DOES NOT WORK ON YOUR IRCD LET ME KNOW, COME TO #DEV ON IRC.TWISTEDNET.ORG I WILL FIX IT FOR YOUR IRCD.

##THINGS TO CHANGE

## Replace the two channels below, replace oper login and password. 
## I also added a spot to put your nickserv password. (Not needed)

## Dependencies / things to install to make this bot work
## pip3 install irc.bot
## pip3 install ssl


## Questions or help or just to visit come to 
### IRC.TWISTEDNET.ORG CHANNEL #DEV & #TWISTED


import ssl
import irc.bot
import irc.connection
import re

class GhostBot(irc.bot.SingleServerIRCBot):
    def __init__(self):
        irc.bot.SingleServerIRCBot.__init__(
            self,
            server_list=[("irc.twistednet.org", 6697)],
            nickname="TestBot3",
            realname="TestBot3",
            connect_factory=irc.connection.Factory(wrapper=ssl.wrap_socket)
        )

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join("#ghost2")
        c.join("#ghost")
        c.send_raw("OPER OPERUSERNAMEHERE OPERPASSWORDHERE")
        c.send_raw("PRIVMSG nickserv :identify NICKSERVPASSWORD")

    def on_privmsg(self, c, e):
        c.whois([e.source.nick])

    def on_all_raw_messages(self, c, e):
        if '311' in e.arguments[0] or '378' in e.arguments[0]:
            ip_address = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', e.arguments[0])
            if ip_address:
                ip_address = ip_address[0]
                c.send_raw(f"GLINE *@{ip_address} 30 :spam")

if __name__ == "__main__":
    bot = GhostBot()
    bot.start()

