from flet import *

def main(page:Page):

	# AND NOW CUSTOMIZE COLOR TABS
	page.theme = Theme(
	tabs_theme = TabsTheme(
		# Change Track line 
		divider_color="blue",

		# AND CHANGE SCROLLBAR COLOR
		indicator_color="red",

		# AND CHANGE SIZE FULL OR NOT YOU SCROLLBAR
		indicator_tab_size=True,

		# AND CHANGE LABEL ACTIVE COLOR
		label_color="red",

		indicator_border_radius=80,

		# AND CHANGE COLOR FOR YOU UNSELECT TAB OR NOT ACTIVE
		unselected_label_color="blue",

		# AND IF YOU HOVER THE TAB YOU CAN CHANGE COLOR HOVER
		overlay_color={
		# NOW IF CURSOR ACTIVE TO HOVER TAB
		MaterialState.FOCUSED:colors.with_opacity(0.3,colors.GREEN),

		# NOW FOR DEFAULT . YOU NOT HOVER THE TAB
		MaterialState.DEFAULT:colors.with_opacity(0.3,colors.PINK),
		

		}



		)
		)


	mytab = Tabs(
		selected_index=1,
		animation_duration=300,
		tabs=[
			Tab(
				tab_content=Icon(name="home"),
				content=Container(
					content=Text("my home",size=20)
					)
				),
			Tab(
				tab_content=Icon(name="settings"),
				content=Container(
					content=Text("my second page",size=20)
					)
				),
			Tab(
				tab_content=Icon(name="thumb_up"),
				content=Container(
					content=Text("my three page",size=20)
					)
				),
		],
		expand=1
		)

	page.add(
	Column([
	Text("Tabs Customize",size=30,weight="bold"),
	mytab 
		])
		)

flet.app(target=main)
