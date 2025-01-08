Développement d'un Chatbot IA interactif
Projet CRM eCommerce : Analyse et Visualisation de données avec MongoDB, FastAPI et Streamlit
Ce projet consiste en la création d'une application web interactive permettant une conversation naturelle avec les utilisateurs, utilisant Streamlit pour l'interface utilisateur et Mistral AI pour les capacités conversationnelles. L'application est conçue pour être intuitive, sécurisée, et facilement extensible.

Table des matières
Structure de l'application
Fonctionnalités principales
Prérequis
Étapes d'installation et de configuration
Cloner le projet
Configurer un environnement Python
Configurer l'API Mistral AI
Lancer le projet
Structure du projet
Dépendances
Résumé des commandes
Structure de l'application
1. Backend
Développé en Python.
Communique avec l'API de Mistral AI pour générer des réponses conversationnelles.
Intègre la gestion sécurisée des clés API via la bibliothèque dotenv.
2. Frontend
Conçu avec Streamlit pour une interface utilisateur simple et intuitive.
Affiche l'historique des conversations et gère les interactions en temps réel.
Fonctionnalités principales
Conversation naturelle :

Les utilisateurs posent des questions et reçoivent des réponses instantanées grâce à Mistral AI.
Gestion de l'historique des conversations :

Les échanges sont affichés dans un format clair et conservés pendant la session.
Sécurité des clés API :

Les informations sensibles, comme la clé API, sont gérées via des variables d'environnement.
Interface web conviviale :

Créée avec Streamlit, elle offre une interaction fluide et intuitive.
Prérequis
Avant de commencer, assurez-vous d’avoir :

Python 3.8+ installé.
Une clé API Mistral AI (disponible après inscription sur leur plateforme).
Une connexion internet pour installer les dépendances et accéder à l'API.
Étapes d'installation et de configuration
1. Cloner le projet
Téléchargez le projet depuis GitHub :

bash
Copier le code
git clone https://github.com/Hajaarh/smart_bot.git
cd smart_bot
2. Configurer un environnement Python
Créer un environnement virtuel :
bash
Copier le code
python -m venv venv
Activer l’environnement virtuel :
Sur Windows :
bash
Copier le code
venv\Scripts\activate
Sur macOS/Linux :
bash
Copier le code
source venv/bin/activate
Installer les dépendances :
bash
Copier le code
pip install -r requirements.txt
Cela installera toutes les bibliothèques nécessaires, comme Streamlit, Mistral AI SDK, et dotenv.
3. Configurer l'API Mistral AI
3.1 Obtenir une clé API
Créez un compte sur la plateforme Mistral AI.
Récupérez votre clé API depuis votre tableau de bord utilisateur.
3.2 Configurer les variables d’environnement
À la racine du projet, créez un fichier .env contenant la clé API :
plaintext
Copier le code
API_KEY=your_mistral_api_key_here
L’application chargera automatiquement cette clé grâce à la bibliothèque python-dotenv.
4. Lancer le projet
4.1 Exécuter l'application avec Streamlit
Assurez-vous que l'environnement virtuel est activé.
Lancez l'application avec la commande suivante :
bash
Copier le code
streamlit run app.py
Une fenêtre s’ouvrira automatiquement dans votre navigateur à l'adresse suivante :
http://localhost:8501.
Structure du projet
app.py : Code principal pour l'application Streamlit.
requirements.txt : Liste des dépendances nécessaires pour exécuter le projet.
.env : Fichier contenant la clé API (à configurer par l'utilisateur).
data/ (optionnel) : Dossier pour stocker d'éventuelles données additionnelles.
README.md : Documentation détaillée du projet.
Dépendances
Les principales dépendances utilisées dans ce projet sont :

Streamlit : Pour créer une interface web interactive.
Mistral AI SDK : Pour accéder aux capacités conversationnelles.
Python-dotenv : Pour gérer les variables d'environnement.
Pandas (optionnel) : Pour manipuler des données structurées.
Toutes les dépendances sont listées dans requirements.txt. Installez-les avec :

bash
Copier le code
pip install -r requirements.txt
Résumé des commandes
Cloner le projet :

bash
Copier le code
git clone https://github.com/Hajaarh/smart_bot.git
cd smart_bot
Créer et activer un environnement virtuel :

bash
Copier le code
python -m venv venv
source venv/bin/activate  # Sur macOS/Linux
venv\Scripts\activate     # Sur Windows
Installer les dépendances :

bash
Copier le code
pip install -r requirements.txt
Configurer l'API Mistral AI :

Créez un fichier .env avec votre clé API.
Lancer l'application Streamlit :

bash
Copier le code
streamlit run app.py
Résultats obtenus
Création d'une application web interactive pour une conversation fluide avec les utilisateurs.
Intégration réussie des technologies Streamlit et Mistral AI.
Gestion sécurisée des clés API via dotenv.
Amélioration des compétences en développement backend et en intégration IA.
