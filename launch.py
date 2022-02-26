import time,os,requests

def requete(url):
    
    
    """
    PARAMETRES :
        url : str --> URL source de la requete vers l'API SNCF
    RETURN :
        Renvoie les variable suivantes sous forme d'un tuple :
            gare : str --> La gare où l'objet à été trouvé
            date : str --> La date où l'objet à été trouvé
            objet : str --> Le nom de l'objet
            nature : str --> La nature de l'objet
        """
    elements=[]
    
    req=requests.get(url)
    req=req.text
    
    req=req.split("},")
    

    
    req_content = req[1].split(",")
    for i in range(len(req_content)):
        
        element=req_content[i].split(": ")
        elements.append(element)

    for i in range(len(elements)):
        
        for j in range(len(elements[i])):
            if elements[i][j] == ' "gc_obo_gare_origine_r_name"' :
                gare=elements[i][1]
            elif ' "gc_obo_nature_c"' in elements[i]:
                nature=elements[i][1]
            elif ' "date"' in elements[i]:
                date=elements[i][1]
            elif ' "gc_obo_type_c"' in elements[i]:
                objet=elements[i][1]

        

    return date,gare,objet,nature

url="https://ressources.data.sncf.com/api/records/1.0/search/?dataset=objets-trouves-restitution&q=&lang=fr&sort=date&facet=date&facet=gc_obo_date_heure_restitution_c&facet=gc_obo_gare_origine_r_name&facet=gc_obo_nature_c&facet=gc_obo_type_c&facet=gc_obo_nom_recordtype_sc_c"
i=1
while True :
    print(i)
    resultat1=requete(url)
    time.sleep(900)
    resultat2=requete(url)
    if resultat2!=resultat1:
        print("Un nouvel objet vient d'etre trouvé\n",resultat2)
        os.system("python3 projet.py")
    else :
        print("Aucun nouvel objet trouvé")
        print("Dernier objet :",resultat2)

    i+=1
    