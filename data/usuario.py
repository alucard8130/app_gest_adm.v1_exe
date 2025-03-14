import datetime
from model.user import Usuario
import conexion_db as con


current_datetime = datetime.datetime.now()


class UsuarioData():
    def login(self, user_info=Usuario):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT * FROM usuarios WHERE usuario='{}' AND clave='{}'".format(user_info._usuario,user_info._clave))
        result_info=query.fetchone()
        if result_info:
            self.cursor.close()
            self.db.close()
            return result_info
        else:
            return None
     
            
     #usuario nuevo
    def registrar(self, info:Usuario):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query =self.cursor.execute( "SELECT * FROM usuarios WHERE usuario = '{}'".format(info._usuario))
        result = query.fetchone()
        if result is None:    
            self.db = con.Conexion().conectarBd()
            self.cursor= self.db.cursor()
            query= self.cursor.execute("INSERT INTO usuarios(nombre,usuario,clave,status,fecha_reg,usuario_reg) VALUES('{}','{}','{}','{}','{}','{}')"
                                    .format(info._nombre,info._usuario,info._clave,"True",current_datetime,info._user_reg))
            self.db.commit()
            self.cursor.close()
            self.db.close()
            return True
        else:
            return False 
    
    #recuperar contraseña
    def recuperar(self, usuario):
        self.db = con.Conexion().conectarBd()
        self.cursor = self.db.cursor()
        if usuario.lower() == 'administrador':
            self.cursor.close()
            self.db.close()
            return None
        query = self.cursor.execute("SELECT clave FROM usuarios WHERE usuario='{}'".format(usuario))
        result = query.fetchone()
        if result:
            self.cursor.close()
            self.db.close()
            return result[0]
        else:
            self.cursor.close()
            self.db.close()
            return None
    
    
    #eliminar usuario
    def eliminar(self, info:Usuario):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("DELETE FROM usuarios WHERE usuario='{}'".format(info._usuario))
        self.db.commit()
        self.cursor.close()
        self.db.close()
        return True  
        
    
                