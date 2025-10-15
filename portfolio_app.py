import streamlit as st
from PIL import Image

# --- CONFIGURATION DE LA PAGE ---
# titre de l'onglet, l'icône et la mise en page.
st.set_page_config(
    page_title="Williams Ouattara | Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# --- CHARGEMENT DES RESSOURCES ---
# IMPORTANT : Renommez la photo en "profile_pic.jpeg" .
try:
    profile_pic = Image.open("profile_pic.jpeg")
except FileNotFoundError:
    # Image de substitution si le fichier n'est pas trouvé
    profile_pic = Image.new('RGB', (160, 160), color = (233, 233, 233))


# --- SECTION D'EN-TÊTE ---
# Utilise les colonnes pour organiser l'affichage
col1, col2 = st.columns([1, 2.5], gap="small")
with col1:
    st.image(profile_pic, width=160)

with col2:
    st.title("Williams Ouattara")
    st.subheader("Manager en Transformation Digitale | Profil Hybride Data & Business")
    st.write(
        """
        Je fais le pont entre la performance business et la technologie. 
        Je transforme les données en décisions rentables et les risques en opportunités de sécurisation.
        """
    )
    # Pensez à mettre le lien vers le PDF de votre CV (hébergé sur Google Drive, Dropbox, etc.)
    st.link_button("📄 Télécharger mon CV", "https://drive.google.com/file/d/1de9P9iLuXom91IjDidsWgapamCN-XzrU/view?usp=share_link")


# --- MON PROJET ---
st.write("---")
st.header("Mon Projet : Devenir un Traducteur de la Donnée")
st.write(
    """
    Mon parcours de manager chez KFC m'a appris une chose essentielle : la performance se pilote par les chiffres. Chaque jour, mon rôle était de transformer des données brutes (ventes, coûts, stocks) en décisions qui avaient un impact direct sur notre rentabilité.

    Cette expérience a confirmé ma vocation : je veux utiliser la data pour aider les entreprises à prendre de meilleures décisions et à se sécuriser. C'est pourquoi j'ai intégré un **MBA en Innovation & Tech**. Mon but est de devenir un manager "hybride", capable de comprendre les enjeux business et de dialoguer avec les experts techniques pour piloter des projets complexes, que ce soit en **Analyse de Données** ou en **Cybersécurité**.
    """
)

# --- COMPÉTENCES ---
st.write("---")
st.header("Mes Compétences")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Business & Management")
    st.markdown(
        """
        - ✓ Gestion de Projet (Agile, Scrum)
        - ✓ Analyse de Performance (KPIs)
        - ✓ Optimisation de Processus
        - ✓ Stratégie Commerciale & Marketing
        - ✓ Analyse de Rentabilité (COS/COL)
        - ✓ Pilotage RH & Contrôle de Gestion Sociale
        """
    )
with col2:
    st.subheader("Data & Analyse")
    st.markdown(
        """
        - ✓ Analyse de Données (SQL, Python)
        - ✓ Data Visualisation (Power BI)
        - ✓ Nettoyage et Préparation (ETL)
        - ✓ Analyse Statistique
        - ✓ Reporting & Dashboarding
        - ✓ CRM & Gestion de la Donnée Client
        """
    )
with col3:
    st.subheader("Cybersécurité (Pilotage)")
    st.markdown(
        """
        - ✓ Gouvernance, Risque, Conformité (GRC)
        - ✓ Audit & Analyse de Risques
        - ✓ Gestion des Incidents (Pilotage)
        - ✓ Sensibilisation & Accompagnement
        - ✓ Protection des Données (RGPD)
        - ✓ Gestion des Identités (IAM)
        """
    )

# --- PROJETS CONCRETS ---
st.write("---")
st.header("Mes Projets Concrets")
st.write("Voici quelques exemples de projets que je développe pour mettre en pratique mes compétences.")

# Projet 1
st.subheader("1. Analyse de la Performance d'un Restaurant (Python & SQL)")
st.write(
    """
    **Objectif :** Simuler une analyse de rentabilité (COS/COL) à partir de données de ventes et de stocks pour identifier des leviers d'optimisation.
    
    **Démarche :**
    1.  Création d'une base de données de test avec des tables (ventes, produits, stocks).
    2.  Écriture de **requêtes SQL** pour agréger les données et calculer les indicateurs clés.
    3.  Utilisation de la **librairie Python `pandas`** pour analyser les résultats, identifier les écarts et les tendances.
    4.  Visualisation des résultats avec **`matplotlib`** pour créer des graphiques clairs et actionnables.
    """
)
# Vous pourrez ajouter un lien vers votre code sur GitHub ici.
st.link_button("Voir le code sur GitHub", "#")


# Projet 2
st.subheader("2. Dashboard de Suivi Commercial (Power BI)")
st.write(
    """
    **Objectif :** Concevoir un tableau de bord interactif sur Power BI pour suivre les KPI de vente d'un portefeuille de produits fictif.
    
    **Démarche :**
    1.  Connexion à une source de données (fichier Excel ou base de données SQL).
    2.  **Nettoyage et transformation des données** avec Power Query.
    3.  **Modélisation des données** et création de mesures DAX pour les calculs.
    4.  Création de **visualisations interactives** (graphiques, cartes, filtres) pour permettre une exploration intuitive des résultats par un manager.
    """
)
# Vous pourrez ajouter un lien vers le rapport public Power BI ici.
st.link_button("Voir le Dashboard en ligne", "#")

# --- CONTACT ---
st.write("---")
st.header("Contact")
st.write(
    """
    Je suis à la recherche d'une alternance de 24 mois à partir de Septembre 2025.
    N'hésitez pas à me contacter pour échanger sur vos projets.
    """
)
st.write("📧 williamsouattara@gmail.com")
st.write("📞 06 51 77 99 46")
