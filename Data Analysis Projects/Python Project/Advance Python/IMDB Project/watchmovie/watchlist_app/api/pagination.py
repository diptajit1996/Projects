from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    page_size = 3  # it will display the number of item in each page according to the page_size number you provide and it will also provide the same number of item in next page and so on
    page_query_param = 'p'  # if you want to provide another name in place of default 'page' name in url you can do that
    page_size_query_param = 'size'  # here you are giving client permission of how many items they want to see in each page to display
    max_page_size = 10  # we are fixing the maximum number of page size. So that even if client gives more than that max size number than it will restrict to this fix size number only.
    last_page_strings = 'end'  # this will take you to last page by providing these value over there
    # even if you don't provide last_page_strings than also you can use 'p=last' in postman and it will take you to last page.


class WatchListLOPagination(LimitOffsetPagination):  # Limit Offset Pagination
    default_limit = 5  # it will provide by default 5 items on each page and count the offset according to each page continuously
    max_limit = 10  # it will display the max limit 10 items
    limit_query_param = 'limit'  # giving name of limit
    offset_query_param = 'start'  # giving name of offset


class WatchListCPagination(CursorPagination):
    page_size = 5
    ordering = 'created'  # it will order the record in ascending order. If you want descending order just put '-' sign in front 'created'. It is only used for field purpose
    cursor_query_param = 'record'  # if you want to provide another name in place of default 'cursor' name in url you can do that
