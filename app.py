import tkinter as tk
from tkinter import ttk

# Unified Elemental Database as a dictionary
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

def update_culture_dropdown(*args):
    element = element_var.get()
    if element:
        cultures = list(database[element]['cultures'].keys())
        culture_dropdown['values'] = cultures
        culture_var.set('')  # Clear current selection
        output_label.config(text="Select a culture to view details.")

def update_output(*args):
    element = element_var.get()
    culture = culture_var.get()
    if element and culture:
        data = database[element]['cultures'][culture]
        output_text = f"Element: {element} 🌟\nDescription: {database[element]['description']}\n\nSpirit Animal: {data['animal']}\nProperties: {data['properties']}\nDirection/Season: {data['direction_season']}\n\nExplore links: This cultural inference highlights unique flavors while connecting to shared themes across traditions, such as power in dragons or growth in earth symbols."
        output_label.config(text=output_text)

# Create GUI
root = tk.Tk()
root.title("Unified Elemental Explorer")

# Element dropdown
element_label = ttk.Label(root, text="Select Element:")
element_label.grid(row=0, column=0, padx=10, pady=5)
element_var = tk.StringVar()
element_dropdown = ttk.Combobox(root, textvariable=element_var, values=list(database.keys()), state="readonly")
element_dropdown.grid(row=0, column=1, padx=10, pady=5)
element_dropdown.bind("<<ComboboxSelected>>", update_culture_dropdown)

# Culture dropdown
culture_label = ttk.Label(root, text="Select Culture:")
culture_label.grid(row=1, column=0, padx=10, pady=5)
culture_var = tk.StringVar()
culture_dropdown = ttk.Combobox(root, textvariable=culture_var, state="readonly")
culture_dropdown.grid(row=1, column=1, padx=10, pady=5)
culture_dropdown.bind("<<ComboboxSelected>>", update_output)

# Output
output_label = ttk.Label(root, text="Select an element and culture to view details.", wraplength=400, justify="left")
output_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()