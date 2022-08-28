# conding: utf-8
from remo import NatureRemoAPI
api = NatureRemoAPI('pass code')

appliance = api.get_appliances()[1]

api.send_light_infrared_signal(appliance.id,appliance.light.buttons[0].name)
