from flask import Flask, request, jsonify
import pandas as pd
import os

application = Flask(__name__)


# add an index page
@application.route("/")
def index():
    return "Hello World!"


# Get the excel file path from an environment variable, default to 'data.xlsx'
data_file = os.environ.get("DATA_FILE", "data.xlsx")

try:
    df_ARTG = pd.read_excel(data_file, sheet_name="ARTG")
    df_risk = pd.read_excel(data_file, sheet_name="pregnancy_risk")
except FileNotFoundError:
    print(f"Error: File '{data_file}' not found.")
    exit()


@application.route("/get_info", methods=["GET"])
def get_info():
    id = request.args.get("id")
    column_name = request.args.get("column")

    if not id or not column_name:
        return jsonify({"error": "Missing 'id' or 'column' parameters."}), 400

    if column_name not in df_ARTG.columns:
        return jsonify({"error": f"Column '{column_name}' not found."}), 400

    matches = df_ARTG[df_ARTG["ARTG ID"] == int(id)]
    if not matches.empty:
        value = str(matches[column_name].values[0])
    else:
        value = None
    return jsonify({"value": value})


@application.route("/get_id", methods=["GET"])
def get_id():
    name = request.args.get("name")

    if not name:
        return jsonify({"error": "Missing 'name' parameter."}), 400

    # Check if name is one of the products in df['Product Name'] (case insensitive and partial match)
    matches = df_ARTG[
        df_ARTG["Product Name"].astype(str).str.contains(name, case=False)
    ]
    # Return the first match
    if not matches.empty:
        id = str(matches["ARTG ID"].values[0])
    else:
        id = None
    return jsonify({"id": id})


@application.route("/get_pregnancy_data", methods=["GET"])
def get_pregnancy_data():
    name = request.args.get("name")

    if not name:
        return jsonify({"error": "Missing 'name' parameter."}), 400

    # case insensitive and partial match
    matches = df_risk[df_risk["Drug Name"].astype(str).str.contains(name, case=False)]
    # Return the first match
    if not matches.empty:
        category = str(matches["Category"].values[0])
        class_1 = str(matches["Classification Level 1"].values[0])
        class_2 = str(matches["Classification Level 2"].values[0])
        class_3 = str(matches["Classification Level 2"].values[0])
        return jsonify(
            {
                "Category": category,
                "Classification Level 1": class_1,
                "Classification Level 2": class_2,
                "Classification Level 3": class_3,
            }
        )
    return jsonify({"error": "Drug not found."}), 404


if __name__ == "__main__":
    # Use 0.0.0.0 to make the app accessible externally
    # application.run(host="0.0.0.0", port=5000, debug=True)
    pass
