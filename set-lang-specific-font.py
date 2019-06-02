# In the name of Allah
"""
module for Set up a language-specific font
License: MIT
"""

import os

print("== In the name of Allah ==")
print("\tSet up a language-specific font")

lang_code = input("Enter the language code(example fa, ar, en, fr): ")

print("if use special language please use one language font format. example: Vazir WL")
font_name = input("Enter the font name: ")

font_folder = input("Enter the font folder address (installed? empty): ")
try:
	# Install ------------
	if font_folder:
		if not os.path.exists(font_folder):
			print("Not found font folder")
			exit()
		
		os.system("cp {} /usr/local/share/fonts/".format(font_folder))
	
	# Set ----------------
	font_local_config = """
	<?xml version='1.0'?>
	<!DOCTYPE fontconfig SYSTEM 'fonts.dtd'>
	<fontconfig>
	  <!-- Default font for the {lang_code} locale (no fc-match pattern) -->
	  <match>
	    <test compare="contains" name="lang">
	      <string>{lang_code}</string>
	    </test>
	    <edit mode="prepend" name="family">
	      <string>{font_name}</string>
	    </edit>
	  </match>
	  <alias>
	    <family>serif</family>
	      <prefer>
	       <family>{font_name}</family>
	      	<family>Noto Serif</family>
	      	<family>Heuristica</family>
		<family>Noto Color Emoji</family>
	      </prefer>
	  </alias>
	  <alias>
	    <family>sans-serif</family>
	      <prefer>
		<family>{font_name}</family>
		<family>Noto Sans</family>
		<family>Droid Sans</family>
		<family>Noto Color Emoji</family>
	      </prefer>
	  </alias>
	  <alias>
	    <family>monospace</family>
	      <prefer>
	       <family>{font_name}</family>
		<family>Hack</family>
		<family>Noto Sans Mono</family>
		<family>Liberation Mono</family>
		<family>Droid Sans Mono</family>
		<family>DejaVu Sans Mono</family>
		<family>Noto Color Emoji</family>
	      </prefer>
	  </alias>
	</fontconfig>
	""".format(font_name=font_name, lang_code=lang_code)
	
	if not os.path.exists('/etc/fonts/'):
		os.system('mkdir /etc/fonts')
	if os.path.exists('/etc/fonts/local.conf'):
		os.system("cp /etc/fonts/local.conf /etc/fonts/local.conf.backup")
	font_local_config_file = open('/etc/fonts/local.conf', 'w')
	font_local_config_file.write(font_local_config)

	print("---"*20)
	print("Done")
	print("---"*20)

except IOError as e:
	if type(e) == PermissionError:
		print("---"*20)
		print("You need root permissions to do this. please use sudo or su")
		print("---"*20)
	exit()