# Python program to download webcomics 

# import Request module to interact with web pages
import requests

# import module to create directory/folder to store comic
import os

import utils

# Function to recieve input from user
def recieveInput():
    # input comic URL of 1st page
    while True:
        url = input('Comic URL: ')

        try:
            requests.get(url)
            break
        except requests.exceptions.MissingSchema:
            print("Invalid URL")
        except requests.ConnectionError:
            print("Invalid URL")
    
    # Clear Terminal when downloading a new comic
    os.system('cls')

    print(f'URL: {url}')

    # input comic name
    name = input('Comic Name: ')
    name = name.replace('/',' ').replace("?",'')

    # User inputs type URL format
    urlFormat = 0
    while True:
        if '/1.jpg' in url or '/1.png' in url or '/01.jpg' in url or '/01.png':
            urlFormat = 1
        elif '-01.jpg' in url or '-01.png' in url:
            urlFormat = 2
        elif '_01.jpg' in url or '_01.png' in url:
            urlFormat = 3

        if urlFormat == 1 or urlFormat == 2 or urlFormat == 3:
            break
        else:
            print('Invalid format')

    return url, name, urlFormat 

# Function to download comic
def downloadComic(url, name, urlFormat):
    j = 1
    # Loop to iterate through all the pages of the comic
    while True:
        newURL = utils.nextPage(url, urlFormat, j)

        # combines split URL and saves URL with new page number
        url = ''.join(newURL)

        # Sends request to recieve data from webpage
        r = requests.get(url)

        # Check if page exists, if not, break
        if r.status_code == 404 and '.jpg' in url:
            url = url.replace('.jpg', '.png')
            r = requests.get(url)
        
        if r.status_code == 404 and '.png' in url:
            url = url.replace('.png', '.jpg')
            r = requests.get(url)

        #print(f"TEST: {url}")
        
        if r.status_code == 404:
            break
        else:
            utils.savePage(url, name, j, r)    

        # Prints current page
        print("\rSaving pg{}".format(j), end='')

        j+=1

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
    url, name, urlFormat= recieveInput()

    # Calls makeFolder method to create folder to store comic
    makeFolder(name)

    # Calls downloadComic function and sends URL, name and length to download comic and store in folder
    downloadComic(url, name, urlFormat)

    # Asks user to download new comic
    again = input('Download another comic? y/n: ').lower()

    # If user answer is 'n' program is over
    if again == 'n':
        next = False

    # Clear Terminal when downloading a new comic
    os.system('cls')
