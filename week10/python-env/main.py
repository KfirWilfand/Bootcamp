from module1 import get_letters
from module4 import get_letters as get_letters4
from module5 import get_letters5
from last.w_z import get_last_letters
from last.t_v import get_letters as get_t_v
from last.medium import q_s
from middle.m_p.get_m_p import  m_p

def get_alphabet():
    return get_letters() + get_letters4() + get_letters5() + \
        m_p() + q_s.get_letters() + get_t_v() + get_last_letters()


print(get_alphabet())