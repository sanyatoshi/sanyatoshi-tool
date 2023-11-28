import time
from colorama import init, Style

import social_deanon as sd
import ipdean as ipd, phonenum as phn

init()

resetstyle = Style.RESET_ALL
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
reset = "\033[0m"

def logo():
    logo_text = """{}

░██████╗░█████╗░███╗░░██╗██╗░░░██╗░█████╗░████████╗░█████╗░░██████╗██╗░░██╗██╗    
██╔════╝██╔══██╗████╗░██║╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██║░░██║██║     
╚█████╗░███████║██╔██╗██║░╚████╔╝░███████║░░░██║░░░██║░░██║╚█████╗░███████║██║   
░╚═══██╗██╔══██║██║╚████║░░╚██╔╝░░██╔══██║░░░██║░░░██║░░██║░╚═══██╗██╔══██║██║
██████╔╝██║░░██║██║░╚███║░░░██║░░░██║░░██║░░░██║░░░╚█████╔╝██████╔╝██║░░██║██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝ by sanyatoshi  на русском
    {}""".format(red, reset)

    for line in logo_text.split('\n'):
        print(line)
        time.sleep(0.1)

    print(Style.BRIGHT + 'download sanyatoshi tool....' + resetstyle)
    time.sleep(2)


def menu():
    while True:
        print('''{}                                               
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
████╗░████║██╔════╝████╗░██║██║░░░██║
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
████████╗░█████╗░░█████╗░██╗░░░░░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░░██║░░░╚█████╔╝╚█████╔╝███████╗
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝  by sanyatoshi на русском 
{}'''.format(red, reset))
        print(' {}{}WELCOME TO SANYATOSHI TOOL!{}{}\n  поиск по нику\n  поиск по айпи \n  поиск по номеру телефона'.format(Style.BRIGHT, red, reset, resetstyle))
        print('  выйти из тула')
        home_page = int(input('\n {}{}'.format(red, reset)))

        if home_page == 0:
            print('\n {}{}BYE BYE!{}{}'.format(Style.BRIGHT, red, reset, resetstyle))
            break
        elif home_page == 1:
            sd.SocialDeanon()
        elif home_page == 2:
            ipd.Ipcheck()
        elif home_page == 3:
            phn.PhoneNumber()
        else:
            print(' {}wrong!{}'.format(red, reset))
            continue


if __name__ == '__main__':
    logo()
    menu()