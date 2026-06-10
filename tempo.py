import streamlit as st

# Dati della linea del tempo
STORIA_DATI = [
    {"anno": "776 a.C.", "evento": "Prime Olimpiadi", "dettaglio": "I primi giochi olimpici registrati a Olimpia, dedicati a Zeus. Segnano l'inizio della cronologia ufficiale greca."},
    {"anno": "733 a.C.", "evento": "Fondazione di Siracusa", "dettaglio": "I coloni di Corinto sbarcano in Sicilia e fondano quella che diventerà una delle póleis più ricche e potenti del Mediterraneo."},
    {"anno": "VII sec a.C.", "evento": "Nascita della Moneta", "dettaglio": "In Lidia e nelle póleis della Ionia si inizia a battere moneta, rivoluzionando i commerci commerciali dell'età arcaica."},
    {"anno": "VI sec a.C.", "evento": "Scintilla della Filosofia", "dettaglio": "A Mileto, scienziati e pensatori come Talete iniziano a cercare spiegazioni naturali (e non mitologiche) sull'origine del cosmo."}
]

st.title("⏳ LA LINEA DEL TEMPO INTERATTIVA")

# CSS per creare la linea verticale e i nodi oro
st.markdown("""
    <style>
    .timeline-container { position: relative; padding-left: 30px; border-left: 3px solid #8c6d31; margin-left: 20px; }
    .timeline-node { position: absolute; left: -39px; background-color: #fffdfa; border: 3px solid #bfa16f; width: 16px; height: 16px; border-radius: 50%; }
    .timeline-year { font-family: 'Cinzel', serif; color: #8c6d31; font-weight: bold; font-size: 18px; }
    </style>
""", unsafe_allow_html=True)

# Stato per tracciare l'evento selezionato
if "selected_event" not in st.session_state:
    st.session_state.selected_event = 0

col1, col2 = st.columns([2, 3])

with col1:
    st.write("### 📅 Le Tappe")
    # Generiamo la linea del tempo
    st.markdown("<div class='timeline-container'>", unsafe_allow_html=True)
    for idx, item in enumerate(STORIA_DATI):
        st.markdown("<div class='timeline-node'></div>", unsafe_allow_html=True)
        # Un bottone per ogni tappa
        if st.button(f"{item['anno']} — {item['evento']}", key=f"time_{idx}"):
            st.session_state.selected_event = idx
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.write("### 📜 Dettagli dell'Epoca")
    evento_attivo = STORIA_DATI[st.session_state.selected_event]
    
    # Box di approfondimento stile pergamena
    st.info(f"**Epoca:** {evento_attivo['anno']}\n\n**Cosa accadde:** {evento_attivo['evento']}\n\n{evento_attivo['dettaglio']}")
