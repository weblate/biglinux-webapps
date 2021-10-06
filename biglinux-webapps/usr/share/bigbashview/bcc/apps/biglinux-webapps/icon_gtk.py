import gi, sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Icon(Gtk.IconTheme):
    """docstring for Icon."""
    def __init__(self, icon_name):
        super(Icon, self).__init__()
        icon_theme = self.get_default()

        icon_info = icon_theme.lookup_icon(icon_name, 48, 0)
        print(icon_info.get_filename())

if __name__ == "__main__":
    Icon(sys.argv[1])
