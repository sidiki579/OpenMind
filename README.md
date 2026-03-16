# 🧠 OpenMind - Your Intelligent Personal Assistant / Votre assistant personnel intelligent

OpenMind is an intelligent assistant that controls your Windows computer through natural language. It can open applications, visit websites, control volume, take photos, and answer your questions using Mistral AI.

OpenMind est un assistant intelligent qui contrôle votre ordinateur Windows en langage naturel. Il peut ouvrir des applications, visiter des sites web, contrôler le volume, prendre des photos et répondre à vos questions grâce à Mistral AI.

---

## ✨ Features / Fonctionnalités

### 🇬🇧 English
- 📱 **Applications**: Open any app (`open whatsapp`, `open telegram`, `open chrome`, `open calculator`...)
- 🌐 **Websites**: Open any website (`open youtube`, `open google`, `open spotify`, `open facebook`...)
- 🔍 **Search**: Google search (`search pizza recipe`, `search Paris weather`)
- 🧮 **Calculations**: Math (`calculate 15 * 3`, `calculate 25 + 10`)
- 🔊 **Volume**: Control sound (`volume up`, `volume down`, `mute`)
- 📷 **Webcam**: Take photos (`take photo`, `photo`)
- 🔆 **Brightness**: Adjust screen brightness (`brightness up`, `brightness 50%`)
- 📧 **Email**: Open your inbox (`open gmail`, `mail`)
- 🔋 **Battery**: Check battery level (`battery`, `battery level`)
- 📋 **Clipboard**: Copy and paste text (`copy hello`, `paste`)
- 📸 **Screenshot**: Capture your screen (`screenshot`, `capture screen`)
- 🔒 **Security**: Lock your computer (`lock`, `lock pc`)
- ⏻ **System**: Shutdown or restart (`shutdown`, `restart`)
- 🌤️ **Weather**: Get weather info (`weather Paris`, `weather Lyon`)
- 📝 **Notes**: Save quick notes (`note that I need to buy milk`)
- 💬 **Questions**: Ask Mistral AI (`who is Macron?`, `what time is it?`)

### 🇫🇷 Français
- 📱 **Applications**: Ouvrir n'importe quelle app (`ouvre whatsapp`, `ouvre telegram`, `ouvre chrome`, `ouvre calculatrice`...)
- 🌐 **Sites web**: Ouvrir n'importe quel site (`ouvre youtube`, `ouvre google`, `ouvre spotify`, `ouvre facebook`...)
- 🔍 **Recherche**: Recherche Google (`cherche recette pizza`, `recherche météo Paris`)
- 🧮 **Calculs**: Mathématiques (`calcule 15 * 3`, `calcule 25 + 10`)
- 🔊 **Volume**: Contrôle du son (`monte le volume`, `baisse le son`, `mute`)
- 📷 **Webcam**: Prendre des photos (`photo`, `prends une photo`)
- 🔆 **Luminosité**: Ajuster la luminosité de l'écran (`monte la luminosité`, `luminosité 50%`)
- 📧 **Mail**: Ouvrir ta boîte mail (`mail`, `ouvre gmail`)
- 🔋 **Batterie**: Vérifier le niveau de batterie (`batterie`, `niveau batterie`)
- 📋 **Presse-papiers**: Copier et coller du texte (`copie bonjour`, `colle`)
- 📸 **Capture d'écran**: Capturer l'écran (`capture`, `capture d'écran`)
- 🔒 **Sécurité**: Verrouiller l'ordinateur (`verrouille`, `lock`)
- ⏻ **Système**: Éteindre ou redémarrer (`éteins`, `redémarre`)
- 🌤️ **Météo**: Obtenir la météo (`météo Paris`, `meteo Lyon`)
- 📝 **Notes**: Enregistrer des notes rapides (`note que je dois acheter du lait`)
- 💬 **Questions**: Poser une question à Mistral (`qui est Macron ?`, `quelle heure est-il ?`)

---

## 🚀 Installation

### 🇬🇧 English

#### Method 1: Executable (Recommended)
1. Download `OpenMind.exe` from the [Releases](https://github.com/sidiki579/OpenMind/releases) section
2. Double-click to run
3. Get a free API key from [console.mistral.ai](https://console.mistral.ai)
4. Paste the key when OpenMind asks for it
5. Start using OpenMind!

#### Method 2: From Source
```bash
git clone https://github.com/sidiki579/OpenMind.git
cd OpenMind
pip install -r requirements.txt
python openmind_final.py
```

### 🇫🇷 Français

#### Méthode 1 : Exécutable (Recommandée)
1. Télécharge `OpenMind.exe` depuis la section [Releases](https://github.com/sidiki579/OpenMind/releases)
2. Double-clique pour lancer
3. Obtiens une clé API gratuite sur [console.mistral.ai](https://console.mistral.ai)
4. Colle la clé quand OpenMind te la demande
5. Commence à utiliser OpenMind !

#### Méthode 2 : Depuis les sources
```bash
git clone https://github.com/sidiki579/OpenMind.git
cd OpenMind
pip install -r requirements.txt
python openmind_final.py
```

---

## 🔑 Getting a Free Mistral AI API Key / Obtenir une clé API Mistral gratuite

### 🇬🇧 English
1. Go to **[console.mistral.ai](https://console.mistral.ai)**
2. Click **"Sign up"**
3. Use your email or Google account
4. Verify your account via SMS (one number per account)
5. In the left menu, click **"API Keys"**
6. Click **"Create new key"**
7. Give it a name (e.g., "OpenMind")
8. **Copy the key** (it starts with `sk-...`)
9. Launch OpenMind and paste the key in the popup window

> ⚠️ **Keep your key secret!** Never share it on GitHub.

### 🇫🇷 Français
1. Va sur **[console.mistral.ai](https://console.mistral.ai)**
2. Clique sur **"S'inscrire"** (Sign up)
3. Utilise ton email ou ton compte Google
4. Vérifie ton compte par SMS (un numéro par compte)
5. Dans le menu de gauche, clique sur **"API Keys"**
6. Clique sur **"Create new key"** (Créer une clé)
7. Donne-lui un nom (par exemple "OpenMind")
8. **Copie la clé** (elle commence par `sk-...`)
9. Lance OpenMind et colle la clé dans la fenêtre popup

> ⚠️ **Garde ta clé secrète !** Ne la partage jamais sur GitHub.

---

## 🎯 Command Examples / Exemples de commandes

### 🇬🇧 English
```
👤 > open whatsapp
🤖 ✅ WhatsApp opened

👤 > open youtube
🤖 ✅ Website youtube opened

👤 > search pizza recipe
🤖 ✅ Search: pizza recipe

👤 > calculate 15 * 3
🤖 🧮 = 45

👤 > volume up
🤖 🔊 Volume up

👤 > take photo
🤖 ✅ Photo saved: openmind_photo_20250316_143022.jpg

👤 > brightness 50%
🤖 🔆 Brightness set to 50%

👤 > battery
🤖 🔋 Battery: 78% (2h15 remaining)

👤 > copy hello
🤖 ✅ Copied: hello...

👤 > paste
🤖 📋 Clipboard: hello

👤 > screenshot
🤖 ✅ Screenshot: capture_20250316_143156.png

👤 > lock
🤖 🔒 Computer locked

👤 > weather Paris
🤖 🌤️ Weather Paris: +12°C ☀️ 15km/h

👤 > note that I need to buy milk
🤖 📝 Note saved

👤 > who is Macron?
🤖 Emmanuel Macron is the president of France...

👤 > who created you?
🤖 My creator is Coulibaly Aboubakar Sidiki...

👤 > help
🤖 (displays all commands)

👤 > quit
🤖 👋 Goodbye!
```

### 🇫🇷 Français
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

---

## 📦 Dependencies / Dépendances

- Python 3.8 or higher
- Libraries listed in `requirements.txt`:
  - `requests` : API calls
  - `pyautogui` : mouse/keyboard control
  - `opencv-python` : webcam
  - `screen-brightness-control` : brightness control
  - `psutil` : battery info
  - `pyperclip` : clipboard management
  - `mistralai` : AI integration
  - `pywin32` : CD drive control (optional)

---

## 📁 Project Structure / Structure du projet

```
OpenMind/
├── 📄 openmind_final.py         # Main program / Programme principal
├── 📄 requirements.txt          # Dependencies / Dépendances
├── 📄 README.md                  # This file / Ce fichier
├── 📄 LICENSE                    # MIT License / Licence MIT
├── 📁 dist/                      # Executable folder / Dossier exécutable
│   ├── 📄 OpenMind.exe
│   └── 📄 README.txt
└── 📁 templates/                  # WhatsApp images (optional) / Images WhatsApp (optionnel)
    ├── whatsapp_search.png
    ├── whatsapp_text.png
    └── whatsapp_contact.png
```

---

## 📄 License / Licence

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 👨‍💻 Creator / Créateur

**Coulibaly Aboubakar Sidiki**  
Passionate amateur programmer from Côte d'Ivoire / Programmeur amateur passionné de Côte d'Ivoire

- GitHub : [@sidiki579](https://github.com/sidiki579)
- Project / Projet : [OpenMind](https://github.com/sidiki579/OpenMind)
- Email : coulibalysidiki046@gmail.com

---

## ⭐ Acknowledgments / Remerciements

- [Mistral AI](https://mistral.ai) for their free API / pour leur API gratuite
- All OpenMind users and contributors! / Tous les utilisateurs et contributeurs d'OpenMind !

---

## 📢 Contributing / Contribuer

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Add new features

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Suggérer des améliorations
- Ajouter de nouvelles fonctionnalités

---

**Made with ❤️ in Côte d'Ivoire / Fait avec ❤️ en Côte d'Ivoire**