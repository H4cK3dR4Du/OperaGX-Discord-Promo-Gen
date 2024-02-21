import os, json, time, random, string, ctypes, concurrent.futures

try:
    import tls_client
    import pystyle
    import colorama
    import requests
    import uuid
    import datetime
except ModuleNotFoundError:
    os.system("pip install tls_client")
    os.system("pip install pystyle")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install uuid")
    os.system("pip install datetime")

from pystyle import Write, System, Colors, Colorate, Center, Anime, Box
from colorama import Fore, Style, init

class Console_Colors:
    reset = Fore.RESET
    black = Fore.BLACK
    red = Fore.RED
    green = Fore.GREEN
    yellow = Fore.YELLOW
    blue = Fore.BLUE
    magenta = Fore.MAGENTA
    cyan = Fore.CYAN
    white = Fore.WHITE
    gray = Fore.LIGHTBLACK_EX
    light_gray = Fore.LIGHTWHITE_EX
    light_red = Fore.LIGHTRED_EX
    light_green = Fore.LIGHTGREEN_EX
    light_yellow = Fore.LIGHTYELLOW_EX
    light_blue = Fore.LIGHTBLUE_EX
    light_magenta = Fore.LIGHTMAGENTA_EX
    light_cyan = Fore.LIGHTCYAN_EX

class OperaGX_Generator:
    def __init__(self) -> None:
        self.chrome_version = random.randint(115, 121)
        self.owner = "H4cK3dR4Du"
        self.promo_path = "promos.txt"
        self.promo_link = "https://discord.com/billing/partner-promotions/1180231712274387115/"
        ctypes.windll.kernel32.SetConsoleTitleW(f"OperaGX Promo Gen | t.me/{self.owner} - github.com/{self.owner}")

        with requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all", stream=True) as response:
            response.raise_for_status()
            with open("proxies.txt", "w") as f:
                for line in response.iter_lines():
                    if line:
                        f.write(line.decode('utf-8') + '\n')

    def get_session(self):
        session = tls_client.Session(
            client_identifier=f"chrome{self.chrome_version}",
            random_tls_extension_order=True,
        )

        with open("proxies.txt", "r") as f:
            proxies = f.read().splitlines()
            if proxies:
                proxy = random.choice(proxies)
                session.proxies = {
                    "http": "http://" + proxy,
                    "https": "http://" + proxy
                }
                return session
            else:
                return session
        
    def getCurrentTime(self) -> str:
        date = datetime.datetime.now()
        hour, minute, second, = date.hour, date.minute, date.second
        timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
        return timee
    
    def promo_gen(self):
        session = self.get_session()

        headers = {
            "Origin": "https://www.opera.com",
            "Content-Type": "application/json",
            "Sec-Ch-Ua": f'"Opera GX";v="105", "Chromium";v="{self.chrome_version}", "Not?A_Brand";v="24"',
            "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.chrome_version}.0.0.0 Safari/537.36 OPR/105.0.0.0"
        }

        data = {
            "partnerUserId": str(uuid.uuid4())
        }

        r = session.post("https://api.discord.gx.games/v1/direct-fulfillment", headers=headers, json=data)
        token = r.json()['token']
        with open("promos.txt", "a+") as f:
            f.write(self.promo_link + token + "\n")

        yeah = self.getCurrentTime()
        print(f"{Console_Colors.cyan}[ {Console_Colors.magenta}{yeah}{Console_Colors.cyan} ] {Console_Colors.reset}({Console_Colors.green}+{Console_Colors.reset}) {Console_Colors.green}Generated {Console_Colors.reset}: {Console_Colors.light_blue}{self.promo_link[:30]}.../{token[:39]}***********")

if __name__ == "__main__":
    Write.Print(f"""
\t\t\t\t\t\t╔═╗╔═╗╔═╗╦═╗╔═╗  ╔═╗═╗ ╦
\t\t\t\t\t\t║ ║╠═╝║╣ ╠╦╝╠═╣  ║ ╦╔╩╦╝
\t\t\t\t\t\t╚═╝╩  ╚═╝╩╚═╩ ╩  ╚═╝╩ ╚═
\t\t\t\t\t╔═╗╦═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗
\t\t\t\t\t╠═╝╠╦╝║ ║║║║║ ║  ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝
\t\t\t\t\t╩  ╩╚═╚═╝╩ ╩╚═╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═

\t\t\t            t.me/H4cK3dR4Du - github.com/H4cK3dR4Du - tls_spoof      
\n""", Colors.blue_to_purple, interval=0.000)
    i = OperaGX_Generator()
    threads = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        for _ in range(1000):
            threads.append(executor.submit(i.promo_gen))

    for thread in concurrent.futures.as_completed(threads):
        try:
            thread.result()
        except:
            pass # I don't care