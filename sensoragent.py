import asyncio
from datetime import datetime
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from environment import DisasterEnvironment

env = DisasterEnvironment()

class SenseEnvironmentBehaviour(CyclicBehaviour):
    async def run(self):
        level, description = env.get_disaster_status()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_message = f"[{timestamp}] Disaster Status Detected: {description} (Level {level})"
        print(log_message)

        # Save to log file
        with open("event_log.txt", "a") as f:
            f.write(log_message + "\n")

        await asyncio.sleep(5)  # Sense every 5 seconds

class SensorAgent(Agent):
    async def setup(self):
        print("SensorAgent started. Monitoring environment...")
        self.add_behaviour(SenseEnvironmentBehaviour())

if __name__ == "__main__":
    agent = SensorAgent("agent1@localhost", "password123")
    agent.start().result()

    try:
        while agent.is_alive():
            asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Stopping SensorAgent...")
        agent.stop()
