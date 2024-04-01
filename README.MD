# Volunteer

## About

This is project created for school №1236.

## Install from localhost

```
git clone https://github.com/gepolis/EBook4.git
cd EBook4
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py runserver
```

## **Update** script from hosting
```sh
rm -r Ebook1R
mv Ebook1 Ebook1R
git clone https://github.com/gepolis/Ebook4.git
mv Ebook4 Ebook1
cd Ebook1
nohup python3 manage.py runserver &

echo "Updated!"

```
