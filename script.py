import os

if __name__ == "__main__":
    jobname = "tesis"
    for _ in range(2):
        os.system("pdflatex  -synctex=1 -interaction=nonstopmode -file-line-error -recorder -output-directory='./' -jobname={}  './thesis.tex'".format(jobname))
        folders = {
            ".": {
                "files": [".toc", ".xml", ".gz", ".out", ".log", ".fls", ".blg", ".bbl", ".aux", ".fdb_latexmk"],
            },
            "content": {
                "files": [".aux"],
            },
            "content/introduction": {
                "files": [".aux"],
            },
            "content/development": {
                "files": [".aux"],
            }
        }
        if (os.path.exists("./thesis-blx.bib")):
            os.remove("./thesis-blx.bib")
        for path in folders:
            folder = os.listdir(path)
            for item in folder:
                for extension in folders[path]["files"]:
                    if (item.endswith(extension)):
                        os.remove(os.path.join(path, item))

        if(jobname == "tesis"):
            jobname = "thesis"
            thesis = open("thesis.tex", "r")
            list_of_lines = thesis.readlines()
            list_of_lines[1] = "\\usepackage[english,bibtex]{thesis-style}"

            thesis = open("thesis.tex", "w")
            thesis.writelines(list_of_lines)
            thesis.close()
        elif(jobname == "thesis"):
            thesis = open("thesis.tex", "r")
            list_of_lines = thesis.readlines()
            list_of_lines[1] = "\\usepackage[spanish,bibtex]{thesis-style}"

            thesis = open("thesis.tex", "w")
            thesis.writelines(list_of_lines)
            thesis.close()