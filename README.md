# qa_python
1. test_add_new_book_add_two_books(self) 
# Проверяем, что добавилось именно две, т.к. у 3-й книги длинное название
# словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
2. test_set_book_genre_not_listed(self):
# Проверяем что жанр не добавился для книги
# get_book_genre возвращает жанр по названию книги, вернет пустую строку
3. test_get_book_genre_check_genre(self):
# проверяем жанр книги
# get_book_genre возвращает жанр по названию книги, должен вернуть "Фантастика"
4. test_get_books_with_specific_genre_get_two_books(self):
# Проверяем, что метод выводит именно 2 книги
# get_books_with_specific_genre возвращает список книг по жанру, имеет длину 2
5. test_get_books_genre_get_dict(self):
# Проверяем, что все книги добавились и соответствуют именам
# get_books_genre возвращает словарь books_genre, через keys получаем ключи и оборачиваем в список,
# который равен ["Book1", "Book2", "Book3"]
6. test_get_books_for_children_add_two_books(self):
# Проверяем, что выдало 2 книги только с жанром "Фантастика" и "Мультфильмы"
# Получаем список get_books_for_children, у каждого элемента проверяем жанр книги через get_book_genre
# Получаем ["Book1", "Book2"]
7. test_add_book_in_favorites_add_zero_books_in_favorites(self):
# Проверяем, что не добавилась книга
# get_list_of_favorites_books возвращает список избранных книг, длинна списка 0,
# т.к. "Book1" не может быть добавлена
8. test_delete_book_from_favorites_delete_one_book(self):
# Проверяем, что в избранных осталось 1 книга с названием "Book2"
# get_list_of_favorites_books возвращает список равный 1
9. test_get_list_of_favorites_books_add_book_in_favorites(self):
# Проверяем, что добавилась 1 книга
# get_list_of_favorites_books возвращает список, вернёт 1
