from django.db import migrations
def cargar_datos_desde_sql():
    from proyecto.settings import BASE_DIR
    import os
    sql_script = open(os.path.join(BASE_DIR,'libreria/sql/migracion.sql'),'r').read()
    return sql_script
class Migration(migrations.Migration):
    dependencies = [('libreria', '0003_librocronica_libro_edicion_anterior_libro_editorial_and_more'),]
    operations = [migrations.RunSQL(cargar_datos_desde_sql(),)]

