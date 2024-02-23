from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_two_books(self):
        books_collector = BooksCollector()
        for book_name in ('Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить', "A" * 43):
            books_collector.add_new_book(book_name)
        assert len(books_collector.get_books_genre()) == 2

    def test_set_book_genre_not_listed(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Book1")
        books_collector.set_book_genre("Book1", 'Триллер')
        assert books_collector.get_book_genre("Book1") == ''

    def test_get_book_genre_check_genre(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Book1")
        books_collector.set_book_genre("Book1", "Фантастика")
        assert books_collector.get_book_genre("Book1") == "Фантастика"

    def test_get_books_with_specific_genre_get_two_books(self):
        books_collector = BooksCollector()
        for book_name in ("Book1", "Book2"):
            books_collector.add_new_book(book_name)
            books_collector.set_book_genre(book_name, "Фантастика")
        assert len(books_collector.get_books_with_specific_genre("Фантастика")) == 2

    def test_get_books_genre_get_dict(self):
        books_collector = BooksCollector()
        for book_name in ("Book1", "Book2", "Book3"):
            books_collector.add_new_book(book_name)
        assert list(books_collector.get_books_genre().keys()) == ["Book1", "Book2", "Book3"]

    def test_get_books_for_children_add_two_books(self):
        books_collector = BooksCollector()
        for book_name, genre in [
            ("Book1", "Фантастика"),
            ("Book2", "Мультфильмы"),
            ("Book3", "Ужасы"),
            ("Book4", "Детективы"),
        ]:
            books_collector.add_new_book(book_name)
            books_collector.set_book_genre(book_name, genre)
        assert [book for book in books_collector.get_books_for_children()
                if books_collector.get_book_genre(book) not in books_collector.genre_age_rating] == ["Book1", "Book2"]

    def test_add_book_in_favorites_add_zero_books_in_favorites(self):
        books_collector = BooksCollector()
        books_collector.add_book_in_favorites("Book1")
        assert len(books_collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_delete_one_book(self):
        books_collector = BooksCollector()
        for book_name in ("Book1", "Book2"):
            books_collector.add_new_book(book_name)
            books_collector.add_book_in_favorites(book_name)
        books_collector.delete_book_from_favorites("Book1")
        lst = books_collector.get_list_of_favorites_books()
        assert len(lst) == 1 and lst[0] == "Book2"

    def test_get_list_of_favorites_books_add_book_in_favorites(self):
        books_collector = BooksCollector()
        books_collector.add_new_book("Book1")
        books_collector.add_book_in_favorites("Book1")
        assert len(books_collector.get_list_of_favorites_books()) == 1
