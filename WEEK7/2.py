import pygame
import sys
import pygame.mixer

pygame.init()
pygame.mixer.init()
pygame.font.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music player")

music_album = [
    r"C:\Users\user\Desktop\Labs_2025\zion-y-lennox-daddy-yankee-yo-voy.mp3", # 0
    r"C:\Users\user\Desktop\Labs_2025\daddy_yankee_-_con_calma_(feat._snow)_muzrecord.net.mp3", # 1
    r"C:\Users\user\Desktop\Labs_2025\arctic-monkeys-i-wanna-be-yours.mp3", # 2
    r"C:\Users\user\Desktop\Labs_2025\billie-eilish-ocean-eyes.mp3", # 3
    r"C:\Users\user\Desktop\Labs_2025\moldanazar-mahabbatym.mp3", # 4
    r"C:\Users\user\Desktop\Labs_2025\kali-uchis-moonlight.mp3", # 5
    r"C:\Users\user\Desktop\Labs_2025\PSY - Gangnam Style.mp3", # 6
    r"C:\Users\user\Desktop\Labs_2025\DJ Snake feat. Selena Gomez, Cardi B & Ozuna - Taki Taki.mp3",  # 7
    r"C:\Users\user\Desktop\Labs_2025\Bonapart - Жаным, если ты.mp3",  # 8
    r"C:\Users\user\Desktop\Labs_2025\dudeontheguitar-monro-boiy-bulgan-orkenoff-remix_(muzstars.kz).mp3" # 9
]

music_pictures = [
    pygame.image.load(r"C:\Users\user\Desktop\Labs_2025\music_pictures\ab67616d0000b273f016efa8ba3d5557a53d3076.jpeg"),  # 0
    pygame.image.load(r"C:\Users\user\Desktop\Labs_2025\music_pictures\R.jpeg"),  # 1
    pygame.image.load(r"C:\Users\user\Desktop\Labs_2025\music_pictures\R (1).jpeg"),  # 2
    pygame.image.load(r"C:\Users\user\Desktop\Labs_2025\music_pictures\a92bf27c423644c9ef77a00b155796ff.jpg"),  # 3
    pygame.image.load(r"C:\Users\user\Desktop\Labs_2025\music_pictures\hqdefault.jpg"),  # 4
    pygame.image.load(r"C:\Users\user\Desktop\Labs_2025\music_pictures\OIP (1).jpeg"),  # 5
    pygame.image.load(r"C:\Users\user\Desktop\Labs_2025\music_pictures\440x440.webp")  # 6
]

music_names = [
    "Yo voy",
    "Con calma",
    "I wanna be yours",
    "Ocean eyes",
    "Mahabbatym",
    "Moonlight",
    "Gangnam Style",
    "Taki Taki",
    "Жаным, если ты",
    "Boiy Bulgan"
]

def start_music(index):
    pygame.mixer.music.load(music_album[index])
    pygame.mixer.music.play()

track = 0

MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)

start_music(track)
is_paused = False

font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 150, HEIGHT // 2 - 180, 300, 300), 2)

    # Adjust image display based on track
    if track == 0:
        image = music_pictures[0]  # Yo voy
    elif track == 1:
        image = music_pictures[1]  # Con calma
    elif track == 2:
        image = music_pictures[2]  # I wanna be yours
    elif track == 3:
        image = music_pictures[3]  # Ocean eyes
    elif track == 4:
        image = music_pictures[4]  # Mahabbatym
    elif track == 5:
        image = music_pictures[5]  # Moonlight
    elif track in [6, 7, 8, 9]:
        image = music_pictures[6]  # Gangnam Style

    image = pygame.transform.scale(image, (300, 300))
    screen.blit(image, (WIDTH // 2 - 150, HEIGHT // 2 - 180))

    track_text = font.render(music_names[track], True, (255, 255, 255))
    text_rect = track_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 140))
    screen.blit(track_text, text_rect)

    pygame.draw.line(screen, (255, 255, 255), (WIDTH // 2 - 150, HEIGHT // 2 + 167), (WIDTH // 2 + 150, HEIGHT // 2 + 167), 2)

    pygame.draw.polygon(screen, (255, 255, 255), [
        (WIDTH // 2 - 90, HEIGHT // 2 + 180),
        (WIDTH // 2 - 110, HEIGHT // 2 + 200),
        (WIDTH // 2 - 90, HEIGHT // 2 + 220)
    ])

    pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 15, HEIGHT // 2 + 183, 30, 30))

    pygame.draw.polygon(screen, (255, 255, 255), [
        (WIDTH // 2 + 90, HEIGHT // 2 + 180),
        (WIDTH // 2 + 110, HEIGHT // 2 + 200),
        (WIDTH // 2 + 90, HEIGHT // 2 + 220)
    ])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MUSIC_END:
            track = (track + 1) % len(music_album)
            start_music(track)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                else:
                    pygame.mixer.music.pause()
                    is_paused = True

            elif event.key == pygame.K_l:
                # Play next track
                track = (track + 1) % len(music_album)
                start_music(track)

            elif event.key == pygame.K_j:
                # Play previous track
                track = (track - 1) % len(music_album)
                start_music(track)

    pygame.display.update()

pygame.quit()
sys.exit()
