# Python program to download webcomics 

# import Request module to interact with web pages
import requests

# import module to create directory/folder to store comic
import os

# Function to recieve input from user
def recieveInput():
    # input comic URL of 1st page
    url = input('Comic URL: ')

    # input comic name
    name = input('Comic Name: ')
    # Length of comic for Loop
    comicLength = int(input('Amount of pages: '))

    # User inputs type URL format
    urlFormat = 0
    while True:
        formato = input('Page number as /#, type 1 \nPage numeber as -##, type 2 \nPage number as _##, type 3\nFormat: ')
        urlFormat = int(formato)

        if urlFormat == 1 or urlFormat == 2 or urlFormat == 3:
            break
        else:
            print('Invalid format')

    return url, name, comicLength, urlFormat 

# Function to download comic
def downloadComic(url, name, comicLength, urlFormat):
    # Loop to iterate through all the pages of the comic
    for i in range(comicLength + 1):
        # Breaks loop if i reaches comicLength so empty page is not created
        if i == comicLength:
            break
        # Increases page counter by 1 so Page doesn't start at 0
        j = i+1

        # Splits URL at . to add new page number
        newURL = url.rsplit('.', 1)

        # Cheks URL page number format
        # If page number in URL is written as: /#
        if urlFormat == 1:
            # Adds page number to iterate to next page
            if j < 10:
                newURL[0] = newURL[0][:-1] + str(j) + '.'
            elif j < 100:
                if j == 10:
                    newURL[0] = newURL[0][:-2] + '/' + str(j) + '.'
                else:
                    newURL[0] = newURL[0][:-2] + str(j) + '.'
            else:
                if j == 100:
                    newURL[0] = newURL[0][:-3] + '/' + str(j) + '.'
                else:     
                    newURL[0] = newURL[0][:-3] + str(j) + '.'
        # If page number in URL is written as -#
        elif urlFormat == 2:
            # Adds page number to iterate to next page
            if j < 10:
                newURL[0] = newURL[0][:-1] + str(j) + '.'
            elif j < 100:
                if j == 10:
                    newURL[0] = newURL[0][:-2] + '-' + str(j) + '.'
                else:
                    newURL[0] = newURL[0][:-2] + str(j) + '.'
            else:
                if j == 100:
                    newURL[0] = newURL[0][:-3] + '-' + str(j) + '.'
                else:     
                    newURL[0] = newURL[0][:-3] + str(j) + '.'
        
        elif urlFormat == 3:
            # Adds page number to iterate to next page
            if j < 10:
                newURL[0] = newURL[0][:-1] + str(j) + '.'
            elif j < 100:
                if j == 10:
                    newURL[0] = newURL[0][:-2] + '_' + str(j) + '.'
                else:
                    newURL[0] = newURL[0][:-2] + str(j) + '.'
            else:
                if j == 100:
                    newURL[0] = newURL[0][:-3] + '_' + str(j) + '.'
                else:     
                    newURL[0] = newURL[0][:-3] + str(j) + '.'

        # combines split URL and saves URL with new page number
        url = ''.join(newURL)

        # Prints current comic page URL
        print(url)

        # Sends request to recieve data from webpage
        r = requests.get(url)

        # Saves comic page as PNG
        with open(f'{name}/{name} pg{j}.jpg', 'wb') as f:
            f.write(r.content)

# Function to create new folder to store comic
def makeFolder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(f'{name} already exists')

next = True

# Main method to run program until user quits
while next is True:
    # Calls recieveInput function to recieve comic URL, name and length from user
    url, name, comicLength, urlFormat= recieveInput()

    # Calls makeFolder method to create folder to store comic
    makeFolder(name)

    # Calls downloadComic function and sends URL, name and length to download comic and store in folder
    downloadComic(url, name, comicLength, urlFormat)

    # Asks user to download new comic
    again = input('Download another comic? y/n: ').lower()

    # If user answer is 'n' program is over
    if again == 'n':
        next = False

    os.system('cls')
