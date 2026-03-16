# 🧠 OpenMind - Votre assistant personnel intelligent

OpenMind est un assistant qui contrôle votre ordinateur en langage naturel. Il peut ouvrir des applications, des sites web, contrôler le volume, prendre des photos, et répondre à vos questions grâce à l'IA Mistral.

## ✨ Fonctionnalités

| Catégorie | Commandes |
|-----------|-----------|
| 📱 **Applications** | `ouvre whatsapp`, `ouvre telegram`, `ouvre chrome`, `ouvre calculatrice`... |
| 🌐 **Sites web** | `ouvre youtube`, `ouvre google`, `ouvre spotify`, `ouvre facebook`... |
| 🔍 **Recherche** | `cherche recette pizza`, `recherche météo Paris` |
| 🧮 **Calculs** | `calcule 15 * 3`, `calcule 25 + 10` |
| 🔊 **Volume** | `monte le volume`, `baisse le son`, `mute` |
| 📷 **Webcam** | `photo`, `prends une photo` |
| 🔆 **Luminosité** | `monte la luminosité`, `luminosité 50%` |
| 📧 **Mail** | `mail`, `ouvre gmail` |
| 🔋 **Batterie** | `batterie`, `niveau batterie` |
| 📋 **Presse-papiers** | `copie bonjour`, `colle` |
| 📸 **Capture** | `capture`, `capture d'écran` |
| 🔒 **Sécurité** | `verrouille`, `lock` |
| ⏻ **Système** | `éteins`, `redémarre` |
| 🌤️ **Météo** | `météo Paris`, `meteo Lyon` |
| 📝 **Notes** | `note que je dois acheter du lait` |
| 💬 **Questions** | `qui est Macron ?`, `quelle heure est-il ?` |

## 🚀 Installation

### Méthode 1 : Exécutable (recommandée)
1. Télécharge `OpenMind.exe` depuis la section [Releases](https://github.com/tonpseudo/OpenMind/releases)
2. Double-clique pour lancer
3. Obtiens une clé API gratuite sur [console.mistral.ai](https://console.mistral.ai)
4. Colle la clé quand OpenMind te la demande
5. Commence à utiliser OpenMind !

### Méthode 2 : Depuis les sources
```bash
git clone https://github.com/tonpseudo/OpenMind.git
cd OpenMind
pip install -r requirements.txt
python openmind.py
```

## 🔑 Obtenir une clé API Mistral (gratuite, sans carte bancaire)

1. Va sur **[console.mistral.ai](https://console.mistral.ai)**
2. Clique sur **"Sign up"** (Inscription)
3. Utilise ton email ou connecte-toi avec Google
4. Vérifie ton compte par SMS (un seul numéro par compte)
5. Dans le menu de gauche, clique sur **"API Keys"**
6. Clique sur **"Create new key"**
7. Donne un nom à ta clé (ex: "OpenMind")
8. **Copie la clé** (elle commence par `sk-...`)
9. Lance OpenMind et colle la clé dans la fenêtre popup

> ⚠️ **Garde ta clé secrète** ! Ne la partage pas sur GitHub.

## 🎯 Exemples de commandes

```
👤 > ouvre whatsapp
🤖 ✅ WhatsApp ouvert

👤 > ouvre youtube
🤖 ✅ Site youtube ouvert

👤 > cherche recette pizza
🤖 ✅ Recherche: recette pizza

👤 > calcule 15 * 3
🤖 🧮 = 45

👤 > monte le volume
🤖 🔊 Volume monté

👤 > photo
🤖 ✅ Photo sauvegardée: openmind_photo_20250316_143022.jpg

👤 > luminosité 50%
🤖 🔆 Luminosité à 50%

👤 > batterie
🤖 🔋 Batterie: 78% (2h15 restant)

👤 > copie bonjour
🤖 ✅ Copié: bonjour...

👤 > colle
🤖 📋 Presse-papiers: bonjour

👤 > capture
🤖 ✅ Capture: capture_20250316_143156.png

👤 > verrouille
🤖 🔒 Ordinateur verrouillé

👤 > météo Paris
🤖 🌤️ Météo Paris: +12°C ☀️ 15km/h

👤 > note que je dois acheter du lait
🤖 📝 Note sauvegardée

👤 > qui est Macron ?
🤖 Emmanuel Macron est le président de la France...

👤 > qui t'a créé ?
🤖 Mon créateur est Coulibaly Aboubakar Sidiki...

👤 > aide
🤖 (affiche toutes les commandes)

👤 > quit
🤖 👋 Au revoir !
```

## 📦 Dépendances

- Python 3.8 ou supérieur
- Bibliothèques listées dans `requirements.txt` :
  - `requests` : appels API
  - `pyautogui` : contrôle souris/clavier
  - `opencv-python` : webcam
  - `screen-brightness-control` : luminosité
  - `psutil` : batterie
  - `pyperclip` : presse-papiers
  - `mistralai` : IA (optionnel)
  - `pywin32` : lecteur CD (optionnel)

## 📁 Structure du projet

```
OpenMind/
├── 📄 openmind.py              # Programme principal
├── 📄 requirements.txt          # Dépendances
├── 📄 README.md                 # Ce fichier
├── 📄 LICENSE                   # Licence MIT
├── 📁 dist/                     # Exécutable
│   ├── 📄 OpenMind.exe
│   └── 📄 README.txt
└── 📁 templates/                 # Images WhatsApp (optionnel)
    ├── whatsapp_search.png
    ├── whatsapp_text.png
    └── whatsapp_contact.png
```

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE).

## 👨‍💻 Créateur

**Coulibaly Aboubakar Sidiki**  
Programmeur amateur passionné

- GitHub : [@tonpseudo](https://github.com/tonpseudo)
- Projet : [OpenMind](https://github.com/tonpseudo/OpenMind)

## ⭐ Remerciements

- [Mistral AI](https://mistral.ai) pour leur API gratuite
- Tous les utilisateurs et contributeurs d'OpenMind !

## 📢 Contribuer

Les contributions sont les bienvenues !  
N'hésite pas à :
- Signaler des bugs
- Proposer des améliorations
- Ajouter des fonctionnalités

---

**Fait avec ❤️ en Côte d'Ivoire**