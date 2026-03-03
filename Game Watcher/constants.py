FLASK_URL = "http://localhost:5000/control"
POLL_INTERVAL = 2  # segundos entre comprobaciones

GAME_COLORS = {
    "default": {"r": 200, "g": 220, "b": 255},

    # ── Valve ──────────────────────────────────────────────────────────────────
    "Half-Life 2": {"r": 255, "g": 140, "b": 0},
    "Half-Life Deathmatch": {"r": 255, "g": 100, "b": 0},
    "Portal": {"r": 0, "g": 200, "b": 180},
    "Portal 2": {"r": 0, "g": 210, "b": 190},
    "Black Mesa": {"r": 255, "g": 120, "b": 0},
    "Counter-Strike 2": {"r": 255, "g": 160, "b": 0},
    "Team Fortress 2": {"r": 200, "g": 80, "b": 0},
    "Left 4 Dead 2": {"r": 180, "g": 0, "b": 0},

    # ── MOBA ──────────────────────────────────────────────────────────────────
    "League of Legends": {"r": 0, "g": 180, "b": 220},
    "Dota 2": {"r": 180, "g": 0, "b": 0},

    # ── Sandbox / Construcción ─────────────────────────────────────────────────
    "Garry's Mod": {"r": 180, "g": 180, "b": 180},
    "Besiege": {"r": 100, "g": 160, "b": 60},
    "Minecraft": {"r": 100, "g": 180, "b": 60},
    "Terraria": {"r": 80, "g": 200, "b": 80},
    "Stardew Valley": {"r": 120, "g": 200, "b": 80},
    "Factorio": {"r": 200, "g": 140, "b": 0},
    "Satisfactory": {"r": 255, "g": 160, "b": 0},
    "Subnautica": {"r": 0, "g": 160, "b": 220},
    "No Man's Sky": {"r": 255, "g": 100, "b": 0},
    "RimWorld": {"r": 160, "g": 120, "b": 60},

    # ── Rockstar ───────────────────────────────────────────────────────────────
    "Grand Theft Auto IV": {"r": 100, "g": 160, "b": 80},
    "Grand Theft Auto V": {"r": 0, "g": 180, "b": 120},
    "Red Dead Redemption 2": {"r": 180, "g": 80, "b": 30},

    # ── Battle Royale / Shooter ────────────────────────────────────────────────
    "PUBG": {"r": 200, "g": 160, "b": 60},
    "Fortnite": {"r": 100, "g": 200, "b": 255},
    "Apex Legends": {"r": 180, "g": 60, "b": 0},
    "Valorant": {"r": 255, "g": 60, "b": 60},
    "Overwatch": {"r": 255, "g": 180, "b": 0},
    "Battlefield™ 6": {"r": 200, "g": 120, "b": 0},
    "Call of Duty": {"r": 60, "g": 80, "b": 40},
    "Rainbow Six Siege": {"r": 0, "g": 100, "b": 180},

    # ── Soulslike / Action RPG ─────────────────────────────────────────────────
    "ELDEN RING": {"r": 220, "g": 180, "b": 40},
    "DARK SOULS™ III": {"r": 180, "g": 30, "b": 30},
    "DARK SOULS™: REMASTERED": {"r": 160, "g": 20, "b": 20},
    "Sekiro": {"r": 200, "g": 0, "b": 0},
    "Bloodborne": {"r": 120, "g": 0, "b": 0},

    # ── RPG / Mundo Abierto ────────────────────────────────────────────────────
    "The Witcher 3": {"r": 180, "g": 120, "b": 200},
    "Kingdom Come: Deliverance": {"r": 140, "g": 100, "b": 40},
    "Dishonored": {"r": 60, "g": 0, "b": 100},
    "Dishonored 2": {"r": 80, "g": 0, "b": 120},
    "Hogwarts Legacy": {"r": 120, "g": 60, "b": 200},
    "The Elder Scrolls V: Skyrim": {"r": 100, "g": 140, "b": 200},
    "The Elder Scrolls IV: Oblivion": {"r": 150, "g": 200, "b": 100},
    "Mass Effect™ Legendary Edition": {"r": 0, "g": 120, "b": 255},
    "Fallout: New Vegas": {"r": 180, "g": 200, "b": 0},
    "Fallout 4": {"r": 160, "g": 180, "b": 0},
    "Cyberpunk 2077": {"r": 255, "g": 220, "b": 0},
    "Baldur's Gate 3": {"r": 140, "g": 0, "b": 180},
    "Dragon Age: Origins": {"r": 160, "g": 0, "b": 40},
    "Divinity: Original Sin 2": {"r": 200, "g": 60, "b": 0},
    "Pathfinder: Wrath of the Righteous": {"r": 200, "g": 100, "b": 0},

    # ── Metro ──────────────────────────────────────────────────────────────────
    "Metro 2033 Redux": {"r": 60, "g": 80, "b": 60},
    "Metro: Last Light Redux": {"r": 50, "g": 70, "b": 50},
    "Metro Exodus": {"r": 70, "g": 100, "b": 60},

    # ── Terror / Suspense ──────────────────────────────────────────────────────
    "SOMA": {"r": 0, "g": 60, "b": 120},
    "Dying Light": {"r": 0, "g": 180, "b": 60},
    "Little Nightmares": {"r": 80, "g": 60, "b": 20},
    "Lethal Company": {"r": 0, "g": 200, "b": 80},
    "Phasmophobia": {"r": 0, "g": 80, "b": 60},
    "Alien: Isolation": {"r": 200, "g": 120, "b": 0},
    "Resident Evil 2": {"r": 180, "g": 0, "b": 0},
    "Resident Evil 4": {"r": 100, "g": 140, "b": 40},
    "Amnesia": {"r": 40, "g": 20, "b": 60},

    # ── Indie / Plataformas ────────────────────────────────────────────────────
    "Hollow Knight": {"r": 80, "g": 0, "b": 160},
    "Hollow Knight: Silksong": {"r": 100, "g": 0, "b": 200},
    "Celeste": {"r": 255, "g": 100, "b": 150},
    "Cuphead": {"r": 255, "g": 80, "b": 40},
    "Blasphemous": {"r": 180, "g": 0, "b": 0},
    "The Binding of Isaac: Rebirth": {"r": 140, "g": 0, "b": 0},
    "Crash Bandicoot™ N. Sane Trilogy": {"r": 255, "g": 120, "b": 0},
    "Ori and the Will of the Wisps": {"r": 180, "g": 220, "b": 255},
    "Shovel Knight": {"r": 60, "g": 100, "b": 200},

    # ── Roguelike ─────────────────────────────────────────────────────────────
    "Hades": {"r": 255, "g": 60, "b": 0},
    "Hades II": {"r": 200, "g": 0, "b": 120},
    "Balatro": {"r": 180, "g": 0, "b": 60},
    "Slay the Spire": {"r": 60, "g": 0, "b": 160},
    "Vampire Survivors": {"r": 200, "g": 0, "b": 60},
    "Cult of the Lamb": {"r": 160, "g": 0, "b": 80},
    "Loop Hero": {"r": 0, "g": 120, "b": 80},
    "Enter the Gungeon": {"r": 255, "g": 180, "b": 0},
    "Dead Cells": {"r": 200, "g": 60, "b": 0},
    "Risk of Rain 2": {"r": 100, "g": 0, "b": 200},

    # ── Narrative / Puzzle ─────────────────────────────────────────────────────
    "Disco Elysium": {"r": 180, "g": 100, "b": 60},
    "Outer Wilds": {"r": 255, "g": 180, "b": 60},
    "Papers, Please": {"r": 120, "g": 100, "b": 60},
    "Return of the Obra Dinn": {"r": 220, "g": 220, "b": 180},
    "Undertale": {"r": 0, "g": 160, "b": 160},
    "Omori": {"r": 255, "g": 200, "b": 220},
    "What Remains of Edith Finch": {"r": 120, "g": 160, "b": 120},
    "Inside": {"r": 60, "g": 40, "b": 60},

    # ── Estrategia / Táctica ───────────────────────────────────────────────────
    "XCOM 2": {"r": 0, "g": 160, "b": 220},
    "Civilization VI": {"r": 180, "g": 140, "b": 0},
    "Total War: Warhammer III": {"r": 180, "g": 0, "b": 0},
    "Age of Empires IV": {"r": 180, "g": 120, "b": 0},
    "Crusader Kings III": {"r": 120, "g": 0, "b": 0},

    # ── Multijugador / Cooperativo ─────────────────────────────────────────────
    "HELLDIVERS™ 2": {"r": 200, "g": 180, "b": 0},
    "Warhammer 40,000: Space Marine": {"r": 180, "g": 20, "b": 20},
    "PAYDAY 2": {"r": 220, "g": 60, "b": 0},
    "ARC Raiders": {"r": 60, "g": 180, "b": 120},
    "Don't Starve Together": {"r": 60, "g": 40, "b": 20},
    "Tabletop Simulator": {"r": 80, "g": 140, "b": 80},
    "Duck Game": {"r": 255, "g": 200, "b": 0},
    "Fall Guys": {"r": 255, "g": 100, "b": 200},
    "SpeedRunners": {"r": 255, "g": 160, "b": 0},
    "Among Us": {"r": 200, "g": 0, "b": 0},
    "It Takes Two": {"r": 255, "g": 140, "b": 0},
    "Split Fiction": {"r": 0, "g": 200, "b": 255},

    # ── Simulación / Deportes ──────────────────────────────────────────────────
    "F1® 25": {"r": 220, "g": 0, "b": 0},
    "NBA 2K19": {"r": 0, "g": 80, "b": 200},
    "Golf It!": {"r": 60, "g": 200, "b": 60},
    "Rocket League": {"r": 0, "g": 160, "b": 255},
    "FIFA": {"r": 0, "g": 180, "b": 60},
    "EA FC": {"r": 0, "g": 180, "b": 60},

    # ── Acción / Cyberpunk / Sci-Fi ────────────────────────────────────────────
    "Ghostrunner 2": {"r": 0, "g": 220, "b": 255},
    "9 Kings": {"r": 200, "g": 160, "b": 0},
    "Shotgun King: The Final Checkmate": {"r": 220, "g": 220, "b": 220},
    "Doom Eternal": {"r": 220, "g": 60, "b": 0},
    "Prey": {"r": 0, "g": 160, "b": 200},
    "Deus Ex: Mankind Divided": {"r": 200, "g": 140, "b": 0},

    # ── Aventura / Exploración ─────────────────────────────────────────────────
    "Horizon Zero Dawn": {"r": 255, "g": 160, "b": 0},
    "Ghost of Tsushima": {"r": 255, "g": 120, "b": 60},
    "Death Stranding": {"r": 80, "g": 160, "b": 120},
    "Journey": {"r": 220, "g": 160, "b": 40},

    # ── Varios Steam ──────────────────────────────────────────────────────────
    "Black Desert": {"r": 100, "g": 0, "b": 160},
    "Prince of Persia: The Two Thrones": {"r": 180, "g": 100, "b": 0},
    "Sid Meier's Pirates!": {"r": 0, "g": 100, "b": 180},
    "Arma Tactics": {"r": 60, "g": 80, "b": 40},
    "Half Sword Playtest": {"r": 160, "g": 60, "b": 0},
}