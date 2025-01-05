CONNECTION = "dbname=vision-kapture-database host=vision-kapture-server.postgres.database.azure.com port=5432 sslmode=require user=kqghsorhda password=tzaAteNjgzaZ$ZYb"
CONNECTION_STR = {pair.split('=')[0]:pair.split('=')[1] for pair in CONNECTION.split(' ')}
print(CONNECTION_STR)