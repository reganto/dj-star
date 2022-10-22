import socket

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Test database connectivity."
    
    def add_arguments(self, parser):
        parser.add_argument("db", type=str, help="Particular database to connect.")

    def handle(self, *args, **optoins):
        db = optoins["db"]
        try:
            if db == "mysql":
                s = socket.create_connection(("localhost", 3306), 5)
            if db == "pg":
                s = socket.create_connection(("localhost", 5432), 5)
            s.close()
        except socket.timeout:
            raise socket.timeout(self.style.ERROR("Can't detect the database server."))
        except ConnectionRefusedError as e:
            raise ConnectionRefusedError(self.style.ERROR(e))
        else:
            self.stdout.write(self.style.SUCCESS("Connection established successfully!"))