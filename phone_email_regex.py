import pyperclip, re

# dicky_arya@apps.ipb.ac.id
# abc@apps.ipb.ac.id
# def@gmail.com
# 123-234-345
# 0812-9226-2530
# regex untuk phonenumber
phoneRegex = re.compile(
r'''
    (
        (\d{3,4}|\(\d{3,4}\))           # area code,group1
        (\s|-|\.)?                   # separator,group2
        (\d{3,4})                       # first 3 digits,group3
        (\s|-|\.)?                    # separator,group4
        (\d{3,4})                        # last 4 digits,group5
        (\s*(ext|x|ext.)\s*\d{2,5})? # extension
    )
''', re.VERBOSE
)

# TODO: regex untuk email

emailIPBRegex = re.compile(
r'''
    (
    ([a-zA-Z0-9._]+)
    @apps.ipb.ac.id
    )
''', re.VERBOSE

)

emailRegex = re.compile(
r'''
    (
        [a-zA-Z0-9._%+-]+   # text sebelum @
        @                   # @
        [a-zA-Z0-9.-]+      # text domain
        (\.[a-zA-Z]{2,4})  # dot sesuatu
    )
''', re.VERBOSE
)

# TODO: temukan yang match dari text clipboard
# paste dari clipboard ke text
text = str(pyperclip.paste())
# list di bawah untuk nampung yg match
matches=[]
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    matches.append(phoneNum)

for groups in emailIPBRegex.findall(text):
    matches.append(groups[0])

for groups in emailRegex.findall(text):
    if groups[0] not in matches:
        matches.append(groups[0])


# copy results ke clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
