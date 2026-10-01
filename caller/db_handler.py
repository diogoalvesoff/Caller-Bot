import os
import asyncpg
import socket
import ssl
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("SUPABASE_DB_URL")
pool = None

async def create_pool():
    """Creates a Supabase conection pool. Needs to be called on_ready or setup_hook"""
    global pool
    
    domain = "aws-0-ca-central-1.pooler.supabase.com"
    ipv4_ip = socket.gethostbyname(domain)
    ipv4_url = DB_URL.replace(domain, ipv4_ip)

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    pool = await asyncpg.create_pool(ipv4_url, ssl=ctx)


async def setup_db_tables():
    query_inactives = """
        CREATE TABLE IF NOT EXISTS inactives (
            user_id TEXT PRIMARY KEY,
            reason TEXT
        );
        CREATE TABLE IF NOT EXISTS role_system (
            user_id TEXT PRIMARY KEY
        );
    """
    async with pool.acquire() as conn:
        await conn.execute(query_inactives)


async def get_inactive_reason(user_id: int) -> str:
    query = "SELECT reason FROM inactives WHERE user_id = $1"
    async with pool.acquire() as conn:
        record = await conn.fetchrow(query, str(user_id))
        return record['reason'] if record else None

async def set_inactive(user_id: int, reason: str):
    query = """
        INSERT INTO inactives (user_id, reason)
        VALUES ($1, $2)
        ON CONFLICT (user_id)
        DO UPDATE SET reason = EXCLUDED.reason
    """
    async with pool.acquire() as conn:
        await conn.execute(query, str(user_id), reason)

async def remove_inactive(user_id: int):
    query = "DELETE FROM inactives WHERE user_id = $1"
    async with pool.acquire() as conn:
        await conn.execute(query, str(user_id))



async def get_role_system (user_id: int) -> bool:
    query = "SELECT EXISTS (SELECT 1 FROM role_system WHERE user_Id = $1)"
    async with pool.acquire() as connection:
        exists = await connection.fetchval(query, str(user_id))
        return exists

async def set_role_system(user_id: int):
    query = """
        INSERT INTO role_system (user_id)
        VALUES ($1)
        ON CONFLICT (user_id) DO NOTHING
    """
    async with pool.acquire() as conn:
        await conn.execute(query, str(user_id))

async def remove_role_system(user_id: int):
    query = "DELETE FROM role_system WHERE user_id = $1"
    async with pool.acquire() as conn:
        await conn.execute(query, str(user_id))