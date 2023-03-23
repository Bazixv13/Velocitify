typing_animation = True
loading_bars = True
manual_typing_animation_speed = False
typing_animation_speed = 0.045
bot_token = 'MTAxNDE5OTgwOTQzMjg5NTQ4OA.GQKFPH.p02DL7jg9hmaVEchcj_4VrzaMcC1KfMVfJWmlw'
def save_config():
    import os
    with open('config.py', 'w') as f:
        f.write(f"typing_animation = {typing_animation}\n")
        f.write(f"loading_bars = {loading_bars}\n")
        f.write(f"manual_typing_animation_speed = {manual_typing_animation_speed}\n")
        f.write(f"typing_animation_speed = {typing_animation_speed}\n")
        f.write(f"bot_token = '{bot_token}'\n")
