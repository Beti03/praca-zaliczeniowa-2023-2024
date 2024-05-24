import re


def convert_data_to_a_new_temporary_list(new_elements_list):
    """
    Funkcja przyjmuje listę elementów ze strony www i konwertuje do nowej listy.
    Dane pobrane np. '120 ml (1)' po konwersji '120 ml'
    :param new_elements_list:list()
    :return: list()
    """
    # Utworzenie listy tymczasowej dla zmienionych
    tmp_elements_list = []
    for i in range(len(new_elements_list)):
        tmp_elements_list.append(re.sub(r"\s*\(\d+\)", "", str(new_elements_list[i].text)))
    return tmp_elements_list