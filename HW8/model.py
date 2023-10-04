from copy import deepcopy
phone_book = {}
original_book = {}
path = 'contacts.txt'


def open_file():
    global original_book
    with open(path, 'r', encoding='UTF-8') as file:
        contacts = file.readlines()
    for u_id, contact in enumerate(contacts, 1):
        contact = contact.strip().split(';')
        phone_book[u_id] = contact
    original_book = deepcopy(phone_book)


def save_file():
    contacts = [';'.join(contact) for contact in phone_book.values()]
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(contacts))


def next_id():
    return max(phone_book) + 1


def new_contact(contact: list):
    phone_book[next_id()] = contact


def search(word: str) -> dict[int, list[str, str, str]]:
    result = {}
    for u_id, contact in phone_book.items():
        if word.lower() in ''.join(contact).lower():
            result[u_id] = contact
    return result


def delete(u_id: int) -> str:
    return phone_book.pop(u_id)[0]
