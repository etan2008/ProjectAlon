# ProjectAlon
ALON Repository for Karagathon Submission

## Included Files:
- Django App for Database and Dashboard
- Arduino Code for Fisher ID and Buoys

## For Django App
1. Download the PHL_adm folder (data from gadm.com) from this drive folder: https://drive.google.com/drive/folders/151tUSZPQDzj0C5yD0BrGdsiRkra9A9Nh?usp=sharing
2. Place contents inside Alon Folder
3. Launch a virtual environment (this guide will use pip for installing packages)
4. Run <code>pip install -r requirements.txt</code> to install needed packages
(**note**: Windows users may have problems installing the Fiona package/GPAL, refer 
to this site https://jingwen-z.github.io/how-to-install-python-module-fiona-on-windows-os/ for details)
5. Run <code>python manage.py collectstatic</code>
6. Then to launch, run <code>python manage.py server</code>
7. Go to http://127.0.0.1:8000/admin and log-in with the following credentials:
    > username: martin

    > password: djang0_123

## Available sites within the Django App:
- http://127.0.0.1:8000/admin for data adding
- http://127.0.0.1:8000/performance for database viewing
- http://127.0.0.1:8000/statistics for statistics
- http://127.0.0.1:8000/plots for buoy geoplots
