import re

charlong = re.compile(r'\w{8,}', re.VERBOSE)
contain_uppercase = re.compile(r'[A-Z]', re.VERBOSE)
contain_lowercase = re.compile(r'[a-z]', re.VERBOSE)
contain_digit = re.compile(r'\d+', re.VERBOSE)

print("Please Input Your Password...")
password = str(input())

matches=[]
for groups in charlong.findall(password):
     matches.append(1)
     continue
for groups in contain_uppercase.findall(password):
     matches.append(2)
     continue
for groups in contain_lowercase.findall(password):
     matches.append(3)
     continue
for groups in contain_digit.findall(password):
     matches.append(4)
     continue


condition = ['more than 8 character',
            'contain uppercase',
            'contain lowercase',
            'contain at least 1 digit'
]


# print(matches)
if len(matches)>=4:
    print("Passwors is not strong...")


for num in range(0,4):
    if num+1 not in matches:
        print('password must have ' + condition[num])
