kv = """
#:import NoTransition kivy.uix.screenmanager.NoTransition

MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    ScreenManager:
        id: scr
        transition: NoTransition()

        MDScreen:
            name: "Loginscr"

            FitImage:
                source:"gradient.png"

            MDBoxLayout:
                orientation: 'vertical'
                MDGridLayout:
                    cols: 1
                    padding: 30, 60, 30, 80
                    spacing: 10
                    pos_hint: {"center_x": .5, "center_y": .5}
                    MDCard:
                        #size_hint
                        #size: "360dp", "180dp"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        radius: [20,]
                        elevation: 2
                        opacity: 1
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: 10, 100, 10, 100
                            spacing: 10

                            Image: 
                                source: 'HackathonLogo.png'
                                #opacity : 1
                                pos_hint: {"center_x": .5, "center_y": 8}
                                size_hint: .8, .8

                            MDTextField:
                                hint_text: "Enter username "
                                helper_text: 'Hint: codeyy, codeaj'
                                helper_text_mode: "on_focus"
                                icon_right_color: app.theme_cls.primary_color
                                pos_hint: {'center_x': 0.5, 'center_y': 1}
                                size_hint_x: None
                                width: 220

                            MDTextField:
                                hint_text: "Password"
                                icon_right: "eye-off"
                                password: True
                                icon_right_color: app.theme_cls.primary_color
                                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
                                required: True
                                size_hint_x: None
                                width: 220

                            MDRoundFlatButton:
                                text: "Enter"
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                on_release:   
                                    scr.current = "Matchscr"

        MDScreen:
            name: "Matchscr"
            MDBoxLayout:
                orientation: 'vertical'
                spacing: 10
                padding: 10, 10, 10, 300
                MDLabel:
                    text: "Match screen"
                    pos_hint: {"center_y": .5}
                    halign: "center"
    
                MDRoundFlatButton:
                    text: "Test like"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: 
                        



        MDScreen:
            name: "Connectionscr"
            MDLabel:
                text: "Connectionscr"
                pos_hint: {"center_y": .5}
                halign: "center"
        MDScreen:
            name: "Profilescr"
            MDLabel:
                text: "Profilescr"
                pos_hint: {"center_y": .5}
                halign: "center"
                
    NavBar:
        id: navbar
        size_hint: .85, .1
        pos_hint: {"center_x": .5, "center_y": .1}
        elevation: 2
        md_bg_color: 1, 1, 1, 1
        radius: {16}
        disabled: scr.current == "Loginscr"  # Disable the NavBar when screens that don't need it active
        opacity: int(scr.current != "Loginscr")
        MDGridLayout:
            cols: 3
            size_hint_x: .9
            spacing: 20
            pos_hint: {"center_x": .6, "center_y": .4}
            MDIconButton: 
                id: nav_icon1
                icon: "account-search"
                ripple_scale: 0
                user_font_size: "30sp"
                theme_text_color: "Custom"
                text_color: 1, 0, 0, 1
                on_release: 
                    scr.current = "Matchscr"
                    app.change_color(self)
            MDIconButton: 
                id: nav_icon2
                icon: "heart"
                ripple_scale: 0
                user_font_size: "30sp"
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1
                on_release: 
                    scr.current = "Connectionscr"
                    app.change_color(self)
            MDIconButton: 
                id: nav_icon3
                icon: "account"
                ripple_scale: 0
                user_font_size: "30sp"
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1
                on_release: 
                    scr.current = "Profilescr"
                    app.change_color(self)
"""
