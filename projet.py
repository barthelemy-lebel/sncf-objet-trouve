import tweepy
import requests

def replace_caractere(variable):
    variable=variable.replace("/u00e0","à")
    variable = variable.replace("\u00e9","é")
    variable = variable.replace('"',"")


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


API_KEY = "4z46hvPEx60NKZQkEsxDMPh8S"
API_SECRET = "66LLwmNGaCu7BC26lxX4dGjxnU4IrimUjNQpkboKZh7VRJ38tC"

ACCESS_TOKEN = "1486752003179126787-o5ZBWTywbSwND7ru8S6M44uvzaPQrW"
ACCESS_TOKEN_SECRET = "tNKsbhNeTcR5gyNgENWaaTgAnjf8kc9VOR9wzNiKUphob"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

requete_sncf=requete(url)

date=requete_sncf[0]
gare=requete_sncf[1]
objet=requete_sncf[2]
nature=requete_sncf[3]

#réencoder les caractères
replace_caractere(gare)
replace_caractere(date)
replace_caractere(objet)
replace_caractere(nature)

tweet="""[IMPORTANT]
Nous avons retrouvé {0} de type {1} à la gare de {2} le {3}.""".format(objet,nature,gare,date)

api.update_status(tweet)

