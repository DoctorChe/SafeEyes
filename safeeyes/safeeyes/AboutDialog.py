# Safe Eyes is a utility to remind you to take break frequently
# to protect your eyes from eye strain.

# Copyright (C) 2016  Gobinath

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkX11

class AboutDialog:
	def __init__(self, glade_file, version):
		builder = Gtk.Builder()
		builder.add_from_file(glade_file)
		builder.connect_signals(self)
		self.window = builder.get_object("window_about")
		builder.get_object("lbl_app_name").set_label("Safe Eyes " + version)

	def show(self):
		self.window.show_all()

	def on_window_delete(self, *args):
		self.window.destroy()

	def on_close_clicked(self, button):
		self.window.destroy()
