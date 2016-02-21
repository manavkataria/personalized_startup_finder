-- Enter URL Into Your Browser. Once you’ve located your user key, type the following URL address into your browser and replacing "user_key" with the value that you received in your email.
-- https://api.crunchbase.com/v/3/snapshot/crunchbase_2013_snapshot.tar.gz?user_key=user_key
-- For example, if your "user_key" is 1a2b3c4d5e6f7g8h9i0j, you would type:
-- https://api.crunchbase.com/v/3/snapshot/crunchbase_2013_snapshot.tar.gz?user_key=1a2b3c4d5e6f7g8h9i0j


--To upload the company information to mysql

--mysql -u root -p -h localhost mydb < cb_objects.sql

--SQL to extract important information

SELECT id, name, normalized_name, category_code, status, founded_at, overview, tag_list, country_code, city, investment_rounds, funding_total_usd 
FROM mydb.cb_objects
WHERE entity_type = 'Company';