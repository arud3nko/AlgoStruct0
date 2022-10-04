from dataclasses import dataclass


def get_config():
    """
    Датакласс Config содержит конфигурацию для черепахи
    :return: Config - датакласс с конфигом
    """
    @dataclass
    class Config:
        size: int = 90
        levels: int = 8
        angle: int = 30
        speed: int = 0
        colormode: int = 255
        width: int = 5

    return Config()


if __name__ == '__main__':
    pass
