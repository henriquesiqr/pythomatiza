def sort_asc(my_list):
    # TODO: Retorne a lista de nomes recebida em ordem alfabética ascendente
    return sorted(my_list)

def sort_desc(my_list):
    # TODO: Retorne a lista de nomes recebida em ordem alfabética descendente
    return sorted(my_list, reverse=true)

def find_list_element(my_list):
    # TODO: Retorne o segundo elemento da lista recebida
    return my_list[1]

def find_last_list_element(my_list):
    # TODO: Retorne o último elemento da lista recebida
    return my_list[-1]

def find_out_of_range_error():
    # TODO: Encontrar o erro no código abaixo
    # TODO: my_list não deverá ser modificada
    my_list = [1, 2, 3, 4, 5]
    return my_list[4]

def x_not_in_the_list_error():
    # TODO: Encontrar o erro no código abaixo
    # TODO: my_list não deverá ser modificada
    # TODO: Último elemento da lista deverá ser removido
    my_list = [1, 2, 3, 4, 5]
    my_list.pop(-1)
    return my_list[0]

def list_remove_last(my_list):
    # TODO: Retorne a lista recebida como argumento sem o último elemento
    return my_list[0:-2]
