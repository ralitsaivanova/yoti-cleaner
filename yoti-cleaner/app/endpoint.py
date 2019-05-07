
import psycopg2
from flask import jsonify
from flask import request
from werkzeug.exceptions import BadRequest

from app.room import Floor
from app.vacuum_cleaner import VacuumCleaner
from database.db_conn import conn

from flask import Flask
app = Flask(__name__)
app.config["APPLICATION_ROOT"] = f"{app.config['APPLICATION_ROOT']}app/"

@app.route("/", methods=['POST',])
def cleaning():
    if request.is_json:
        payload = request.get_json()
    else:
        return BadRequest(description="Mimetype needs to be json")

    try:
        room_width, room_length = payload["roomSize"]
        dirty_patches = payload["patches"]
        cleaning_instructions = payload["instructions"]
        cleaner_coord_x, cleaner_coord_y = payload["coords"]
    except (KeyError, TypeError):
        return BadRequest(description="Mal formed payload")

    try:
        floor = Floor(room_width, room_length, dirty_patches)

        cleaner = VacuumCleaner(cleaner_coord_x, cleaner_coord_y, floor)
    except ValueError as v_err:
        return BadRequest(description=v_err)

    result = cleaner.clean_floor(cleaning_instructions)

    cleaning_session = (
        room_width, room_length, cleaner_coord_x, cleaner_coord_y,
        result["coords"][0], result["coords"][1], f"{dirty_patches}",
        result['patches'], cleaning_instructions
    )

    _persist_cleaning_request(*cleaning_session)

    return jsonify(result)


def _persist_cleaning_request(*cleaning_session):
    sql = (
        f"INSERT INTO cleaning_session"
        f"(room_width,room_length,starting_x,starting_y,final_x,final_y,"
        f"dirty_patches,num_patches_cleaned,instructions) "
        f"VALUES{cleaning_session}"
    )

    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
    except (Exception, psycopg2.DatabaseError):
        pass
