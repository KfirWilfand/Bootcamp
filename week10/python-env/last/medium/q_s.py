from ..q import get_q
from .s import get_s


def get_letters():
    return get_q() + ["r"] + get_s()
