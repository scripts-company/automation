import requests
import sys
import os
imprt send_mail

def send_mail():
    with open(".env", "r") as env.readlines():
        env = env.strip().split('=')
        send_mail(user=env[1], password=env[2])

def more_code():
    print("This is another code...")

def main(url):
    more_code()
    print("Starting automation...")
    r = requests.get(url, headers={'SEC': "Aa123456!"}, verify=False)

    for i in range(100):
        print(r.json() + r.status_code)

    send_mail()

if __name__ == '__main__':
    if not sys.argv[1]:
        print("Please give me the link...")
        exit(1)
    main(sys.argv[1])
