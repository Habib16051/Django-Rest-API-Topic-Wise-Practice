from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'name'
    # cursor_query_param = 'cu'
    # limit_query_param = 'l'
    # offset_query_param = 'o'
    # max_limit = 3
    # page_size = 4
    # page_query_param = 'q'
    # page_size_query_param = 'records'
    # # max_page_size = 5
    # # last_page_strings = 'end'
