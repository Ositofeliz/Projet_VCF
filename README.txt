    
Nous vous remercions d'avoir choisi notre logiciel pour vos traitements de fichiers vcf.
Nous vous tiendrons informé des nouveaux dispositifs et améliorations proposés.



Conditions de confidentialité

    Notre logiciel est soumis à des droits d'auteur, ne pas partager la licence.


Conditions d'utilisation

    Compatible avec tout système GNU/Linux de distribution apparu à partir de 2014.
    En aucun cas notre entreprise pourra être tenu pour responsable.
    Ne pas revendre ce logiciel.
    En choisissant d'utiliser Python3.6 vos résultats d'analyses seront dans l'ordre croissant et/ou alphabétique.
    Ne convient pas aux enfants de moins de 7 ans.


Service client

    Si vous relevez des anomalies ou des bugs dans le logiciel, merci de prendre contact avec notre service client. 
    Co-Responsables :  Costa Remy (remy.costa@etu.umontpellier.fr) - Gautier Petitjean (gautier.petitjean@etu.umontpellier.fr).
    Nous vous répondrons dans les plus brefs délais.
    Merci de votre confiance





Question biologique

    Dans cette étude nous permettons à nos utilisateurs de pouvoir connaître comment se répartissent les mutations dans le génome qu'ils étudient.


Installation

    Déplacer l'ensemble des documents dans votre dossier de partage.
    
    Sous Xubuntu
        /public_HTML 
        Ouvrez votre terminal (Ctrl+Alt+T) à l'intérieur du dossier.
        Effectuer un chmod +x (nomdufichier.sonextension) pour chacun des documents.
        
    Sous Ubuntu
        /usr/lib/cgi-bin
        Dans le cas où le dossier cgi-bin n'existe pas, créez le puis ouvrez votre terminal (Ctrl+Alt+T) à l'intérieur du dossier /cgi-bin.
        Effectuer un chmod +x (nomdufichier.sonextension) pour chacun des documents.
            
    Installer la dernière version de Python3.6 (selon http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/)
        Dans un terminal, entrer cette ligne de commande :
            sudo add-apt-repository ppa:jonathonf/python-3.6
        Ensuite, vérifier les mises à jour disponibles avec ces deux lignes à lancer l'une après l'autre :
            sudo apt-get update
            sudo apt-get install python3.6
        Puis, créer les alternatives d'utilisation entre les différentes version de Python :
            sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
            sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
        Enfin, choisir la version de Python3.6 :
            sudo update-alternatives --config python3
            Entrer le numéro qui s'affichera dans la colone Selection en fonction de votre choix.
        Répéter cette dernière étape si vous souhaitez changer de version.
            
            
Utilisation des fichiers

    Dans le navigateur, entrer l'adresse :
        http://localhost/cgi-bin/page1.cgi


Politique d'amélioration :

    Nous utiliserons le language css dans nos futurs distributions qui reste difficile à utiliser avec cgi.
    Ajouter une balise de vérification recaptcha en collaboration avec Google.
    Créer une boite mail
    Améliorer les options de recherche avancée :
        Permettre de sélectionner plusieurs options à la fois
        Trier les informations du document différemment (en sous partie)
        Afficher le chromosome avec la localisation des mutations en fonction de la recherche
        Etendre les fonctionnalités d'analyses à toutes les fonctions vcf non compatibles 
        Supprimer l'étape de rechargement du fichier en page2.cgi en améliorant le transfert entre pages

