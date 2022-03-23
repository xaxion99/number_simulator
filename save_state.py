# Import Python Libraries
from json import *


class SaveState:

    def save(self, clk, cntr, mod):
        # Collect data to save and create JSON object
        data = {
            'clocks': [{
                'start_date': clk.start_date,
                'start_time': clk.start_time,
                'start_time_str': clk.start_time_str,
                'current_date': clk.current_date,
                'current_time': clk.current_time,
                'time_since_start': clk.time_since_start
            }],
            'counters': [{
                'current_count': cntr.current_count
            }],
            'modifiers': [{
                'click_mod': mod.click_mod,
                'tick_mod': mod.tick_mod
            }]
        }

        json_string = dumps(data)
        print(json_string)

        # Write to save.json file the above data
        with open('save.json', 'w') as outfile:
            outfile.write(json_string)

        print("Saved")

    def load(self, clk, cntr, mod):
        # Load data from save.json
        with open('save.json') as json_file:
            data = load(json_file)

        # Set relevant save parameters
        # Clock Parameters
        clk.set_start_date(data['clocks'][0]['start_date'])
        clk.set_start_time(data['clocks'][0]['start_time'])
        clk.set_start_time_str(data['clocks'][0]['start_time_str'])
        # Counter Parameters
        cntr.set_current_count(data['counters'][0]['current_count'])
        # Modifiers Parameters
        mod.set_click_mod(data['modifiers'][0]['click_mod'])
        mod.set_tick_mod(data['modifiers'][0]['tick_mod'])

        print("Loaded")
