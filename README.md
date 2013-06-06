Row-level permissions
=========================
Ejemplo de como personalizar el admin de django para que cada usuario solo visualise los registros que el mismo creó.

Ver cambios importantes en:
---------------------------
* Ver demito/myapp/models.py
* Ver demito/myapp/admin.py

Cómo usarlo
-----------
Al ejecutar el proyecto demito(demo chiquito) se tiene un usuario admin y dos usuarios adicionales(user===password). 
Cada usuario adicional ha creado registros y solo el puede verlos, con exepción del administrador que es quien puede 
ver todos los registros creados por los usuarios.

Links importantes
-----------------

* DOING MORE WITH THE DJANGO ADMIN (Listing 13 y Listing 14)
http://www.ibm.com/developerworks/library/os-django-admin/

* CUSTOMIZING-THE-DJANGO-ADMIN (Diapositiva 48)
http://www.slideshare.net/lincolnloop/customizing-the-django-admin

