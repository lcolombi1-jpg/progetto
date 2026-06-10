import streamlit as st

# Configurazione della pagina
st.set_page_config(page_title="LE OLIMPIADI DELLA STORIA", page_icon="🏛️", layout="wide")

# --- STILE CSS PERSONALIZZATO (Estetica Tempio Antico) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Fauna+One&display=swap');
    
    /* Sfondo generale color pergamena/marmo chiaro */
    .stApp {
        background-color: #fdfbf7;
        color: #3c362a;
        font-family: 'Fauna One', serif;
    }
    
    /* Titoli in stile epico classico */
    h1, h2, h3 {
        font-family: 'Cinzel', serif;
        color: #8c6d31 !important;
        text-align: center;
    }
    
    /* Colonne del Tempio (Simulate via CSS) */
    .pillar-left, .pillar-right {
        background: linear-gradient(90deg, #e0d5c1 0%, #fffdfa 50%, #e0d5c1 100%);
        border-left: 2px solid #bfa16f;
        border-right: 2px solid #bfa16f;
        height: 80vh;
        box-shadow: 3px 0px 10px rgba(0,0,0,0.1);
        border-radius: 4px;
        position: relative;
    }
    .pillar-left::before, .pillar-right::before {
        content: "🏛️";
        font-size: 24px;
        position: absolute;
        top: -10px;
        left: 25%;
    }
    
    /* Contenitore principale del Quiz (Cella del Tempio) */
    .quiz-box {
        background-color: #fffdfa;
        border: 4px double #bfa16f;
        padding: 25px;
        border-radius: 8px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.05);
    }
    
    /* Bottoni stile antico bronzo/oro */
    .stButton>button {
        background-color: #8c6d31 !important;
        color: white !important;
        font-family: 'Cinzel', serif;
        border-radius: 4px;
        border: 1px solid #bfa16f;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #bfa16f !important;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# --- DATABASE DELLE DOMANDE (Basato sulla fonte condivisa) ---
QUIZ_DATA = {
    1: {
        "title": "Livello I: Le Stirpi e le Origini dell'Età Arcaica",
        "questions": [
            {
                "q": "Da quale popolo i Greci adattarono il proprio sistema alfabetico nel corso dell'VIII secolo a.C.?",
                "options": ["Dai Cretesi", "Dai Fenici", "Dagli Egizi", "Dai Babilonesi"],
                "answer": "Dai Fenici",
                "explanation": "L'alfabeto greco venne elaborato adattando alla propria lingua il sistema alfabetico dei Fenici."
            },
            {
                "q": "In quale area geografica si stanziarono prevalentemente i Dori alla fine dell'età oscura?",
                "options": ["Nel Peloponneso", "Nell'Attica", "Nell'isola di Lesbo", "Nella Ionia"],
                "answer": "Nel Peloponneso",
                "explanation": "I Dori occuparono principalmente il Peloponneso, dove sorsero città fondamentali come Sparta, Corinto e Argo."
            },
            {
                "q": "Cos'erano gli 'oboli' utilizzati in Grecia prima della nascita della moneta vera e propria?",
                "options": ["Monete d'oro zecchino", "Piccole barre di ferro facilmente trasportabili", "Sigilli di terracotta dipinta", "Preziosi cilindretti incisi babilonesi"],
                "answer": "Piccole barre di ferro facilmente trasportabili",
                "explanation": "Prima dell'introduzione del sistema monetario, in Grecia venivano impiegate piccole barre di ferro chiamate oboli."
            },
            {
                "q": "Quale tiranno di Corinto fece costruire una rampa di 8 chilometri per trasportare le navi via terra attraverso l'istmo?",
                "options": ["Cipselo", "Periandro", "Pittaco", "Pisistrato"],
                "answer": "Periandro",
                "explanation": "Il tiranno Periandro, inserito tra i Sette Sapienti, ideò la celebre rampa per evitare alle navi il periplo del Peloponneso."
            },
            {
                "q": "Nel poema 'Le opere e i giorni' di Esiodo, quale valore viene esaltato come motore positivo per lo sviluppo della società?",
                "options": ["La guerra d'espansione", "L'emulazione/competizione sul lavoro", "L'ozio dei nobili", "La ricchezza intrinseca dei mercanti"],
                "answer": "L'emulazione/competizione sul lavoro",
                "explanation": "Esiodo celebra la contesa buona, ovvero l'emulazione virtuosa che stimola l'individuo a impegnarsi nel lavoro onesto."
            }
        ]
    },
    2: {
        "title": "Livello II: La Pólis e la Grande Espansione Coloniale",
        "questions": [
            {
                "q": "Come venivano chiamati i contadini-soldati greci che combattevano affiancati nella falange?",
                "options": ["Opliti", "Metropoli", "Basileis", "Arconti"],
                "answer": "Opliti",
                "explanation": "Gli opliti erano contadini-soldati protetti da un armamento standardizzato che combattevano a ranghi serrati."
            },
            {
                "q": "Quale nome assunse l'Italia meridionale in seguito alla massiccia colonizzazione greca?",
                "options": ["Magna Grecia", "Apoikia", "Ionia", "Etruria centrale"],
                "answer": "Magna Grecia",
                "explanation": "Gli insediamenti sorti nel Sud Italia assunsero in latino il nome di 'Magna Grecia' (Grande Grecia)."
            },
            {
                "q": "Chi era l'ecista nel contesto della fondazione di una nuova colonia greca (apoikía)?",
                "options": ["Il sacerdote addetto ai sacrifici", "Il fondatore scelto per guidare la spedizione", "Il capo della fazione aristocratica rivale", "Il banchiere privato che finanziava la flotta"],
                "answer": "Il fondatore scelto per guidare la spedizione",
                "explanation": "L'ecista era il capo designato dalla metropoli con pieni poteri civili e militari per guidare i coloni verso la nuova terra."
            },
            {
                "q": "Quale importante città della Sicilia fu fondata da coloni di Corinto nel 733 a.C. e divenne un ricchissimo granaio?",
                "options": ["Agrigento", "Siracusa", "Gela", "Catania"],
                "answer": "Siracusa",
                "explanation": "Siracusa fu fondata nel 733 a.C. da coloni corinzi, espandendosi poi fino a controllare fertili pianure strategiche."
            },
            {
                "q": "Che cosa si intende per ordinamento 'timocratico' introdotto in molte póleis?",
                "options": ["Un governo guidato esclusivamente dai sacerdoti dell'oracolo", "Un governo basato sulla partecipazione in funzione della ricchezza", "Una monarchia ereditaria assoluta di stampo vicino-orientale", "La democrazia totale del démos"],
                "answer": "Un governo basato sulla partecipazione in funzione della ricchezza",
                "explanation": "Timocrazia significa letteralmente 'governo basato sulla ricchezza', legata principalmente alla proprietà fondiaria."
            }
        ]
    },
    3: {
        "title": "Livello III: Religione, Oracoli e il Pensiero Filosofico",
        "questions": [
            {
                "q": "Presso quale famosissimo santuario panellenico operava la sacerdotessa Pizia per trasmettere i responsi di Apollo?",
                "options": ["A Olimpia", "A Delfi", "A Eleusi", "A Corinto"],
                "answer": "A Delfi",
                "explanation": "L'oracolo di Apollo a Delfi era il più importante centro diplomatico e religioso del mondo greco."
            },
            {
                "q": "A partire dal 776 a.C., ogni quattro anni si tenevano i giochi sacri di Olimpia. In onore di quale divinità venivano celebrati?",
                "options": ["Apollo", "Zeus", "Poseidone", "Dioniso"],
                "answer": "Zeus",
                "explanation": "Le Olimpiadi erano gare sacre quadriennali dedicate a Zeus; durante il loro svolgimento vigeva la 'tregua sacra'."
            },
            {
                "q": "Quale celebre massima morale incisa sul tempio di Apollo a Delfi fu adottata da Socrate come pilastro del proprio pensiero?",
                "options": ["Pensa al tutto", "Conosci te stesso", "Il denaro ha un prezzo", "Evita l'ebbrezza"],
                "answer": "Conosci te stesso",
                "explanation": "La frase 'conosci te stesso' invitava il fedele a riconoscere i propri limiti umani di fronte alla divinità."
            },
            {
                "q": "Quale regione storica dell'Asia Minore, e in particolare la città di Mileto, fu la culla della filosofia nel VI secolo a.C.?",
                "options": ["La Ionia", "L'Attica", "Il Peloponneso", "La Beozia"],
                "answer": "La Ionia",
                "explanation": "La Ionia (e la città di Mileto con Talete, Anassimandro e Anassimene) rappresentò il laboratorio culturale in cui nacque il pensiero razionale."
            },
            {
                "q": "Quale filosofo criticò l'antropomorfismo religioso dicendo che se i buoi o i cavalli avessero le mani disegnerebbero dèi a loro somiglianza?",
                "options": ["Pitagora", "Senofane di Colofone", "Eraclito", "Parmenide"],
                "answer": "Senofane di Colofone",
                "explanation": "Senofane relativizzò la religione tradizionale greca criticando l'abitudine umana di immaginare gli dèi con sembianze antropomorfe."
            }
        ]
    }
}

# --- INIZIALIZZAZIONE STATI DI GIOCO (Session State) ---
if "max_unlocked_level" not in st.session_state:
    st.session_state.max_unlocked_level = 1
if "active_level" not in st.session_state:
    st.session_state.active_level = 1
if "current_question_idx" not in st.session_state:
    st.session_state.current_question_idx = 0
if "level_score" not in st.session_state:
    st.session_state.level_score = 0
if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False
if "show_feedback" not in st.session_state:
    st.session_state.show_feedback = False

# --- LAYOUT ESTETICO DEL TEMPIO ---
st.write("<h1>🏛️ LVDVS HISTORIAE 🏛️</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center; font-style:italic;'>Mettiti alla prova con le cronache e gli orizzonti della storia greca arcaica!</p>", unsafe_allow_html=True)

# Layout a 3 colonne per posizionare i pilastri del tempio ai lati
col_pillar_left, col_main, col_pillar_right = st.columns([1, 6, 1])

with col_pillar_left:
    st.markdown("<div class='pillar-left'></div>", unsafe_allow_html=True)

with col_pillar_right:
    st.markdown("<div class='pillar-right'></div>", unsafe_allow_html=True)

# --- BLOCCO CENTRALE DEL QUIZ ---
with col_main:
    # Selezione del livello tramite bottoni abilitati/disabilitati
    st.write("### 🧭 Seleziona il tuo livello:")
    lvl_cols = st.columns(3)
    for i in range(1, 4):
        with lvl_cols[i-1]:
            is_locked = i > st.session_state.max_unlocked_level
            label = f"🔓 Livello {i}" if not is_locked else f"🔒 Livello {i} (Bloccato)"
            if st.button(label, key=f"btn_lvl_{i}", disabled=is_locked, use_container_width=True):
                st.session_state.active_level = i
                st.session_state.current_question_idx = 0
                st.session_state.level_score = 0
                st.session_state.show_feedback = False
                st.session_state.quiz_completed = False
                st.rerun()

    st.markdown("<hr style='border:1px solid #bfa16f;'>", unsafe_allow_html=True)

    # Gestione dello svolgimento del quiz
    lvl = st.session_state.active_level
    questions = QUIZ_DATA[lvl]["questions"]
    q_idx = st.session_state.current_question_idx

    st.markdown(f"<div class='quiz-box'>", unsafe_allow_html=True)
    st.write(f"### ⚡ {QUIZ_DATA[lvl]['title']}")
    
    if not st.session_state.quiz_completed:
        st.write(f"**Domanda {q_idx + 1} di 5**")
        current_q = questions[q_idx]
        
        st.write(f"#### {current_q['q']}")
        
        # Form per inviare la risposta in modo controllato
        with st.form(key=f"q_form_{lvl}_{q_idx}"):
            user_choice = st.radio("Scegli la risposta corretta:", current_q["options"], key=f"radio_{lvl}_{q_idx}")
            submit_answer = st.form_submit_button(label="Invia Risposta 🏛️")
            
        if submit_answer or st.session_state.show_feedback:
            st.session_state.show_feedback = True
            if user_choice == current_q["answer"]:
                st.success(f"🎯 **Risposta Corretta!**")
                if not submit_answer: # Evita doppie aggiunte al punteggio sul rerun
                    pass
            else:
                st.error(f"❌ **Risposta Errata!** La risposta corretta era: *{current_q['answer']}*")
            
            st.info(f"📜 *Approfondimento:* {current_q['explanation']}")
            
            # Pulsante per avanzare alla domanda successiva
            if st.button("Continua il cammino ➡️", key=f"next_btn_{q_idx}"):
                if user_choice == current_q["answer"] and not submit_answer:
                    pass
                if user_choice == current_q["answer"]:
                    st.session_state.level_score += 1
                
                st.session_state.show_feedback = False
                if q_idx < 4:
                    st.session_state.current_question_idx += 1
                else:
                    st.session_state.quiz_completed = True
                st.rerun()
                
    else:
        # Schermata Finale del Livello
        final_score = st.session_state.level_score
        st.write("### 🏺 Resoconto della Prova")
        st.write(f"Hai risposto correttamente a **{final_score}** domande su **5**.")
        
        if final_score >= 4:
            st.balloons()
            st.success("🎉 **Per l'alloro di Olimpia!** Hai superato brillantemente il livello!")
            if lvl < 3 and st.session_state.max_unlocked_level == lvl:
                st.session_state.max_unlocked_level = lvl + 1
                st.write("🔓 **Nuovo Livello Sbloccato!** Scegli il livello successivo in alto.")
        else:
            st.error("📉 **Gli dèi ti invitano a ripassare!** Per sbloccare il livello successivo devi indovinarne almeno 4 su 5.")
            if st.button("Riprova questo livello 🔄"):
                st.session_state.current_question_idx = 0
                st.session_state.level_score = 0
                st.session_state.quiz_completed = False
                st.session_state.show_feedback = False
                st.rerun()
                
    st.markdown("</div>", unsafe_allow_html=True)
