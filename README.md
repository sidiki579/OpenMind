# 🧠 OpenMind - Your Intelligent Personal Assistant

OpenMind is an intelligent assistant that controls your Windows computer through natural language. It can open applications, visit websites, control volume, take photos, and answer your questions using Mistral AI.

## ✨ Features

| Category | Commands |
|----------|----------|
| 📱 **Applications** | `ouvre whatsapp`, `ouvre telegram`, `ouvre chrome`, `ouvre calculatrice`... |
| 🌐 **Websites** | `ouvre youtube`, `ouvre google`, `ouvre spotify`, `ouvre facebook`... |
| 🔍 **Search** | `cherche recette pizza`, `recherche météo Paris` |
| 🧮 **Calculations** | `calcule 15 * 3`, `calcule 25 + 10` |
| 🔊 **Volume** | `monte le volume`, `baisse le son`, `mute` |
| 📷 **Webcam** | `photo`, `prends une photo` |
| 🔆 **Brightness** | `monte la luminosité`, `luminosité 50%` |
| 📧 **Email** | `mail`, `ouvre gmail` |
| 🔋 **Battery** | `batterie`, `niveau batterie` |
| 📋 **Clipboard** | `copie bonjour`, `colle` |
| 📸 **Screenshot** | `capture`, `capture d'écran` |
| 🔒 **Security** | `verrouille`, `lock` |
| ⏻ **System** | `éteins`, `redémarre` |
| 🌤️ **Weather** | `météo Paris`, `meteo Lyon` |
| 📝 **Notes** | `note que je dois acheter du lait` |
| 💬 **Questions** | `qui est Macron ?`, `quelle heure est-il ?` |

> 💡 **Note:** Commands are in French, but OpenMind understands various languages and spelling mistakes!

## 🚀 Installation

### Method 1: Executable (Recommended)
1. Download `OpenMind.exe` from the [Releases](https://github.com/sidiki579/OpenMind/releases) section
2. Double-click to run
3. Get a free API key from [console.mistral.ai](https://console.mistral.ai)
4. Paste the key when OpenMind asks for it
5. Start using OpenMind!

### Method 2: From Source
```bash
git clone https://github.com/sidiki579/OpenMind.git
cd OpenMind
pip install -r requirements.txt
python openmind_final.py
```

## 🔑 Getting a Free Mistral AI API Key

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

## 🎯 Command Examples

```
👤 > ouvre whatsapp
🤖 ✅ WhatsApp opened

👤 > ouvre youtube
🤖 ✅ Website youtube opened

👤 > cherche recette pizza
🤖 ✅ Search: recette pizza

👤 > calcule 15 * 3
🤖 🧮 = 45

👤 > monte le volume
🤖 🔊 Volume up

👤 > photo
🤖 ✅ Photo saved: openmind_photo_20250316_143022.jpg

👤 > luminosité 50%
🤖 🔆 Brightness set to 50%

👤 > batterie
🤖 🔋 Battery: 78% (2h15 remaining)

👤 > copie bonjour
🤖 ✅ Copied: bonjour...

👤 > colle
🤖 📋 Clipboard: bonjour

👤 > capture
🤖 ✅ Screenshot: capture_20250316_143156.png

👤 > verrouille
🤖 🔒 Computer locked

👤 > météo Paris
🤖 🌤️ Weather Paris: +12°C ☀️ 15km/h

👤 > note que je dois acheter du lait
🤖 📝 Note saved

👤 > qui est Macron ?
🤖 Emmanuel Macron is the president of France...

👤 > qui t'a créé ?
🤖 My creator is Coulibaly Aboubakar Sidiki...

👤 > aide
🤖 (displays all commands)

👤 > quit
🤖 👋 Goodbye!
```

## 📦 Dependencies

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

## 📁 Project Structure

```
OpenMind/
├── 📄 openmind_final.py         # Main program
├── 📄 requirements.txt          # Dependencies
├── 📄 README.md                  # This file
├── 📄 LICENSE                    # MIT License
├── 📁 dist/                      # Executable folder
│   ├── 📄 OpenMind.exe
│   └── 📄 README.txt
└── 📁 templates/                  # WhatsApp images (optional)
    ├── whatsapp_search.png
    ├── whatsapp_text.png
    └── whatsapp_contact.png
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👨‍💻 Creator

**Coulibaly Aboubakar Sidiki**  
Passionate amateur programmer from Côte d'Ivoire

- GitHub : [@sidiki579](https://github.com/sidiki579)
- Project : [OpenMind](https://github.com/sidiki579/OpenMind)
- Email : coulibalysidiki046@gmail.com

## ⭐ Acknowledgments

- [Mistral AI](https://mistral.ai) for their free API
- All OpenMind users and contributors!

## 📢 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Add new features

---

**Made with ❤️ in Côte d'Ivoire**