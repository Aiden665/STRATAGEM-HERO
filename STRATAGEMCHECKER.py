import json
with open('stratdict.json') as f:

    while True:
        stratdict = json.load(f)
        strat_Name = stratdict.
            try:
                screen.blit(pygame.image.load(f"StratagemIcons/{strat_Name}_Icon.png"), (((screen.get_width())-(44))/2, 600))
            except: