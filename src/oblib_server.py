# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This program implements a rudimentary REST server with a backend RDBMS for the Utility Entrypoint.  The
Utility Entrypoint is selected since it is the smallest Entrypoint (one Axis and four Concepts) in the Orange
Button Taxonomy.  Thus this can be used as a starting point on how to build a REST server for other larger
Entrypoints.

This uses the Flask framework for the HTTP interface and ANSI SQL for the database.  It has been tested with MySQL
but should work with any RDBMS.  The Flask usage is minimal to emphasize that this is not tied to any particular
framework.  For a full size application it is suggested to use a full scale framework and ORM system as opposed to
using the code that is written here.

Before running this program a database needs to be setup with the following table placed in it:

    CREATE TABLE utility (
        utility_id CHAR(36),
        name VARCHAR(80),
        contact_name_and_title VARCHAR(80),
        identifier CHAR(20),
        email_address VARCHAR(40)
    );

And the configuration file (oblib-server.cfg) needs to be place in the startup directory.  Its contents should be:

    [database]
    server=<SERVER_NAME>
    user=<USER>
    password=<PASSWORD>
    database=<DATABASE>

Then use the following comand to start the REST server.

    $ pip install Flask
    $ FLASK_APP=oblib_server.py flask run

Here are some working queries:

    curl -X POST -H "Content-Type: application/json" -d @"oblib_server_test.json"  http://localhost:5000/utility/62511403-0fe9-4775-a9c3-7b1b59e497c0
    curl -X GET http://localhost:5000/utility/62511403-0fe9-4775-a9c3-7b1b59e497c0
    curl -X DELETE http://localhost:5000/utility/62511403-0fe9-4775-a9c3-7b1b59e497c0
"""

from oblib import taxonomy, data_model, parser

import configparser
import mysql.connector
from flask import Flask, request

"""Global Variables"""
orange_db = None
ob_taxonomy = None
ob_parser = None


def get_fact_value(fact):
    """ Convenience function for dealing with facts set to None"""

    if fact is None:
        return ""
    else:
        return fact.value


class Utility:
    """ Main Utility class to hold Orange Button Utility Data"""

    def __init__(self):
        self.utility_id = None
        self.name = None
        self.contact_name_and_title = None
        self.identifier = None
        self.email_address = None

    def __str__(self):
        return "utility_id: " + str(self.utility_id) + \
              "; name: " + str(self.name) + \
              "; contact_name_and_title: " + str(self.contact_name_and_title) + \
              "; identifier: " + str(self.identifier) + \
              "; email_address: " + str(self.email_address)

    def from_JSON_string(self, json):
        """ Load self from Orange Button JSON string"""

        entrypoint = ob_parser.from_JSON_string(json, "Utility")
        print(self.utility_id)
        ctx = data_model.Context(duration="forever", UtilityIdentifierAxis=self.utility_id)
        self.name = get_fact_value(entrypoint.get("solar:UtilityName", ctx))
        self.contact_name_and_title = get_fact_value(entrypoint.get("solar:UtilityContactNameAndTitle", ctx))
        self.identifier = get_fact_value(entrypoint.get("solar:UtilityIdentifier", ctx))
        self.email_address = get_fact_value(entrypoint.get("solar:UtilityEmailAddress", ctx))

    def to_JSON_string(self):
        """ Convert and return an Orange Button JSON string"""

        entrypoint = data_model.OBInstance("Utility", ob_taxonomy)
        kwargs = {}
        kwargs["duration"] = "forever"
        kwargs["solar:UtilityIdentifierAxis"] = self.utility_id
        entrypoint.set("solar:UtilityName", self.name, **kwargs)
        entrypoint.set("solar:UtilityContactNameAndTitle", self.contact_name_and_title, **kwargs)
        #entrypoint.set("solar:UtilityIdentifier", rec.identifier, **kwargs)
        entrypoint.set("solar:UtilityEmailAddress", self.email_address, **kwargs)
        json = ob_parser.to_JSON_string(entrypoint)
        return json


class OrangeDb:
    """ Orange Button Database class with straight SQL (tested with MySQL) and no ORM"""

    __connection = None

    def open(self, server, user, pwd, db):
        """Open Database"""

        OrangeDb.__connection = mysql.connector.connect(host=server, user=user, passwd=pwd, database=db)

    def close(self):
        """Close Database"""

        if OrangeDb.__connection != None:
            OrangeDb.__connection.close()

    def insert_utility(self, rec):
        """Insert a utility record"""
        cursor = OrangeDb.__connection.cursor()
        cursor.execute("""
            INSERT INTO utility (
                utility_id, name, contact_name_and_title, identifier, email_address)
            VALUES(
                %s, %s, %s, %s, %s)
            """, (rec.utility_id, rec.name, rec.contact_name_and_title, rec.identifier, rec.email_address))
        cursor.execute("commit")
        cursor.close()

    def read_utility(self, rec):
        """Read utility record"""
        cursor = OrangeDb.__connection.cursor()
        results = cursor.execute("SELECT * FROM utility WHERE utility_id=%s",
            (rec.utility_id,))
        for row in cursor:
            rec.utility_id = row[0]
            rec.name = row[1]
            rec.contact_name_and_title = row[2]
            rec.identifier = row[3]
            rec.email_address = row[4]
            break
        cursor.execute("commit")
        cursor.close()
        return rec

    def delete_utility(self, rec):
        """Delete utility record"""
        cursor = OrangeDb.__connection.cursor()
        cursor.execute("DELETE FROM utility WHERE utility_id=%s",
            (rec.utility_id,))
        cursor.execute("commit")
        cursor.close()


def init():
    """Initialize program"""
    global orange_db
    global ob_taxonomy
    global ob_parser

    config = configparser.ConfigParser()
    config.read("oblib_server.ini")
    server = config.get("database", "server")
    user = config.get("database", "user")
    pwd = config.get("database", "password")
    db = config.get("database", "database")
    orange_db = OrangeDb()
    orange_db.open(server, user, pwd, db)
    ob_taxonomy = taxonomy.Taxonomy()
    ob_parser = parser.Parser(ob_taxonomy)
    print("Initialization completed")


"""Main Code - Start Flask"""
init()
app = Flask(__name__)
"""End of Main Code"""


@app.route('/utility/<utility_id>', methods=['DELETE'])
def delete_handler(utility_id):
    """Flask Delete Handler for utility"""

    try:
        rec = Utility()
        rec.utility_id = utility_id
        orange_db.delete_utility(rec)
        return '{"type": "Success"}'
    except Exception as e:
        print(e)
        return '{"type": "Error", "message": "Input is not correct."}'


@app.route('/utility/<utility_id>', methods=['GET'])
def read_handler(utility_id):
    """Flask Read Handler for utility"""

    try:
        rec = Utility()
        rec.utility_id = utility_id
        orange_db.read_utility(rec)
        json = rec.to_JSON_string()
        return '{"type": "Success", "message": ' + json + '}'
    except Exception as e:
        print(e)
        return '{"type": "Error", "message": "Input is not correct."}'


@app.route('/utility/<utility_id>', methods=['POST'])
def write_hander(utility_id):
    """Flask Write Handler for utility"""

    try:
        rec = Utility()
        rec.utility_id = utility_id
        rec.from_JSON_string(request.data)
        orange_db.insert_utility(rec)
        return '{"type": "Success"}'
    except Exception as e:
         print(e)
         return '{"type": "Error", "message": "Input is not correctly formatted JSON"}'
