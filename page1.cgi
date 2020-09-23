#!/usr/bin/env python3

print("""Content-type: text/html\n\n
	<head>
		<meta charset="utf-8" />
		<title> Interpr&eacute;teur de fichier vcf </title>
	</head>


	<body style="background-color:#E6E6E6;">

        <h1 align="center"> Interpr&eacute;teur de fichier vcf</h1>
        <h5 align="center"> D&eacute;velopp&eacute; par R&eacute;my Costa et Gautier Petitjean </h5></br>
        <form method="post" action="page2.cgi" enctype="multipart/form-data"> <!--Envoi du document vcf-->
		    <h3> Charger votre fichier (.vcf)</h3>
		        &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
                <input type="file" name="fi" value="Entrer votre fichier ici" accept=".vcf" required="require"/></br></br></br> 
                &emsp;&emsp;&emsp;
                <input type="submit" value="Soumettre la demande" />
		</form> </br></br></br>


        <i>    
            <div style="position:absolute; top: 400px; right: 30px;">	
                &emsp;
                <img src="https://media1.giphy.com/media/l3nWgXCpQpMUOrkoo/giphy.gif"  width="180" height="145" alt ="dna1" /> </br> 
                <center>  Site(s) op&eacute;rationnel(s) </center>
            </div>

            <fieldset style="background-color:#BDBDBD";>
                <legend> <h2> Aide </h2> </legend>
                    <h4> Plus d'informations sur les vcf compatibles </h4>    	           	
               	        &emsp;&emsp;&emsp;
                        <a href="http://www.internationalgenome.org/wiki/Analysis/vcf4.0/">Fichier vcf version 4.0</a></br> 
               	        &emsp;&emsp;&emsp;
                        <a href="https://samtools.github.io/hts-specs/VCFv4.1.pdf">Fichier vcf version 4.1</a></br> 
               	        &emsp;&emsp;&emsp;
                        <a href="https://samtools.github.io/hts-specs/VCFv4.2.pdf">Fichier vcf version 4.2</a></br> 
               	        &emsp;&emsp;&emsp;
                        <a href="https://samtools.github.io/hts-specs/VCFv4.3.pdf">Fichier vcf version 4.3</a></br></br>
            </fieldset>
        
            <div style="position:absolute; top: 660px; right: 30px;">	
                <center> Les champs suivis par * sont obligatoires </center>
            </div>
            
            <fieldset style="background-color:#BDBDBD";>
                <legend> <h2> Contacter les web-masters </h2> </legend>
            
                    <form action="mailto:gautier.petitjean@etu.umontpellier.fr", action="mailto:g=remy.costa@etu.umontpellier.fr" method="post" enctype="text/plain">
                        Votre nom* :
                        <input type="text" name="name" required="require"></br>
                        Votre adresse email* :
                        <input type="email" name="mail" required="require"></br>
                        Votre question ou commentaire* :
                        <input type="text" name="comment" size="50" required="require"></br></br>""")
                        
#<script src='https://www.google.com/recaptcha/api.js'></script>  // A venir après mise en ligne !
print("""
                        <input type="submit" value="Envoyer" ></br>
                    </form>
            </fieldset>
        </i>
        

	</body>
</html>""")
