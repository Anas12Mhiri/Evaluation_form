import streamlit as st
import pandas as pd
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="Évaluation Exposé Oral",
    page_icon="📊",
    layout="wide"
)

# Initialize session state for storing evaluations
if 'evaluations' not in st.session_state:
    st.session_state.evaluations = []

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1e3a8a;
        padding: 20px;
        background: linear-gradient(90deg, #3b82f6 0%, #1e40af 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .section-header {
        background-color: #dbeafe;
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
        margin-bottom: 15px;
        font-weight: bold;
        color: #1e40af;
    }
    .stRadio > label {
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header"><h1>GRILLE D\'ÉVALUATION DE L\'EXPOSÉ ORAL</h1></div>', unsafe_allow_html=True)

# Evaluation criteria structure
criteria = {
    "CONTENU": [
        "Respect de la consigne et compréhension complète du sujet",
        "Sujet clairement annoncé dès l'introduction",
        "Sujet argumentatif (prise de position explicite)",
        "Arguments clairs, développés et compréhensible",
        "Exemples concrets pour appuyer les arguments",
        "Organisation logique (introduction / développement / conclusion)",
        "Qualité et fiabilité des informations, maîtrise des connaissances",
        "Gestion efficace du temps et équilibre des parties"
    ],
    "NON VERBALE": [
        "Contact visuel avec le public",
        "Posture stable et adaptée",
        "Interaction avec le public (attention et réponses aux questions)",
        "Gestuelle naturelle et cohérente avec le discours",
        "Gestion du stress (pas de lecture excessive)",
        "Voix audible et articulation claire",
        "Intonation expressive (évite la monotonie)"
    ],
    "SUPPORT VISUEL": [
        "Page de garde complète (titre, nom, contexte)",
        "Lisibilité (police, taille, contraste)",
        "Contenu synthétique (mots-clés, pas de paragraphes)",
        "Cohérence entre discours oral et support",
        "Support utilisé comme aide, pas comme texte à lire"
    ],
    "ORIGINALITÉ": [
        "Angle personnel ou approche originale du sujet",
        "Langage approprié au contexte académique",
        "Créativité et valeur ajoutée de la présentation"
    ]
}

# Create tabs for form and results
tab1, tab2 = st.tabs(["📝 Formulaire d'Évaluation", "📊 Résultats Agrégés"])

with tab1:
    st.markdown("### Informations de l'Évaluateur")
    
    col1, col2 = st.columns(2)
    with col1:
        evaluator_name = st.text_input("Nom de l'évaluateur", key="evaluator_name")
    with col2:
        student_name = st.text_input("Nom de l'étudiant évalué", key="student_name")
    
    # Dictionary to store responses
    responses = {}
    
    # Create form for each category
    with st.form("evaluation_form"):
        for category, items in criteria.items():
            st.markdown(f'<div class="section-header">{category}</div>', unsafe_allow_html=True)
            
            for i, criterion in enumerate(items):
                col1, col2, col3 = st.columns([3, 1, 2])
                
                with col1:
                    st.write(f"**{criterion}**")
                
                with col2:
                    response = st.radio(
                        "Évaluation",
                        ["Satisfait", "Non Satisfait"],
                        key=f"{category}_{i}",
                        label_visibility="collapsed",
                        horizontal=True
                    )
                    responses[f"{category}_{criterion}"] = response
                
                with col3:
                    remark = st.text_input(
                        "Remarques",
                        key=f"remark_{category}_{i}",
                        label_visibility="collapsed",
                        placeholder="Remarques optionnelles..."
                    )
                    responses[f"remark_{category}_{criterion}"] = remark
        
        # Submit button
        st.markdown("---")
        submitted = st.form_submit_button("✅ Soumettre l'Évaluation", use_container_width=True, type="primary")
        
        if submitted:
            if not evaluator_name or not student_name:
                st.error("⚠️ Veuillez renseigner le nom de l'évaluateur et de l'étudiant.")
            else:
                # Store evaluation
                evaluation = {
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'evaluator': evaluator_name,
                    'student': student_name,
                    'responses': responses
                }
                st.session_state.evaluations.append(evaluation)
                st.success(f"✅ Évaluation soumise avec succès pour {student_name} par {evaluator_name}!")
                st.balloons()

with tab2:
    st.markdown("### 📊 Résultats Agrégés des Évaluations")
    
    if not st.session_state.evaluations:
        st.info("ℹ️ Aucune évaluation soumise pour le moment. Utilisez l'onglet 'Formulaire d'Évaluation' pour commencer.")
    else:
        # Display summary statistics
        st.markdown(f"**Nombre total d'évaluations:** {len(st.session_state.evaluations)}")
        
        # Get unique students and evaluators
        students = list(set([e['student'] for e in st.session_state.evaluations]))
        evaluators = list(set([e['evaluator'] for e in st.session_state.evaluations]))
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Étudiants évalués", len(students))
        with col2:
            st.metric("Évaluateurs", len(evaluators))
        
        # Filter options
        st.markdown("---")
        st.markdown("### Filtrer les résultats")
        selected_student = st.selectbox(
            "Sélectionner un étudiant (optionnel)",
            ["Tous"] + students
        )
        
        # Filter evaluations
        filtered_evals = st.session_state.evaluations
        if selected_student != "Tous":
            filtered_evals = [e for e in st.session_state.evaluations if e['student'] == selected_student]
        
        st.markdown("---")
        
        # Calculate statistics for each criterion
        for category, items in criteria.items():
            st.markdown(f'<div class="section-header">{category}</div>', unsafe_allow_html=True)
            
            results_data = []
            for criterion in items:
                key = f"{category}_{criterion}"
                satisfait_count = sum(1 for e in filtered_evals if e['responses'].get(key) == "Satisfait")
                non_satisfait_count = sum(1 for e in filtered_evals if e['responses'].get(key) == "Non Satisfait")
                total = satisfait_count + non_satisfait_count
                
                if total > 0:
                    percentage = (satisfait_count / total) * 100
                else:
                    percentage = 0
                
                results_data.append({
                    'Critère': criterion,
                    'Satisfait': satisfait_count,
                    'Non Satisfait': non_satisfait_count,
                    '% Satisfait': f"{percentage:.1f}%"
                })
            
            df = pd.DataFrame(results_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # Bar chart
            if not df.empty:
                st.bar_chart(df.set_index('Critère')[['Satisfait', 'Non Satisfait']])
        
        # Show all remarks
        st.markdown("---")
        st.markdown("### 💬 Remarques Détaillées")
        
        for eval_data in filtered_evals:
            with st.expander(f"📝 {eval_data['student']} - Évalué par {eval_data['evaluator']} ({eval_data['timestamp']})"):
                for category, items in criteria.items():
                    st.markdown(f"**{category}**")
                    for criterion in items:
                        remark_key = f"remark_{category}_{criterion}"
                        remark = eval_data['responses'].get(remark_key, "")
                        if remark:
                            st.write(f"- {criterion}: *{remark}*")
        
        # Export options
        st.markdown("---")
        st.markdown("### 📥 Exporter les Données")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Export to JSON
            if st.button("Télécharger JSON"):
                json_str = json.dumps(st.session_state.evaluations, indent=2, ensure_ascii=False)
                st.download_button(
                    label="💾 Télécharger le fichier JSON",
                    data=json_str,
                    file_name=f"evaluations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
        
        with col2:
            # Clear all data
            if st.button("🗑️ Effacer toutes les données", type="secondary"):
                if st.session_state.get('confirm_delete', False):
                    st.session_state.evaluations = []
                    st.session_state.confirm_delete = False
                    st.rerun()
                else:
                    st.session_state.confirm_delete = True
                    st.warning("⚠️ Cliquez à nouveau pour confirmer la suppression.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; padding: 20px;'>
        <small>Grille d'Évaluation de l'Exposé Oral - Université de Sfax - ENET'COM</small>
    </div>
    """,
    unsafe_allow_html=True
)
