from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "voting_secret"

# 👇 ADD THIS BELOW
@app.route("/constituency/<name>")
def constituency_parties(name):

    data = {
        "Tiruttani": ["party_dmk.png", "party_admk.png", "party_tvk.png", "party_ntk.png", "party_pmk.png", "party_bjp.png", "party_congress.png"],
        "Thiruvallur": ["party_dmk.png", "party_admk.png", "party_tvk.png", "party_ntk.png", "party_pmk.png", "party_bjp.png", "party_congress.png"],
        "Ambattur": ["party_dmk.png", "party_admk.png", "party_tvk.png", "party_ntk.png", "party_pmk.png", "party_bjp.png", "party_congress.png"],
    }

    parties = data.get(name, [])

    return render_template("parties.html", name=name, parties=parties)
# ---------------- CONSTITUENCY LIST ----------------
constituencies = [
"Gummidipoondi","Ponneri (SC)","Tiruttani","Thiruvallur","Poonamallee (SC)",
"Avadi","Maduravoyal","Ambattur","Madhavaram","Tiruvottiyur",
"Dr. Radhakrishnan Nagar","Perambur","Kolathur","Villivakkam","Thiru-Vi-Ka-Nagar (SC)",
"Egmore (SC)","Royapuram","Harbour","Chepauk-Thiruvallikeni","Thousand Lights",
"Anna Nagar","Virugambakkam","Saidapet","T. Nagar","Mylapore",
"Velachery","Sholinganallur","Alandur","Sriperumbudur (SC)","Pallavaram",
"Tambaram","Chengalpattu","Thiruporur","Cheyyur (SC)","Madurantakam (SC)",
"Uthiramerur","Kancheepuram","Arakkonam (SC)","Sholingur","Katpadi",
"Ranipet","Arcot","Vellore","Anaikattu","Kilvaithinankuppam (SC)",
"Gudiyattam (SC)","Vaniyambadi","Ambur","Jolarpet","Tirupattur",
"Uthangarai (SC)","Bargur","Krishnagiri","Veppanahalli","Hosur",
"Thalli","Palacode","Pennagaram","Dharmapuri","Pappireddippatti",
"Harur (SC)","Chengam (SC)","Tiruvannamalai","Kilpennathur","Kalaiyarkovil",
"Arani","Polur","Cheyyar","Vandavasi (SC)","Gingee",
"Mailam","Tindivanam (SC)","Vanur (SC)","Villupuram","Vikravandi",
"Tirukoilur","Ulundurpettai","Rishivandiyam","Sankarapuram","Kallakurichi (SC)",
"Gangavalli (SC)","Attur (SC)","Yercaud (ST)","Omalur","Salem North",
"Salem South","Salem West","Edappadi","Mettur","Veerapandi",
"Sankari","Rasipuram (SC)","Senthamangalam (ST)","Namakkal","Paramathi-Velur",
"Tiruchengode","Kumarapalayam","Erode East","Erode West","Modakkurichi",
"Dharapuram (SC)","Kangayam","Perundurai","Bhavani","Anthiyur",
"Gobichettipalayam","Bhavanisagar (SC)","Udhagamandalam","Gudalur (SC)","Coonoor",
"Mettupalayam","Avanashi (SC)","Tiruppur North","Tiruppur South","Palladam",
"Udumalpet","Madathukulam","Pollachi","Kinathukadavu","Valparai (SC)",
"Singanallur","Coimbatore North","Coimbatore South","Kavundampalayam","Thondamuthur",
"Perur","Sulur","Karur","Krishnarayapuram (SC)","Kulithalai",
"Manapparai","Srirangam","Tiruchirappalli West","Tiruchirappalli East","Thiruverumbur",
"Lalgudi","Musiri","Thuraiyur (SC)","Perambalur (SC)","Kunnam",
"Ariyalur","Jayankondam","Tittagudi (SC)","Vriddhachalam","Neyveli",
"Panruti","Cuddalore","Kurinjipadi","Bhuvanagiri","Chidambaram",
"Kattumannarkoil (SC)","Sirkazhi (SC)","Mayiladuthurai","Poompuhar","Nagapattinam",
"Kilvelur (SC)","Vedaranyam","Thiruthuraipoondi (SC)","Mannargudi","Thiruvarur",
"Nannilam","Thanjavur","Orathanadu","Papanasam","Kumbakonam",
"Tiruvaiyaru","Thiruvonam","Pattukkottai","Peravurani","Gandharvakottai (SC)",
"Viralimalai","Pudukkottai","Thirumayam","Alangudi","Aranthangi",
"Karaikudi","Sivaganga","Manamadurai (SC)","Melur","Madurai East",
"Sholavandan (SC)","Madurai North","Madurai South","Madurai Central","Madurai West",
"Thiruparankundram","Thirumangalam","Usilampatti","Andipatti","Periyakulam (SC)",
"Bodinayakanur","Cumbum","Rajapalayam","Srivilliputhur (SC)","Sattur",
"Sivakasi","Virudhunagar","Aruppukkottai","Tiruchuli","Paramakudi (SC)",
"Tiruvadanai","Ramanathapuram","Mudukulathur","Vilathikulam","Thoothukkudi",
"Tiruchendur","Srivaikuntam","Ottapidaram (SC)","Kovilpatti","Sankarankovil (SC)",
"Vasudevanallur (SC)","Kadayanallur","Tenkasi","Alangulam","Tirunelveli",
"Palayamkottai","Ambasamudram","Nanguneri","Radhapuram","Kanyakumari",
"Nagercoil","Colachel","Padmanabhapuram","Vilavancode","Kulachal"
]


# ---------------- LANGUAGE DATA ----------------

languages = {

    "en": {
        "welcome": "Welcome to Online Voting",
        "tagline": "Secure • Transparent • Digital India",
        "vote": "Vote Now",
        "gov": "Government of India | Online Voting System",
        "home": "Home",
        "about": "About",
        "service": "Service",
        "manifesto": "Party Manifesto",
        "login": "Login",
        "title": "Online Voting System – Election Commission of India",
        "ministry": "Ministry of Digital Affairs, Government of India"
    },

    "hi": {
        "welcome": "ऑनलाइन वोटिंग में आपका स्वागत है",
        "tagline": "सुरक्षित • पारदर्शी • डिजिटल इंडिया",
        "vote": "अभी वोट करें",
        "gov": "भारत सरकार | ऑनलाइन वोटिंग सिस्टम",
        "home": "होम",
        "about": "परिचय",
        "service": "सेवाएं",
        "manifesto": "पार्टी घोषणा पत्र",
        "login": "लॉगिन",
        "title": "ऑनलाइन वोटिंग सिस्टम – भारत निर्वाचन आयोग",
        "ministry": "डिजिटल मामलों का मंत्रालय, भारत सरकार"
    },

    "ta": {
        "welcome": "ஆன்லைன் வாக்குப்பதிவிற்கு வரவேற்கிறோம்",
        "tagline": "பாதுகாப்பான • வெளிப்படையான • டிஜிட்டல் இந்தியா",
        "vote": "வாக்களிக்கவும்",
        "gov": "இந்திய அரசு | ஆன்லைன் வாக்குப்பதிவு",
        "home": "முகப்பு",
        "about": "பற்றி",
        "service": "சேவைகள்",
        "manifesto": "கட்சிக் கொள்கை",
        "login": "உள்நுழை",
        "title": "ஆன்லைன் வாக்குப்பதிவு – இந்திய தேர்தல் ஆணையம்",
        "ministry": "டிஜிட்டல் விவகார அமைச்சகம், இந்திய அரசு"
    },

    "te": {
        "welcome": "ఆన్‌లైన్ ఓటింగ్‌కు స్వాగతం",
        "tagline": "సురక్షిత • పారదర్శక • డిజిటల్ ఇండియా",
        "vote": "ఇప్పుడే ఓటు వేయండి",
        "gov": "భారత ప్రభుత్వం | ఆన్‌లైన్ ఓటింగ్",
        "home": "హోమ్",
        "about": "గురించి",
        "service": "సేవలు",
        "manifesto": "పార్టీ మేనిఫెస్టో",
        "login": "లాగిన్",
        "title": "ఆన్‌లైన్ ఓటింగ్ – భారత ఎన్నికల సంఘం",
        "ministry": "డిజిటల్ వ్యవహారాల మంత్రిత్వ శాఖ, భారత ప్రభుత్వం"
    },

    "ml": {
        "welcome": "ഓൺലൈൻ വോട്ടിംഗിലേക്ക് സ്വാഗതം",
        "tagline": "സുരക്ഷിത • സുതാര്യ • ഡിജിറ്റൽ ഇന്ത്യ",
        "vote": "വോട്ട് ചെയ്യുക",
        "gov": "ഇന്ത്യ സർക്കാർ | ഓൺലൈൻ വോട്ടിംഗ്",
        "home": "ഹോം",
        "about": "കുറിച്ച്",
        "service": "സേവനങ്ങൾ",
        "manifesto": "പാർട്ടി പ്രഖ്യാപനം",
        "login": "ലോഗിൻ",
        "title": "ഓൺലൈൻ വോട്ടിംഗ് – ഇന്ത്യ തിരഞ്ഞെടുപ്പ് കമ്മീഷൻ",
        "ministry": "ഡിജിറ്റൽ കാര്യ മന്ത്രാലയം, ഇന്ത്യ സർക്കാർ"
    }
}


# ---------------- STORE USERS ----------------

users = []


# ---------------- PARTY VOTES ----------------

votes = {
    "TVK": 0,
    "DMK": 0,
    "Congress": 0,
    "ADMK": 0,
    "NTk": 0,
    "BJP": 0,
    "PMK": 0
}

# ---------------- SET LANGUAGE ----------------

@app.route("/set_language/<lang>")
def set_language(lang):
    session["lang"] = lang
    return redirect(request.referrer or url_for("home"))


# ---------------- HOME ----------------

@app.route("/")
@app.route("/home")
def home():
    lang = session.get("lang", "en")
    texts = languages.get(lang, languages["en"])
    return render_template("home.html", texts=texts, lang=lang)


# ---------------- ABOUT ----------------

@app.route("/about")
def about():
    lang = session.get("lang", "en")
    texts = languages.get(lang, languages["en"])
    return render_template("about.html", texts=texts, lang=lang)


# ---------------- SERVICE ----------------

@app.route("/service")
def service():
    lang = session.get("lang", "en")
    texts = languages.get(lang, languages["en"])
    return render_template("service.html", texts=texts, lang=lang)


# ---------------- MANIFESTO ----------------

@app.route("/manifesto")
def manifesto():
    lang = session.get("lang", "en")
    texts = languages.get(lang, languages["en"])
    return render_template("manifesto.html", texts=texts, lang=lang)
#-------------------CONSTITUENCY---------------

@app.route('/constituency')
def constituency():
    return render_template("constituency.html", constituencies=constituencies)


# ---------------- ADMIN LOGIN ----------------

@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            session["admin"] = True
            return redirect("/secure_result")
        else:
            return "Invalid Admin Login ❌"

    return render_template("admin.html")


# ---------------- SECURE RESULT ----------------

@app.route("/secure_result")
def secure_result():

    if "admin" not in session:
        return redirect("/admin")

    return render_template("result.html", votes=votes)

# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        voterid = request.form["voterid"]

        for user in users:
            if user["voterid"] == voterid:
                return "Voter ID already registered ❌"

        users.append({
            "name": request.form["name"],
            "email": request.form["email"],
            "address": request.form["address"],
            "phone": request.form["phone"],
            "aadhar": request.form["aadhar"],
            "voterid": voterid,
            "username": request.form["username"],
            "password": request.form["password"],
            "voted": False
        })

        return redirect("/login")

    return render_template("register.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        for user in users:
            if user["username"] == username and user["password"] == password:

                if user["voted"]:
                    return "You already voted ❌"

                session["user"] = username
                return redirect("/vote")

        return "Invalid Login ❌"

    return render_template("login.html")


# ---------------- VOTE ----------------

@app.route("/vote", methods=["GET", "POST"])
def vote():

    global votes

    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":

        party = request.form["party"]

        if party in votes:
            votes[party] += 1

        for user in users:
            if user["username"] == session["user"]:
                user["voted"] = True

        return redirect("/success")   # ✅ Now correct

    return render_template("vote.html", parties=votes.keys())

# ---------------- SUCCESS PAGE ----------------

@app.route("/success")
def success():
    return render_template("success.html")



# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("admin", None)
    return redirect("/home")


# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)

    #---------------new----------------
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)