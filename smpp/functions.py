import asyncio
import naz
import smpplib

client = smpplib.client.Client('smscsim.melroselabs.com', 2775)
client.bind_transceiver()

naz.broker.SimpleBroker

loop = asyncio.get_event_loop()
broker = naz.broker.SimpleBroker(maxsize=1000)
cli = naz.Client(
    smsc_host="10.203.10.74",
    smsc_port=2556,
    system_id="SQM",
    password="PASQM^$!",
    broker=broker,
)

# queue messages to send
for i in range(0, 4):
    print("submit_sm round:", i)

    msg = naz.protocol.SubmitSM(
            short_message="Hello World-{0}".format(str(i)),
            log_id="myid12345",
            source_addr="988938004",
            destination_addr="09128387233",
        )
    loop.run_until_complete(
       cli.send_message(msg)
)

try:
    # 1. connect to the SMSC host
    # 2. bind to the SMSC host
    # 3. send any queued messages to SMSC
    # 4. read any data from SMSC
    # 5. continually check the state of the SMSC
    tasks = asyncio.gather(
        cli.connect(),
        cli.tranceiver_bind(),
        cli.dequeue_messages(),
        cli.receive_data(),
        cli.enquire_link(),
    )
    loop.run_until_complete(tasks)
except Exception as e:
    print("exception occured. error={0}".format(str(e)))
finally:
    loop.run_until_complete(cli.unbind())
    loop.stop()