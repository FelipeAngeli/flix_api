from rest_framework import permissions

class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        #logica da permissao, sempre retornar um true ou false
        # por padrão sempre retorna False 
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genres.view_genre')
        
        #permissao de add genero
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        #para alterar dados
        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('genres.change_genre')
        
        #para deletar dados
        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')
        
        return False
    