from cx_Freeze import setup, Executable

setup( name = "ventana",
           version = "0.1" ,
           description = "ventana" ,
           executables = [Executable("interfaz_grafica2.py")] , )
