### **STUDENTS API (Python & Django + DRF & Swagger)**

**TO RUN APP:**
1. $ python3 -m venv venv
2. $ source venv/bin/activate
   
Verify that virtualenv is working
(at the beginning of the command line must be (env))

3. (env) $ pip install -r requirements.txt
4. (env) $ python manage.py migrate && python manage.py runserver 0.0.0.0:8888
----------------------------------------------------

**OR:**

$ docker-compose up --build

----------------------------------------------------

**TO EXECUTE TEST CASES:**
(env) $ python manage.py test

----------------------------------------------------

**ENDPOINTS OF APP:**
1. http://0.0.0.0:8888/ - swagger API
2. http://0.0.0.0:8888/students/ - Django REST Framework API for students 
   instances
3. http://0.0.0.0:8888/openapi/ - dynamically generated OPENAPI YAML JSONSchema 
   from python dataclasses
