import csv


every_product = ["hamburguer", "coxinha", "misto-quente", "pizza"]
days = ["sabado", "terça-feira", "segunda-feira"]


def get_data(path_file):
    if ".csv" not in path_file:
        raise FileNotFoundError(f"Extensão inválida. {path_file}")
    try:
        with open(path_file, encoding="utf8") as file:
            csv_reader = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = csv_reader
            return data

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_file}")


def get_list(list):
    repeated_names = []
    person_list = []
    for row in list:
        if row[0] not in repeated_names:
            repeated_names.append(row[0])
            person_list.append(
                {
                    row[0]: {
                        "pedidos": [
                            {
                                "produto": row[1],
                                "dia": row[2],
                            }
                        ]
                    }
                }
            )
        for person in person_list:
            keys = person.keys()
            if row[0] in keys:
                person[row[0]]["pedidos"].append(
                    {
                        "produto": row[1],
                        "dia": row[2],
                    }
                )
    return person_list


def get_food_count_by_person(person, list):
    for row in list:
        keys = row.keys()
        if person in keys:
            return row


def most_requested_food_by_maria(list):
    maria_food_count = get_food_count_by_person("maria", list)
    products_list = []

    for row in maria_food_count["maria"]["pedidos"]:
        products_list.append(row["produto"])

    counter = 0
    element = products_list[0]

    for maria in products_list:
        maria_most_ordered_food = products_list.count(maria)
        if maria_most_ordered_food > counter:
            counter = maria_most_ordered_food
            element = maria

    return element


def count_requested_hamburger_by_arnaldo(list):
    arnaldo_food_count = get_food_count_by_person("arnaldo", list)
    products_list = []

    for row in arnaldo_food_count["arnaldo"]["pedidos"]:
        products_list.append(row["produto"])

    counter = 0

    for arnaldo in products_list:
        if arnaldo == 'hamburguer':
            counter += 1

    return counter


def food_joao_never_requested(list):
    joao_food_count = get_food_count_by_person("joao", list)
    products_list = []

    for row in joao_food_count["joao"]["pedidos"]:
        products_list.append(row["produto"])

    never_asked = set()

    for joao in every_product:
        if joao not in products_list:
            never_asked.add(joao)

    return never_asked


def days_that_joao_never_went(list):
    joao_food_days = get_food_count_by_person("joao", list)
    days_list = []

    for row in joao_food_days["joao"]["pedidos"]:
        days_list.append(row["dia"])

    never_asked = set()

    for joao_days in days:
        if joao_days not in days_list:
            never_asked.add(joao_days)

    return never_asked


def analyze_log(path_to_file):
    csv_list = get_data(path_to_file)
    person_list = get_list(csv_list)
    maria = most_requested_food_by_maria(person_list)
    arnaldo = count_requested_hamburger_by_arnaldo(person_list)
    joao = food_joao_never_requested(person_list)
    joao_days = days_that_joao_never_went(person_list)

    file = open("data/mkt_campaign.txt", mode="w")
    LINES = [f"{maria}\n", f"{arnaldo}\n", f"{joao}\n", f"{joao_days}\n"]
    file.writelines(LINES)
    file.close()            