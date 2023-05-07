class Email:
    __idCuenta: int
    __dominio: str
    __tipodominio: str
    __contraseña: str | None

def __init__(self, idCuenta: str, dominio: str, tipodominio: str, contraseña: str | None):
    self.__idCuenta = idCuenta
    self.__dominio = dominio
    self.__tipodominio = tipodominio
    self.__contraseña = contraseña

def retornaEmail(self) -> str:
    return self.__idCuenta + "@" + self.__dominio + "." + self.__tipodominio

def getDominio(self) -> str:
    return self.__dominio

def IDCuenta(self) -> int:
    return self.__idcuenta

def modificarContraseña(self, contraseñaActual: str, nuevaContraseña: str) -> None:
    if self.__contraseña == contraseñaActual:
        self.__contraseña = nuevaContraseña
        print("La constraseña ha sido modificada")
    else:
        print("La contraseña actual no es correcta")

def __str__(self) -> str:
    return self.retornaEmail()

