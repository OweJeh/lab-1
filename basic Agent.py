import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

class HelloBehaviour(CyclicBehaviour):
    async def run(self):
        print("Hello! I am an active SPADE agent.")
        await asyncio.sleep(5)

class BasicAgent(Agent):
    async def setup(self):
        print("Agent starting...")
        self.add_behaviour(HelloBehaviour())

if __name__ == "__main__":
    agent = BasicAgent("agent1@localhost", "password123")
    future = agent.start()
    future.result()

    try:
        while agent.is_alive():
            asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Stopping agent...")
        agent.stop()

