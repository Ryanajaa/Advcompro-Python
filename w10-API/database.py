from databases import Database

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

# Function to insert a new user into the users table
async def insert_user(username: str, password_hash: str, email: str):
	query = """
	INSERT INTO users (username, password_hash, email)
	VALUES (:username, :password_hash, :email)
	RETURNING user_id, username, password_hash, email, created_at
	"""
	values = {"username": username, "password_hash": password_hash, "email": email}
	return await database.fetch_one(query=query, values=values)

# Function to select a user by user_id from the users table
async def get_user(user_id: int):
	query = "SELECT * FROM users WHERE user_id = :user_id"
	return await database.fetch_one(query=query, values={"user_id": user_id})

# Function to update a user in the users table
async def update_user(user_id: int, username: str, password_hash: str, email: str):
	query = """
	UPDATE users
	SET username = :username, password_hash = :password_hash, email = :email
	WHERE user_id = :user_id
	RETURNING user_id, username, password_hash, email, created_at
	"""
	values = {"user_id": user_id, "username": username, "password_hash": password_hash, "email": email}
	return await database.fetch_one(query=query, values=values)

# Function to delete a user from the users table
async def delete_user(user_id: int):
	query = "DELETE FROM users WHERE user_id = :user_id RETURNING *"
	return await database.fetch_one(query=query, values={"user_id": user_id})