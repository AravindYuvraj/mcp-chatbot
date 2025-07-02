# MCP Troubleshooting Guide

## Common Issues

### 1. Connection Errors
- **Symptom:** Client cannot connect to MCP server.
- **Solution:**
  - Check server URL and port.
  - Ensure server is running and accessible.
  - Verify network/firewall settings.

### 2. Schema Validation Failures
- **Symptom:** Server rejects context data.
- **Solution:**
  - Validate data against the expected schema.
  - Check for missing or extra fields.

### 3. Authentication Failures
- **Symptom:** Unauthorized errors from server.
- **Solution:**
  - Ensure correct API keys or tokens are used.
  - Check user permissions.

### 4. Version Mismatch
- **Symptom:** Client and server use different MCP versions.
- **Solution:**
  - Confirm both use compatible protocol versions.
  - Update client or server as needed. 