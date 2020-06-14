#soal1
def Hashtag (string):
    if not string.strip():
          print ('False')
    else:
        string = '#' + ''.join([letter.capitalize() for letter in string.split()])

    return string if len(string)<=140 else print ('False')

#soal2
def create_phone_number(number):
    listphone = []
    for num in number:
        listphone.append("".join(str(num)))
    phnstr = listphone
    first = "".join(phnstr[:3])
    second = "".join(phnstr[3:6])
    third = "".join(phnstr[6:])

    print("({}) {}-{}".format(first,second,third))


#soal 3
def sort_odd_even (num): 
    for i in range(len(num)):
        for j in range 