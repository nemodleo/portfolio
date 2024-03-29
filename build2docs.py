#-*- coding: utf-8 -*- 
import os, glob, shutil 
from pathlib import Path

def build2docs():
    _, git_repo = os.path.split(os.getcwd())
    print(git_repo)

    if Path("docs").exists():
        shutil.rmtree("docs")

    html = [file for file in glob.glob("build/**", recursive=True) if file.endswith(".html")]
    print(html)

    for h in html:
        f = open(h, 'rt',  encoding='UTF8')
        code = f.read()
        f.close()
        g = open(h, 'w',  encoding='UTF8')
        code = code.replace("/static", "/{}/static".format(git_repo))
        code = code.replace('<a href="/">', '<a href="/{}/">'.format(git_repo))
        code = code.replace('<a href="/experiences/">', '<a href="/{}/experiences/">'.format(git_repo))
        code = code.replace('<a href="/projects/">', '<a href="/{}/projects/">'.format(git_repo))
        g.write(code)
        g.close()

    shutil.move("build", "docs")

if __name__=="__main__":
    build2docs()