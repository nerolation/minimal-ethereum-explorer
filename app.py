from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import requests
from eth2spec.deneb.mainnet import BeaconBlock
import snappy

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

node_url = "http://localhost:5052"

@app.route('/block/<int:block_number>', methods=['GET'])
def get_block(block_number):
    slot_number = block_number  # Use the provided block number as the slot number

    # Construct the URL to query the beacon block by slot
    url = f"{node_url}/eth/v1/beacon/blocks/{slot_number}"

    try:
        # Send the GET request to fetch the beacon block
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the JSON response
        block_data = response.json()

        # Display the block data
        return jsonify(block_data)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
