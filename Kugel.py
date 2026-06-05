import pygame
import pygame.gfxdraw
import random
import sys
import os
import json
from pathlib import Path

# --- Resource Path für PyInstaller EXE ---
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS          # EXE: temporäres Entpack-Verzeichnis
    except AttributeError:
        base_path = os.path.abspath('.')  # normaler Python-Start
    return os.path.join(base_path, relative_path)


def get_settings_path():
    # Findet automatisch den richtigen Ordner für das jeweilige Betriebssystem:
    # Windows:    C:\Users\Name\AppData\Roaming\BallSortPuzzle\settings.json
    # Mac/Linux:  /home/name/.config/BallSortPuzzle/settings.json
    if sys.platform == "win32":
        base_dir = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    else:
        base_dir = Path.home() / ".config"
        
    app_dir = base_dir / "BallSortPuzzle"
    
    # Erstellt den Ordner "BallSortPuzzle", falls er noch nicht existiert
    app_dir.mkdir(parents=True, exist_ok=True)
    return app_dir / "settings.json"

SETTINGS_FILE = get_settings_path()

def load_settings():
    try:
        # encoding="utf-8" sorgt dafür, dass kyrillische/tschechische Zeichen fehlerfrei geladen werden
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_settings(data):
    try:
        # indent=4 macht die JSON-Datei schön lesbar, falls du mal reinschauen willst
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except:
        pass

# --- Sprachsystem ---
# Neue Sprache hinzufügen:
# 1. Neuen Block in LANGUAGES eintragen
# 2. Kürzel in LANGUAGE_ORDER eintragen
# → Erscheint automatisch im Auswahlfenster

LANGUAGES = {
    "DE": {
        "name":         "Deutsch",
        "title":        "BALL SORT",
        "easy":         "Einfach",
        "medium":       "Mittel",
        "hard":         "Schwer",
        "sound_on":     "Ton: AN",
        "sound_off":    "Ton: AUS",
        "language_btn": "🌐 Sprache",
        "select_lang":  "Sprache wählen",
        "moves":        "Züge",
        "level":        "Level",
        "menu":         "Menü",
        "undo":         "Undo",
        "won":          "GEWONNEN!",
        "again":        "Nochmal",
        "to_menu":      "Zum Menü",
        "quit":         "Beenden",
    },
    "EN": {
        "name":         "English",
        "title":        "BALL SORT",
        "easy":         "Easy",
        "medium":       "Medium",
        "hard":         "Hard",
        "sound_on":     "Sound: ON",
        "sound_off":    "Sound: OFF",
        "language_btn": "🌐 Language",
        "select_lang":  "Select Language",
        "moves":        "Moves",
        "level":        "Level",
        "menu":         "Menu",
        "undo":         "Undo",
        "won":          "YOU WON!",
        "again":        "Play Again",
        "to_menu":      "Main Menu",
        "quit":         "Quit",
    },
    "FR": {
        "name":         "Français",
        "title":        "BALL SORT",
        "easy":         "Facile",
        "medium":       "Moyen",
        "hard":         "Difficile",
        "sound_on":     "Son: ACTIVÉ",
        "sound_off":    "Son: DÉSACTIVÉ",
        "language_btn": "🌐 Langue",
        "select_lang":  "Choisir la langue",
        "moves":        "Coups",
        "level":        "Niveau",
        "menu":         "Menu",
        "undo":         "Annuler",
        "won":          "GAGNÉ!",
        "again":        "Rejouer",
        "to_menu":      "Menu Principal",
        "quit":         "Quitter",
    },
    "ES": {
        "name":         "Español",
        "title":        "BALL SORT",
        "easy":         "Fácil",
        "medium":       "Medio",
        "hard":         "Difícil",
        "sound_on":     "Sonido: SÍ",
        "sound_off":    "Sonido: NO",
        "language_btn": "🌐 Idioma",
        "select_lang":  "Seleccionar idioma",
        "moves":        "Movimientos",
        "level":        "Nivel",
        "menu":         "Menú",
        "undo":         "Deshacer",
        "won":          "¡GANASTE!",
        "again":        "Jugar de nuevo",
        "to_menu":      "Menú principal",
        "quit":         "Salir",
    },
    "IT": {
        "name":         "Italiano",
        "title":        "BALL SORT",
        "easy":         "Facile",
        "medium":       "Medio",
        "hard":         "Difficile",
        "sound_on":     "Audio: ON",
        "sound_off":    "Audio: OFF",
        "language_btn": "🌐 Lingua",
        "select_lang":  "Scegli lingua",
        "moves":        "Mosse",
        "level":        "Livello",
        "menu":         "Menu",
        "undo":         "Annulla",
        "won":          "HAI VINTO!",
        "again":        "Gioca ancora",
        "to_menu":      "Menu principale",
        "quit":         "Esci",
    },
    "NL": {
        "name":         "Nederlands",
        "title":        "BALL SORT",
        "easy":         "Makkelijk",
        "medium":       "Gemiddeld",
        "hard":         "Moeilijk",
        "sound_on":     "Geluid: AAN",
        "sound_off":    "Geluid: UIT",
        "language_btn": "🌐 Taal",
        "select_lang":  "Kies taal",
        "moves":        "Zetten",
        "level":        "Level",
        "menu":         "Menu",
        "undo":         "Ongedaan maken",
        "won":          "GEWONNEN!",
        "again":        "Opnieuw",
        "to_menu":      "Hoofdmenu",
        "quit":         "Stoppen",
    },
    "PL": {
        "name":         "Polski",
        "title":        "BALL SORT",
        "easy":         "Łatwy",
        "medium":       "Średni",
        "hard":         "Trudny",
        "sound_on":     "Dźwięk: WŁ",
        "sound_off":    "Dźwięk: WYŁ",
        "language_btn": "🌐 Język",
        "select_lang":  "Wybierz język",
        "moves":        "Ruchy",
        "level":        "Poziom",
        "menu":         "Menu",
        "undo":         "Cofnij",
        "won":          "WYGRAŁEŚ!",
        "again":        "Zagraj ponownie",
        "to_menu":      "Menu główne",
        "quit":         "Wyjdź",
    },
    "PT": {
        "name":         "Português",
        "title":        "BALL SORT",
        "easy":         "Fácil",
        "medium":       "Médio",
        "hard":         "Difícil",
        "sound_on":     "Som: LIGADO",
        "sound_off":    "Som: DESLIGADO",
        "language_btn": "🌐 Idioma",
        "select_lang":  "Selecionar idioma",
        "moves":        "Jogadas",
        "level":        "Nível",
        "menu":         "Menu",
        "undo":         "Desfazer",
        "won":          "GANHASTE!",
        "again":        "Jogar de novo",
        "to_menu":      "Menu principal",
        "quit":         "Sair",
    },
    "TR": {
        "name":         "Türkçe",
        "title":        "BALL SORT",
        "easy":         "Kolay",
        "medium":       "Orta",
        "hard":         "Zor",
        "sound_on":     "Ses: AÇIK",
        "sound_off":    "Ses: KAPALI",
        "language_btn": "🌐 Dil",
        "select_lang":  "Dil Seç",
        "moves":        "Hamleler",
        "level":        "Seviye",
        "menu":         "Menü",
        "undo":         "Geri al",
        "won":          "KAZANDIN!",
        "again":        "Tekrar Oyna",
        "to_menu":      "Ana Menü",
        "quit":         "Çıkış",
    },
    "RU": {
        "name":         "Русский",
        "title":        "BALL SORT",
        "easy":         "Легко",
        "medium":       "Средне",
        "hard":         "Сложно",
        "sound_on":     "Звук: ВКЛ",
        "sound_off":    "Звук: ВЫКЛ",
        "language_btn": "🌐 Язык",
        "select_lang":  "Выбрать язык",
        "moves":        "Ходы",
        "level":        "Уровень",
        "menu":         "Меню",
        "undo":         "Назад",
        "won":          "ПОБЕДА!",
        "again":        "Играть снова",
        "to_menu":      "Главное меню",
        "quit":         "Выйти",
    },
    "UA": {
        "name":         "Українська",
        "title":        "BALL SORT",
        "easy":         "Легко",
        "medium":       "Середньо",
        "hard":         "Складно",
        "sound_on":     "Звук: УКМ",
        "sound_off":    "Звук: ВИМК",
        "language_btn": "🌐 Мова",
        "select_lang":  "Вибрати мову",
        "moves":        "Ходи",
        "level":        "Рівень",
        "menu":         "Меню",
        "undo":         "Назад",
        "won":          "ПЕРЕМОГА!",
        "again":        "Грати знову",
        "to_menu":      "Головне меню",
        "quit":         "Вийти",
    },
    "CS": {
        "name":         "Čeština",
        "title":        "BALL SORT",
        "easy":         "Snadná",
        "medium":       "Střední",
        "hard":         "Těžká",
        "sound_on":     "Zvuk: ZAP",
        "sound_off":    "Zvuk: VYP",
        "language_btn": "🌐 Jazyk",
        "select_lang":  "Vybrat jazyk",
        "moves":        "Tahy",
        "level":        "Úroveň",
        "menu":         "Menu",
        "undo":         "Zpět",
        "won":          "VYHRÁL JSI!",
        "again":        "Hrát znovu",
        "to_menu":      "Hlavní menu",
        "quit":         "Ukončit",
    },
}

LANGUAGE_ORDER = ["DE", "EN", "FR", "ES", "IT", "NL", "PL", "PT", "TR", "RU", "UA", "CS"]

# --- Windows App-Lautstärke auf 100% setzen ---
# Damit klingt VOLUME=0.4 auf jedem PC gleich, egal was im
# Windows Volume Mixer für diese App eingestellt war.
def set_app_volume_to_max():
    if sys.platform != "win32":
        return
    try:
        from ctypes import POINTER, cast
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioVolume
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.pid == os.getpid():
                volume = session._ctl.QueryInterface(IAudioVolume)
                volume.SetMasterVolume(1.0, None)
                break
    except Exception:
        pass  # pycaw nicht verfügbar → kein Problem, Spiel läuft normal weiter

# --- Initialisierung ---
pygame.init()

# Mixer explizit mit festen Werten initialisieren.
# Ohne diese Parameter wählt Windows in der EXE oft einen
# inkompatiblen Treiber und der Sound bleibt stumm.
try:
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init(44100, -16, 2, 512)
except Exception:
    pass

set_app_volume_to_max()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Sort Puzzle - Ultimate Edition")
clock = pygame.time.Clock()

# --- Farben ---
BG_COLOR   = (20, 20, 30)
TUBE_COLOR = (220, 220, 220)
GOLD       = (255, 215, 0)
WHITE      = (255, 255, 255)
OVERLAY_BG = (15, 15, 25)

# --- Lautstärke (0.0 = stumm, 1.0 = volle Lautstärke) ---
VOLUME = 0.03

BALL_COLORS = [
    (220, 20, 60),
    (34, 139, 34),
    (30, 144, 255),
    (255, 215, 0),
    (255, 20, 147),
    (0, 206, 209),
    (255, 140, 0),
    (138, 43, 226),
    (230, 230, 230)
]

# SysFont mit Fallback-Kette: Arial → Segoe UI → freesansbold
# Segoe UI unterstützt kyrillische / osteuropäische Zeichen auf Windows-EXE
def best_font(size, bold=False):
    for name in ["Arial", "Segoe UI", "freesansbold", "DejaVu Sans"]:
        f = pygame.font.SysFont(name, size, bold=bold)
        if f:
            return f
    return pygame.font.Font(None, size)

font_title = best_font(60, bold=True)
font_ui    = best_font(30, bold=True)
font_ball  = best_font(22, bold=True)
font_lang  = best_font(26, bold=True)


class Game:
    def __init__(self):
        self.state = "MENU"
        self.difficulty = "Medium"
        self.tubes = []
        self.history = []
        self.selected_tube = None
        self.moves = 0
        self.muted = False
        self.show_lang_picker = False   # Sprachauswahl-Overlay
        self.lang_buttons = []          # Wird beim Zeichnen befüllt

        # Gespeicherte Sprache laden, Fallback: DE
        settings = load_settings()
        saved_lang = settings.get("language", "DE")
        self.language = saved_lang if saved_lang in LANGUAGES else "DE"

        self.snd_select = self.load_sound("select.wav")
        self.snd_place  = self.load_sound("place.wav")
        self.snd_win    = self.load_sound("win.wav")


    def t(self, key):
        return LANGUAGES[self.language].get(key, key)

    def set_language(self, lang):
        self.language = lang
        save_settings({"language": lang})   # Sofort speichern
        self.show_lang_picker = False

    def load_sound(self, file):
        if not pygame.mixer.get_init():
            try:
                pygame.mixer.pre_init(44100, -16, 2, 512)
                pygame.mixer.init(44100, -16, 2, 512)
            except Exception:
                return None
        try:
            path = resource_path(file)
            snd = pygame.mixer.Sound(path)
            return snd
        except Exception:
            return None

    def play_snd(self, sound):
        if sound and not self.muted:
            # Channel-basierte Lautstärke – funktioniert zuverlässig in Windows-EXE
            ch = sound.play()
            if ch:
                ch.set_volume(VOLUME)

    def start_game(self, diff):
        self.difficulty = diff
        self.state = "PLAYING"
        self.moves = 0
        self.selected_tube = None
        self.history = []

        configs = {"Easy": (3, 2), "Medium": (6, 2), "Hard": (9, 2)}
        num_colors, num_empty = configs[diff]

        all_balls = []
        for i in range(num_colors):
            all_balls.extend([BALL_COLORS[i]] * 4)
        random.shuffle(all_balls)

        self.tubes = [all_balls[i*4:(i+1)*4] for i in range(num_colors)]
        for _ in range(num_empty):
            self.tubes.append([])

    def undo(self):
        if self.history:
            self.tubes = self.history.pop()
            self.moves -= 1
            self.selected_tube = None

    # -------------------------------------------------------
    # Zeichnen
    # -------------------------------------------------------
    def draw_ball(self, color, x, y):
        r = 25
        pygame.gfxdraw.aacircle(screen, x, y, r, color)
        pygame.gfxdraw.filled_circle(screen, x, y, r, color)
        pygame.gfxdraw.aacircle(screen, x, y, 12, WHITE)
        pygame.gfxdraw.filled_circle(screen, x, y, 12, WHITE)
        try:
            idx = BALL_COLORS.index(color) + 1
            num_txt = font_ball.render(str(idx), True, (0, 0, 0))
            screen.blit(num_txt, (x - num_txt.get_width()//2, y - num_txt.get_height()//2))
        except:
            pass

    def draw_button(self, text, x, y, w, h, color, highlight=False):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, color, rect, border_radius=12)
        border_color = GOLD if highlight else WHITE
        border_w = 3 if highlight else 2
        pygame.draw.rect(screen, border_color, rect, border_w, border_radius=12)
        try:
            txt = font_ball.render(text, True, WHITE)
        except Exception:
            txt = font_ball.render("???", True, WHITE)
        screen.blit(txt, (x + w//2 - txt.get_width()//2, y + h//2 - txt.get_height()//2))
        return rect

    def draw_menu(self):
        title = font_title.render(self.t("title"), True, GOLD)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 80))

        self.btn_e    = self.draw_button(self.t("easy"),   WIDTH//2-125, 220, 250, 50, (46, 204, 113))
        self.btn_m    = self.draw_button(self.t("medium"), WIDTH//2-125, 285, 250, 50, (52, 152, 219))
        self.btn_h    = self.draw_button(self.t("hard"),   WIDTH//2-125, 350, 250, 50, (231, 76, 60))

        sound_label   = self.t("sound_off") if self.muted else self.t("sound_on")
        self.btn_mute = self.draw_button(sound_label, WIDTH//2-125, 430, 250, 50, (100, 100, 100))
        self.btn_lang_open = self.draw_button(
            f"{self.t('language_btn')}  [{LANGUAGES[self.language]['name']}]",
            WIDTH//2-125, 495, 250, 50, (70, 70, 160)
        )

    def draw_game_screen(self):
        txt = font_ball.render(
            f"{self.t('moves')}: {self.moves} | {self.t('level')}: {self.difficulty}",
            True, WHITE
        )
        screen.blit(txt, (30, 30))
        self.btn_back = self.draw_button(self.t("menu"), WIDTH-110, 20, 90, 40, (70, 70, 90))
        self.btn_undo = self.draw_button(self.t("undo"), WIDTH-210, 20, 90, 40, (180, 140, 50))

        num = len(self.tubes)
        gap = (WIDTH - (num * 70)) // (num + 1)
        for i, tube in enumerate(self.tubes):
            x = gap + i * (70 + gap)
            pygame.draw.rect(screen, TUBE_COLOR, (x, 350, 70, 200), 3, border_radius=10)
            for j, color in enumerate(tube):
                bx = x + 35
                by = 300 if (self.selected_tube == i and j == len(tube)-1) else 550 - (j * 48) - 28
                self.draw_ball(color, bx, int(by))

    def draw_win_overlay(self):
        s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        s.fill((0, 0, 0, 210))
        screen.blit(s, (0, 0))

        box = pygame.Rect(WIDTH//2-200, HEIGHT//2-160, 400, 320)
        pygame.draw.rect(screen, (40, 40, 60), box, border_radius=20)
        pygame.draw.rect(screen, GOLD, box, 3, border_radius=20)

        t = font_ui.render(self.t("won"), True, GOLD)
        screen.blit(t, (WIDTH//2 - t.get_width()//2, HEIGHT//2 - 110))

        self.btn_next    = self.draw_button(self.t("again"),   WIDTH//2-150, HEIGHT//2-30, 300, 45, (46, 204, 113))
        self.btn_to_menu = self.draw_button(self.t("to_menu"), WIDTH//2-150, HEIGHT//2+30, 300, 45, (100, 100, 120))
        self.btn_quit    = self.draw_button(self.t("quit"),    WIDTH//2-150, HEIGHT//2+90, 300, 45, (200, 60, 60))

    def draw_lang_picker(self):
        """Sprach-Auswahlfenster als kompaktes 2-Spalten-Overlay."""
        # Halbtransparenter Hintergrund
        s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        s.fill((0, 0, 0, 180))
        screen.blit(s, (0, 0))

        # Box-Größe angepasst: Höhe von 320 auf 440 erhöht, damit alle 6 Zeilen reinpassen!
        box_w, box_h = 600, 440
        bx = WIDTH//2 - box_w//2
        by = HEIGHT//2 - box_h//2

        # Box zeichnen
        pygame.draw.rect(screen, (30, 30, 50), (bx, by, box_w, box_h), border_radius=18)
        pygame.draw.rect(screen, GOLD, (bx, by, box_w, box_h), 2, border_radius=18)

        # Titel
        title_txt = font_lang.render(self.t("select_lang"), True, GOLD)
        screen.blit(title_txt, (WIDTH//2 - title_txt.get_width()//2, by + 20))

        # Sprach-Buttons in 2 Spalten aufteilen
        self.lang_buttons = []
        btn_w, btn_h = 240, 45
        start_y = by + 80
        gap_x = 40  # Abstand zwischen den Spalten
        gap_y = 15  # Abstand zwischen den Zeilen

        for i, code in enumerate(LANGUAGE_ORDER):
            col = i % 2
            row = i // 2

            if col == 0:
                btn_x = WIDTH//2 - btn_w - (gap_x // 2)
            else:
                btn_x = WIDTH//2 + (gap_x // 2)

            btn_y = start_y + row * (btn_h + gap_y)

            is_active = (code == self.language)
            color = (70, 120, 200) if is_active else (55, 55, 80)
            
            btn = self.draw_button(
                LANGUAGES[code]["name"],
                btn_x, btn_y, btn_w, btn_h,
                color, highlight=is_active
            )
            self.lang_buttons.append((btn, code))

    def handle_click(self, pos):
        # Sprachauswahl hat höchste Priorität
        if self.show_lang_picker:
            for btn, code in self.lang_buttons:
                if btn.collidepoint(pos):
                    self.set_language(code)
                    return
            
            # Schließen bei Klick außerhalb der vergrößerten Box (jetzt auch 440 hoch)
            box_w, box_h = 600, 440
            bx = WIDTH//2 - box_w//2
            by = HEIGHT//2 - box_h//2
            box_rect = pygame.Rect(bx, by, box_w, box_h)
            
            if not box_rect.collidepoint(pos):
                self.show_lang_picker = False
            return

        if self.state == "MENU":
            if self.btn_e.collidepoint(pos):          self.start_game("Easy")
            elif self.btn_m.collidepoint(pos):        self.start_game("Medium")
            elif self.btn_h.collidepoint(pos):        self.start_game("Hard")
            elif self.btn_mute.collidepoint(pos):     self.muted = not self.muted
            elif self.btn_lang_open.collidepoint(pos): self.show_lang_picker = True

        elif self.state == "WIN":
            if self.btn_next.collidepoint(pos):       self.start_game(self.difficulty)
            elif self.btn_to_menu.collidepoint(pos):  self.state = "MENU"
            elif self.btn_quit.collidepoint(pos):     pygame.quit(); sys.exit()

        elif self.state == "PLAYING":
            if self.btn_back.collidepoint(pos):  self.state = "MENU"
            elif self.btn_undo.collidepoint(pos): self.undo()
            else:
                num = len(self.tubes)
                gap = (WIDTH - (num * 70)) // (num + 1)
                for i in range(num):
                    if pygame.Rect(gap + i*(70+gap), 300, 70, 250).collidepoint(pos):
                        self.process_move(i); break

    def process_move(self, idx):
        if self.selected_tube is None:
            if self.tubes[idx]:
                self.selected_tube = idx
                self.play_snd(self.snd_select)
        else:
            src, dst = self.selected_tube, idx
            if src == dst:
                self.selected_tube = None
            elif len(self.tubes[dst]) < 4 and (not self.tubes[dst] or self.tubes[dst][-1] == self.tubes[src][-1]):
                self.history.append([t[:] for t in self.tubes])
                self.tubes[dst].append(self.tubes[src].pop())
                self.moves += 1
                self.selected_tube = None
                self.play_snd(self.snd_place)
                if all((not t or (len(t) == 4 and len(set(t)) == 1)) for t in self.tubes):
                    self.state = "WIN"
                    self.play_snd(self.snd_win)
            else:
                self.selected_tube = None


# --- Main Loop ---
game = Game()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.handle_click(event.pos)

    screen.fill(BG_COLOR)
    if game.state == "MENU":
        game.draw_menu()
    else:
        game.draw_game_screen()
    if game.state == "WIN":
        game.draw_win_overlay()
    if game.show_lang_picker:
        game.draw_lang_picker()

    pygame.display.flip()
    clock.tick(60)
