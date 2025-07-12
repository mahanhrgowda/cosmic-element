import streamlit as st
import datetime
from math import sin, radians, degrees
import zoneinfo

# Unified Elemental Database
database = {
    "Wood/Earth": {
        "description": "Represents grounding, growth, stability, nourishment, and physicality. Emojis evoke fertility and roots.",
        "cultures": {
            "Chinese/Taoist": {
                "animal": "Azure Dragon (Qinglong) 🐉",
                "properties": "Growth, renewal, vitality, health, strength, luck, fertility, power, wisdom, yang energy.",
                "direction_season": "East/Spring."
            },
            "Japanese": {
                "animal": "Kirin/Qilin or Yellow Dragon 🦄🐉",
                "properties": "Grounding, benevolence, stability, expansion, harvest influence.",
                "direction_season": "Center/Late Summer (Earth/Chi)."
            },
            "Western Occult": {
                "animal": "Gnome (dwarf-like spirit) or Bull/Bear 🧑‍🌾🐂",
                "properties": "Stability, growth, physicality, protection, endurance.",
                "direction_season": "North/Winter."
            },
            "Native American": {
                "animal": "Turtle, Bear, or Buffalo 🐢🐻",
                "properties": "Balance, introspection, healing, endurance, provision, interconnectedness.",
                "direction_season": "North or Center/Winter or Late Summer."
            },
            "Hindu": {
                "animal": "Cow or Elephant 🐄🐘",
                "properties": "Grounding, nourishment, stability, fertility (linked to Prithvi).",
                "direction_season": "Varied (cosmic foundation)."
            },
            "Celtic/Druidic": {
                "animal": "Bear, Bull, or Tree/Stag 🐻🌳",
                "properties": "Strength, fertility, protection, sovereignty.",
                "direction_season": "North/Winter."
            }
        }
    },
    "Fire": {
        "description": "Symbolizes passion, transformation, energy, destruction/creation, and vigor. Emojis highlight heat and rebirth.",
        "cultures": {
            "Chinese/Taoist": {
                "animal": "Vermilion Bird (Zhuque, phoenix-like) 🐦‍🔥",
                "properties": "Vigor, elegance, virtue, duty, success, joy, confidence, strong yang energy.",
                "direction_season": "South/Summer."
            },
            "Japanese": {
                "animal": "Vermilion Bird or Phoenix (Houou) 🐦‍🔥",
                "properties": "Rebirth, energy, transformation, harmony.",
                "direction_season": "South/Summer (Ka)."
            },
            "Western Occult": {
                "animal": "Salamander (lizard spirit) or Lion 🦎🦁",
                "properties": "Passion, will, destruction/creation, light.",
                "direction_season": "South/Summer."
            },
            "Native American": {
                "animal": "Coyote, Mouse, or Falcon 🐺🐭🦅",
                "properties": "Adaptability, growth, innocence, enlightenment (fire-like energy).",
                "direction_season": "South/Summer."
            },
            "Hindu": {
                "animal": "Ram or Lion 🐏🦁",
                "properties": "Transformation, light, sacrifice, purification (Agni).",
                "direction_season": "Varied (cosmic heat)."
            },
            "Celtic/Druidic": {
                "animal": "Salmon or Boar 🐟🐗",
                "properties": "Wisdom, courage, transformation, warrior spirit.",
                "direction_season": "South/Summer."
            }
        }
    },
    "Metal/Air/Wind": {
        "description": "Encompasses movement, intellect, harvest, ferocity, and intuition. Emojis suggest flow and sharpness.",
        "cultures": {
            "Chinese/Taoist": {
                "animal": "White Tiger (Baihu) 🐅",
                "properties": "Harvest, bravery, protection, intuition, motherhood, prudence, yin energy.",
                "direction_season": "West/Autumn."
            },
            "Japanese": {
                "animal": "White Tiger (Byakko) 🐅",
                "properties": "Movement, ferocity, protection, creativity.",
                "direction_season": "West/Autumn (Fu/Wind)."
            },
            "Western Occult": {
                "animal": "Sylph (airy fairy) or Eagle/Bird 🧚‍♀️🦅",
                "properties": "Intellect, communication, winds, vision.",
                "direction_season": "East/Spring."
            },
            "Native American": {
                "animal": "Eagle or Butterfly 🦅🦋",
                "properties": "Vision, enlightenment, spiritual connection, adaptability.",
                "direction_season": "East/Spring."
            },
            "Hindu": {
                "animal": "Bird (Peacock or Garuda/Eagle) 🦚🦅",
                "properties": "Movement, breath, freedom, divine knowledge (Vayu).",
                "direction_season": "Varied (atmospheric flow)."
            },
            "Celtic/Druidic": {
                "animal": "Hawk or Raven 🦅🐦‍⬛",
                "properties": "Vision, prophecy, air/wind, insight.",
                "direction_season": "East/Spring."
            }
        }
    },
    "Water": {
        "description": "Denotes flow, emotions, endurance, adaptability, and intuition. Emojis reflect fluidity and depth.",
        "cultures": {
            "Chinese/Taoist": {
                "animal": "Black Tortoise/Black Warrior (Xuanwu) 🐢",
                "properties": "Stability, longevity, endurance, happiness, mental agility, balance.",
                "direction_season": "North/Winter."
            },
            "Japanese": {
                "animal": "Black Tortoise (Genbu) or Sea Creatures 🐢🌊",
                "properties": "Flow, adaptability, night, wisdom.",
                "direction_season": "North/Winter (Sui)."
            },
            "Western Occult": {
                "animal": "Undine (water nymph) or Dolphin/Fish 🧜‍♀️🐬",
                "properties": "Emotions, intuition, healing, purification.",
                "direction_season": "West/Autumn."
            },
            "Native American": {
                "animal": "Frog, Deer, or White Wolf 🐸🦌🐺",
                "properties": "Healing, grace, introspection, provision.",
                "direction_season": "West/Autumn."
            },
            "Hindu": {
                "animal": "Fish or Makara (sea-goat) 🐟🐐",
                "properties": "Fluidity, life-giving, purification, intuition (Apas).",
                "direction_season": "Varied (cosmic waters)."
            },
            "Celtic/Druidic": {
                "animal": "Deer (Hind), Swan, or Salmon 🦌🦢🐟",
                "properties": "Grace, love, otherworld journeys, wisdom.",
                "direction_season": "West/Autumn."
            }
        }
    },
    "Spirit/Ether/Void": {
        "description": "The transcendent element for spirituality, infinity, balance, and divine connection. Emojis convey ethereal mystery.",
        "cultures": {
            "Chinese/Taoist": {
                "animal": "Yellow Dragon (Huanglong) or Kirin 🐉🦄",
                "properties": "Heaven, divine guardianship, invincibility, transformation, center balance.",
                "direction_season": "Center/All Seasons."
            },
            "Japanese": {
                "animal": "Azure Dragon (Seiryu) 🐉",
                "properties": "Spirituality, creativity, the infinite, void harmony.",
                "direction_season": "East or Center/Varied (Ku/Void)."
            },
            "Western Occult": {
                "animal": "Phoenix, Dragon, or Angelic Figure 🐦‍🔥🐉😇",
                "properties": "Transcendence, unity, ethereal being, enlightenment.",
                "direction_season": "Center/All."
            },
            "Native American": {
                "animal": "Spider, Tree, or Turtle (central) 🕷️🌳🐢",
                "properties": "Creation, interconnectedness, spirit guidance.",
                "direction_season": "Center/All Cycles."
            },
            "Hindu": {
                "animal": "Human, Swan (Hamsa), or Ether Symbol 👤🦢",
                "properties": "Sound, space, divine knowledge, cosmic consciousness (Akasha).",
                "direction_season": "Varied (universal ether)."
            },
            "Celtic/Druidic": {
                "animal": "Stag or Tree 🦌🌳",
                "properties": "Sovereignty, interconnectedness, animistic spirit.",
                "direction_season": "Center/All."
            }
        }
    }
}

# List of Nakshatras
nakshatras = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
    "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
    "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati",
    "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
    "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha", "Purva Bhadrapada",
    "Uttara Bhadrapada", "Revati"
]

# Mapping Nakshatra to Siddha Force for Shukla and Krishna Paksha
def get_siddha_force(nak_name, paksha):
    nak_index = nakshatras.index(nak_name)
    if paksha == "Shukla":
        if 0 <= nak_index <= 4:
            return "Vulture-Ether 🦅🌌"
        elif 5 <= nak_index <= 10:
            return "Owl-Air 🦉💨"
        elif 11 <= nak_index <= 15:
            return "Crow-Fire 🐦‍⬛🔥"
        elif 16 <= nak_index <= 20:
            return "Cock-Water 🐓🌊"
        else:  # 21-26
            return "Peacock-Earth 🦚🌍"
    else:  # Krishna
        if 0 <= nak_index <= 4:
            return "Peacock-Earth 🦚🌍"
        elif 5 <= nak_index <= 10:
            return "Cock-Water 🐓🌊"
        elif 11 <= nak_index <= 15:
            return "Crow-Fire 🐦‍⬛🔥"
        elif 16 <= nak_index <= 20:
            return "Owl-Air 🦉💨"
        else:  # 21-26
            return "Vulture-Ether 🦅🌌"

# Descriptions for each Siddha Force
descriptions = {
    "Vulture-Ether 🦅🌌": "🌟 As the Vulture-Ether force governs your essence 🦅🌌, you embody profound intuition and spiritual detachment, soaring high above earthly concerns like a vulture circling the skies. 🦅✨ Your life path is marked by visionary insights and a deep connection to the cosmos, allowing you to perceive hidden truths that others miss. 🌌🔮 In challenges, you rise with resilience, transforming obstacles into opportunities for growth. 💪🌱 Your personality radiates a mysterious aura, drawing people to your wisdom, yet you maintain independence, avoiding superficial bonds. 🤝🚫 Relationships flourish when you embrace vulnerability, balancing your ethereal nature with grounded emotions. ❤️🌍 Career-wise, fields like spirituality, research, or aviation suit you, where your broad perspectives shine. ✈️📚 Health may involve occasional detachment from physical needs, so prioritize meditation and etheric practices like yoga to stay balanced. 🧘‍♂️🍃 Karmically, past lives of exploration grant you current-life gifts in foresight, but beware of isolation—engage with community for fulfillment. 👥🌟 Auspicious times align when your force is in Ruling state, empowering bold decisions. ⏰👑 Overall, embrace your soaring spirit to manifest dreams, turning the intangible into reality with grace and power. 🦅💫 This divination reveals a journey of enlightenment, where ether's vastness fuels your eternal quest for truth and freedom. 🌌🕊️ Lengthy paths await, filled with cosmic wonders and self-discovery. 🚀📖",
    "Owl-Air 🦉💨": "🌟 Guided by the Owl-Air force 🦉💨, your core vibrates with intellectual wisdom and adaptable winds of change, much like an owl navigating the night with silent wings. 🦉🌬️ You possess sharp analytical skills and a thirst for knowledge, making you a natural learner and communicator in all realms. 📚🗣️ Life's winds may shift directions, but your flexibility turns them into advantages, fostering innovation and quick adaptations. 🔄💡 Personality-wise, you're witty and curious, enchanting others with your insights, though restlessness can lead to scattered energies—focus is key. 🎯🤔 In love, air's flow brings dynamic partnerships; nurture stability to avoid fleeting connections. ❤️🏠 Careers in writing, teaching, or technology harness your airy intellect for success. 💻🖋️ Health benefits from breathing exercises and fresh air, countering any nervous tendencies. 🌬️🧘 Karmic threads from past intellectual pursuits gift you eloquence, but learn patience to avoid superficiality. ⏳👥 Favorable periods emerge in Harmonizing states, ideal for collaborations and ideas. 🤝⏰ This Siddha force propels you toward enlightened adaptability, where air's freedom unlocks boundless potentials. 💨🕊️ Your divination unfolds as a whirlwind of discoveries, blending wisdom with whimsy for a fulfilling existence. 🌪️📖 Profound transformations await as you ride the currents of destiny with grace. 🚀✨",
    "Crow-Fire 🐦‍⬛🔥": "🌟 The Crow-Fire force ignites your being 🐦‍⬛🔥, symbolizing vigilant transformation and communal energy, akin to a crow's clever spark amid flames. 🐦‍⬛🕯️ You exude passion and leadership, driving change with fiery determination and sharp observation. 🔥👀 Life's trials forge you stronger, turning adversity into triumphs through resourcefulness. ⚒️🏆 Your personality is energetic and social, thriving in groups where your charisma shines, but temper impulsiveness to build lasting alliances. 👥😊 Relationships burn brightly; channel fire's warmth for deep bonds, avoiding conflicts. ❤️🔥 Ideal careers include management, activism, or arts, where your fire fuels creativity. 🎨📈 Health requires cooling practices like hydration and calm activities to balance heat. 💧🧘 Karmically, past communal roles endow you with networking prowess, but resolve old rivalries. 🤝🕰️ Optimal times in Observing states enhance vigilance for opportunities. 👁️⏰ This force divines a path of passionate evolution, where fire's light illuminates success and connections. 🔥🌟 Your journey is a blazing trail of achievements, embroidered with transformative experiences and joyful camaraderie. 🚀📖 Embrace the flames to forge a legacy of inspiration and warmth. 🐦‍⬛💫",
    "Cock-Water 🐓🌊": "🌟 Under the Cock-Water force's influence 🐓🌊, you reflect alertness and emotional renewal, like a rooster heralding dawn over flowing waters. 🐓💦 Your essence is protective and fluid, navigating life's currents with intuition and resilience. 🌊🛡️ You excel in empathy and healing, offering support that refreshes souls around you. 🤗💙 Challenges dissolve in your adaptable flow, emerging stronger through emotional depths. 🌊💪 Personality radiates charm and vigilance, fostering nurturing environments, though over-sensitivity needs boundaries. 🛡️😌 Love thrives in watery depths; seek partners who match your depth for harmonious unions. ❤️🌊 Careers in counseling, healthcare, or marine fields align with your watery vigilance. 🩺🚢 Health flourishes with water-based activities and emotional release practices. 🏊🧘 Karmic echoes from protective pasts grant intuitive gifts, but release fears for growth. 🕊️🕰️ Prime moments in Querying states aid insightful decisions and healings. ❓⏰ This divination promises a refreshing voyage, where water's flow carries you to emotional fulfillment and prosperity. 🌊🌟 Waves of opportunity and serenity define your path, enriched with profound connections and renewals. 🚀📖 Let the waters guide your vigilant spirit to shores of abundance. 🐓💫",
    "Peacock-Earth 🦚🌍": "🌟 The Peacock-Earth force grounds your soul 🦚🌍, embodying beauty, stability, and manifestation, as a peacock displays splendor on solid ground. 🦚🌳 You manifest creativity and reliability, building lasting foundations with artistic flair. 🎨🛠️ Life's beauty unfolds through your efforts, turning visions into tangible realities. 🌍💎 Your personality is grounded yet vibrant, attracting admiration with poise, but avoid rigidity by embracing change. 😊🔄 Relationships bloom in stable soils; cultivate openness for colorful unions. ❤️🌿 Careers in design, agriculture, or business leverage your earthly grace for success. 🏗️🌱 Health stabilizes with nature walks and balanced diets, rooting your vitality. 🌳🍎 Karmic roots from creative lifetimes bestow manifestation powers, but humility tempers pride. 🌟🕰️ Auspicious phases in Remediating states foster healing and growth. 🛠️⏰ This force foretells a grounded odyssey, where earth's bounty yields beauty and security. 🌍🦚 Your divination is a tapestry of achievements, woven with elegance, stability, and joyous expressions. 🚀📖 Dance through life with peacock's allure, creating a world of enduring wonder. 💫🌟"
}

# String Theory Mappings
string_mappings = {
    "Ether": "Ether (Akasha) ↔ Type IIB: Ether, the all-encompassing void of space in Vedic lore, echoes Type IIB’s self-dual, chiral strings that mirror infinite reflections like Indra’s Net in Rashmi vibrations! 🌌🕸️🔄 Soar through boundless dimensions, weaving cosmic harmony like a starry dance party! ✨💃🌠",
    "Air": "Air (Vayu) ↔ Heterotic E8×E8: Vayu, the dynamic wind of motion and breath from Brahma Sutra’s creation cycles, aligns with Heterotic E8×E8’s grand unified symmetries—hybrid strings zipping like Rashmi rays across the universe! 💨🌀⚡ Gust through challenges with whirlwind wisdom, turning breezy chaos into epic adventures! 🌪️🚀😎",
    "Fire": "Fire (Tejas) ↔ Type I: Tejas, the transformative blaze illuminating Vedic dissolution and rebirth, matches Type I’s open-closed strings that spark like fiery Rashmi threads in the cosmic forge! 🔥🧵💥 Ignite passions with blazing trails, roasting obstacles into victory s’mores! 🌟🏆🍫",
    "Water": "Water (Apas) ↔ Type IIA: Apas, the fluid essence flowing through Brahma Sutra’s maintenance of existence, flows like Type IIA’s balanced chiral strings—Rashmi waves rippling in eternal cycles! 🌊🌀💧 Dive deep into emotional oceans, surfing waves of adaptability with mermaid flair! 🏄‍♀️🔮🧜‍♀️",
    "Earth": "Earth (Prithvi) ↔ Heterotic SO(32): Prithvi, the stable foundation grounding Vedic creation as per Rashmi’s woven fabric, grounds Heterotic SO(32)’s hybrid symmetries like rooted strings threading the material world! 🌍🌿🧶 Build unbreakable empires with earthy vibes, planting seeds of cosmic stability like a boss gardener! 🏰🌱👑"
}

def datetime_to_jd(dt):
    if dt.month < 3:
        y = dt.year - 1
        m = dt.month + 12
    else:
        y = dt.year
        m = dt.month
    a = y // 100
    b = 2 - a + a // 4
    jd = int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + dt.day + b - 1524.5
    jd += dt.hour / 24.0 + dt.minute / 1440.0 + dt.second / 86400.0
    return jd

def moon_long(mjd, dt_tt=69.184):
    T = (mjd - 51544.5 + dt_tt / 86400) / 36525
    L0 = radians(218.31617 + 481267.88088 * T)
    l = radians(134.96292 + 477198.86753 * T)
    lp = radians(357.52543 + 35999.04944 * T)
    F = radians(93.27283 + 483202.01873 * T)
    D = radians(297.85027 + 445267.11135 * T)
    dL = radians((22640 * sin(l) + 769 * sin(2 * l)
        - 4586 * sin(l - 2 * D) + 2370 * sin(2 * D)
        - 668 * sin(lp) - 412 * sin(2 * F)
        - 212 * sin(2 * l - 2 * D) - 206 * sin(l + lp - 2 * D)
        + 192 * sin(l + 2 * D) - 165 * sin(lp - 2 * D)
        + 148 * sin(l - lp) - 125 * sin(D)
        - 110 * sin(l + lp) - 55 * sin(2 * F - 2 * D)) / 3600)
    lon = L0 + dL
    return degrees(lon) % 360

def sun_long(mjd, dt_tt=69.184):
    T = (mjd - 51544.5 + dt_tt / 86400) / 36525
    M = radians(357.52772 + 35999.05034 * T - 0.0001603 * T**2 - T**3 / 300000)
    L0 = radians(280.46646 + 36000.76983 * T + 0.0003032 * T**2)
    DL = (1.914602 - T * (0.004817 + 0.000014 * T)) * sin(M) + (0.019993 - 0.000101 * T) * sin(2 * M) + 0.000289 * sin(3 * M)
    L = L0 + radians(DL)
    omega = 125.04 - 1934.136 * T
    lambda_ = degrees(L) - 0.00569 - 0.00478 * sin(radians(omega))
    return lambda_ % 360

def get_lahiri_ayanamsa(decimal_year):
    base_ayan = 23 + 9/60 + 18/3600  # 23.155 degrees in 1950
    rate = 50.2388475 / 3600  # degrees per year
    return base_ayan + rate * (decimal_year - 1950)

# Streamlit App
st.title("Cosmic Element Weaver 🔮🦅🧵")

st.write("Enter your birth details (UTC time) to weave your Siddha Pakshi force with cultural insights and cosmic string vibes! 🌍⏰ Select a culture to customize the elemental output.")

birth_date = st.date_input("Birth Date 📅", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 12, 31), value=datetime.date(1993, 7, 12))
birth_time = st.time_input("Birth Time ⏰", value=datetime.time(12, 26), step=datetime.timedelta(minutes=1))
place = st.text_input("Place of Birth 🏙️ (Optional)")
timezones = sorted(zoneinfo.available_timezones())
timezone = st.selectbox("Timezone 🌍", timezones, index=timezones.index("Asia/Kolkata") if "Asia/Kolkata" in timezones else 0)
culture = st.selectbox("Select Culture 🌐", options=["Chinese/Taoist", "Japanese", "Western Occult", "Native American", "Hindu", "Celtic/Druidic"])

if st.button("Weave Insights ✨"):
    if birth_date and birth_time:
        local_dt = datetime.datetime.combine(birth_date, birth_time)
        local_tz = zoneinfo.ZoneInfo(timezone)
        local_dt = local_dt.replace(tzinfo=local_tz)
        utc_dt = local_dt.astimezone(zoneinfo.ZoneInfo("UTC"))
        dt = utc_dt
        decimal_year = dt.year + (dt.timetuple().tm_yday - 1) / 365.0
        jd = datetime_to_jd(dt)
        mjd = jd - 2400000.5
        moon_lon = moon_long(mjd)
        sun_lon = sun_long(mjd)
        ayan = get_lahiri_ayanamsa(decimal_year)
        moon_sid = (moon_lon - ayan) % 360
        sun_sid = (sun_lon - ayan) % 360
        elong = (moon_sid - sun_sid) % 360
        paksha = "Shukla" if elong < 180 else "Krishna"
        nak_index = int(moon_sid // (360 / 27))
        nak_name = nakshatras[nak_index % 27]
        force = get_siddha_force(nak_name, paksha)
        element_part = force.split('-')[1].split(' ')[0]  # e.g., "Ether"
        
        # Map to database key
        if element_part == "Earth":
            db_key = "Wood/Earth"
        elif element_part == "Air":
            db_key = "Metal/Air/Wind"
        elif element_part == "Ether":
            db_key = "Spirit/Ether/Void"
        else:
            db_key = element_part  # Fire, Water
        
        # Get cultural data
        if db_key in database and culture in database[db_key]['cultures']:
            cult_data = database[db_key]['cultures'][culture]
            elem_desc = database[db_key]['description']
            output_text = f"**Spirit Animal:** {cult_data['animal']}\n\n**Properties:** {cult_data['properties']}\n\n**Direction/Season:** {cult_data['direction_season']}\n\nExplore links: This cultural inference highlights unique flavors while connecting to shared themes across traditions, such as power in dragons or growth in earth symbols."
        else:
            output_text = "No data available for this combination."
        
        # String mapping
        string_desc = string_mappings.get(element_part, "No cosmic string vibe found! 🌌")
        
        # Display
        st.subheader(f"Insights for {place or 'Mystic Realm'} Birth 🌟")
        st.write(f"**Nakshatra:** {nak_name} ⭐")
        st.write(f"**Paksha:** {paksha} 🌒🌘")
        st.write(f"**Your Siddha Force:** {force}")
        st.write(descriptions[force])
        st.subheader(f"Elemental View in {culture} Culture 🌍")
        st.write(f"**Element Description:** {elem_desc}")
        st.write(output_text)
        st.subheader("Cosmic String Analogy 🧵")
        st.write(string_desc)
    else:
        st.warning("Please enter birth date and time. ⚠️")
