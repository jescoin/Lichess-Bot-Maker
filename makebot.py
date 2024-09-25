from colorama import init

init()
from colorama import Fore, Back, Style
# my github - https://github.com/jescoin

import berserk
import art
from art import tprint

tprint('jesbot')
print(Fore.RED + '                           dev:jescoin')
print('')
print('')
print(Fore.GREEN + 'My github:', Fore.BLUE + 'https://github.com/jescoin')
print(Fore.YELLOW + 'This is lichess bot creator')
print(Fore.RED + 'CHOOSE:')
print('')
print(Fore.BLACK + '[1] Upgrade to BOT status')

print('[2] Our BOTs')
answer = int(input('?'))
if answer == 1:
    token = input('Give me your API TOKEN ')
else:
    print('Our BOTs:\n@JesBot1\n@TheExampleBots')
    exit()


def create_a_bot():
    session = berserk.TokenSession(token)
    client = berserk.Client(session=session)

    client.account.upgrade_to_bot()
    print('Done!')


create_a_bot()