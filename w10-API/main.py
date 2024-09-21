from databases import Database
import asyncio
POSTGRES_USER = "temp"
POSTGRES_PASSWORD = "temp"
POSTGRES_DB = "advcompro_w10"

database = Database(f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DB}')

async def connect_db():
	await database.connect()
	print("Database connected")

async def disconnect_db():
	await database.disconnect()
	print("Database disconnected")

# Function to select data from a table
async def select_data():
	query = "SELECT * FROM users" # 'users' with the actual table name
	rows = await database.fetch_all(query)
	for row in rows:
		print(dict(row)) # Prints each row in the result

# Function to insert data into the items table
async def insert_user(username, password_hash,email):
	query = """
	INSERT INTO users (username, password_hash,email)

	VALUES (:username, :password_hash, :email)
	RETURNING user_id, username, password_hash,email,created_at
	"""
	values = {"username": username, "password_hash": password_hash,"email": email}
	result = await database.execute(query=query, values=values)
	print(f"Inserted User ID: {result}") # Prints the inserted item's ID

# Function to update data in the items table
async def update_user(user_id, username=None, password_hash=None,email=None):
	# Construct the base update query
	query = "UPDATE users SET "
	values = {"user_id": user_id}

# Dynamically build the update fields based on provided values
	update_fields = []
	if username is not None:
		update_fields.append("username = :username")
		values["username"] = username
	if password_hash is not None:
		update_fields.append("password_hash = :password_hash")
		values["password_hash"] = password_hash
	if email is not None:
		update_fields.append("email = :email")
		values["email"] = email

	# Join the fields and complete the query
	query += ", ".join(update_fields) + " WHERE user_id = :user_id RETURNING *"

	# Execute the update query
	updated_row = await database.fetch_one(query=query, values=values)
	if updated_row:
		print(f"Updated item: {dict(updated_row)}")
	else:
		print(f"No item found with ID: {user_id}")

# Function to delete data from the items table
async def delete_user(user_id):
	query = "DELETE FROM users WHERE user_id = :user_id RETURNING *"
	values = {"user_id": user_id}

	# Execute the delete query and fetch the deleted row
	deleted_row = await database.fetch_one(query=query, values=values)
	if deleted_row:
		print(f"Deleted item: {dict(deleted_row)}")
	else:
		print(f"No item found with ID: {user_id}")

# Main function to run the async functions
async def main():
	await connect_db() # Connect to the database
	# await select_data() #add function sql : select
	# await insert_user('TA2', '1234','TA2@kmitl.ac.th') # Insert a sample User
	# await update_user(1, username='TA', password_hash='123',email='TA1@kmitl.ac.th') # Update a specific item
	# await delete_user(2) # Delete a specific item by ID
	await disconnect_db() # Disconnect from the database

if __name__ == "__main__":
	asyncio.run(main())