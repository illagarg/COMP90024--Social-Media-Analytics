import fileinput
import sys

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)


replaceAll("/home/ubuntu/COMP90024--Social-Media-Analytics/dev_env_deploy/settings.py","REPLACED!!!", "ASKJDHADJASLKJLKJDALKKDSAJ")
