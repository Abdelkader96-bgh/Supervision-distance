Projet que j'ai réalisé durant mon PFE au Maroc à l'entreprise OCP :
le projet permet de surveiller la variation d'acide en temps réel  via une inetrface web  qui permet de visuliser la variation d'acide via un graphe chart.js , puis envoyé des sms et des emails aux responsables s'il y'a un changement grave au niveau de la variation d'accide .

le projet est dévisé en 3 parties :
1/ Code Arduino :
permet de lire le signal généré par le capteur de la variation d'acide en le transférer en signal numérique .

2/ Code Raspberry Pi 3b+ :

1/permet de lire des données via le port série entre Arduino et Raspberry pi .
2/ traiter les données pour les recevoirs chaque second .
3/ création de la base de donnée Mysql et stocké les données en temps réel ( Python) 
4/ envoyer les résultat par mail et sms aux responsable en utilisnat la bibliothèque smtplib python 

4/ création d'une interface web HTML/CSS/JS/PHP
pour visualiser la variation d'acide chaque second via un graphe chart.js 
