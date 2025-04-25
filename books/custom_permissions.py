from rest_framework import permissions


class IsLibrarianWithBookPermissions(permissions.BasePermission):
    """ This class is used for checking the user permission"""

    def has_permission(self, request, view):
        user = request.user
        return (
            user.is_authenticated and
            user.role == 'librarian' and (
                user.has_perm('library.add_book') or
                user.has_perm('library.change_book') or
                user.has_perm('library.delete_book')
            )
        )
