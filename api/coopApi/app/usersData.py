"""This module will serve the api request."""

from config import client
from app import app
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
from importlib.machinery import SourceFileLoader

# Import the helpers module
helper_module = SourceFileLoader('*', './app/helpers.py').load_module()

# Select the database
db = client.Mile12
# Select the collection
collection = db.coop


@app.route("/coop", methods=['POST'])
def create_coop():
    """
       Function to create new coop
       """
    try:
        # Create new users
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            # Bad request as request body is not available
            # Add message for debugging purpose
            return "request body not available", 400

        record_created = collection.insert(body)

        # Prepare the response
        if isinstance(record_created, list):
            # Return list of Id of the newly created item
            return jsonify([str(v) for v in record_created]), 201
        else:
            # Return Id of the newly created item
            return jsonify(str(record_created)), 201
    except:
        # Error while trying to create the resource
        # Add message for debugging purpose
        return "Error inserting into database", 500


@app.route("/coop", methods=['GET'])
def fetch_coops():
    """
       Function to fetch the coop.
       """
    try:
        # Call the function to get the query params
        query_params = helper_module.parse_query_params(request.query_string)
        # Check if dictionary is not empty
        if query_params:
            # Try to convert the value to int
            #query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params.items()}

            # Fetch all the record(s)
            records_fetched = collection.find(query_params)
            x = dumps(records_fetched)
            # Check if the records are found
            if records_fetched.count() > 0:
                # Prepare the response
                return x
            else:
                # No records are found
                return "No records found", 404

        # If dictionary is empty
        else:
            # Return all the records as query string parameters are not available
            if collection.find().count() > 0:
                # Prepare response if the users are found
                return dumps(collection.find())
            else:
                # Return empty array if no users are found
                return jsonify([])
    except:
        # Error while trying to fetch the resource
        # Add message for debugging purpose
        return "Error Fetching response", 500


@app.route("/coop/<coop_id>", methods=['POST'])
def update_coop(coop_id):
    """
       Function to update a coop.
       """
    try:
        # Get the value which needs to be updated
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            # Bad request as the request body is not available
            # Add message for debugging purpose
            return "", 400

        # Updating the user
        records_updated = collection.update_one({"id": coop_id}, body)

        # Check if resource is updated
        if records_updated.modified_count > 0:
            # Prepare the response as resource is updated successfully
            return "", 200
        else:
            # Bad request as the resource is not available to update
            # Add message for debugging purpose
            return "", 404
    except:
        # Error while trying to update the resource
        # Add message for debugging purpose
        return "", 500


@app.route("/coop/<coop_id>", methods=['DELETE'])
def remove_coop(coop_id):
    """
       Function to remove a coop.
       """
    try:
        # Delete the user
        delete_user = collection.delete_one({"id": coop_id})

        if delete_user.deleted_count > 0 :
            # Prepare the response
            return "", 204
        else:
            # Resource Not found
            return "", 404
    except:
        # Error while trying to delete the resource
        # Add message for debugging purpose
        return "", 500

@app.route("/coop/members/<member_id>/<coop_id>", methods=['POST'])
def add_member(member_id, coop_id):
    """
       Function to add a member
       """
    try:
        body ={'$push': {'Members':member_id}}
        # Updating the user
        records_updated = collection.update_one({"id": coop_id}, body)

        # Check if resource is updated
        if records_updated.modified_count > 0:
            # Prepare the response as resource is updated successfully
            return "", 200
        else:
            # Bad request as the resource is not available to update
            # Add message for debugging purpose
            return "", 404
    except:
        # Error while trying to update the resource
        # Add message for debugging purpose
        return "", 500

@app.route("/coop/removeMember/<member_id>/<coop_id>", methods=['POST'])
def remove_member(member_id, coop_id):
    """
       Function to remove a member
       """
    try:
        body ={'$pull': {'Members':{'$in':[member_id]}}}
        # Updating the user
        records_updated = collection.update({"id": coop_id}, body)

        # Check if resource is updated
        if records_updated.modified_count > 0:
            # Prepare the response as resource is updated successfully
            return "", 200
        else:
            # Bad request as the resource is not available to update
            # Add message for debugging purpose
            return "", 404
    except:
        # Error while trying to update the resource
        # Add message for debugging purpose
        return "", 500

@app.route("/coop/product/<product_id>/<coop_id>", methods=['POST'])
def add_product (product_id, coop_id):
    """
       Function to add a product
       """
    try:
        body ={'$push': {'Products':product_id}}
        # Updating the user
        records_updated = collection.update({"id": coop_id}, body)

        # Check if resource is updated
        if records_updated.modified_count > 0:
            # Prepare the response as resource is updated successfully
            return "", 200
        else:
            # Bad request as the resource is not available to update
            # Add message for debugging purpose
            return "", 404
    except:
        # Error while trying to update the resource
        # Add message for debugging purpose
        return "", 500

@app.route("/coop/removeProduct/<product_id>/<coop_id>", methods=['POST'])
def remove_product(product_id, coop_id):
    """
       Function to remove a product
       """
    try:
        body ={'$pull': {'Members':{'$in':[product_id]}}}
        # Updating the user
        records_updated = collection.update({"id": coop_id}, body)

        # Check if resource is updated
        if records_updated.modified_count > 0:
            # Prepare the response as resource is updated successfully
            return "", 200
        else:
            # Bad request as the resource is not available to update
            # Add message for debugging purpose
            return "", 404
    except:
        # Error while trying to update the resource
        # Add message for debugging purpose
        return "", 500


@app.errorhandler(404)
def page_not_found(e):
    """Send message to the user with notFound 404 status."""
    # Message to the user
    message = {
        "err":
            {
                "msg": "This route is currently not supported. Please refer API documentation."
            }
    }
    # Making the message looks good
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    # Returning the object
    return resp
