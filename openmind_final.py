# openmind_final.py - Version ULTIME avec Mistral intelligent
import subprocess
import os
import re
import json
import time
import sys
import requests
import pyautogui
from pathlib import Path
import tkinter as tk
from tkinter import simpledialog
import threading
import ctypes

# ===== BIBLIOTHÈQUES SPÉCIFIQUES =====
import cv2
from screen_brightness_control import get_brightness, set_brightness
import psutil
import pyperclip

# ===== FICHIER DE CONFIGURATION =====
CONFIG_FILE = "openmind_config.json"

def charger_config():
    """Charge la configuration ou demande la clé API à l'utilisateur"""
    if Path(CONFIG_FILE).exists():
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        print(f"✅ Configuration chargée")
        return config
    
    # Fenêtre popup pour demander la clé
    root = tk.Tk()
    root.withdraw()
    
    cle = simpledialog.askstring(
        "🔑 Clé API Mistral AI",
        "Colle ta clé API Mistral ici:\n\n"
        "1. Va sur: console.mistral.ai\n"
        "2. Dans 'API Keys', crée une clé\n"
        "3. Colle-la ci-dessous\n\n"
        "La clé commence par 'sk-...'"
    )
    
    root.destroy()
    
    if not cle:
        print("❌ Aucune clé fournie. Le programme va s'arrêter.")
        sys.exit(1)
    
    config = {"mistral_key": cle}
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)
    
    print(f"✅ Clé sauvegardée")
    time.sleep(1)
    return config

# ===== CONFIGURATION MISTRAL =====
config = charger_config()
MISTRAL_API_KEY = config.get("mistral_key")

# Test de la clé
try:
    headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}"}
    response = requests.get("https://api.mistral.ai/v1/models", headers=headers, timeout=10)
    if response.status_code == 200:
        print("✅ Connexion Mistral réussie !")
        mistral_disponible = True
    else:
        print(f"⚠️ Erreur de clé: {response.status_code}")
        mistral_disponible = False
except Exception as e:
    print(f"⚠️ Erreur de connexion: {e}")
    mistral_disponible = False

# ===== APPLICATIONS =====
apps = {
    "whatsapp": "WhatsApp.exe",
    "telegram": "C:\\Users\\HP\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe",
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "calculatrice": "calc.exe",
    "explorateur": "explorer.exe",
    "notepad": "notepad.exe",
    "paint": "mspaint.exe",
    "word": "WINWORD.EXE",
    "excel": "EXCEL.EXE",
}

# ===== SITES =====
sites = {
    "youtube": "youtube.com",
    "google": "google.com",
    "spotify": "open.spotify.com",
    "tiktok": "tiktok.com",
    "facebook": "facebook.com",
    "twitter": "twitter.com",
    "instagram": "instagram.com",
    "amazon": "amazon.fr",
    "netflix": "netflix.com",
    "twitch": "twitch.tv",
    "github": "github.com",
    "gmail": "gmail.com",
    "discord": "discord.com",
    "whatsapp": "web.whatsapp.com",
}

# ===== FONCTIONS DE BASE =====
def ouvrir_application(nom):
    if nom in apps:
        try:
            subprocess.Popen([apps[nom]])
            return f"✅ {nom} ouvert"
        except:
            if nom == "whatsapp":
                subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "https://web.whatsapp.com"])
                return f"✅ WhatsApp Web ouvert"
            return f"❌ Erreur ouverture"
    return f"❌ Application '{nom}' non trouvée"

def ouvrir_site(nom):
    if nom in sites:
        url = f"https://{sites[nom]}"
        subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", url])
        return f"✅ Site {nom} ouvert"
    return f"❌ Site non reconnu"

def rechercher_google(requete):
    url = f"https://www.google.com/search?q={requete.replace(' ', '+')}"
    subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", url])
    return f"✅ Recherche: {requete}"

def calculer(expression):
    try:
        expr = expression.replace("x", "*").replace("fois", "*").replace("divisé", "/")
        resultat = eval(expr)
        return f"🧮 = {resultat}"
    except:
        return "❌ Calcul impossible"

def controler_volume(commande):
    cmd = commande.lower()
    if "monte" in cmd:
        pyautogui.press('volumeup', 3)
        return "🔊 Volume monté"
    elif "baisse" in cmd:
        pyautogui.press('volumedown', 3)
        return "🔉 Volume baissé"
    elif "mute" in cmd:
        pyautogui.press('volumemute')
        return "🔇 Muet"
    return "❌ Commande volume"

def prendre_photo():
    try:
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            return "❌ Webcam non trouvée"
        
        ret, frame = cam.read()
        if ret:
            nom_fichier = f"openmind_photo_{time.strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(nom_fichier, frame)
            cam.release()
            return f"✅ Photo sauvegardée: {nom_fichier}"
        
        cam.release()
        return "❌ Impossible de prendre la photo"
    except Exception as e:
        return f"❌ Erreur webcam: {e}"

def controler_luminosite(commande):
    try:
        cmd = commande.lower()
        current = get_brightness()[0]
        
        if "monte" in cmd or "+" in cmd or "augmente" in cmd:
            new = min(current + 20, 100)
            set_brightness(new)
            return f"🔆 Luminosité à {new}%"
        elif "baisse" in cmd or "-" in cmd or "diminue" in cmd:
            new = max(current - 20, 0)
            set_brightness(new)
            return f"🔆 Luminosité à {new}%"
        else:
            match = re.search(r'(\d+)', cmd)
            if match:
                val = int(match.group(1))
                val = max(0, min(val, 100))
                set_brightness(val)
                return f"🔆 Luminosité à {val}%"
            return f"🔆 Luminosité actuelle: {current}%"
    except Exception as e:
        return f"❌ Erreur luminosité: {e}"

def ouvrir_mail(service="gmail"):
    urls = {
        "gmail": "https://mail.google.com",
        "outlook": "https://outlook.live.com",
        "yahoo": "https://mail.yahoo.com",
        "proton": "https://mail.proton.me",
        "laposte": "https://www.laposte.net/accueil"
    }
    service = service.lower()
    url = urls.get(service, urls["gmail"])
    
    chrome_paths = [
        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
        "C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
    ]
    
    for path in chrome_paths:
        if os.path.exists(path):
            try:
                subprocess.Popen([path, url])
                return f"✅ {service.capitalize()} ouvert"
            except:
                continue
    
    try:
        os.startfile(url)
        return f"✅ {service.capitalize()} ouvert (navigateur par défaut)"
    except:
        return "❌ Impossible d'ouvrir le navigateur"

def info_batterie():
    try:
        battery = psutil.sensors_battery()
        if battery:
            pourcent = battery.percent
            if battery.power_plugged:
                if pourcent == 100:
                    etat = "chargé, branché"
                else:
                    etat = f"en charge ({pourcent}%)"
            else:
                if battery.secsleft > 0 and battery.secsleft != -1:
                    heures = battery.secsleft // 3600
                    minutes = (battery.secsleft % 3600) // 60
                    temps = f"{heures}h{minutes:02d}"
                    etat = f"{pourcent}% ({temps} restant)"
                else:
                    etat = f"{pourcent}%"
            return f"🔋 Batterie: {etat}"
        return "ℹ️ Aucune batterie détectée"
    except Exception as e:
        return f"❌ Erreur batterie: {e}"

def copier_texte(texte):
    try:
        pyperclip.copy(texte)
        return f"✅ Copié: {texte[:30]}..."
    except:
        return "❌ Erreur copie"

def coller_texte():
    try:
        contenu = pyperclip.paste()
        return f"📋 Presse-papiers: {contenu[:50]}..." if contenu else "📋 Presse-papiers vide"
    except:
        return "❌ Erreur collage"

def capture_ecran():
    nom = f"capture_{time.strftime('%Y%m%d_%H%M%S')}.png"
    pyautogui.screenshot().save(nom)
    return f"✅ Capture: {nom}"

def verrouiller():
    ctypes.windll.user32.LockWorkStation()
    return "🔒 Ordinateur verrouillé"

def eteindre():
    rep = input("⚠️ Veux-tu vraiment éteindre ? (oui/non) ")
    if rep.lower() == "oui":
        os.system("shutdown /s /t 10")
        return "🖥️ Extinction dans 10 secondes"
    return "⏸️ Annulé"

def redemarrer():
    rep = input("⚠️ Veux-tu vraiment redémarrer ? (oui/non) ")
    if rep.lower() == "oui":
        os.system("shutdown /r /t 10")
        return "🔄 Redémarrage dans 10 secondes"
    return "⏸️ Annulé"

def meteo(ville="Paris"):
    try:
        url = f"https://wttr.in/{ville}?format=%t+%c+%w"
        response = requests.get(url, timeout=10)
        return f"🌤️ Météo {ville}: {response.text.strip()}"
    except:
        return "❌ Erreur météo"

def noter(texte):
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M')} - {texte}\n")
    return "📝 Note sauvegardée"

def ouvrir_lecteur():
    return "ℹ️ Aucun lecteur CD/DVD détecté sur ce PC."

def info_createur():
    return "🤖 Mon créateur est Coulibaly Aboubakar Sidiki, un programmeur amateur talentueux !"

# ===== FONCTIONS INTELLIGENTES AVEC MISTRAL =====
def repondre_question_intelligente(question):
    """Utilise Mistral pour répondre directement ou ouvrir des sites"""
    if not mistral_disponible:
        return None
    
    try:
        prompt = f"""
        Tu es OpenMind, un assistant intelligent.
        
        Analyse cette demande: "{question}"
        
        Réponds UNIQUEMENT au format JSON avec :
        
        1. Si c'est une QUESTION (qui, quand, pourquoi, comment, etc.) :
           {{"type": "question", "reponse": "ta réponse"}}
           
        2. Si c'est une DEMANDE D'OUVRIR UN SITE (même si le nom est mal écrit) :
           {{"type": "site", "nom": "nom du site", "url": "url complète"}}
           Exemple: "ouvre facebook" → {{"type": "site", "nom": "facebook", "url": "https://facebook.com"}}
           Exemple: "va sur youtube" → {{"type": "site", "nom": "youtube", "url": "https://youtube.com"}}
           Exemple: "instagram" → {{"type": "site", "nom": "instagram", "url": "https://instagram.com"}}
           Exemple: "tik tok" → {{"type": "site", "nom": "tiktok", "url": "https://tiktok.com"}}
           Exemple: "discord" → {{"type": "site", "nom": "discord", "url": "https://discord.com"}}
           Exemple: "whatsapp web" → {{"type": "site", "nom": "whatsapp", "url": "https://web.whatsapp.com"}}
           
        3. Si c'est une autre action (volume, photo, etc.) :
           {{"type": "action", "commande": "..."}}
        """
        
        response = requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={"Authorization": f"Bearer {MISTRAL_API_KEY}", "Content-Type": "application/json"},
            json={
                "model": "mistral-small-latest",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1,
                "max_tokens": 300
            },
            timeout=10
        )
        
        if response.status_code == 200:
            resultat = response.json()
            texte_json = resultat['choices'][0]['message']['content']
            match = re.search(r'\{.*\}', texte_json, re.DOTALL)
            if match:
                decision = json.loads(match.group())
                
                # Si c'est une question, on répond directement
                if decision["type"] == "question":
                    return f"🤖 {decision['reponse']}"
                
                # Si c'est un site, on l'ouvre
                elif decision["type"] == "site":
                    url = decision.get("url", f"https://{decision['nom']}.com")
                    try:
                        subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", url])
                        return f"✅ Site {decision['nom']} ouvert"
                    except:
                        return f"❌ Impossible d'ouvrir {decision['nom']}"
                
                # Si c'est une action, on redirige vers l'analyseur classique
                elif decision["type"] == "action":
                    return None
    except:
        pass
    
    return None

def ouvrir_site_avec_mistral(nom_site):
    """Utilise Mistral pour trouver l'URL d'un site même s'il n'est pas dans la liste"""
    try:
        prompt = f"Donne-moi l'URL complète de {nom_site}. Réponds UNIQUEMENT avec l'URL, rien d'autre."
        
        response = requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={"Authorization": f"Bearer {MISTRAL_API_KEY}", "Content-Type": "application/json"},
            json={
                "model": "mistral-small-latest",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1,
                "max_tokens": 50
            },
            timeout=5
        )
        
        if response.status_code == 200:
            resultat = response.json()
            url = resultat['choices'][0]['message']['content'].strip()
            if url.startswith("http"):
                subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", url])
                return f"✅ Site {nom_site} ouvert via Mistral"
    except:
        pass
    
    return None

# ===== ANALYSEUR CLASSIQUE =====
def analyser_classique(texte):
    t = texte.lower().strip()
    
    if t in ["aide", "help"]: return {"action": "aide"}
    if t in ["quit", "exit"]: return {"action": "quit"}
    
    if t.startswith("ouvre "):
        nom = t[6:].strip()
        # D'abord on cherche dans les sites
        if nom in sites:
            return {"action": "ouvrir_site", "nom": nom}
        # Ensuite dans les applis
        elif nom in apps:
            return {"action": "ouvrir_app", "nom": nom}
        else:
            # Sinon, on demande à Mistral
            reponse = ouvrir_site_avec_mistral(nom)
            if reponse:
                print(f"🤖 {reponse}")
                return {"action": "ignore"}
            return {"action": "ouvrir_app", "nom": nom}
    
    if t.startswith("site "):
        nom = t[5:].strip()
        if nom in sites:
            return {"action": "ouvrir_site", "nom": nom}
        else:
            reponse = ouvrir_site_avec_mistral(nom)
            if reponse:
                print(f"🤖 {reponse}")
                return {"action": "ignore"}
            return {"action": "ouvrir_site", "nom": nom}
    
    if t.startswith("cherche "): return {"action": "rechercher", "requete": t[8:]}
    if t.startswith("calcule "): return {"action": "calculer", "expression": t[8:]}
    
    if any(m in t for m in ["volume", "son", "mute"]): return {"action": "volume", "commande": t}
    
    if "photo" in t or "webcam" in t: return {"action": "photo"}
    if "luminosité" in t or "lumiere" in t: return {"action": "luminosite", "commande": t}
    
    if "mail" in t or "gmail" in t or "outlook" in t:
        service = "gmail"
        if "outlook" in t: service = "outlook"
        return {"action": "mail", "service": service}
    
    if "batterie" in t: return {"action": "batterie"}
    
    if t.startswith("copie "): return {"action": "copier", "texte": t[6:]}
    if "colle" in t: return {"action": "coller"}
    
    if "capture" in t or "screenshot" in t: return {"action": "capture"}
    if "verrouille" in t or "lock" in t: return {"action": "verrouiller"}
    if "éteins" in t or "eteins" in t: return {"action": "eteindre"}
    if "redémarre" in t or "restart" in t: return {"action": "redemarrer"}
    
    if "météo" in t or "meteo" in t:
        ville = t.replace("météo", "").replace("meteo", "").strip()
        return {"action": "meteo", "ville": ville if ville else "Paris"}
    
    if "note que" in t:
        texte = t.split("note que")[1].strip()
        return {"action": "note", "texte": texte}
    
    if "créateur" in t or "createur" in t or "qui t'a créé" in t:
        return {"action": "créateur"}
    
    if "lecteur" in t or "cd" in t or "dvd" in t or "éjecte" in t:
        return {"action": "lecteur"}
    
    # Si rien d'autre, on considère que c'est une question pour Mistral
    return {"action": "question", "texte": t}

# ===== ANALYSEUR PRINCIPAL =====
def analyser(commande):
    # D'abord on essaie avec Mistral intelligent
    reponse = repondre_question_intelligente(commande)
    if reponse:
        print(f"🤖 {reponse}")
        return {"action": "ignore"}
    
    # Sinon, on utilise l'analyseur classique
    return analyser_classique(commande)

# ===== PROGRAMME PRINCIPAL =====
def main():
    print("=" * 60)
    print("🧠 OPENMIND - Version ULTIME avec Mistral intelligent")
    print("=" * 60)
    print("\n📋 Commandes possibles:")
    print("  • [question]         → Réponse directe de Mistral")
    print("  • ouvre [site/app]   → ouvre site ou application")
    print("  • site [nom]         → ouvre un site")
    print("  • cherche [sujet]    → recherche Google")
    print("  • calcule [expr]     → calcul")
    print("  • [volume]           → monte/baisse/mute")
    print("  • photo              → prend une photo")
    print("  • luminosité         → contrôle luminosité")
    print("  • mail               → ouvre boîte mail")
    print("  • batterie           → niveau batterie")
    print("  • copie [texte]      → copie texte")
    print("  • colle              → colle texte")
    print("  • capture            → capture d'écran")
    print("  • verrouille         → verrouille PC")
    print("  • éteins             → éteint PC")
    print("  • redémarre          → redémarre PC")
    print("  • météo [ville]      → météo")
    print("  • note que [texte]   → note")
    print("  • aide               → cette aide")
    print("  • quit               → quitter")
    print("-" * 60)
    
    while True:
        try:
            cmd = input("\n👤 > ").strip()
            if not cmd: continue
            
            d = analyser(cmd)
            
            if d["action"] == "aide":
                print("\n📋 Commandes listées ci-dessus")
            elif d["action"] == "quit":
                print("👋 Au revoir !")
                break
            elif d["action"] == "ignore":
                continue  # Déjà traité par Mistral
            elif d["action"] == "ouvrir_app": print(f"🤖 {ouvrir_application(d['nom'])}")
            elif d["action"] == "ouvrir_site": print(f"🤖 {ouvrir_site(d['nom'])}")
            elif d["action"] == "rechercher": print(f"🤖 {rechercher_google(d['requete'])}")
            elif d["action"] == "calculer": print(f"🤖 {calculer(d['expression'])}")
            elif d["action"] == "volume": print(f"🤖 {controler_volume(d['commande'])}")
            elif d["action"] == "photo": print(f"🤖 {prendre_photo()}")
            elif d["action"] == "luminosite": print(f"🤖 {controler_luminosite(d['commande'])}")
            elif d["action"] == "mail": print(f"🤖 {ouvrir_mail(d.get('service', 'gmail'))}")
            elif d["action"] == "batterie": print(f"🤖 {info_batterie()}")
            elif d["action"] == "copier": print(f"🤖 {copier_texte(d['texte'])}")
            elif d["action"] == "coller": print(f"🤖 {coller_texte()}")
            elif d["action"] == "capture": print(f"🤖 {capture_ecran()}")
            elif d["action"] == "verrouiller": print(f"🤖 {verrouiller()}")
            elif d["action"] == "eteindre": print(f"🤖 {eteindre()}")
            elif d["action"] == "redemarrer": print(f"🤖 {redemarrer()}")
            elif d["action"] == "meteo": print(f"🤖 {meteo(d.get('ville', 'Paris'))}")
            elif d["action"] == "note": print(f"🤖 {noter(d['texte'])}")
            elif d["action"] == "lecteur": print(f"🤖 {ouvrir_lecteur()}")
            elif d["action"] == "créateur": print(f"🤖 {info_createur()}")
            elif d["action"] == "question": 
                # Si on arrive ici, c'est que Mistral n'a pas répondu
                print("🤖 ❌ Je n'ai pas compris")
            else:
                print("🤖 ❌ Commande non reconnue")
                
        except KeyboardInterrupt:
            print("\n👋 Au revoir !")
            break

if __name__ == "__main__":
    main()