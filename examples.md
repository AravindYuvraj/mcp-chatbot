# MCP Code Examples

## Example: MCP Server (Python Flask)
```python
from flask import Flask, request, jsonify
app = Flask(__name__)

# Example context store
context_store = {}

@app.route('/mcp/context', methods=['GET', 'POST'])
def context():
    if request.method == 'POST':
        data = request.json
        # Validate and store context
        context_store.update(data)
        return jsonify({'status': 'success'}), 201
    else:
        return jsonify(context_store)

if __name__ == '__main__':
    app.run(port=5000)
```

## Example: MCP Client (Python requests)
```python
import requests

# Get context
resp = requests.get('http://localhost:5000/mcp/context')
print(resp.json())

# Update context
resp = requests.post('http://localhost:5000/mcp/context', json={'user': 'alice', 'role': 'admin'})
print(resp.json())
``` 