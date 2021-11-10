from discord_webhook import *

class Hook():
    def __init__(self, url) -> None:
        self.url = url

    
    def send_msg(self, msg, **kwargs) -> None:
        tmp = DiscordWebhook(self.url, content=msg, **kwargs)
        tmp.execute()
        del tmp
    def send_embed(self, embed, **kwargs) -> None:
        tmp = DiscordWebhook(self.url, embeds=[embed], **kwargs)
        tmp.execute()
        del tmp