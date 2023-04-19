from tls_client import Session
from requests import Session
from yaml import safe_load
from itertools import cycle
from threading import Thread
from utils.drinksome import Drinksome

class NyaouuX(Drinksome):

    def __init__(self, session, userAgent, counterId, basicId) -> None:
        super().__init__(session, userAgent)
        self.counterId = counterId
        self.basicId = basicId

    def send(self, message: str, proxy: str):
        self.sendMessage(counterId=self.counterId,basicId=self.basicId,message=message,proxy=proxy)

if (__name__ == '__main__'):
    session, config = Session(), safe_load(open('./config.yml', 'r', encoding='utf-8'))
    proxyList = cycle([proxy.strip() for proxy in open('./proxies.txt')])
    count = 0
    nyax = NyaouuX(session=session,userAgent=config['userAgent'],counterId=config['counterId'],basicId=config['basicId'])
    for you in range(int(config['threadAmount'])):
        count += 1
        Thread(target=nyax.send, args=(f'{config["message"]} {count}',next(proxyList),)).start()