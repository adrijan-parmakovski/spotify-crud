from src.utils.configs import SPOTIFY_CONFIGS


def foo():
    print(SPOTIFY_CONFIGS.__dict__)
    print(SPOTIFY_CONFIGS.base_64_secret)


foo()
