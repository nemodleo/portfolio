#-*- coding: utf-8 -*- 
import os, glob, shutil 

def build2docs():
    _, git_repo = os.path.split(os.getcwd())
    print(git_repo)

    html = [file for file in glob.glob("build/**", recursive=True) if file.endswith(".html")]
    print(html)

    for h in html:
        f = open(h, 'rt',  encoding='UTF8')
        code = f.read()
        f.close()
        g = open(h, 'w',  encoding='UTF8')
        code_w = code.replace("/static","/{}/static".format(git_repo))
        g.write(code_w)
        g.close()

    shutil.move("build", "docs")

if __name__=="__main__":
    build2docs()