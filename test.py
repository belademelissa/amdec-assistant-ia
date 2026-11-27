import io

import pandas as pd
import streamlit as st

st.title("test MINI AMDEC sans IA")
st.write("Modifiez le tableau : la criticité se calcule toute seule dans le tableau resultat")

# Quelques lignes d'exemple 
donnees = pd.DataFrame({
    "Composant": ["Moteur de vantail", "Capteur de fin de course", "Courroie"],
    "Mode de défaillance": ["Ne démarre pas", "Information erronée", "Rupture"],
    "Effet": ["Vantail bloqué", "Fausse alarme de fermeture", "Vantail bloqué ouvert"],
    "Gravité": [3, 2, 3],
    "Occurrence": [2, 3, 1],
})

# Tableau DYNAMIQUE
tableau = st.data_editor(donnees, num_rows="dynamic")

 
tableau["Criticité"] = tableau["Gravité"] * tableau["Occurrence"]

st.subheader("Résultat")
st.dataframe(tableau)


# Bouton pour télécharger le tableau en Excel
fichier = io.BytesIO()
tableau.to_excel(fichier, index=False)
st.download_button("Télécharger en Excel", fichier.getvalue(), "amdec_test.xlsx")