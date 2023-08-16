import asyncio
import httpx
import json
from app.logs import logging


class Checker:
    URL = "https://qr-mint.g7p.io/api/checkWhitelist?wallet="

    @staticmethod
    async def check(wallet):
        try:
            async with httpx.AsyncClient(timeout=15) as client:
                response = await client.get(f"{Checker.URL}{wallet}")

            if response.status_code == 200 and json.loads(response.text)['success'] is True:
                logging.info(f"{wallet}: {json.loads(response.text)}")
                return "✅"
            elif response.status_code == 400:
                logging.info(f"{wallet}: {json.loads(response.text)}")
                return "❌"
            else:
                logging.info(f"{wallet}: {json.loads(response.text)}")
                return "Something went wrong while getting info"

        except httpx.ConnectTimeout:
            logging.info("Connection timed out")
            return "Connection timed out"
        except httpx.RequestError as error:
            return f"An error occurred: {error}"
