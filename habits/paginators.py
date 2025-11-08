from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """Пагинатор дял привычек"""

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class RewordPaginator(PageNumberPagination):
    """Пагинатор для вознаграждения"""

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20
