THESIS:

    We have business task that represents work of storages 
    (like logistic business, e-commerce etc.)
    We need to create an agile data processing solution that can be 
    later implemented in data streaming(large scale).
    Output of this project should be usable 
    for data analysis like SQL format(databases, PowerBi etc.).

SOLUTION:

    We assuming that task might be changing in future, 
    like any business task that client prodives.
    So by this conception all possinble options 
    should be agile and scalable.
    That means code should be able work in future 
    with more than 7 Warehouses with Products
    Also python code should usable for PySpark to create SQL Transaction database
    For this demo we will not set .env files and version control

INSTALLATIONS | Packages:
    for this project we need to install in virtual environment of project:
    -PySpark


PROJECT STRUCTURE:
    -data - folder for RAW data (txt)
    -out - folder for processed data (sql)
    -src - source executive code (python)
        - data_deserializer - for processing input data format to python objects(classes).
        - warehouse_processor - for applying external NonWareHose operations like "New = Old / 3".
        - main_python_1.py - is executable file for solving "Python_1" task.
        - main_PySpark_SQL_2.py - is executable file/notebook for solving "PySpark_SQL_2" task.
    -venv - folder for all external libraries / virtual environment

LOGIC:
    - converting txt data to python objects
    - storing ware into lits
    - parsing the list

ENTITIES:
    business_day - variable represents one operational day

    class Product - describes a abstact product with 2 values(initial and lst)
                    product was set by class for ability to call initial number
    class Warehouse - class stac contains Products inside (in lits)
    class Transaction - make record in SQL(or else) about Product movement between Warehouses

REMARKS AND IMPROVEMENTS:

    function names was set according to context of task
    variable names was set readable, but might be possible shorted/optimized in future
    might be implemented tests for each function