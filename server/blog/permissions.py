 ###########! PERMISSONS ##############
 
from rest_framework import permissions

#class BasePermission(metaclass=BasePermissionMetaclass):
    # """
    # A base class from which all permission classes should inherit.
    # """

    #def has_permission(self, request, view):
        # """
        # Return `True` if permission is granted, `False` otherwise.
        # """
        #return True

    #def has_object_permission(self, request, view, obj):
        # """
        # Return `True` if permission is granted, `False` otherwise.
        # """
        #return True
class IsPostOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author
#! Yukarıda da belirttiğimiz üzere has_object_permission methodunu kullanarak SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS') izin güvenliyse ve istek bunun içindeyse  true dönder ve istek yapan kişi ile User objesi içindeki author a eşitse yada değilse döndür

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin
#! IsAdminUser içindeki has_permission methodunu kullanarak  güvenli yada yetkili ise ve istek bunların içindeyse true değilse false döndür   
# class IsAdminUser(BasePermission):
#     """
#     Allows access only to admin users.
#     """
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_staff)