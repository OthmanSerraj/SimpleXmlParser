# coding: utf-8
import os
from lxml import etree
class ToParse_ATQ:
    def __init__(self,mydirectory):
        self.mydirectory=mydirectory
        self.myfiles,self.mytrees=self.get_file_n_tree()
        self.mabalise="AT %Q*"
        self.mydata=self.get_all_vars()
    def get_all_vars(self):
        List_all_vars=[]
        for i,tree in enumerate(self.mytrees):
            filer=self.myfiles[i]
            root = tree.getroot()
            for element in root.iter():
                X=element.text
                try:Y=X.split("\n")
                except:Y=[]
                for pseudo_var in Y:
                    StringOut=pseudo_var.split("//")[0]
                    if StringOut.find(self.mabalise)!=-1:
                        StringOut=StringOut.replace("\t"," ")
                        try:
                            x1,x2=StringOut.split(":")[:2]
                        except:
                            continue
                        Stype=x2.replace(" ","")
                        Sname=x1.split("AT")[0].replace(" ","")
                        mydic={"Name":Sname,
                        "Type":Stype,
                        "File":"ToParse"+filer.split("ToParse")[1]
                        }
                        List_all_vars.append(mydic)
        return List_all_vars
    def get_file_n_tree(self):
        fichiers=[]
        mytrees=[]
        for root, dirs, files in os.walk(self.mydirectory):
            for file in files:
                try:
                    filer=os.path.join(root, file)
                    tree = etree.parse(filer)
                    fichiers.append(filer)
                    mytrees.append(tree)
                except:pass
        return fichiers,mytrees

if __name__== "__main__":
    # mondossierdata="C:\\Users\\Elève\\Desktop\\Parser_Data\\ToParse"
    MonParser=ToParse_ATQ(mondossierdata)
    MesDonnees=MonParser.mydata
    for dic in MesDonnees:print(dic)
