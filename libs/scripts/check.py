from datetime import datetime
from pyotrs import Client
from pyotrs.lib import TICKET_CONNECTOR_CONFIG_DEFAULT

def check():
    TICKET_CONNECTOR_CONFIG = TICKET_CONNECTOR_CONFIG_DEFAULT
    TICKET_CONNECTOR_CONFIG['Config']['TicketSearch']['RequestMethod'] = 'POST'
    TICKET_CONNECTOR_CONFIG['Config']['TicketSearch']['Route'] = '/TicketSearch'

    client = Client("http://192.168.0.15", "aleksandrakiseleva", "wXHsjt0tdpmzNcgo",
                    webservice_config_ticket=TICKET_CONNECTOR_CONFIG)
    client.session_create()

    f = open('C:/Users/aleks/Desktop/dip/input/Tickets.txt')
    lines = f.readlines()
    f.close()

    t = f'{datetime.now():%Y%m%d%H%M%S}'
    with open(f"C:/Users/aleks/Desktop/dip/system_logs/State_tickets_{t}.txt", 'a') as f:
        for line in lines:
            ticket = client.ticket_get_by_id(line)
            state = line.strip() + ': ' + ticket.field_get("State") + '\n'
            f.write(state)

    print("Состояния успешно записаны.\n")