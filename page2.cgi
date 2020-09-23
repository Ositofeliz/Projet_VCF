#!/usr/bin/env python3

import cgi, cgitb
import re, os
#import matplotlib.pyplot as plt
from vcf_functions import *

cgitb.enable()

dico = cgi.FieldStorage()                                                   #le fichier chargé depuis la page1.cgi est stocké dans un formulaire
fd = dico.getvalue("fi").decode('utf-8')                                    #à partir de ce formulaire, on extrait le fichier chargé

if not fd:                                                                  #s'il n'y a pas de fichier, on affiche une page différente de la page des résultats
    print("""Content-type: text/html\n\n
            <head>
                <meta charset="utf-8" />
                <title> R&eacute;sultats du fichier vcf </title>
            </head>
            
            <body style="background-color:#E6E6E6;"></br>
                <i>Le fichier est vide</i>
	        </body>
        </html>""")

else:                                                                       #si non, on affiche la page des résultats
    myFile = fd.split("\n")                                                 #le fichier est compiler en ligne, en le séparant au niveau des tabulations, on obtient le fichier de départ de l'utilisateur


    # Déclarations
    dicoChrom = {}
    dicoRef = {}
    dicoBox = {}
    varNum_list = []
    alt_list = []
    fltr_List =[]

           
    for e in myFile:
        resLine = re.search("^\w", e) 
        if resLine :                                                        #si la ligne est sans #
            line = e.split("\t")                                            #séparation au niveau des tabulations
            list = [line[2], line[3],line[4],line[5],line[6],line[7]]       #création d'une liste avec le reste des éléments
            if line[0] in dicoChrom:                                        #si il y a un numéro de chrom : ajout à dicoChrom
                dicoChrom[line[0]][line[1]]= []                             #création un dictionnaire de listes
                for i in list:                                              #pour chaque éléments dans la liste list
                    dicoChrom[line[0]][line[1]].append(i)                   #on les ajoute à la liste 
            else :
                dicoChrom[line[0]] = {}                                     #s'il n'y a pas de dico de numéro de chromosome, on le crée



    varNum_list, var_nbr = getVarNumber(dicoChrom)

    alt_list, fltr_list = getALFI(dicoChrom)
  
    format = getFormat(myFile)
                    
    print("""Content-type: text/html\n\n
        <head>
            <meta charset="utf-8" />
            <title> R&eacute;sultats du fichier vcf </title>
        </head>
    
    
        <body style="background-color:#E6E6E6;"></br>
        
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
            </div> """)
            
    if format != "4.0" and format != "4.1" and format != "4.2" and format != "4.3":
        print("""</br></br></br></br></br>
                    <i>Le fichier n'a pas pu &ecirc;tre analys&eacute; </br>
                        Reportez-vous aux versions vcf compatibles sur la page pr&eacute;c&eacute;dente</i>
	            </body>
            </html>""")
            
    else:        
        print("""<h1 align="center"> Fichier analys&eacute; avec succ&egrave;s </h1></br></br></br>

        
                <table border="1" cellpadding="10" width="100%" bordercolor="grey"> <!--Taille de bordure du tableau -- Hauteur de colone -- Largeur du tableau -- Couleur de la colone gauche--> 
                    <caption>Tableau de r&eacute;sultats</caption> </br>
                        <tr>
                            <th bgcolor="#BDBDBD" width="20%" align="left"> Format vcf</th> <!--Couleur de fond -- Largeur colone de gauche--> 
                            <td> """)
        print(format, """ </td>
                        </tr>
                        
                        <tr>
                            <th bgcolor="#BDBDBD" width="20%" align="left"> Date</th>
                            <td> """)
        print(getDate(myFile), """ </td>
                        </tr>
                        
                        <tr>
                            <th bgcolor="#BDBDBD" width="20%" align="left"> Source</th>
                            <td> """)
        print(getSource(myFile), """ </td>
                        </tr>
        
                        <tr>
                            <th bgcolor="#BDBDBD" width="20%" align="left"> Nombre de variations par chromosomes </br></br>
                            &emsp;
                            <font size="2"> (Pourcentage de variations)</font> </th> <!--Taille de texte-->""")
        
        if not varNum_list:                                                     #s'il n'y a pas de ligne de résultat, on le signal
            print(""" <td> <i>Pas de ligne de r&eacute;sultat &agrave traiter</i></td>
                                </tr>
                            </table>
                        </body>
                    </html>""")
        else:                                                                   #si non, on affiche les résultats et les options de recherche avancée
            print("""
                        
                            <td>
                                <table> """)
            i=0
            count = 0
            countv = 0
            for e in varNum_list:
                i+=1
                print("<td> Ch.", e[0], "-", e[1], "(", round(e[1]/var_nbr*100, 2), "%) &emsp;</td>")
                count += e[1]/var_nbr*100
                countv += e[1]
                if i%5==0:
                    print("<tr></tr>")
            print("</table> </br>")
            print("Nombre de variations total :", countv, "</br>")
            print("Pourcentage total : ", round(count, 2 ), "%", """  
                                            </td>
                                        </tr>
                                    </table>

                            <fieldset style="background-color:#BDBDBD";>
                                <legend> <h2> Options de recherches avanc&eacute;es </h2> </legend>
        	                        <form method="post" action="page3.cgi" enctype="multipart/form-data">
        	                            &emsp;&emsp;&emsp;
                                        Chromosome
                		                    <select name="chrom"> 
                                                <option> All </option>""")
            for e in dicoChrom:
                print("<option>", e, "</option>")
            print("""                       </select></br>
                                        &emsp;&emsp;&emsp;
                                        Base de r&eacute;f&eacute;rence
                                            <select name="base">
                                                <option> All </option>
                                                <option> A </option>
                                                <option> T </option>
                                                <option> C </option>
                                                <option> G </option>
                                            </select></br>
                		                &emsp;&emsp;&emsp;
                                        Type de mutation
                		                    <select name="mutation">
                		                        <option> All </option>""")
            for e in alt_list:
                if e[0] == '<':
                    print("<option> &lt;"+ e[1:-1]+ "&gt; </option>")
                else :
                    print("<option>", e, "</option>")
            print("""                       </select></br>
	                                    &emsp;&emsp;&emsp;
                                        Qualit&eacute; minimale
        	            	                <input name="value" placeholder="Entrer une valeur" /> </br>
        	                            &emsp;&emsp;&emsp;
                                        Filtre
                		                    <select name="filtre">   
                                                <option> Aucun </option>""")
            for e in fltr_list:
                print("<option>", e, "</option>")
            print("""                       </select></br>
	                        
	                                    &emsp;&emsp;&emsp;
                                        Informations du document
                                            <select name="infos">
                                                <option> Oui </option>
                                                <option> Non </option>
                                            </select> 
                           
                                        <center></br> 
                                            <input type="file" name="fl" value="Entrer votre fichier ici" accept=".vcf" required="require"/> </br></br>
                                            <input type="submit" value="R&eacute;sultat de la recherche" />   
                                        </center>
        
	                                </form>         
        
                            </fieldset> </br>
        
	            </body>
            </html>""")
