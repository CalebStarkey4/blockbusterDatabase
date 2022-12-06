from xml.dom import minidom

def addRecord():
    print("This is to add a record.")


def dropRecord():
    print("This is to drop a record.")


def updateRecord():
    print("This is to update a record.") 

    
def getRecord():
    file = minidom.parse('movies.xml')

    print(file.firstChild.tagName)

    title = file.getElementsByTagName("field")
    print("%d fields:" % title.length)

    for skill in title:
        print(skill.getAttribute("name"))



    """models = file.getElementsByTagName('row')
    print('\nAll attributes:')
    for elem in models:
        print(elem.attributes['name'].value)

    print('\nmodel #2 data:')
    print(models[0].firstChild.data)

    print('model #2 attribute:')
    print(models[1].attributes['001'].value)"""


def filterRecord():
    print("This is to filter a record.")


getRecord()