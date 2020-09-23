import re

# Obtenir la version/format
def getFormat(myFile):
    for e in myFile:
        res = re.search("..fileformat=VCFv(.*)", e)
        if res :
            format = res.group(1)
            break # Arrête la boucle une fois le format trouvé
        else :
            format =  "<i> Non renseign&eacute </i>"
    return format

# Obtenir la date de publication
def getDate(myFile):
    for e in myFile:
        resDate = re.search("..fileDate=([0-9]{4})([0-9]{2})([0-9]{2})", e)
        if resDate :
            year = resDate.group(1)
            month = resDate.group(2)
            day = resDate.group(3)
            date = day + "/" + month + "/" + year
            break
        else :
            date = "<i> Non renseign&eacute </i>"
    return date

# Obtenir la source
def getSource(myFile):
    for e in myFile :
        resSource = re.search("..source=(.*)", e)
        if resSource:
            source = resSource.group(1)
            break
        else :
            source = "<i> Non renseign&eacute </i>"
    return source     

# Nombre de variation par chromosomes
def getVarNumber(dico):
    varNumList = []
    count = 0
    varNumber = 0
    for e in dico:
        count = 0
        for f in dico[e]:
            count += 1
            varNumber += 1
        varNumList.append((e, count))
    return varNumList, varNumber


# Obtenir ALT et FILTER
def getALFI(dico):
    alt_list = []
    alt_dict = {}
    fltr_list = []
    fltr_dict = {}
    for e in dico:
        for f in dico[e]:
            my_alt = dico[e][f][2]
            if my_alt not in alt_dict:
                alt_dict[my_alt] = ""
            my_fltr = dico[e][f][4]
            if my_fltr not in fltr_dict:
                fltr_dict[my_fltr] = ""
    for e in alt_dict:
        alt_list.append(e)
    for e in fltr_dict:
        fltr_list.append(e)

    return alt_list, fltr_list


# Affichage selectif
# dico[e][f][valeur] : 0-ID, 1-REF, 2-ALT, 3-QUAL, 4-FILTER, 5-INFO
def getSelection(dico, ch, ref, alt, qual, fltr):
    mod_dict = dico

    # Sélection du chromosome
    if ch != "All":
        del_list = []
        for e in mod_dict:
            if ch != e:
                del_list.append(e)
        for e in del_list:
            del mod_dict[e]
        
    # Sélection REF
    if ref != "All":
        del_ref = []
        for e in mod_dict:
            for f in mod_dict[e]:
                if mod_dict[e][f][1] != ref:
                    del_ref.append(f)
        for e in mod_dict:
            for d in del_ref:
                if d in mod_dict[e].keys():
                    del mod_dict[e][d]

    # Sélection ALT
    if alt != "All":
        del_alt = []
        for e in mod_dict:
            for f in mod_dict[e]:
                if mod_dict[e][f][2] != alt:
                    del_alt.append(f)
        for e in mod_dict:
            for d in del_alt:
                if d in mod_dict[e].keys():
                    del mod_dict[e][d]

    # Sélection QUAL
    if qual != "All":
        del_qual = []
        for e in mod_dict:
            for f in mod_dict[e]:
                if int(mod_dict[e][f][3]) < int(qual):
                    del_qual.append(f)
        for e in mod_dict:
            for d in del_qual:
                if d in mod_dict[e].keys():
                    del mod_dict[e][d]

    # Sélection FILTER
    if fltr != "." and fltr != "Aucun":
        del_fltr = []
        for e in mod_dict:
            for f in mod_dict[e]:
                if mod_dict[e][f][4] != fltr:
                    del_fltr.append(f)
        for e in mod_dict:
            for d in del_fltr:
                if d in mod_dict[e].keys():
                    del mod_dict[e][d]

    return mod_dict
