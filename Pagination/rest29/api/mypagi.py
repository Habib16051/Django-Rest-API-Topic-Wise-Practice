from rest_framework.pagination import PageNumberPagination


class MypageNumberPagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'q'
    page_size_query_param = 'records'
    # max_page_size = 5
    # last_page_strings = 'end'
