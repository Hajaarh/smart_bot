# Chatbot avec Streamlit et MistralAI
Ce projet consiste en une application web interactive de chatbot développée avec Streamlit et utilisant le modèle de langage large (LLM) de MistralAI. L'application permet aux utilisateurs d'interagir avec le chatbot en posant des questions et en recevant des réponses générées par le modèle Mistral.

# Fonctionnalités
Interface web simple et conviviale pour la saisie des questions.
Réponse instantanée générée par un modèle de langage basé sur MistralAI.
Historique des conversations conservé durant la session.
Utilisation sécurisée de l'API MistralAI avec gestion des clés API via les variables d'environnement.

# Interface du Chatbot
![Capture d'écran 2024-10-15 203503](https://github.com/user-attachments/assets/be4f9143-05cb-44f2-afbd-4a515adcf267)


# Installation

1. Cloner le dépôt
# Commencez par cloner ce dépôt sur votre machine locale :
git clone https://github.com/Hajaarh/smart_bot.git
cd smart_bot

2. Configurer un environnement virtuel
Il est recommandé de créer un environnement virtuel pour isoler les dépendances :
python -m venv venv
source venv/bin/activate  # Pour Linux/Mac
venv\Scripts\activate  # Pour Windows

3. Installer les dépendances
Les dépendances du projet sont spécifiées dans le fichier requirements.txt. Installez-les avec pip :
pip install -r requirements.txt

4. Configurer l'API MistralAI
Pour utiliser MistralAI, vous avez besoin d'une clé API. Voici comment configurer l'accès sécurisé à l'API :

# Créer un compte sur MistralAI : Rendez-vous sur MistralAI pour créer un compte et obtenir une clé API.

Configurer les variables d'environnement : Créez un fichier .env à la racine du projet et ajoutez-y votre clé API Mistral :
API_KEY=your_mistral_api_key_here
Charger les variables d'environnement : Le projet utilise la librairie python-dotenv pour charger automatiquement les variables d'environnement définies dans le fichier .env.

# Utilisation
Pour démarrer l'application, exécutez le fichier Python principal avec Streamlit :
streamlit run app.py
Cela ouvrira une fenêtre de navigateur avec l'interface du chatbot. Vous pouvez alors entrer vos questions dans l'interface et recevoir des réponses en temps réel.

# Dépendances
Voici les principales dépendances utilisées dans ce projet :

Streamlit : Pour créer une interface web interactive.
MistralAI SDK : Pour accéder au modèle de langage et générer des réponses.
Python-dotenv : Pour gérer les variables d'environnement, en particulier la clé API Mistral.
Pandas (si nécessaire) : Pour gérer les données structurées.
Toutes les dépendances sont listées dans requirements.txt. Elles seront installées automatiquement lorsque vous exécuterez pip install -r requirements.txt.

Fichier .env
Le fichier .env contient la clé API pour accéder à MistralAI. Ne partagez jamais ce fichier ou la clé API publiquement. Un exemple de fichier .env peut ressembler à ceci :
API_KEY=your_mistral_api_key_here


# Explication du Code
Voici une explication détaillée du fonctionnement du code principal :

1. Importation des bibliothèques :

streamlit pour l'interface web.
Mistral pour interagir avec l'API de MistralAI.
os et dotenv pour gérer les variables d'environnement.
2. Chargement de la clé API : Le fichier .env est chargé avec load_dotenv(), et la clé API est récupérée de manière sécurisée à l'aide de os.getenv("API_KEY").

3. Fonction generate_response() : Cette fonction prend en entrée le texte de l'utilisateur, envoie la requête au modèle MistralAI via l'API, et retourne la réponse générée par l'IA.


def generate_response(user_input):
    api_key = os.getenv("API_KEY")
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)
    chat_response = client.chat.complete(
        model = model,
        messages = [
            {
                "role": "user",
                "content": user_input,
            },
        ]
    )
    return chat_response.choices[0].message.content
    
# Gestion de l'interface Streamlit :

L'interface est créée avec st.title() et st.write().
Le texte saisi par l'utilisateur est récupéré à l'aide de st.text_input().
L'historique des conversations est stocké dans st.session_state.chat_history.

5. Affichage de l'historique : L'historique des conversations est affiché au fur et à mesure, avec une distinction visuelle entre les messages de l'utilisateur et ceux du bot.



# Problèmes connus
### Gestion des erreurs API :

- Actuellement, il n'y a pas de gestion sophistiquée des erreurs lorsque l'API échoue (par exemple, en cas d'absence de réponse, de clé API invalide ou de surcharge du serveur).
  
- Suggestion d'optimisation : Ajouter des exceptions personnalisées pour gérer les erreurs API (timeouts, erreurs de réseau, réponses inattendues) et afficher des messages d'erreur clairs à l'utilisateur. Utiliser des blocs try-except pour capturer et traiter ces erreurs.
Latence :

- Les réponses peuvent parfois être lentes en fonction des performances du serveur Mistral ou de la connexion réseau.
Suggestion d'optimisation : Mettre en place une file d'attente des requêtes ou implémenter une approche asynchrone (avec asyncio par exemple) pour rendre l'application plus réactive. Cela permettrait à l'utilisateur de continuer à interagir avec l'interface pendant que la réponse du serveur arrive.

- Absence de cache :
Chaque requête est envoyée au serveur sans aucune forme de mise en cache des réponses précédentes. Cela peut entraîner des appels redondants à l'API pour des questions similaires.
  
- Suggestion d'optimisation : Implémenter un système de cache en local (via une bibliothèque comme functools.lru_cache ou Redis) pour stocker temporairement les réponses fréquemment demandées et réduire les appels à l'API.
Limitation de la longueur des requêtes utilisateur :

- Si l'utilisateur envoie une question trop longue ou des entrées non structurées, cela pourrait poser problème avec l'API ou impacter la qualité de la réponse.

- Suggestion d'optimisation : Ajouter une validation d'entrée côté frontend pour limiter la longueur des questions ou prévenir les entrées non valides (ex. caractères spéciaux, trop d'espace, etc.).
Gestion de la charge serveur :

- Si plusieurs utilisateurs accèdent simultanément à l'application, cela pourrait surcharger l'API de Mistral et entraîner des retards ou des interruptions.
  
- Suggestion d'optimisation : Mettre en place un mécanisme de limitation du nombre de requêtes par utilisateur (ex. via un "rate-limiting") ou introduire des mécanismes de répartition de la charge côté backend pour éviter les surcharges.
Historique de conversation perdu à la déconnexion :

- L'historique des conversations est stocké uniquement en mémoire (dans st.session_state), ce qui signifie qu'il est perdu lorsque l'utilisateur ferme la page ou recharge l'application.

- Suggestion d'optimisation : Implémenter un mécanisme de persistance pour stocker l'historique des conversations dans une base de données légère (SQLite, par exemple) ou dans un fichier local. Cela permettrait de récupérer l'historique à la reconnection.
 
- Absence de personnalisation du modèle de réponse :
Actuellement, le modèle utilise une version générique de MistralAI, sans ajustement ni personnalisation en fonction du domaine ou du contexte utilisateur.

- Suggestion d'optimisation : Ajouter des options pour ajuster les paramètres du modèle (comme la température, la longueur des réponses, etc.) ou entraîner le modèle sur des données spécifiques au projet pour améliorer la pertinence des réponses.

- Absence d'accessibilité multilingue :
Le chatbot ne prend peut-être pas en charge plusieurs langues ou n'informe pas l'utilisateur si une langue non supportée est utilisée.

- Suggestion d'optimisation : Ajouter la détection de langue pour gérer les entrées multilingues ou avertir l'utilisateur si une langue non supportée est utilisée. Cela pourrait être couplé à des API de traduction automatique pour offrir une expérience multilingue plus fluide.
