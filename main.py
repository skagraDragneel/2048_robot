from game_objects import Game
import os
from pathlib import Path
from users import BasicBot


def main():
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    config_path = str(current_dir / 'resources' / 'config' / 'basic_ui.ini')
    game = Game(config_path)
    basic_bot = BasicBot(config_path, game)
    basic_bot.run()


if __name__ == '__main__':
    main()
