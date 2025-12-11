# ===============================
# APP STREAMLIT POUR L'ANALYSE DU DATASET CREDITCARD
# ===============================

# Importation des librairies nécessaires
import streamlit as st          # Framework pour créer des applications web interactives
import pandas as pd             # Manipulation des données
import matplotlib.pyplot as plt # Graphiques (utilisé avec Streamlit)
import seaborn as sns           # Graphiques statistiques

# Configuration du style Seaborn
sns.set(style="whitegrid")

# -------------------------------
# Fonction pour charger les données (avec cache)
# -------------------------------
@st.cache_data   # Permet de ne pas recharger le fichier à chaque fois (optimise les performances)
def load_data():
    # Lecture du fichier CSV contenant les transactions
    df = pd.read_csv("creditcard.csv")
    return df

# Chargement du dataset
df = load_data()

# -------------------------------
# Mise en page de l'application
# -------------------------------

# Titre principal de l'application
st.title("💳 Détection de fraude - Analyse exploratoire (Credit Card Fraud Dataset)")

# Petit texte d'introduction
st.markdown("""
Cette application Streamlit permet d'explorer le jeu de données de transactions bancaires anonymisées,
utilisé pour la détection de fraude.  
Les visualisations sont basées sur les variables **Time**, **Amount**, et les composantes PCA **V1 à V28**.
""")

# -------------------------------
# Barre latérale (sidebar) pour la navigation
# -------------------------------
st.sidebar.title("Navigation")

# Menu pour choisir la section à afficher
page = st.sidebar.selectbox(
    "Choisir une section :",
    [
        "📁 Aperçu du dataset",
        "📊 Répartition de la variable Class",
        "💰 Distribution du montant (Amount)",
        "⏱️ Analyse temporelle (Time / Hour)",
    ]
)

# ===============================
# PAGE 1 : Aperçu du dataset
# ===============================
if page == "📁 Aperçu du dataset":
    st.header("📁 Aperçu du dataset")

    # Affichage des dimensions
    st.write(f"**Nombre de lignes :** {df.shape[0]}")
    st.write(f"**Nombre de colonnes :** {df.shape[1]}")

    # Aperçu des premières lignes
    st.subheader("Aperçu des premières lignes")
    st.dataframe(df.head())

    # Informations sur les valeurs manquantes
    st.subheader("Valeurs manquantes")
    st.write(df.isna().sum())

    # Informations sur les doublons
    st.subheader("Lignes dupliquées")
    st.write(f"Nombre de lignes dupliquées : **{df.duplicated().sum()}**")

    # Infos sur les types de données
    st.subheader("Types de données")
    st.write(df.dtypes)

# ===============================
# PAGE 2 : Répartition de la variable Class
# ===============================
elif page == "📊 Répartition de la variable Class":
    st.header("📊 Répartition de la variable cible : Class")

    st.markdown("""
La variable **Class** indique :  
- `0` : transaction normale  
- `1` : transaction frauduleuse  
    """)

    # Comptage des classes
    class_counts = df["Class"].value_counts()
    class_percent = df["Class"].value_counts(normalize=True) * 100

    # Affichage tableau
    st.subheader("Tableau des fréquences")
    st.write(pd.DataFrame({
        "Nombre": class_counts,
        "Pourcentage (%)": class_percent.round(4)
    }))

    # Graphique : barplot de la variable Class
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x=class_counts.index, y=class_counts.values, ax=ax)
    ax.set_title("Répartition des classes (0 = normal, 1 = fraude)")
    ax.set_xlabel("Classe")
    ax.set_ylabel("Nombre de transactions")
    st.pyplot(fig)

    st.markdown("""
On observe un **fort déséquilibre** : la classe 1 (fraude) est extrêmement minoritaire
par rapport à la classe 0.  
Ce déséquilibre est un point central à prendre en compte pour l'entraînement des modèles.
""")

# ===============================
# PAGE 3 : Distribution du montant (Amount)
# ===============================
elif page == "💰 Distribution du montant (Amount)":
    st.header("💰 Distribution de la variable Amount")

    st.markdown("""
La variable **Amount** représente le montant de la transaction (en unités monétaires).  
Sa distribution est très asymétrique, avec beaucoup de petites transactions et quelques montants très élevés.
""")

    # Slider pour choisir un maximum de montant (zoom)
    max_amount = st.slider(
        "Choisir le montant maximal à afficher (zoom) :",
        min_value=10.0,
        max_value=float(df["Amount"].max()),
        value=500.0,
        step=10.0
    )

    # Filtrage du dataset en fonction du slider
    df_filtered = df[df["Amount"] <= max_amount]

    st.write(f"Nombre de transactions affichées : {df_filtered.shape[0]}")

    # Histogramme avec KDE
    fig, ax = plt.subplots(figsize=(10,4))
    sns.histplot(df_filtered["Amount"], bins=100, kde=True, ax=ax)
    ax.set_title(f"Distribution des montants (Amount ≤ {max_amount})")
    ax.set_xlabel("Montant")
    ax.set_ylabel("Nombre de transactions")
    st.pyplot(fig)

    st.markdown("""
On remarque une concentration très forte des montants vers les petites valeurs.
En augmentant ou réduisant le **slider**, on peut explorer plus finement la répartition des montants.
""")

# ===============================
# PAGE 4 : Analyse temporelle (Time / Hour)
# ===============================
elif page == "⏱️ Analyse temporelle (Time / Hour)":
    st.header("⏱️ Analyse temporelle des transactions")

    st.markdown("""
La variable **Time** représente le nombre de secondes écoulées depuis la première transaction du dataset.  
Pour simplifier l'interprétation, on peut convertir ce temps en **heures**.
""")

    # Création d'une colonne Hour si elle n'existe pas déjà
    if "Hour" not in df.columns:
        df["Hour"] = (df["Time"] // 3600).astype(int)

    # Affichage d'un countplot des transactions par heure
    fig, ax = plt.subplots(figsize=(10,4))
    sns.countplot(x="Hour", data=df, ax=ax)
    ax.set_title("Nombre de transactions par heure (0 à 47)")
    ax.set_xlabel("Heure (à partir du début de l'enregistrement)")
    ax.set_ylabel("Nombre de transactions")
    st.pyplot(fig)

    st.markdown("""
On observe des **pics d'activité** à certaines heures de la journée et des périodes plus calmes,
ce qui reflète un comportement temporel typique des utilisateurs (moins d'activité la nuit, par exemple).
""")
