def export_table_to_txt_passenger():
    import mysql.connector
    import os
    from db import get_connection



    # ---------- DATABASE CONNECTION ----------
    con = get_connection()
    cursor = con.cursor()

    # ---------- FETCH DATA ----------
    cursor.execute("SELECT * FROM PASSENGER")
    rows = cursor.fetchall()
    headers = [col[0] for col in cursor.description]

    cursor.close()
    con.close()

    # ---------- CALCULATE COLUMN WIDTHS ----------
    col_widths = []
    for i in range(len(headers)):
        max_len = len(headers[i])
        for row in rows:
            max_len = max(max_len, len(str(row[i])))
        col_widths.append(max_len + 2)  # padding

    # ---------- WRITE FORMATTED TEXT ----------
    txt_file = "table_data_pasenger.txt"
    with open(txt_file, "w", encoding="utf-8") as f:

        # Header
        header_line = ""
        for i, h in enumerate(headers):
            header_line += h.ljust(col_widths[i])
        f.write(header_line + "\n")

        # Separator
        f.write("-" * sum(col_widths) + "\n")

        # Rows
        for row in rows:
            line = ""
            for i, item in enumerate(row):
                line += str(item).ljust(col_widths[i])
            f.write(line + "\n")

    # ---------- OPEN IN NOTEPAD ----------
    os.system(f'notepad "{txt_file}"')

def export_table_to_txt_booking():
    import mysql.connector
    import os
    from db import get_connection



    # ---------- DATABASE CONNECTION ----------
    con = get_connection()
    cursor = con.cursor()

    # ---------- FETCH DATA ----------
    cursor.execute("SELECT * FROM BOOKING")
    rows = cursor.fetchall()
    headers = [col[0] for col in cursor.description]

    cursor.close()
    con.close()

    # ---------- CALCULATE COLUMN WIDTHS ----------
    col_widths = []
    for i in range(len(headers)):
        max_len = len(headers[i])
        for row in rows:
            max_len = max(max_len, len(str(row[i])))
        col_widths.append(max_len + 2)

    # ---------- WRITE FORMATTED TEXT ----------
    txt_file = "table_data_booking.txt"
    with open(txt_file, "w", encoding="utf-8") as f:

        # Header
        header_line = ""
        for i, h in enumerate(headers):
            header_line += h.ljust(col_widths[i])
        f.write(header_line + "\n")

        # Separator
        f.write("-" * sum(col_widths) + "\n")

        # Rows
        for row in rows:
            line = ""
            for i, item in enumerate(row):
                line += str(item).ljust(col_widths[i])
            f.write(line + "\n")

    # ---------- OPEN IN NOTEPAD ----------
    os.system(f'notepad "{txt_file}"')

def export_table_to_txt_train():
    import mysql.connector
    import os
    from db import get_connection



    # ---------- DATABASE CONNECTION ----------
    con = get_connection()
    cursor = con.cursor()

    # ---------- FETCH DATA ----------
    cursor.execute("SELECT * FROM TRAIN")
    rows = cursor.fetchall()
    headers = [col[0] for col in cursor.description]

    cursor.close()
    con.close()

    # ---------- CALCULATE COLUMN WIDTHS ----------
    col_widths = []
    for i in range(len(headers)):
        max_len = len(headers[i])
        for row in rows:
            max_len = max(max_len, len(str(row[i])))
        col_widths.append(max_len + 2)  # padding

    # ---------- WRITE FORMATTED TEXT ----------
    txt_file = "table_data_train.txt"
    with open(txt_file, "w", encoding="utf-8") as f:

        # Header
        header_line = ""
        for i, h in enumerate(headers):
            header_line += h.ljust(col_widths[i])
        f.write(header_line + "\n")

        # Separator
        f.write("-" * sum(col_widths) + "\n")

        # Rows
        for row in rows:
            line = ""
            for i, item in enumerate(row):
                line += str(item).ljust(col_widths[i])
            f.write(line + "\n")

    # ---------- OPEN IN NOTEPAD ----------
    os.system(f'notepad "{txt_file}"')