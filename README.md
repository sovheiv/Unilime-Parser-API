### Deploy manual
1. `git clone git@github.com:sovheiv/Unilime-Parser-API.git`
1. Rename `example.env` to `.env` and fill the credentials
1. `docker-compose up -d`
1. Connect to Postgres, create `unilime_parser_app`
1. `docker-compose up -build -d`

### Initial import products and reviews
1. `python manage.py import_products` ../start_data/Products.csv
1. `python manage.py import_reviews` ../start_data/Reviews.csv


