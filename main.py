import os
from scraper import getItems


def getProduct():
    getItems('''Get the product's full name from product page the paste inside this function''')


SCRIPT_PATH = os.path.abspath(__file__)
CRONTAB_ENTRY = f"*/5 * * * * python {SCRIPT_PATH}\n"
CRONTAB_FILE = os.path.expanduser('~/.crontab_temp')


def create_crontab_entry():
    if os.path.exists(CRONTAB_FILE):
        return
    with open(CRONTAB_FILE, 'w') as f:
        f.write(CRONTAB_ENTRY)
    os.system('crontab {}'.format(CRONTAB_FILE))
    print("Crontab entry created successfully.")


if __name__ == "__main__":
    getProduct()
    create_crontab_entry()
