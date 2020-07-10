class apiRouter(object):
    def db_for_read(self, model, **hint):
        if model._meta.app_label == 'api':
            return 'experimentos'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'api':
            return 'experimentos'
        return None
    
    def allow_relation(self, obj1, obj2, **hint):
        if obj1._meta.app_label == 'api' or \
            obj2._meta.app_label == 'api':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hint):
        if app_label == 'api':
            return db == 'experimentos'
        return None
    
class usersRouter(object):
    def db_for_read(self, model, **hint):
        if model._meta.app_label == 'users':
            return 'usuarios'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'usuarios'
        return None
    
    def allow_relation(self, obj1, obj2, **hint):
        if obj1._meta.app_label == 'users' or \
            obj2._meta.app_label == 'users':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hint):
        if app_label == 'users':
            return db == 'usuarios'
        return None