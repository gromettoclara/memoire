# Mémoire M2 TNAH - 2024

Ce dépôt rassemble l'ensemble des livrables techniques et le mémoire réalisés dans le cadre de mon stage de M2 TNAH au sein de l'équipe d'histoire des sciences du laboratoire SYRTE de l'Observatoire de Paris, du 02/04/2024 au 31/07/2024.

# Objectif du stage

La plateforme AIKON -- anciennement EIDA -- est déjà dotée d’une chaîne de traitement partiellement automatisée qui intègre des fonctionnalités d’extraction et de recherche de similarités basés sur l'IA. Ces traitements permettent de repérer et de comparer des éléments visuels, en l’occurrence des diagrammes, au sein d’une base de données constituée d’images numérisées provenant de sources variées : institutions de conservation ou collections personnelles. La prochaine étape dans le développement de la plateforme consiste en l’implémentation de la fonctionnalité de vectorisation des diagrammes extraits, visant à affiner encorele niveau de structuration de l’information. Ce processus transforme une image en un ensemble de formes géométriques élémentaires, appelées primitives. Cette représentation, particulièrement adaptée au traitement informatique, permet de traduire les informations visuelles en structures mathématiques, facilitant ainsi leur manipulation, leur analyse etleur exploitation par des méthodes computationnelles.

Mon stage au sein de l’équipe d’histoire des sciences du laboratoire SYRTE (Systèmes de Référence Temps-Espace) de l’Observatoire de Paris a consisté à développer un module de vectorisation automatique dans la plateforme AIKON, tout en participant à une réflexion plus large sur l’architecture de cette plateforme. J'ai eu également l'occasion de participer au développement des interfaces, et de réfélchir aux exigences fonctionnelles d'un outil d'édition des diagrammes astronomiques au format SVG (output de l'algorithme de vectorisation). 

# Structure du dépôt

- memoire : Contient le code Latex du mémoire, [ici](memoire/main.pdf) un accès direct PDF. Les annexes consituent en soi des livrables techniques. 
- vectorization_module_api : Contient le code source du module `vectorization` développé pour l'API Discover-Demo, dont le code source intégral est disponible également [ici](https://github.com/Evarin/discover-demo).
- documentation : Contient la documentation technique ainsi que les présentations rédigées dans le cadre du stage.

# Livrables techniques 

1. Principaux :

- Module `vectorization` pour l'API Discover-Demo : L'intégralité du code se trouve [ici](vectorization_module_api).
- Module `vectorization` pour l'application AIKON : Une description des développements, accompagnée d'extraits de code, se trouve ici.
- Interfaces : Une description des développements, accompagnée de captures d'écran et d'extraits de code, se trouve [ici](dvt_interfaces.pdf).

3. Secondaires :

- Le cahier des charges pour l'implémentation de la vectorisation dans la plateforme AIKON (contenant aussi des réflecions concernant l'outil d'édition des fichiers SVG) se trouve [ici](documentation/cahier_des_charges.pdf). 
- Les slides du DH Seminar du 23 juillet 2024, centré autour de la question de l'exploitation de la vectorisation pour l'édition, se trouve [ici](documentation/slides_DH_seminar.pdf).
- Une documentation destinée aux chercheurs pour la prise en main des nouvelles interfaces se trouve [ici](documentation/doc_interfaces.pdf). 
