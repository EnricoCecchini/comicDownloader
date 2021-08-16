#Util functions for ComicDownloader

# Function to get next page URL
def nextPage(url, urlFormat, j):
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
                
    # If page number in URL is written as -##
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
    
    # If page number in URL is written as _##
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

    return newURL

def savePage(url, name, j, r):
    # Saves comic page as PNG
    if '.gif' in url:
        with open(f'{name}/{name} pg{j}.gif', 'wb') as f:
            f.write(r.content)    

    else:
        with open(f'{name}/{name} pg{j}.jpg', 'wb') as f:
            f.write(r.content)   