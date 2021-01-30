class Staff:
    def __init__(self, name, position, picture, description):
        self.name = name
        self. position = position
        self.picture = picture
        self.description = description


def makeNewMember(name, position, picture, description):
    newmember = Staff()
    newmember.name = name
    print(name)
    return 0


makeNewMember(input("What is their name\n"), input("What is their position\n"), input("What is the file path to the image\n"), input("Enter the description/bio\n"))