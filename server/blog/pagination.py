from rest_framework.pagination import CursorPagination, LimitOffsetPagination


# class CursorPagination(BasePagination):
#     cursor_query_param = 'cursor'
#     cursor_query_description = _('The pagination cursor value.')
#     page_size = api_settings.PAGE_SIZE
#     invalid_cursor_message = _('Invalid cursor')
#     ordering = '-created'
#     template = 'rest_framework/pagination/previous_and_next.html'
#     page_size_query_param = None
#     page_size_query_description = _('Number of results to return per page.')
#     max_page_size = None  
#     offset_cutoff = 1000


class CursorSetPagination(CursorPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    ordering = 'id'  # '-created' is defaultz
    
    
# class LimitOffsetPagination(BasePagination):
#     default_limit = api_settings.PAGE_SIZE
#     limit_query_param = 'limit'
#     limit_query_description = _('Number of results to return per page.')
#     offset_query_param = 'offset'
#     offset_query_description = _('The initial index from which to return the results.')
#     max_limit = None
#     template = 'rest_framework/pagination/numbers.html'


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 6