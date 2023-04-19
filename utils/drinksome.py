from requests import Session

class Drinksome():

    def __init__(self, session = Session(), userAgent = '') -> None:
        self.session = session
        self.userAgent = userAgent

    def sendMessage(self, counterId: str, basicId: str, message: str, proxy: str):
        # while True:
        try:
            response = self.session.post(
                url = f'https://drinksonme.live/api/counters/{counterId}/messages',
                headers = {
                    'accept': 'application/json, text/plain, */*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'basic': basicId,
                    'content-type': 'application/json',
                    'origin': 'https://drinksonme.live',
                    'referer': 'https://drinksonme.live/app',
                    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': self.userAgent,
                },
                json = {
                    'message': message
                },
                proxies = {
                    'http': f'http://{proxy}',
                    'https': f'http://{proxy}'
                }
            )
            print(response.json())
        except:
            pass