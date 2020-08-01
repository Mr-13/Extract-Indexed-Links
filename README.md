``Extract Indexed Links`` a *beautiful* CLI tool.
======================================================================
*A cli tool is to extract your favrouite TV Show links from indexed URL(s).*


Isn't it awesome you click on each indexed url and download with your 
download manager.

*Hell no!*  You know what's awesome?  It's when you simply can extract all 
links in a text file which can be passed to any download manager to download in 
one go.

**How to use?**
======================================================================
*prerequisites: python3 and pip3*

- Clone or download this repository
- Grab all the required dependencies using

        pip install -r requirements.txt
    or

        pip3 install -r requirements.txt

- Use the tools :p 

**Usage**

        Usage:
            extract_link.py <link>
            extract_link.py -i <link> -o FILE

        -h, --help   show this help message and exit
        --version    show program's version number and exit
        -i <link>    specify input link
        -o FILE      specify output file [default: ./extracted_links.txt]


*This tool is part of one of my recovered my hobby projects which got damaged with my old laptop.*