import os

CLIENT_BASE_FILE = 'client_base.txt'


def initialize_client_base():
    # Check if the file exists
    if not os.path.exists(CLIENT_BASE_FILE):
        with open(CLIENT_BASE_FILE, 'w') as f:
            # Write the header
            f.write("client_id  |  telegram_id  |  username  |  contact\n")
            print("Client base initialized with headers.")


def add_user(user_id, username):
    # Read existing user IDs to determine the next client_id
    existing_ids = set()

    with open(CLIENT_BASE_FILE, 'r') as f:
        for line in f:
            if line.strip() and line[0] != 'c':  # Skip the header line
                parts = line.split('|')
                existing_ids.add(parts[1].strip())

    # If the user ID is not already in the file, add it
    if str(user_id) not in existing_ids:
        # Determine the next client_id
        client_id = len(existing_ids) + 1

        with open(CLIENT_BASE_FILE, 'a') as f:
            # Write user data in the specified format
            f.write(f"{client_id}  |  {user_id}  |  {username}  |  Not provided\n")
            print(f"User {username} added with client_id {client_id}.")


def update_contact(user_id, contact):
    lines = []
    with open(CLIENT_BASE_FILE, 'r') as f:
        lines = f.readlines()

    with open(CLIENT_BASE_FILE, 'w') as f:
        for line in lines:
            if line.strip() and line[0] != 'c':  # Skip the header line
                parts = line.split('|')
                if parts[1].strip() == str(user_id):
                    # Update contact info
                    parts[3] = f"  {contact}\n"
                    line = '|'.join(parts)
            f.write(line)

