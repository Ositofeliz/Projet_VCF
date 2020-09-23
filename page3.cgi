#!/usr/bin/env python3

import cgi, cgitb
import re, os
#import matplotlib.pyplot as plt
from vcf_functions import *

dico = cgi.FieldStorage()
fd = dico.getvalue("fl").decode('utf-8')
chrom = dico.getvalue("chrom")
base = dico.getvalue("base")
mutation = dico.getvalue("mutation")
value = dico.getvalue("value")
filtre = dico.getvalue("filtre")
info = dico.getvalue("infos")

#cgitb.enable()
myFile = fd.split("\n")

# Déclarations
dicoChrom = {}
dicoRef = {}
dicoBox = {}
varNum_list = []
alt_list = []
fltr_List =[]
mod_dict = {}

# Création du dictionnaire dicoChrom
for e in myFile:
    resLine = re.search("^\w", e) 
    if resLine :
        line = e.split("\t")
        list = [line[2], line[3],line[4],line[5],line[6],line[7]]
        if line[0] in dicoChrom:
            dicoChrom[line[0]][line[1]]= []
            for i in list:
                dicoChrom[line[0]][line[1]].append(i)
        else :
            dicoChrom[line[0]] = {}

# Attribution des valeurs
varNum_list, var_nbr = getVarNumber(dicoChrom)
alt_list, fltr_list = getALFI(dicoChrom)

if not value:
    value ="All"
    
mod_dict = getSelection(dicoChrom, chrom, base, mutation, value, filtre)
mod_varNumList, mod_varNbr = getVarNumber(mod_dict)
        
print("""Content-type: text/html\n\n
    <head>
        <meta charset="utf-8" />
        <title> R&eacute;sultats du fichier vcf </title>
    </head>


    <body style="background-color:#E6E6E6;"> </br>
                
        <div style="position:absolute; top: 55px; left: 30px;"> 
            <form>
                <input type = "button" value = "Retour &agrave; la page pr&eacute;c&eacute;dente"  onClick="history.back()">
            </form>
        </div>
            
        <div style="position:absolute; top: 40px; right: 30px;"> 
            <form action="pagedon.cgi">
                <input type = "image" src="https://png.pngtree.com/element_origin_min_pic/17/09/24/301a645e077610520ffe9ea9a07774ed.jpg"  width="120"  alt ="don"> </br>
                <center>
                    <a href="pagedon.cgi"> <font color="#0000ff"> Faire un don ! </font> </a>
                </center>
            </form>
        </div> 
            
            
            
        <h1 align="center"> Fichier analys&eacute; avec succ&egrave;s </h1></br></br></br></br></br></br></br>
        <h4 style="position:absolute; right: 25%; top: 15%;"> VCF : Vitesse, C-curit&eacute; et Fiabilit&eacute; </h4>
        <h3 style="position:absolute; right: 20%; top: 20%;"> A bient&ocirc;t sur nos plateformes... </h3> 
        
            <fieldset style="background-color:#BDBDBD";>
                <legend> <h2> D&eacute;tails de l'analyse </h2> </legend>
                    
                    Param&egrave;tre(s) de s&eacute;lection choisi(s): </br>""")
                    
if chrom == "All" and base == "All" and mutation == "All" and (value == "" or value == "All") and (filtre == "Aucun" or filtre =="."):
    print("&emsp; <i>Vous n'avez pas s&eacute;lectionn&eacute; de param&egrave;tre particulier </i> </br>")
if chrom != "All":
    print("&emsp; - Chromosome ", chrom, "</br>")
if base != "All":
    print("&emsp; - Base de r&eacute;f&eacute;rence : ", base, "</br>")
if mutation != "All":
   print("&emsp; - Mutation :")
   if mutation[0] == '<':
       print("&lt;"+ mutation[1:-1] + "&gt; </br>")
   else:
       print(mutation, "</br>") 
if value != "All" and value != "":
    print("&emsp; - Qualit&eacute; minimale : ", value, "</br>")

if not mod_dict:
    print(""" </br></br> <i> Aucun r&eacute;sultat ne correspond &agrave; votre recherche </i>
                    </fieldset>
                </body>
            </html>""")
else:          
    print("</br> La s&eacute;lection repr&eacute;sente : </br>")
    print("&emsp; -", round(mod_varNbr / var_nbr * 100, 2), "% des alt&eacute;rations totales du g&eacute;nome, soit ", mod_varNbr," alt&eacute;rations.</br>")

    if chrom == "All":
        x = 0
        test1 = []
        while x < len(varNum_list):
            test1.append(((round(mod_varNumList[x][1]/varNum_list[x][1]*100, 3)), varNum_list[x][0]))
            x +=1
        print("&emsp; -", round(max(test1)[0], 2), "% des alt&eacute;rations totales du Chromosome", max(test1)[1], "(chromosome le plus affect&eacute;). </br>")

    if base == "All":
        ref_num = {}
        for e in mod_dict:
            for f in mod_dict[e]:
                if mod_dict[e][f][1] in ref_num:
                    ref_num[mod_dict[e][f][1]] += 1
                else :
                    ref_num[mod_dict[e][f][1]] = 0
               
        for e in ref_num:
            if ref_num[e] == max(ref_num.values()) and max(ref_num.values()) != 0:
                print("&emsp; -", round(ref_num[e]/mod_varNbr*100, 2), "% des alt&eacute;rations affectant la base", e, "soit", ref_num[e], "alt&eacute;rations (base la plus touch&eacute;e). </br>")

    if mutation == "All":
        alt_num = {}
        for e in mod_dict:
            for f in mod_dict[e]:
                if mod_dict[e][f][2] in alt_num:
                    alt_num[mod_dict[e][f][2]] += 1
                else :
                    alt_num[mod_dict[e][f][2]] = 0

        for e in alt_num:
            if alt_num[e] == max(alt_num.values()):
                print("&emsp; - ", round(alt_num[e]/mod_varNbr*100, 2), "% d'alt&eacute;rations de type")
                if e[0] == '<':
                    print("&lt;" + e[1:-1] + "&gt")
                else:
                    print(e)
                print("soit", alt_num[e], "alt&eacute;rations (alt&eacute;ration la plus pr&eacute;sente). </br>")
                print(" </br>")

    print("""
                </fieldset></br>


                <fieldset style="background-color:#BDBDBD";>
                    <legend> <h2> R&eacute;sultats </h2> </legend>""")

    # Affichage final
    print("""
                        <table border="1" cellpadding="1" width="100%" bordercolor="grey" bgcolor="#E6E6E6"> 
                            <tr> 
                                <th width=2%> Ch </th>
                                <th width=5%> Position</th>
                                <th width=5%> Base de r&eacute;f&eacute;rence </th>
                                <th width=5%> Type de mutation </th>
                                <th width=3%> Qualit&eacute; </th> 
                                <th width=5%> Filtre </th> """)
    if info == "Oui":
        print("                 <th width=30%> Informations du document </th>")

    print("</tr>")
    for e in mod_dict:
        for f in mod_dict[e]:
            print(""" <tr align="center"> """)
            blu = mod_dict[e][f]
            print("<td>", e, "</td>")
            print("<td>", f, "</td>")
            print("<td>", blu[1], "</td>")
            if blu[2][0] == '<':
                print("<td> &lt;"+ blu[2][1:-1]+ "&gt; </td>")
            else:
                print("<td>", blu[2], "</td>")
            print("<td>", blu[3], "</td>")
            print("<td>", blu[4], "</td>")
            if info == "Oui":
                print("<td>", blu[5], "</td>")
            print("</tr>")

    print("</tr> </table>")
    print("""
                </fieldset></br>
	    </body>
    </html>""")
