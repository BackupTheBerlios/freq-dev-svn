def show_option(t, s, p):
 s.msg(t, s.room.get_option(p, '[unset]'))

bot.register_cmd_handler(show_option, '.show_option', 9, g=1)
