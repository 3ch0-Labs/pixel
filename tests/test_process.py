import asyncio

from livekit.agents import ipc
from livekit.protocol import agent


def fake_usercb():
    pass


async def test_job_process():
    fake_job = agent.Job()
    fake_job.id = "fake_job_id"

    proc = ipc.JobProcess(fake_job, "fake_url", "fake_token", fake_usercb)
    proc.start()

    await asyncio.sleep(10)
    await proc.aclose()
