# librerias/STRUCTVAG.py
# Lectura de bytes binarios estructurados para VAGAX — CERO imports nativos.
# Reimplementa únicamente las operaciones de struct que usa IMAGENVAG:
#   - unpack_from('<I', data, offset)  → uint32 little-endian
#   - unpack_from('<i', data, offset)  → int32  little-endian
#   - unpack_from('<H', data, offset)  → uint16 little-endian
#   - unpack_from('>H', data, offset)  → uint16 big-endian
# Todo implementado manualmente con aritmética de bits, sin 'import struct'.


class STRUCTVAG:
    """
    Lector de campos binarios para VAGAX.
    Opera directamente sobre objetos bytes/bytearray de Python.
    CERO imports de librerías externas.
    """

    # =========================================================
    # HELPERS INTERNOS DE CONVERSIÓN DE BYTES
    # =========================================================

    @staticmethod
    def _bytes_a_uint16_le(data, offset):
        """Lee 2 bytes como entero sin signo little-endian."""
        b0 = data[offset]
        b1 = data[offset + 1]
        return b0 | (b1 << 8)

    @staticmethod
    def _bytes_a_uint32_le(data, offset):
        """Lee 4 bytes como entero sin signo little-endian."""
        b0 = data[offset]
        b1 = data[offset + 1]
        b2 = data[offset + 2]
        b3 = data[offset + 3]
        return b0 | (b1 << 8) | (b2 << 16) | (b3 << 24)

    @staticmethod
    def _bytes_a_int32_le(data, offset):
        """Lee 4 bytes como entero con signo little-endian (complemento a 2)."""
        v = STRUCTVAG._bytes_a_uint32_le(data, offset)
        # Si el bit más significativo está activo → negativo
        if v >= 0x80000000:
            v -= 0x100000000
        return v

    @staticmethod
    def _bytes_a_uint16_be(data, offset):
        """Lee 2 bytes como entero sin signo big-endian."""
        b0 = data[offset]
        b1 = data[offset + 1]
        return (b0 << 8) | b1

    # =========================================================
    # API PÚBLICA — unpack_from compatible con struct de Python
    # =========================================================

    @staticmethod
    def unpack_from(fmt, data, offset=0):
        """
        Desempaqueta bytes en (valor,) según el formato dado.
        Formatos soportados:
            '<I'  → uint32 little-endian
            '<i'  → int32  little-endian
            '<H'  → uint16 little-endian
            '>H'  → uint16 big-endian
        Retorna una tupla de un elemento, igual que struct.unpack_from.
        """
        if fmt == '<I':
            return (STRUCTVAG._bytes_a_uint32_le(data, offset),)

        if fmt == '<i':
            return (STRUCTVAG._bytes_a_int32_le(data, offset),)

        if fmt == '<H':
            return (STRUCTVAG._bytes_a_uint16_le(data, offset),)

        if fmt == '>H':
            return (STRUCTVAG._bytes_a_uint16_be(data, offset),)

        raise Exception(
            "[STRUCTVAG] Formato no soportado: '" + fmt + "'. "
            "Soportados: '<I', '<i', '<H', '>H'"
        )

    # =========================================================
    # HELPERS ADICIONALES DE UTILIDAD
    # =========================================================

    @staticmethod
    def leer_byte(data, offset):
        """Lee un byte sin signo en la posición dada."""
        return data[offset]

    @staticmethod
    def leer_uint16_be(data, offset):
        """Lee uint16 big-endian directamente."""
        return STRUCTVAG._bytes_a_uint16_be(data, offset)

    @staticmethod
    def leer_uint16_le(data, offset):
        """Lee uint16 little-endian directamente."""
        return STRUCTVAG._bytes_a_uint16_le(data, offset)

    @staticmethod
    def leer_uint32_le(data, offset):
        """Lee uint32 little-endian directamente."""
        return STRUCTVAG._bytes_a_uint32_le(data, offset)

    @staticmethod
    def leer_int32_le(data, offset):
        """Lee int32 little-endian directamente."""
        return STRUCTVAG._bytes_a_int32_le(data, offset)
