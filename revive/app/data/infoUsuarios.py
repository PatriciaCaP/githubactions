from flask import request


class Usuario:
   def __init__(self, db):
      self.db = db

   def dameTodos(self):
        cursor = self.db.cursor() # PARA ACCEDER A LA BD
        cursor.execute("SELECT * FROM usuario") # PARA OBTENER TODOS LOS DATOS DE LA BD QUE VAMOS A VER EN NUESTRO INDEX
        myresult = cursor.fetchall()  #PARA ACCEDER A TODOS LOS DATOS
        #CONVERTIR TODOS LOS DATOS A DICCIONARIO.
        insertObject = [] # AQUI VAN GUARDADAS LAS CLAVES DE LAS COLUMNAS
        columnNames = [column[0] for column in cursor.description] # PARA OBTENER LOS NOMBRES DE LAS COLUMNAS
        for record in myresult: # CON UN BUCLE DENTRO DE MYRESULT EXTRAIGO TODA LA INFORMACION 
            insertObject.append(dict(zip(columnNames,record))) # PARA IR METIENDO TODOS LOS DATOS EN FORMATO DICCIONARIO CON EL DICT. LA FUNCION ZIP ES PORQUE VAMOS A USAR COLUMN Y RECORD
        cursor.close() # PARA CERRAR EL CURSOR
        return insertObject 

   def añadirUsuario(self,nombre,apellido,email):
        if nombre and apellido and email: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
            cursor = self.db.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
            sql = "INSERT INTO usuario (nombre,apellido,email) VALUES (%s, %s, %s)" # DEFINIMOS LA CONSULTA INSERT DE TIPO STRING %S
            data = (nombre,apellido,email) # HACEMOS UNA TUPLA CON LOS DATOS 
            cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
            self.db.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO


   def borrarUsuario(self,idusuario):
      cursor = self.db.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
      sql = "DELETE FROM usuario WHERE idusuario=%s"
      data = [idusuario] 
      cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
      self.db.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
