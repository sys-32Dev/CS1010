# Edwin Hui
# asks the user to pick a shape from a image
print("Pick a shape contained in this image: https://csns.cysun.org/download?fileId=7899012")
# asks the user questions to determine what shape they chose
red=input("is the shape red? (Y/N):")
if red == "Y":
    border=input("is does the shape have a border? (Y/N):")
    if border == "Y":
        circle=input("is does the shape have a circle arround it? (Y/N):")
        if circle == "Y":
            print("Your shape is shape 5.")
        else:
            print("Your shape is shape 7.")
    else:
        circle=input("is does the shape have a circle arround it? (Y/N):")
        if circle == "Y":
            print("Your shape is shape 4.")
        else:
            print("Your shape is shape 2.")
# whether the user responds yes or no the same set of questions are asked, with different outcomes.
else:
    border=input("is does the shape have a border? (Y/N):")
    if border == "Y":
        circle=input("is does the shape have a circle arround it? (Y/N):")
        if circle == "Y":
            print("Your shape is shape 8.")
        else:
            print("Your shape is shape 6.")
    else:
        circle=input("is does the shape have a circle arround it? (Y/N):")
        if circle == "Y":
            print("Your shape is shape 1.")
        else:
            print("Your shape is shape 3.")