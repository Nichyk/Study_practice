# TV controller
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one,
# turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
# if the channel N or 'name' exists in the list, or "No" - in the other case.
# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.

class TVController:

    def __init__(self, channels) -> None:
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self) -> str:
        self.current_channel_index = 0
        return self.channels[self.current_channel_index]

    def last_channel(self) -> str:
        self.current_channel_index = len(self.channels) - 1
        return self.channels[self.current_channel_index]

    def turn_channel(self, n) -> str:
        self.current_channel_index = n - 1
        try:
            return self.channels[self.current_channel_index]
        except IndexError:
            print('No such channel')

    def next_channel(self) -> str:
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def previous_channel(self) -> str:
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def current_channel(self) -> str:
        return self.channels[self.current_channel_index]

    def is_exist(self, channel) -> str:
        if type(channel) == str:
            return "Yes" if channel in self.channels else "No"
        elif type(channel) == int:
            return 'Yes' if 1 <= channel <= len(self.channels) else 'No'


CHANNELS = ['BBC', 'Discovery', 'TV1000']
controller = TVController(CHANNELS)
print(controller.first_channel(), controller.last_channel(), controller.turn_channel(5), controller.next_channel(),
      controller.previous_channel(), controller.is_exist(7))
