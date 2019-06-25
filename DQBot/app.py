from .server import DataStore, RenderServer
from os import getenv

import asyncio
import tortoise
from tortoise import Tortoise

class App:
	async def run(self):
		# database init
		await self.db_start()

		# rendering
		self.store = DataStore()
		self.server = RenderServer(self.store)

		await self.server.setup()
		
		# TODO: Discord.py setup

		# For testing rendering quickly
		# from .models import Player, ActiveWorld, PlayerEntity
		# player = Player(discord_id="99999999")
		# await player.save()
		# player_entity = PlayerEntity(x=5, y=5)
		# await player_entity.save()
		# activeworld = ActiveWorld(world_name="test", player=player, player_entity=player_entity)
		# await activeworld.save()

		## or:
		## activeworld = await ActiveWorld.first()
		
		# print(server.add_to_queue(activeworld))

		# keep everything alive by sleeping forever
		while True:
			await asyncio.sleep(3600)

	async def db_start(self):
	    await Tortoise.init(
	        db_url=getenv('DB_URL'), # TODO
	        modules={'models': ['DQBot.models']}
	    )

	    await Tortoise.generate_schemas()

	async def teardown(self):
		print("Tearing down app")

		await Tortoise.close_connections()
		await self.server.teardown()