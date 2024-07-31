# Python File Transfer over LAN

This project demonstrates a simple file transfer system over a LAN using Python's socket module.

## Files Included
- `server.py`: The server script that sends files.
- `client.py`: The client script that receives files.
- `README.txt`: This file.

## Requirements
- Python 3.x

## Instructions

### Server Setup
1. Place `server.py` on the server machine.
2. Ensure the file to send is in the same directory as `server.py`.
3. Run the server script:
   ```sh
   python server.py
   ```

### Client Setup
1. Place `client.py` on the client machine.
2. Update `filename` in `client.py` with the desired file name.
3. Update `host` in `client.py` with the server's IP address.
4. Run the client script:
   ```sh
   python client.py
   ```

## Example
1. Place `example.txt` in the same directory as `server.py` on the server machine.
2. Run the server:
   ```sh
   python server.py
   ```
3. Update `client.py` with:
   ```python
   filename = 'example.txt'
   host = 'SERVER_IP_ADDRESS'
   port = 65432
   ```
4. Run the client:
   ```sh
   python client.py
   ```

## Notes
- Ensure the server is running before starting the client.
- The received file will be saved with the prefix `received_`.

## License
This project is licensed under the MIT License.
