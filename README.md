Travail réalisé par,
Nguiffo Gilles Roy NGUG22060400
Meijomo Hillary Alexandra MEJM28530300

1. Description du projet

Ce mini-projet a pour objectif de réaliser une analyse exploratoire de données (EDA) du jeu de données Credit Card Fraud Detection, qui contient 284 807 transactions bancaires anonymisées, dont une faible proportion de fraudes.

Les principaux objectifs du projet sont :

Examiner la structure du dataset

Effectuer une analyse univariée et bivariée des variables

Explorer les corrélations

Identifier les patterns potentiels associés à la fraude

Produire des visualisations Matplotlib, Seaborn et Plotly

Fournir une interface Streamlit permettant d’explorer les données de manière interactive

Aucun modèle de machine learning n’était requis, mais un notebook supplémentaire (optionnel) explore un modèle Random Forest pour enrichir l’analyse

2. Contenu du dépôt

MINI PROJECT/
│
├── 02_univarie.ipynb                   → Analyse univariée (Amount, Time, V1–V28, Class)
├── 03_bivariate_analysis.ipynb         → Analyse bivariée et corrélations
├── 04_modelisation_random_forest.ipynb → (Optionnel) Modélisation Random Forest + SMOTE
├── app.py                              → Application Streamlit (visualisations interactives)
├── creditcard.csv                      → Dataset complet
├── README.md                           → Ce fichier
└── MiniProjet.pdf                      → Rapport synthèse (2 pages)

3. Visualisations produites

Dans les notebooks :

Histogrammes (Matplotlib & Seaborn)

KDE plots

Boxplots

Heatmap de corrélation

Graphiques interactifs Plotly

Comptage de classes (Class)

Transformations temporelles (Hour)

Dans Streamlit :

Aperçu du dataset

Distribution de la variable Amount (zoomable via slider)

Répartition des classes

Analyse temporelle Time → Hour

 4. Instructions pour exécuter les notebooks

 Ouvrir les notebooks dans Jupyter, VS Code, ou Google Colab :

 jupyter notebook


Les notebooks doivent fonctionner tels quels, car ils utilisent uniquement :

pandas

numpy

seaborn

matplotlib

plotly

5. Lancer l’application Streamlit
1️ Installer Streamlit (si pas encore installé)

pip install streamlit
2.Accéder au dossier contenant app.py

Exemple :
cd "MINI PROJECT"

Lancer l’application

streamlit run app.py

6. Dépendances

Voici les principales bibliothèques utilisées :

pandas
numpy
matplotlib
seaborn
plotly
streamlit
scikit-learn
imbalanced-learn   (optionnel, seulement pour le notebook de modélisation)


7. Notes sur le notebook de modélisation

Le fichier :

04_modelisation_random_forest.ipynb


n’est pas requis par les consignes du projet, mais il est inclus comme analyse complémentaire.
Il contient :

Prétraitement (scaling, train-test split)

Gestion du déséquilibre via SMOTE

Modèle Random Forest

Classification report

Matrice de confusion

ROC-AUC

Importance des variables

Cette section montre comment l’EDA peut être exploitée pour entraîner un modèle performant.


