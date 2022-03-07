from django.db import connection


def query_for_tipo(tipo_activo):
    list_activos = []

    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT a.id, a.nombre, a.descripcion, a.serial, a.numerointerno, a.peso, a.alto,
                        a.ancho, a.largo, a.valorcompra, a.fechacompra, a.fechabaja, a.estadoactual, a.color,
                        p.primernombre, a2.nombre, t.nombre FROM activo a
                        INNER JOIN tipoactivo t ON a.tipo_id = t.id
                        INNER JOIN persona p ON a.persona_id = p.id
                        INNER JOIN area a2 ON a.area_id = a2.id
                        WHERE t.nombre = '{}'
                        """.format(tipo_activo))

        for element in cursor.fetchall():
            list_activos.append({
                "id": element[0],
                "nombre": element[1],
                "descripcion": element[2],
                "serial": element[3],
                "numerointerno": element[4],
                "peso": element[5],
                "alto": element[6],
                "ancho": element[7],
                "largo": element[8],
                "valorcompra": element[9],
                "fechacompra": element[10],
                "fechabaja": element[11],
                "estadoactual": element[12],
                "color": element[13],
                "persona": element[14],
                "area": element[15],
                "tipo": element[16],
            })

    return list_activos

def query_for_fechacompra(fecha_compra):
    list_activos = []

    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT a.id, a.nombre, a.descripcion, a.serial, a.numerointerno, a.peso, a.alto,
                        a.ancho, a.largo, a.valorcompra, a.fechacompra, a.fechabaja, a.estadoactual, a.color,
                        p.primernombre, a2.nombre, t.nombre FROM activo a
                        INNER JOIN tipoactivo t ON a.tipo_id = t.id
                        INNER JOIN persona p ON a.persona_id = p.id
                        INNER JOIN area a2 ON a.area_id = a2.id
                        WHERE a.fechacompra::date = '{}'
                        """.format(fecha_compra))

        for element in cursor.fetchall():
            list_activos.append({
                "id": element[0],
                "nombre": element[1],
                "descripcion": element[2],
                "serial": element[3],
                "numerointerno": element[4],
                "peso": element[5],
                "alto": element[6],
                "ancho": element[7],
                "largo": element[8],
                "valorcompra": element[9],
                "fechacompra": element[10],
                "fechabaja": element[11],
                "estadoactual": element[12],
                "color": element[13],
                "persona": element[14],
                "area": element[15],
                "tipo": element[16],
            })

    return list_activos

def query_for_serial(serial):
    list_activos = []

    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT a.id, a.nombre, a.descripcion, a.serial, a.numerointerno, a.peso, a.alto,
                        a.ancho, a.largo, a.valorcompra, a.fechacompra, a.fechabaja, a.estadoactual, a.color,
                        p.primernombre, a2.nombre, t.nombre FROM activo a
                        INNER JOIN tipoactivo t ON a.tipo_id = t.id
                        INNER JOIN persona p ON a.persona_id = p.id
                        INNER JOIN area a2 ON a.area_id = a2.id
                        WHERE a.serial = '{}'
                        """.format(serial))

        for element in cursor.fetchall():
            list_activos.append({
                "id": element[0],
                "nombre": element[1],
                "descripcion": element[2],
                "serial": element[3],
                "numerointerno": element[4],
                "peso": element[5],
                "alto": element[6],
                "ancho": element[7],
                "largo": element[8],
                "valorcompra": element[9],
                "fechacompra": element[10],
                "fechabaja": element[11],
                "estadoactual": element[12],
                "color": element[13],
                "persona": element[14],
                "area": element[15],
                "tipo": element[16],
            })
    return list_activos