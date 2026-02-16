# Grille d'Évaluation de l'Exposé Oral - Streamlit App

## Description
Cette application Streamlit permet d'évaluer des exposés oraux en utilisant la grille d'évaluation de l'ENET'COM. Elle supporte plusieurs évaluateurs simultanés et affiche les résultats agrégés en temps réel.

## Fonctionnalités

✅ **Formulaire d'évaluation interactif** avec tous les critères de la grille
✅ **Support multi-utilisateurs** - plusieurs évaluateurs peuvent soumettre des évaluations simultanément
✅ **Résultats agrégés en temps réel** avec statistiques et graphiques
✅ **Filtrage par étudiant** pour voir les résultats individuels
✅ **Remarques détaillées** pour chaque critère
✅ **Export des données** en format JSON
✅ **Interface moderne et responsive**

## Installation

### Prérequis
- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Installer Streamlit et pandas**
```bash
pip install streamlit pandas
```

2. **Télécharger le fichier de l'application**
Sauvegardez le fichier `evaluation_form.py` dans un dossier de votre choix.

## Utilisation

### Lancer l'application

1. **Ouvrez un terminal/invite de commandes**

2. **Naviguez vers le dossier contenant le fichier**
```bash
cd chemin/vers/le/dossier
```

3. **Lancez l'application Streamlit**
```bash
streamlit run evaluation_form.py
```

4. **L'application s'ouvrira automatiquement dans votre navigateur**
   - URL par défaut: http://localhost:8501

### Utilisation Multi-Utilisateurs

Pour permettre à plusieurs personnes d'utiliser l'application simultanément:

#### Option 1: Réseau Local (LAN)
```bash
streamlit run evaluation_form.py --server.address 0.0.0.0
```
Les autres utilisateurs sur le même réseau peuvent accéder via: `http://[VOTRE_IP]:8501`

#### Option 2: Streamlit Cloud (Gratuit)
1. Créez un compte sur https://streamlit.io/cloud
2. Connectez votre repository GitHub
3. Déployez l'application
4. Partagez le lien public avec les évaluateurs

## Guide d'utilisation de l'interface

### Onglet "Formulaire d'Évaluation"

1. **Renseignez les informations**
   - Nom de l'évaluateur
   - Nom de l'étudiant évalué

2. **Évaluez chaque critère**
   - Sélectionnez "Satisfait" ou "Non Satisfait"
   - Ajoutez des remarques optionnelles

3. **Soumettez l'évaluation**
   - Cliquez sur "✅ Soumettre l'Évaluation"
   - Confirmation avec animation

### Onglet "Résultats Agrégés"

1. **Vue d'ensemble**
   - Nombre total d'évaluations
   - Nombre d'étudiants évalués
   - Nombre d'évaluateurs

2. **Filtrage**
   - Sélectionnez un étudiant spécifique ou "Tous"

3. **Statistiques par catégorie**
   - Tableaux de résultats
   - Graphiques en barres
   - Pourcentages de réussite

4. **Remarques détaillées**
   - Consultez toutes les remarques par évaluation

5. **Export des données**
   - Téléchargez toutes les évaluations en JSON
   - Option pour effacer toutes les données

## Structure des Données

Les évaluations sont stockées en mémoire (session Streamlit) avec la structure suivante:

```json
{
  "timestamp": "2026-02-16 14:30:00",
  "evaluator": "Nom de l'évaluateur",
  "student": "Nom de l'étudiant",
  "responses": {
    "CONTENU_Respect de la consigne...": "Satisfait",
    "remark_CONTENU_Respect de la consigne...": "Excellente introduction"
  }
}
```

## Notes Importantes

⚠️ **Données temporaires**: Les données sont stockées dans la session Streamlit et seront perdues si vous:
- Fermez l'application
- Redémarrez le serveur
- Actualisez complètement la page (Ctrl+F5)

💡 **Conseils**:
- Exportez régulièrement vos données en JSON
- Pour une persistance permanente, une base de données pourrait être ajoutée
- Utilisez Streamlit Cloud pour un accès facile et permanent

## Catégories d'Évaluation

1. **CONTENU** (8 critères)
   - Respect de la consigne
   - Annonce du sujet
   - Argumentation
   - Exemples concrets
   - Organisation logique
   - Qualité des informations
   - Gestion du temps

2. **NON VERBALE** (7 critères)
   - Contact visuel
   - Posture
   - Interaction avec le public
   - Gestuelle
   - Gestion du stress
   - Articulation
   - Intonation

3. **SUPPORT VISUEL** (5 critères)
   - Page de garde
   - Lisibilité
   - Contenu synthétique
   - Cohérence oral/support
   - Utilisation appropriée

4. **ORIGINALITÉ** (3 critères)
   - Approche personnelle
   - Langage académique
   - Créativité

## Dépannage

### L'application ne se lance pas
```bash
# Vérifiez que Streamlit est bien installé
pip show streamlit

# Réinstallez si nécessaire
pip install --upgrade streamlit pandas
```

### Port déjà utilisé
```bash
# Utilisez un port différent
streamlit run evaluation_form.py --server.port 8502
```

### Problèmes d'affichage
- Videz le cache du navigateur
- Essayez un autre navigateur
- Rafraîchissez la page

## Support

Pour toute question ou problème:
- Vérifiez la documentation Streamlit: https://docs.streamlit.io
- Consultez les logs dans le terminal

## Licence

Application développée pour l'Université de Sfax - ENET'COM
