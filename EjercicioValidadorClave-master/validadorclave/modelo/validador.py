from errores import LongitudInvalidaError, FaltaMayusculaError, FaltaMinusculaError, FaltaNumeroError, FaltaCaracterEspecialError


class ReglaValidacion:
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(char.isupper() for char in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(char.islower() for char in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(char.isdigit() for char in clave)

    def es_valida(self, clave: str) -> bool:
        raise NotImplementedError("Este método debe ser implementado en las subclases")
    

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        caracteres_especiales = {'@', '_', '#', '$', '%'}
        return any(char in caracteres_especiales for char in clave)

    def es_valida(self, clave: str) -> bool:
        
        if not self._validar_longitud(clave):
            raise LongitudInvalidaError("La clave debe tener más de 8 caracteres.")

        if not self._contiene_mayuscula(clave):
            raise FaltaMayusculaError("La clave debe contener al menos una letra mayúscula.")

        if not self._contiene_minuscula(clave):
            raise FaltaMinusculaError("La clave debe contener al menos una letra minúscula.")

        if not self._contiene_numero(clave):
            raise FaltaNumeroError("La clave debe contener al menos un número.")

        if not self.contiene_caracter_especial(clave):
            raise FaltaCaracterEspecialError("La clave debe contener al menos un carácter especial (@, _, #, $, %).")

        return True
    

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str) -> bool:
        index = clave.lower().find("calisto")
        if index == -1:
            return False

        substring = clave[index:index + 7]
        uppercase_count = sum(1 for char in substring if char.isupper())
        
        return 2 <= uppercase_count < 7

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise LongitudInvalidaError("La clave debe tener más de 6 caracteres.")

        if not self._contiene_numero(clave):
            raise FaltaNumeroError("La clave debe contener al menos un número.")

        if not self.contiene_calisto(clave):
            raise ValueError("La clave debe contener la palabra 'calisto' con al menos dos letras en mayúscula, pero no todas.")

        return True


class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)