This is the 1st Version of my Comic Downloader. 

This program uses the Request and OS modules to download images from websites and stores them in a directory

This program works with comics who's URL for each individual page contains the page number at the end, in either /##.jpg/png,  -##.jpg/png or _##.jpg/png.

Instructions:

1 - Open 1st page of comic in web browser

2 - Right click the image of the first page and select 'Copy Image Address'

3 - Make sure the link contains the page number, and that by changin it and reloading, you can change page
    Example: https://readcomicsonline.ru/uploads/manga/deadpool-kills-the-marvel-universe-again-2017-/chapters/5/01.jpg
    By changin the 01 at the end of the link, you can change pages
    
4 - Run program and paste link of first page

5 - Type the name of the comic (This will also be the name of the folder where the comic will be stored)

6 - Type the amount of pages the comic has

*If you want to download another comic, simply type 'y' when prompted*
*The comic will be downloaded wherever the python file is located*
*Program should work even for comics with 100+ pages*

