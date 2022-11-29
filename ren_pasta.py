import os

def main ():
    i = 0
    path =  "C:/Users/Vitor Life/Pictures/Saved Pictures/"
    for filename in os.listdir(path):
        my_dest = "imagem" + str(i) + ".jpg"


if __name__ == '__main__':
    main()

