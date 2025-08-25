import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Hangman Game")

# Optional background image
# background = pygame.image.load("background.jpg")
# background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Colors & Fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
LIGHT_BLUE = (0, 120, 255)
GREEN = (0, 153, 76)
GRAY = (245, 245, 245)

# Custom fonts (optional)
# FONT = pygame.font.Font("Poppins-Bold.ttf", 40)
# LETTER_FONT = pygame.font.Font("Poppins-Regular.ttf", 30)
# WORD_FONT = pygame.font.Font("Poppins-Bold.ttf", 60)
FONT = pygame.font.SysFont("comicsans", 40)
LETTER_FONT = pygame.font.SysFont("comicsans", 30)
WORD_FONT = pygame.font.SysFont("comicsans", 60)

# Load hangman images
images = [pygame.image.load(f"hangman{i}.png") for i in range(7)]

# Word bank
word_bank = [
    {"word": "apple", "hint": "A common fruit"},
    {"word": "brain", "hint": "Controls your body"},
    {"word": "chair", "hint": "You sit on it"},
    {"word": "dream", "hint": "You see it while sleeping"},
    {"word": "eagle", "hint": "A bird with sharp eyesight"},
    {"word": "monitor", "hint": "Displays your computer screen"},
    {"word": "notebook", "hint": "Used to write or take notes"},
    {"word": "keyboard", "hint": "Input device with keys"},
]

# Difficulty settings
difficulties = {
    "easy": {"max_misses": 8, "length_range": (4, 5)},
    "medium": {"max_misses": 6, "length_range": (6, 7)},
    "hard": {"max_misses": 4, "length_range": (8, 100)},
}

# Letter button layout
RADIUS = 20
GAP = 15
letters = []

def reset_letters():
    global letters
    letters = []
    A = 65
    startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
    starty = 600
    for i in range(26):
        x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
        y = starty + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, chr(A + i), True])

score = 0
hint_used = False

def choose_word(difficulty):
    min_len, max_len = difficulties[difficulty]["length_range"]
    filtered = [w for w in word_bank if min_len <= len(w["word"]) <= max_len]
    return random.choice(filtered)

def draw(word, guessed, hangman_status, show_hint_btn, hint):
    # screen.blit(background, (0, 0))  # If using background image
    screen.fill(GRAY)

    # Title
    title = FONT.render("HANGMAN GAME", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

    # Word Display
    display_word = ""
    for letter in word:
        display_word += letter if letter in guessed else "_"
        display_word += " "
    word_text = WORD_FONT.render(display_word.strip(), True, (50, 50, 50))
    screen.blit(word_text, (WIDTH / 2 - word_text.get_width() / 2, 250))

    # Letter Buttons
    mx, my = pygame.mouse.get_pos()
    for x, y, ltr, visible in letters:
        if visible:
            color = LIGHT_BLUE if ((x - mx)**2 + (y - my)**2)**0.5 < RADIUS else BLUE
            pygame.draw.circle(screen, color, (x, y), RADIUS)
            text = LETTER_FONT.render(ltr, True, WHITE)
            screen.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    # Hint Button
    if show_hint_btn:
        hint_rect = pygame.Rect(WIDTH - 180, 30, 140, 40)
        pygame.draw.rect(screen, GREEN, hint_rect, border_radius=12)
        hint_text = LETTER_FONT.render("Show Hint", True, WHITE)
        text_rect = hint_text.get_rect(center=hint_rect.center)
        screen.blit(hint_text, text_rect)

       
    # Score
    score_text = FONT.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (30, 30))

    # Hangman Image
    image = images[min(hangman_status, 6)]
    image = pygame.transform.scale(image, (200, 200))  # Resize image if large
    image_rect = image.get_rect(center=(WIDTH // 5, 360))

    screen.blit(image, image_rect)

    pygame.display.update()

def display_message(message):
    screen.fill(WHITE)
    msg_text = WORD_FONT.render(message, True, BLACK)
    screen.blit(msg_text, (WIDTH/2 - msg_text.get_width()/2, HEIGHT/2))
    pygame.display.update()
    pygame.time.delay(3000)

def select_difficulty():
    clock = pygame.time.Clock()
    selected = None
    buttons = [
        {"label": "Easy", "rect": pygame.Rect(350, 350, 150, 60), "color": BLUE},
        {"label": "Medium", "rect": pygame.Rect(525, 350, 150, 60), "color": BLUE},
        {"label": "Hard", "rect": pygame.Rect(700, 350, 150, 60), "color": BLUE},
    ]

    while not selected:
        screen.fill(WHITE)
        title = WORD_FONT.render(" Select Difficulty", True, BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 150))

        mx, my = pygame.mouse.get_pos()

        for button in buttons:
            rect = button["rect"]
            color = (90, 160, 210) if rect.collidepoint(mx, my) else button["color"]
            pygame.draw.rect(screen, color, rect, border_radius=12)
            text = FONT.render(button["label"], True, WHITE)
            screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        selected = button["label"].lower()
                        break

        clock.tick(60)

    return selected

# Game Loop
while True:
    hint_used = False
    reset_letters()
    difficulty = select_difficulty()
    selected = choose_word(difficulty)
    word = selected["word"].upper()
    hint = selected["hint"]
    guessed = []
    hangman_status = 0
    max_misses = difficulties[difficulty]["max_misses"]
    run = True

    while run:
        draw(word, guessed, hangman_status, not hint_used, hint)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                # Hint button
                if not hint_used and WIDTH - 180 <= mx <= WIDTH - 40 and 30 <= my <= 70:
                    hint_used = True
                    pygame.draw.rect(screen, WHITE, (250, 300, 400, 50))
                    hint_msg = LETTER_FONT.render("Hint: " + hint, True, BLACK)
                    screen.blit(hint_msg, (WIDTH / 2 - hint_msg.get_width() / 2, 300))
                    pygame.display.update()
                    pygame.time.delay(2000)

                # Letter buttons
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible and ((x - mx) ** 2 + (y - my) ** 2) ** 0.5 < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1

            if event.type == pygame.KEYDOWN:
                key = event.unicode.upper()
                if key.isalpha() and key not in guessed:
                    guessed.append(key)
                    if key not in word:
                        hangman_status += 1
                    for letter in letters:
                        if letter[2] == key:
                            letter[3] = False

        if all([ltr in guessed for ltr in word]):
            score += 1
            display_message(" You WON!")
            run = False
        elif hangman_status >= max_misses:
            display_message(f" You LOST! Word was {word}")
            run = False
