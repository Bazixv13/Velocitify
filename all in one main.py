import os
import firston
import config
import time
import tkinter.messagebox as messagebox

if config.manual_typing_animation_speed is True:
    tyn = f"(1 letter per {config.typing_animation_speed} second)"
else:
    tyn = " "
os.system(
    f"title hakier prompt ｜ running with config: loading bars = {config.loading_bars}, typing animations = {config.typing_animation} {tyn}".center(
        130))


def pip():
    print(
        "INFO:Check if u have pip added to path by typing pip in command prompt, Get more info in readme.txt")
    os.system("timeout 30")
    print("please wait....")
    os.system("pip install tqdm")
    os.system("pip install discord.py==1.7.3")
    os.system("pip install keyboard")
    os.system("cls")


try:
    if firston.on is True:
        print(
            "INFO:Everything seems to be downaled skipping... if something is not downalded change on to False in fiston.py ")
        time.sleep(3)
    elif firston.on is False:
        pip()
        f = open("firston.py", "w")
        f.write("on = True")
        f.close()
except:
    print("INFO:Looks like we weren't able to find firston.py file, skipping...")

from sys import stdout
from tqdm import tqdm
import random
from colorama import Fore, Style
import keyboard


def wanimation(text, s=None, t=random.uniform(.04, .05)):
    for i in text:
        stdout.write(i)
        stdout.flush()
        if config.typing_animation is False:
            t = 0
        if config.manual_typing_animation_speed is True and config.typing_animation is True:
            if config.typing_animation_speed > 0:
                t = config.typing_animation_speed
        time.sleep(t)
    if s:
        print("")


def p1():
    print("                         .cccc;;cc;';c.")
    print("                      .,:dkdc:;;:c:,:d:.")
    print("                     .loc'.,cc::c:::,..;:.")
    print("                   .cl;....;dkdccc::,...c;")
    print("                  .c:,';:'..ckc',;::;....;c.")
    print("                .c:'.,dkkoc:ok:;llllc,,c,';:.")
    print("               .;c,';okkkkkkkk:;lllll,:kd;.;:,.")
    print("               co..:kkkkkkkkkk:;llllc':kkc..oNc")
    print("             .cl;.,oxkkkkkkkkkc,:cll;,okkc'.cO;")
    print("             ;k:..ckkkkkkkkkkkl..,;,.;xkko:',l'")
    print("            .,...';dkkkkkkkkkkd;.....ckkkl'.cO;")
    print("         .,,:,.;oo:ckkkkkkkkkkkdoc;;cdkkkc..cd,")
    print("      .cclo;,ccdkkl;llccdkkkkkkkkkkkkkkkd,.c;")
    print("     .lol:;;okkkkkxooc::coodkkkkkkkkkkkko'.oc")
    print("   .c:'..lkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkd,.oc")
    print("  .lo;,:cdkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkd,.c;")
    print(",dx:..;lllllllllllllllllllllllllllllllllc'...")
    print("cNO;........................................")


def p2():
    print("                .ckx;'........':c.")
    print("             .,:c:::::oxxocoo::::,',.")
    print("            .odc'..:lkkoolllllo;..;d,")
    print("            ;c..:o:..;:..',;'.......;.")
    print("           ,c..:0Xx::o:.,cllc:,'::,.,c.")
    print("           ;c;lkXKXXXXl.;lllll;lKXOo;':c.")
    print("         ,dc.oXXXXXXXXl.,lllll;lXXXXx,c0:")
    print("         ;Oc.oXXXXXXXXo.':ll:;'oXXXXO;,l'")
    print("         'l;;kXXXXXXXXd'.'::'..dXXXXO;,l'")
    print("         'l;:0XXXXXXXX0x:...,:o0XXXXx,:x,")
    print("         'l;;kXXXXXXXXXKkol;oXXXXXXXO;oNc")
    print("        ,c'..ckk0XXXXXXXXXX00XXXXXXX0:;o:.")
    print("      .':;..:do::ooookXXXXXXXXXXXXXXXo..c;")
    print("    .',',:co0XX0kkkxxOXXXXXXXXXXXXXXXOc..;l.")
    print("  .:;'..oXXXXXXXXXXXXXXXXXXXXXXXXXXXXXko;';:.")
    print(".ldc..:oOXKXXXXXXKXXKXXXXXXXXXXXXXXXXXXXo..oc")
    print(":0o...:dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo,.:,")
    print("cNo........................................;'")


def p3():
    print("            .cc;.  ...  .;c.")
    print("         .,,cc:cc:lxxxl:ccc:;,.")
    print("        .lo;...lKKklllookl..cO;")
    print("      .cl;.,:'.okl;..''.;,..';:.")
    print("     .:o;;dkd,.ll..,cc::,..,'.;:,.")
    print("     co..lKKKkokl.':lloo;''ol..;dl.")
    print("   .,c;.,xKKKKKKo.':llll;.'oOxl,.cl,.")
    print("   cNo..lKKKKKKKo'';llll;;okKKKl..oNc")
    print("   cNo..lKKKKKKKko;':c:,'lKKKKKo'.oNc")
    print("   cNo..lKKKKKKKKKl.....'dKKKKKxc,l0")
    print("   .c:'.lKKKKKKKKKk;....lKKKKKKo'.oNc")
    print("     ,:.'oxOKKKKKKKOxxxxOKKKKKKxc,;ol:.")
    print("     ;c..'':oookKKKKKKKKKKKKKKKKKk:.'clc.")
    print("   ,xl'.,oxo;'';oxOKKKKKKKKKKKKKKKOxxl:::;,.")
    print("  .dOc..lKKKkoooookKKKKKKKKKKKKKKKKKKKxl,;ol.")
    print("  cx,';okKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKl..;lc.")
    print("  co..:dddddddddddddddddddddddddddddddddl::',::.")
    print("  co...........................................  ")


def p4():
    print("           .ccccccc.                              ")
    print("      .,,,;cooolccoo;;,,.                         ")
    print("     .dOx;..;lllll;..;xOd.                        ")
    print("   .cdo;',loOXXXXXkll;';odc.                      ")
    print("  ,ol:;c,':oko:cccccc,...ckl.                     ")
    print("  ;c.;kXo..::..;c::'.......oc                     ")
    print(",dc..oXX0kk0o.':lll;..cxxc.,ld,                   ")
    print("kNo.'oXXXXXXo',:lll;..oXXOo;cOd.                  ")
    print("KOc;oOXXXXXXo.':lol;..dXXXXl';xc                  ")
    print("Ol,:k0XXXXXX0c.,clc'.:0XXXXx,.oc                  ")
    print("KOc;dOXXXXXXXl..';'..lXXXXXo..oc                  ")
    print("dNo..oXXXXXXXOx:..'lxOXXXXXk,.:; ..               ")
    print("cNo..lXXXXXXXXXOolkXXXXXXXXXkl,..;:';.            ")
    print(".,;'.,dkkkkk0XXXXXXXXXXXXXXXXXOxxl;,;,;l:.        ")
    print("  ;c.;:''''':doOXXXXXXXXXXXXXXXXXXOdo;';clc.      ")
    print("  ;c.lOdood:'''oXXXXXXXXXXXXXXXXXXXXXk,..;ol.     ")
    print("  ';.:xxxxxocccoxxxxxxxxxxxxxxxxxxxxxxl::'.';;.   ")
    print("  ';........................................;l'   ")


def p5():
    print("        .;:;;,.,;;::,.")
    print("     .;':;........'co:.")
    print("   .clc;'':cllllc::,.':c.")
    print("  .lo;;o:coxdllllllc;''::,,.")
    print(".c:'.,cl,.'l:',,;;'......cO;")
    print("do;';oxoc;:l;;llllc'.';;'.,;.")
    print("c..ckkkkkkkd,;llllc'.:kkd;.':c.")
    print("'.,okkkkkkkkc;lllll,.:kkkdl,cO;")
    print("..;xkkkkkkkkc,ccll:,;okkkkk:,co,")
    print("..,dkkkkkkkkc..,;,'ckkkkkkkc;ll.")
    print("..'okkkkkkkko,....'okkkkkkkc,:c.")
    print("c..ckkkkkkkkkdl;,:okkkkkkkkd,.',';.")
    print("d..':lxkkkkkkkkxxkkkkkkkkkkkdoc;,;'..'.,.")
    print("o...'';llllldkkkkkkkkkkkkkkkkkkdll;..'cdo.")
    print("o..,l;'''''';dkkkkkkkkkkkkkkkkkkkkdlc,..;lc.")
    print("o..;lc;;;;;;,,;clllllllllllllllllllllc'..,:c.")
    print("o..........................................;'")


def p7():
    print("                   .ccccccc.                      ")
    print("               .ccckNKOOOOkdcc.                   ")
    print("            .;;cc:ccccccc:,:c::,,.                ")
    print("         .c;:;.,cccllxOOOxlllc,;ol.               ")
    print("        .lkc,coxo:;oOOxooooooo;..:,               ")
    print("      .cdc.,dOOOc..cOd,.',,;'....':l.             ")
    print("      cNx'.lOOOOxlldOc..;lll;.....cO;             ")
    print("     ,do;,:dOOOOOOOOOl'':lll;..:d:''c,            ")
    print("     co..lOOOOOOOOOOOl'':lll;.'lOd,.cd.           ")
    print("     co.'dOOOOOOOOOOOo,.;llc,.,dOOc..dc           ")
    print("     co..lOOOOOOOOOOOOc.';:,..cOOOl..oc           ")
    print("   .,:;.'::lxOOOOOOOOOo:'...,:oOOOc.'dc           ")
    print("   ;Oc..cl'':lldOOOOOOOOdcclxOOOOx,.cd.           ")
    print("  .:;';lxl''''':lldOOOOOOOOOOOOOOc..oc            ")
    print(",dl,.'cooc:::,....,::coooooooooooc'.c:            ")
    print("cNo.................................oc            ")


def p8():
    print("                        .cccccccc.                ")
    print("                  .,,,;;cc:cccccc:;;,.            ")
    print("                .cdxo;..,::cccc::,..;l.           ")
    print("               ,do:,,:c:coxxdllll:;,';:,.         ")
    print("             .cl;.,oxxc'.,cc,.';;;'...oNc         ")
    print("             ;Oc..cxxxc'.,c;..;lll;...cO;         ")
    print("           .;;',:ldxxxdoldxc..;lll:'...'c,        ")
    print("           ;c..cxxxxkxxkxxxc'.;lll:'','.cdc.      ")
    print("         .c;.;odxxxxxxxxxxxd;.,cll;.,l:.'dNc      ")
    print("        .:,''ccoxkxxkxxxxxxx:..,:;'.:xc..oNc      ")
    print("      .lc,.'lc':dxxxkxxxxxxxol,...',lx:..dNc      ")
    print("     .:,',coxoc;;ccccoxxxxxxxxo:::oxxo,.cdc.      ")
    print("  .;':;.'oxxxxxc''''';cccoxxxxxxxxxxxc..oc        ")
    print(",do:'..,:llllll:;;;;;;,..,;:lllllllll;..oc        ")
    print("cNo.....................................oc        ")


def p9():
    print("                              .ccccc.             ")
    print("                         .cc;'coooxkl;.           ")
    print("                     .:c:::c:,,,,,;c;;,.'.        ")
    print("                   .clc,',:,..:xxocc;'..c;        ")
    print("                  .c:,';:ox:..:c,,,,,,...cd,      ")
    print("                .c:'.,oxxxxl::l:.,loll;..;ol.     ")
    print("                ;Oc..:xxxxxxxxx:.,llll,....oc     ")
    print("             .,;,',:loxxxxxxxxx:.,llll;.,,.'ld,   ")
    print("            .lo;..:xxxxxxxxxxxx:.'cllc,.:l:'cO;   ")
    print("           .:;...'cxxxxxxxxxxxxoc;,::,..cdl;;l'   ")
    print("         .cl;':,'';oxxxxxxdxxxxxx:....,cooc,cO;   ")
    print("     .,,,::;,lxoc:,,:lxxxxxxxxxxxo:,,;lxxl;'oNc   ")
    print("   .cdxo;':lxxxxxxc'';cccccoxxxxxxxxxxxxo,.;lc.   ")
    print("  .loc'.'lxxxxxxxxocc;''''';ccoxxxxxxxxx:..oc     ")
    print("olc,..',:cccccccccccc:;;;;;;;;:ccccccccc,.'c,     ")
    print("Ol;......................................;l'      ")


def p10():
    print(" ,ddoodd, ")
    print(" .cc' ,ooccoo,'cc. ")
    print(" .ccldo;...',,...;oxdc. ")
    print(" .,,:cc;.,'..;lol;;,'..lkl. ")
    print(" .dOc';:ccl;..;dl,.''.....oc ")
    print(" .,lc',cdddddlccld;.,;c::'..,cc:. ")
    print(" cNo..:ddddddddddd;':clll;,c,';xc ")
    print(" .lo;,clddddddddddd;':clll;:kc..;' ")
    print(" .,c;..:ddddddddddddd:';clll,;ll,.. ")
    print(" ;Oc..';:ldddddddddddl,.,c:;';dd;.. ")
    print(" .''',:c:,'cdddddddddddo:,''..'cdd;.. ")
    print(" .cdc';lddd:';lddddddddddddd;.';lddl,.. ")
    print(" .,;::;,cdddddol;;lllllodddddddlcldddd:.'l; ")
    print(" .dOc..,lddddddddlcc:;'';cclddddddddddd;;ll. ")
    print(" .coc,;::ldddddddddddddlcccc:ldddddddddl:,cO; ")
    print(",xl::,..,cccccccccccccccccccccccccccccccc:;':xx, ")
    print("cNd.........................................;lOc")


def configurator():
    import os
    import sys
    import tkinter as tk
    from tkinter import ttk
    import tkinter.messagebox as messagebox
    import time
    import webbrowser

    current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

    # Construct the path to the config.py file
    config_file = os.path.join(current_dir, "config.py")

    # Import the config module
    sys.path.insert(0, current_dir)

    import config

    # Determine the path to the executable (needed for PyInstaller)
    if hasattr(sys, '_MEIPASS'):
        # Running as PyInstaller executable
        base_dir = sys._MEIPASS
    else:
        # Running as normal Python script
        base_dir = os.path.abspath(os.path.dirname(__file__))

    root = tk.Tk()
    root.geometry("490x290")
    root.resizable(False, False)
    root.title("Script Settings")
    root.iconbitmap(os.path.join(base_dir, "configs.ico"))
    root.wm_iconbitmap(os.path.join(base_dir, "configs.ico"))

    typing_animation = tk.BooleanVar(value=config.typing_animation)
    loading_bars = tk.BooleanVar(value=config.loading_bars)
    manual_typing_animation_speed = tk.BooleanVar(value=config.manual_typing_animation_speed)
    typing_animation_speed = tk.DoubleVar(value=config.typing_animation_speed)
    bot_token = tk.StringVar(value=config.bot_token)

    def save_values():
        config.typing_animation = typing_animation.get()
        config.loading_bars = loading_bars.get()
        config.manual_typing_animation_speed = manual_typing_animation_speed.get()
        config.typing_animation_speed = typing_animation_speed.get()
        config.bot_token = bot_token.get()
        config.save_config()

        def fixcofig():
            time.sleep(0.1)
            ta = config.typing_animation
            lb = config.loading_bars
            mtas = config.manual_typing_animation_speed
            tas = config.typing_animation_speed
            bt = config.bot_token
            with open('config.py', 'w') as f:
                f.write(f"typing_animation = {ta}\n")
                f.write(f"loading_bars = {lb}\n")
                f.write(f"manual_typing_animation_speed = {mtas}\n")
                f.write(f"typing_animation_speed = {tas}\n")
                f.write(f"bot_token = '{bt}'\n")
                f.write("def save_config():\n")
                f.write("    import os\n")
                f.write("""    with open('config.py', 'w') as f:\n""")
                f.write("""        f.write(f"typing_animation = {typing_animation}\\n")\n""")
                f.write("""        f.write(f"loading_bars = {loading_bars}\\n")\n""")
                f.write("""        f.write(f"manual_typing_animation_speed = {manual_typing_animation_speed}\\n")\n""")
                f.write("""        f.write(f"typing_animation_speed = {typing_animation_speed}\\n")\n""")
                f.write("""        f.write(f"bot_token = '{bot_token}'\\n")\n""")

        fixcofig()
        messagebox.showwarning("WARNING", "To make the changes take effect, restart the program.")
        dsf = messagebox.askyesno("Settings Saved", "Your settings have been saved successfully. Exit?")
        if dsf:
            root.destroy()
        else:
            pass

    def open_bing():
        webbrowser.open(
            "https://scribehow.com/embed-preview/Discord_Workflow__n3Jb3W73SVmpY49ZaBcxAA?size=small&skipIntro=true&removeLogo=true&as=default&preview=true")

    def show_tooltip():
        tooltip = tk.Toplevel(root)
        tooltip.wm_overrideredirect(True)
        x = root.winfo_pointerx()
        y = root.winfo_pointery()
        tooltip.geometry(f"+{x}+{y}")
        label = tk.Label(tooltip, text="Click for help", bg="white", relief="solid", borderwidth=1)
        label.pack()
        label.after(1500, tooltip.destroy)

    def show_tooltip2():
        tooltip2 = tk.Toplevel(root)
        tooltip2.wm_overrideredirect(True)
        x = root.winfo_pointerx()
        y = root.winfo_pointery()
        tooltip2.geometry(f"+{x}+{y}")
        label = tk.Label(tooltip2,
                         text="The amount of time it takes to type one letter (will only take effect \nif you have enabled manual typing animation speed above).",
                         bg="white", relief="solid", borderwidth=1)
        label.pack()
        label.after(1500, tooltip2.destroy)

    def fsd():
        messagebox.showinfo("INFO",
                            "The amount of time it takes to type one letter (will only take effect if you have enabled manual typing animation speed above).")

    def cancel():
        result = messagebox.askyesno("Warning",
                                     "If you haven't saved your changes, all of them will be lost.\nDo you want to Continue?")
        if result == True:
            root.destroy()
        else:
            pass

    root.protocol("WM_DELETE_WINDOW", cancel)

    ttk.Label(root, text="      Script Settings", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2,
                                                                               pady=(20, 10))
    ttk.Label(root, text="Typing animation:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=20, pady=5)
    ttk.Checkbutton(root, variable=typing_animation, onvalue=True, offvalue=False, cursor="hand2").grid(row=1, column=1,
                                                                                                        sticky="e",
                                                                                                        pady=5)
    ttk.Label(root, text="Loading bars:", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", padx=20, pady=5)
    ttk.Checkbutton(root, variable=loading_bars, onvalue=True, offvalue=False, cursor="hand2").grid(row=2, column=1,
                                                                                                    sticky="e", pady=5)
    ttk.Label(root, text="Manual typing animation speed:", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w",
                                                                                        padx=20, pady=5)
    ttk.Checkbutton(root, variable=manual_typing_animation_speed, onvalue=True, offvalue=False, cursor="hand2").grid(
        row=3, column=1, sticky="e", pady=5)
    ttk.Label(root, text="Manual typing animation speed:", font=("Helvetica", 12)).grid(row=4, column=0, sticky="w",
                                                                                        padx=20, pady=5)
    ttk.Entry(root, textvariable=typing_animation_speed, font=("Helvetica", 12), width=10).grid(row=4, column=1,
                                                                                                sticky="e", pady=5)
    question2_button = ttk.Button(root, text='?', command=fsd, width=2, padding=2)
    question2_button.grid(row=4, column=2, pady=(0), padx=(10, 0))
    question2_button.bind("<Enter>", lambda e: show_tooltip2())
    ttk.Label(root, text="Bot token:", font=("Helvetica", 12)).grid(row=5, column=0, sticky="w", padx=20, pady=5)
    ttk.Entry(root, textvariable=bot_token, font=("Helvetica", 12)).grid(row=5, column=1, pady=5)
    question_button = ttk.Button(root, text='?', command=open_bing, width=2, padding=2)
    question_button.grid(row=5, column=2, pady=(0), padx=(10, 0))
    question_button.bind("<Enter>", lambda e: show_tooltip())
    ttk.Button(root, text="Cancel", command=cancel).grid(row=6, column=0, pady=(20, 10), padx=(20, 5), sticky="w")
    ttk.Button(root, text="Save", command=save_values).grid(row=6, column=1, pady=(20, 10), padx=(5, 20), sticky="e")

    root.update_idletasks()
    root.geometry(
        f"+{(root.winfo_screenwidth() - root.winfo_width()) // 2}+{(root.winfo_screenheight() - root.winfo_height()) // 2}")
    root.deiconify()

    root.mainloop()


os.system("cls")
print(Style.BRIGHT)
os.system(
    f"title hakier prompt ｜ running with config: loading bars = {config.loading_bars}, typing animations = {config.typing_animation} {tyn}".center(
        130))
print(Fore.LIGHTGREEN_EX)
print("")
wanimation("Welcome Dear hecker", True)
if config.loading_bars is True:
    for i in tqdm(range(0, 100), desc="Loading avaible options", ascii=" ----------", unit="1 %", ncols=84):
        time.sleep(random.uniform(.001, .01))
    time.sleep(random.randint(1, 3))
os.system("cls")
os.system(f"title hakier prompt ｜ main menu ｜ press [S] for options")
if config.loading_bars is True:
    wanimation("1.destroy the world", True)
    wanimation(f"2.hack user on discord [BETA, probably working]", True)
    wanimation("3.do not select me", True)
    wanimation("4.check for updates [BETA]", True)
    wanimation("5.wipe temp files [BETA]", True)
    wanimation("6.calculator", True)
    # noinspection PyTrailingSemicolon
    wanimation("7.speedtest", True)
    wanimation("chose option: ");
if config.loading_bars is False:
    wanimation("1.destroy the world [unavaible with current config]", True)
    wanimation(f"2.hack user on discord [BETA, probably working]", True)
    wanimation("3.do select click me", True)
    wanimation("4.check for updates [BETA]", True)
    wanimation("5.wipe temp files [BETA]", True)
    wanimation("6.calculator", True)
    # noinspection PyTrailingSemicolon
    wanimation("7.speedtest", True)
    wanimation("chose option: ");
while True:
    key = keyboard.read_event()
    if key.name == "s":
        configurator()
        keyboard.press_and_release('backspace')
    else:
        os.system(f"title hakier prompt ｜ main menu")
        break
tudu = input()
if tudu == "1":
    os.system(f'title hakier prompt ｜ destroy the world ')

    # noinspection PyTrailingSemicolon
    wanimation("are you sure? (y/n) ");
    ays = input(":")
    if ays == "y" and config.loading_bars:
        for i in tqdm(range(0, 100), desc="Destroying world", ascii=" ----------", unit="1 %", ncols=84):
            time.sleep(random.uniform(21, 37))
        time.sleep(5)
        os.system("cls")
        wanimation("┏┓┏┓┏┳━━━┳━━━┳┓╋╋┏━━━┓  ┏━━━┳━━━┳━━━┳━━━━┳━━━┳━━━┳━━━┳━━━┓", True)
        wanimation('┃┃┃┃┃┃┏━┓┃┏━┓┃┃╋╋┗┓┏┓┃  ┗┓┏┓┃┏━━┫┏━┓┃┏┓┏┓┃┏━┓┃┏━┓┃┏━━┻┓┏┓┃', True)
        wanimation('┃┃┃┃┃┃┃╋┃┃┗━┛┃┃╋╋╋┃┃┃┃  ╋┃┃┃┃┗━━┫┗━━╋┛┃┃┗┫┗━┛┃┃╋┃┃┗━━┓┃┃┃┃', True)
        wanimation('┃┗┛┗┛┃┃╋┃┃┏┓┏┫┃╋┏┓┃┃┃┃  ╋┃┃┃┃┏━━┻━━┓┃╋┃┃╋┃┏┓┏┫┃╋┃┃┏━━┛┃┃┃┃', True)
        wanimation('┗┓┏┓┏┫┗━┛┃┃┃┗┫┗━┛┣┛┗┛┃  ┏┛┗┛┃┗━━┫┗━┛┃ ┃┃ ┃┃┃┗┫┗━┛┃┗━━┳┛┗┛┃', True)
        wanimation('╋┗┛┗┛┗━━━┻┛┗━┻━━━┻━━━┛  ┗━━━┻━━━┻━━━┛ ┗┛ ┗┛┗━┻━━━┻━━━┻━━━┛', True)
        print("")
        os.system("pause")
        wanimation("colosing in 1 miute", True)
        os.system("timeout 60")
    elif ays != "y" or config.loading_bars is False:
        if config.loading_bars is False:
            print(Fore.RED)
            wanimation("function unavailable with current config", True)
            wanimation("closing")
            wanimation("...", True, random.uniform(2, 4))
            os.system("exit")
        else:
            os.system("cls")
            wanimation("closing in 3")
            time.sleep(1)
            os.system("cls")
            print("closing in 2")
            time.sleep(1)
            os.system("cls")
            print("closing in 1")
            time.sleep(1)
            os.system("cls")
            exit()

if tudu == "2":
    os.system(f'title hakier prompt ｜ hacking user ')

    messagebox.showinfo("WARNING",
                        "This function may not work properly, If user nickname have unusual characters program will not display them.")
    # noinspection PyTrailingSemicolon

    a = 1
    while a == 1:
        user_id = input("Enter user id: ")
        with open("data.py", "w") as f:
            f.write(f"id = {user_id}\n")
        print("User id saved.")
        import os
        import random
        import time

        import discord
        from colorama import Fore, Style
        from discord import activity
        from discord.ext import commands
        from tqdm import tqdm

        import config
        import data

        print(" ")

        intents = discord.Intents.all()
        bot = commands.Bot(command_prefix=commands.when_mentioned_or('^'), help_command=None, intents=intents)
        activity = activity


        def wanimation(text, s=None, t=random.uniform(.01, .05)):
            for char in text:
                time.sleep(t)
                print(char, end='')
            if s:
                print("")


        @bot.event
        async def on_ready():
            await bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.listening, name="Searching for some things...",
                                          status=discord.Status.idle))
            user = None
            f = open("data.py", "r")
            user_id = data.id
            f.close()

            print(Fore.LIGHTGREEN_EX)
            wanimation("fetching user nickname and hashtag", None, 0)
            wanimation("...", True, 1)
            user = await bot.fetch_user(int(user_id))
            f = open("data2.py", "wb")
            f.write(f"username = '{user}'".encode("utf-8"))
            f.close()
            await bot.close()


        bot.run(config.bot_token)


        def restofall():
            import keyboard
            import data2
            from sys import stdout

            print(Style.BRIGHT)
            os.system("title hakier prompt".center(130))
            print(Fore.LIGHTGREEN_EX)
            dusername = 0

            def wanimation(text, s=None, t=random.uniform(.05, .1)):
                for i in text:
                    stdout.write(i)
                    stdout.flush()
                    time.sleep(t)
                if s:
                    print("")

            words_pass = "emy", "priority", "hypnothize", "drink", "chase", "fox", "reproduce", "express", "dimension", "site", "leader", "physical", "explode", "moving", "allowance", "bulletin", "challenge", "glory", "indulge", "observation", "oh", "classify", "deputy", "midnight", "camp", "crevice", "mention", "folklore", "biography", "flexible", "assignment", "bufet", "cave", "hemisphere", "order", "plastic", "bounce", "part", "quarter", "compartment", "strong", "judgment", "raid", "rice", "congress", "elaborate", "lounge", "basis", "bend", "smart", "have", "harsh", "freight", "devote", "lend", "conglomerate", "sin", "lick", "gown", "pyramid", "smoke", "peak", "offensive", "carpet", "crouch", "safe", "suit", "literacy", "lily", "key", "restrain", "pin", "earthflax", "pat", "council", "contact", "pilot", "feminist", "chew", "sail", "canvas", "lock", "frequency", "continuous", "incentive", "weed", "crack", "praise", "curriculum", "warning", "dramatic", "soak", "conventional", "man", "bank", "reality", "indirect", "element", "publish", "reflection", "cell", "negotiation", "currency", "drawing", "outcome", "proposal", "literature", "operation", "television", "statement", "series", "problem", "opportunity", "drawer", "worker", "selection", "baseball", "king", "buyer", "pizza", "transportation", "moment", "newspaper", "city", "mall", "user", "ear", "food", "meaning", "courage", "tennis", "patience", "wife", "girlfriend", "university", "writing", "sample", "judgment", "historian", "preference", "nation", "argument", "atmosphere", "computer", "promotion", "disaster", "collection", "woman", "thing", "honey", "aspect", "application", "method", "highway", "area", "feedback", "sector", "computer", "disease", "passenger", "emphasis", "administration", "bread", "conversation", "child", "presence", "population", "meal", "lake", "driver", "inspection", "assistant", "garbage", "football", "hat", "marketing", "county", "tension", "attention", "wood", "strategy", "transportation", "heart", "engineering", "history", "bath", "effort", "imagination", "people", "apartment", "bathroom", "piano", "safety", "politics", "music", "cheek", "construction", "language", "magazine", "union", "Tetsuo", "Mine", "Senri", "Teranishi", "Yoshiki", "Takeyama", "Yoshiko", "Nakayama", "Ichi", "Aikawa", "Miki", "Umemoto", "Anna", "Ozeki", "Tokuichi", "Yata", "Masanobu", "Tanaka", "Masashi", "Takanashi", "Koni", "Imanishi", "Miwako", "Yaguchi", "Yuki", "Sagawa", "Seigo", "Fujisaki", "Yasuji", "Hanai", "Kokuei", "Yamauchi", "Takaji", "Kamino", "Masaharu", "Kawamata", "Naka", "Moriya", "Tsune", "Itakura", "Kiichiro", "Nagashima", "Yukihiko", "Yuasa", "Koto", "Yanagihara", "Mitsugi", "Kusumoto", "Kohei", "Toyoda", "Katsuichi", "Kanzaki", "Kozue", "Doi", "Hiroe", "Imaizumi", "Noriaki", "Udagawa", "Takanobu", "Nanbu", "Keizo", "Nishi", "Toshio", "Shigeki", "Teiichi", "Shimura", "Shogo", "Fukuda", "Kiku", "Mochida", "Shizue", "Hashizume", "Yone", "Yoshitake", "Akihiro", "Inui", "Kuniharu", "Takahata", "Toshihiko", "Sawa", "Taizo", "Hosoya", "Kishi", "Takehara", "Masano", "Sugino", "Junzo", "Takahara", "Teruyuki", "Sakamaki", "Naohiro", "Yuki", "Fumiko", "Yasui", "Emi", "Furuta", "Shoken", "Eda", "Toshitaka", "Oshima", "workable", "slope", "numberless", "bed", "abounding", "thumb", "street", "call", "neat", "pancake", "ducks", "mitten", "industry", "hum", "whispering", "gullible", "far-flung", "expansion", "ruin", "writer", "teeny-tiny", "same", "rude", "attend", "reminiscent", "temporary", "erratic", "space", "health", "strengthen", "learn", "precious", "aromatic", "uttermost", "root", "ghost", "receptive", "stranger", "card", "noxious", "parallel", "quiet", "form", "lopsided", "twist", "innocent", "mug", "motionless", "wobble", "sheep", "fabulous", "opposite", "lush", "office", "puzzling", "move", "trace", "turn", "stereotyped", "telling", "tin", "arrogant", "cars", "waiting", "futuristic", "suit", "trite", "imminent", "earthquake", "playground", "payment", "rightful", "governor", "regret", "juicy", "literate", "breakable", "hospital", "alcoholic", "oven", "pot", "flame", "wind", "attract", "impolite", "bruise", "oranges", "vengeful", "unhealthy", "taboo", "fry", "tease", "kittens", "didactic", "zipper", "spray", "long", "moldy", "tight", "youthful", "grease", "grey", "laughable", "approval", "purple", "adhesive", "disillusioned", "joyous", "passenger", "amazing", "domineering", "aboard", "unusual", "label", "minute", "excite", "cannon", "ritzy", "precede", "pretty", "blow", "offer", "discovery", "moor", "hat", "house", "fireman", "coat", "stain", "wish", "cross", "wrestle", "weather", "dizzy", "electric", "things", "pedal", "chivalrous", "sail", "kiss", "riddle", "vigorous", "loose", "purring", "thin", "acrid", "bead", "gray", "common", "tranquil", "malicious", "powder", "silver", "helpful", "tawdry", "ill-fated", "obsolete", "yawn", "nostalgic", "cooperative", "strip", "plucky", "caring", "robin", "change", "silky", "busy", "plastic", "shaky", "flow", "redundant", "airplane", "thoughtful", "jaded", "eggnog", "copy", "profuse", "closed", "boiling", "stupendous", "bells", "political", "hug", "chess", "stage", "unite", "thunder", "boast", "callous", "distinct", "maddening", "organic", "examine", "rhyme", "skirt", "poor", "soft", "wren", "macho", "confess", "deserted", "absurd", "offend", "savory", "animal", "legal", "cute", "rail", "poised", "messy", "toe", "jagged", "jumpy", "able", "roomy", "grain", "murky", "wonderful", "prickly", "apathetic", "assorted", "unbiased", "texture", "fix", "man", "finicky", "cool", "scare", "mend", "place", "wide-eyed", "tense", "acoustic", "educated", "park", "fire", "person", "squirrel", "incompetent", "gifted", "rampant", "craven", "wistful", "wrist", "familiar", "promise", "wound", "attempt", "hot", "collar", "lettuce", "crabby", "rob", "notebook", "men", "towering", "property", "juice", "spooky", "wanting", "highfalutin", "bury", "beef", "good", "sheet", "solid", "free", "shelf", "madly", "wild", "harmonious", "broad", "squeal", "exultant", "fail", "therapeutic", "limping", "average", "befitting", "event", "thing", "elbow", "annoy", "zephyr", "reason", "notice", "ring", "flat", "soap", "perform", "challenge", "view", "farm", "egg", "cast", "irritate", "brave", "help", "fetch", "charge", "keen", "fretful", "food", "undress", "elegant", "deep", "cellar", "vivacious", "rot", "direful", "earsplitting", "bell", "glossy", "writing", "magical", "heavy", "decorate", "religion", "gather", "unequal", "best", "colorful", "aboriginal", "tow", "eggs", "clam", "gratis", "repair", "aspiring", "van", "sigh", "automatic", "faint", "mess", "up", "loss", "lumber", "quill", "momentous", "tray", "nondescript", "cup", "elfin", "wry", "tasteless", "donkey", "book", "doctor", "creature", "snake", "preach", "discreet", "spectacular", "boat", "lumpy", "puzzled", "own", "eyes", "rake", "grumpy", "calendar", "end", "finger", "careless", "verse", "oil", "irate", "boundary", "poison", "clover", "adjustment", "crawl", "tested", "reign", "thread", "retire", "button", "tour", "pocket", "government", "straight", "handle", "downtown", "serve", "cherries", "pop", "cows", "crooked", "capable", "experience", "elastic", "materialistic", "aunt", "sparkle", "reflect", "design", "allow", "sharp", "drag", "black-and-white", "burn", "penitent", "stop", "carve", "stamp", "nine", "zinc", "wrong", "leg", "wet", "abandoned", "truculent", "ossified", "actor", "meal", "careful", "new", "cake", "sponge", "coordinated", "adaptable", "visitor", "stupid", "file", "rambunctious", "daily", "unknown", "guttural", "run", "page", "baby", "substance", "delicate", "remarkable", "cabbage", "wacky", "cooing", "kindhearted", "communicate", "cave", "agreeable", "thaw", "hulking", "head", "possible", "aware", "number", "quarter", "succinct", "fragile", "scandalous", "store", "work", "cure", "prose", "check", "wise", "nappy", "nosy", "unable", "snail", "toothbrush", "cushion", "clap", "hallowed", "big", "bless", "songs", "whip", "silly", "vanish", "obnoxious", "geese", "blue-eyed", "edge", "star", "last", "sin", "river", "tent", "orange", "cakes", "gabby", "torpid", "drawer", "deranged", "carry", "acoustics", "growth", "pets", "scared", "fancy", "hole", "bored", "zesty", "mammoth", "road", "shade", "yielding", "fresh", "angry", "mountain", "handsomely", "mixed", "company", "smelly", "kneel", "general", "kind", "group", "plough", "fly", "disappear", "divide", "effect", "male", "month", "joke", "business", "minister", "accurate", "obeisant", "near", "melt", "frogs", "mine", "repulsive", "pencil", "cloistered", "whistle", "thrill", "abashed", "analyze", "smoke", "whine", "plausible", "ray", "agonizing", "decision", "hang", "march", "spiky", "destroy", "hope", "icy", "marry", "greasy", "cheer", "abhorrent", "hard", "bang", "wilderness", "jealous", "carpenter", "bikes", "hypnotic", "cumbersome", "toys", "calculating", "utter", "harass", "queue", "alert", "money", "mouth", "respect", "right", "spiritual", "gun", "giant", "pen", "staking", "pointless", "gorgeous", "confuse", "leather", "building", "protest", "tame", "graceful", "oceanic", "skin", "dance", "decisive", "arrest", "admit", "back", "potato", "milky", "alive", "jellyfish", "hideous", "synonymous", "hobbies", "animated", "perfect", "round", "chicken", "flawless", "behavior", "produce", "plantation", "rely", "terrific", "lace", "used", "successful", "mean", "party", "boil", "meddle", "unruly", "faithful", "introduce", "pizzas", "cluttered", "bad", "industrious", "polite", "rinse", "painstaking", "thank", "choke", "tooth", "machine", "desk", "intelligent", "knife", "guarded", "zip", "realize", "knotty", "roasted", "happy", "phone", "quick", "clumsy", "tremble", "bridge", "huge", "rainstorm", "shut", "shelter", "flaky", "suggestion", "macabre", "enchanted", "tedious", "advertisement", "hill", "pan", "calculate", "godly", "nod", "lavish", "salt", "pat", "hesitant", "dirt", "disagreeable", "rejoice", "kindly", "panoramic", "distance", "fearless", "multiply", "children", "teaching", "toes", "selection", "quartz", "threatening", "wood", "conscious", "bee", "arm", "snakes", "sand", "knock", "scale", "tart", "zonked", "station", "adorable", "self", "cagey", "rifle", "divergent", "sign", "rod", "bare", "snow", "sparkling", "shivering", "serious", "dad", "quarrelsome", "cowardly", "deeply", "blink", "obedient", "interrupt", "library", "hover", "caption", "shoe", "ban", "well-made", "freezing", "lip", "sulky", "dress", "railway", "include", "corn", "wink", "play", "license", "cats", "special", "subdued", "festive", "toy", "understood", "weary", "mass", "misty", "windy", "spotty", "mailbox", "black", "pipe", "accept", "yummy", "jog", "name", "cub", "knee", "sleep", "resonant", "oafish", "curl", "disastrous", "bite", "makeshift", "question", "overwrought", "nutty", "door", "room", "humdrum", "lazy", "scattered", "curtain", "scissors", "hate", "cheerful", "argue", "stay", "ruddy", "report", "swing", "horrible", "girl", "visit", "sturdy", "first", "decorous", "one", "ill-informed", "snatch", "peel", "bow", "strong", "magic", "earthy", "pleasant", "pushy", "shiny", "loaf", "abject", "beginner", "basketball", "belief", "screw", "chop", "stingy", "absorbing", "steel", "laugh", "letters", "obsequious", "strange", "release", "onerous", "ink", "squealing", "sneeze", "judicious", "nose", "contain", "water", "listen", "psychedelic", "town", "liquid", "measure", "curved", "aggressive", "fumbling", "rest", "crowded", "fade", "sloppy", "low", "scarce", "birthday", "bomb", "uneven", "romantic", "rapid", "grandmother", "soothe", "brief", "plate", "lowly", "dare", "rebel", "fog", "income", "dynamic", "ugliest", "decay", "raise", "please", "addicted", "scribble", "dear", "happen", "bolt", "border", "linen", "step", "harbor", "gaping", "bounce", "overt", "decide", "travel", "verdant", "boring", "milk", "better", "parched", "homeless", "immense", "agree", "meaty", "iron", "sour", "horses", "locket", "drain", "lame", "humorous", "continue", "pickle", "look", "long-term", "remember", "trot", "entertain", "plot", "sable", "peck", "vest", "ambiguous", "kettle", "past", "unarmed", "weight", "dull", "brick", "action", "memorize", "matter", "cultured", "quickest", "reply", "control", "miss", "rescue", "ragged", "exciting", "umbrella", "arithmetic", "hissing", "ball", "fertile", "ladybug", "week", "race", "north", "substantial", "account", "well-off", "numerous", "stitch", "calm", "omniscient", "tasteful", "ready", "rigid", "elderly", "standing", "deafening", "plant", "crazy", "glistening", "mind", "increase", "magenta", "coal", "flash", "healthy", "bumpy", "wandering", "melodic", "way", "mix", "drip", "adventurous", "jail", "pause", "wasteful", "feeble", "toothpaste", "truck", "want", "quack", "panicky", "blot", "neck", "vegetable", "fortunate", "harm", "debt", "snobbish", "even", "face", "thankful", "found", "overrated", "spiffy", "plug", "sock", "berserk", "tangible", "flavor", "recognise", "ripe", "snails", "winter", "satisfy", "yell", "exist", "flock", "eminent", "dogs", "charming", "feigned", "paltry", "soda", "vacuous", "tender", "heavenly", "can", "part", "helpless", "equal", "wine", "great", "badge", "depend", "beg", "scent", "attack", "theory", "rush", "rule", "voracious", "invention", "idiotic", "complain", "smile", "hateful", "obtain", "representative", "applaud", "naughty", "houses", "workable", "slope", "numberless", "bed", "abounding", "thumb", "street", "call", "neat", "pancake", "ducks", "mitten", "industry", "hum", "whispering", "gullible", "far-flung", "expansion", "ruin", "writer", "teeny-tiny", "same", "rude", "attend", "reminiscent", "temporary", "erratic", "space", "health", "strengthen", "learn", "precious", "aromatic", "uttermost", "root", "ghost", "receptive", "stranger", "card", "noxious", "parallel", "quiet", "form", "lopsided", "twist", "innocent", "mug", "motionless", "wobble", "sheep", "fabulous", "opposite", "lush", "office", "puzzling", "move", "trace", "turn", "stereotyped", "telling", "tin", "arrogant", "cars", "waiting", "futuristic", "suit", "trite", "imminent", "earthquake", "playground", "payment", "rightful", "governor", "regret", "juicy", "literate", "breakable", "hospital", "alcoholic", "oven", "pot", "flame", "wind", "attract", "impolite", "bruise", "oranges", "vengeful", "unhealthy", "taboo", "fry", "tease", "kittens", "didactic", "zipper", "spray", "long", "moldy", "tight", "youthful", "grease", "grey", "laughable", "approval", "purple", "adhesive", "disillusioned", "joyous", "passenger", "amazing", "domineering", "aboard", "unusual", "label", "minute", "excite", "cannon", "ritzy", "precede", "pretty", "blow", "offer", "discovery", "moor", "hat", "house", "fireman", "coat", "stain", "wish", "cross", "wrestle", "weather", "dizzy", "electric", "things", "pedal", "chivalrous", "sail", "kiss", "riddle", "vigorous", "loose", "purring", "thin", "acrid", "bead", "gray", "common", "tranquil", "malicious", "powder", "silver", "helpful", "tawdry", "ill-fated", "obsolete", "yawn", "nostalgic", "cooperative", "strip", "plucky", "caring", "robin", "change", "silky", "busy", "plastic", "shaky", "flow", "redundant", "airplane", "thoughtful", "jaded", "eggnog", "copy", "profuse", "closed", "boiling", "stupendous", "bells", "political", "hug", "chess", "stage", "unite", "thunder", "boast", "callous", "distinct", "maddening", "organic", "examine", "rhyme", "skirt", "poor", "soft", "wren", "macho", "confess", "deserted", "absurd", "offend", "savory", "animal", "legal", "cute", "rail", "poised", "messy", "toe", "jagged", "jumpy", "able", "roomy", "grain", "murky", "wonderful", "prickly", "apathetic", "assorted", "unbiased", "texture", "fix", "man", "finicky", "cool", "scare", "mend", "place", "wide-eyed", "tense", "acoustic", "educated", "park", "fire", "person", "squirrel", "incompetent", "gifted", "rampant", "craven", "wistful", "wrist", "familiar", "promise", "wound", "attempt", "hot", "collar", "lettuce", "crabby", "rob", "notebook", "men", "towering", "property", "juice", "spooky", "wanting", "highfalutin", "bury", "beef", "good", "sheet", "solid", "free", "shelf", "madly", "wild", "harmonious", "broad", "squeal", "exultant", "fail", "therapeutic", "limping", "average", "befitting", "event", "thing", "elbow", "annoy", "zephyr", "reason", "notice", "ring", "flat", "soap", "perform", "challenge", "view", "farm", "egg", "cast", "irritate", "brave", "help", "fetch", "charge", "keen", "fretful", "food", "undress", "elegant", "deep", "cellar", "vivacious", "rot", "direful", "earsplitting", "bell", "glossy", "writing", "magical", "heavy", "decorate", "religion", "gather", "unequal", "best", "colorful", "aboriginal", "tow", "eggs", "clam", "gratis", "repair", "aspiring", "van", "sigh", "automatic", "faint", "mess", "up", "loss", "lumber", "quill", "momentous", "tray", "nondescript", "cup", "elfin", "wry", "tasteless", "donkey", "book", "doctor", "creature", "snake", "preach", "discreet", "spectacular", "boat", "lumpy", "puzzled", "own", "eyes", "rake", "grumpy", "calendar", "end", "finger", "careless", "verse", "oil", "irate", "boundary", "poison", "clover", "adjustment", "crawl", "tested", "reign", "thread", "retire", "button", "tour", "pocket", "government", "straight", "handle", "downtown", "serve", "cherries", "pop", "cows", "crooked", "capable", "experience", "elastic", "materialistic", "aunt", "sparkle", "reflect", "design", "allow", "sharp", "drag", "black-and-white", "burn", "penitent", "stop", "carve", "stamp", "nine", "zinc", "wrong", "leg", "wet", "abandoned", "truculent", "ossified", "actor", "meal", "careful", "new", "cake", "sponge", "coordinated", "adaptable", "visitor", "stupid", "file", "rambunctious", "daily", "unknown", "guttural", "run", "page", "baby", "substance", "delicate", "remarkable", "cabbage", "wacky", "cooing", "kindhearted", "communicate", "cave", "agreeable", "thaw", "hulking", "head", "possible", "aware", "number", "quarter", "succinct", "fragile", "scandalous", "store", "work", "cure", "prose", "check", "wise", "nappy", "nosy", "unable", "snail", "toothbrush", "cushion", "clap", "hallowed", "big", "bless", "songs", "whip", "silly", "vanish", "obnoxious", "geese", "blue-eyed", "edge", "star", "last", "sin", "river", "tent", "orange", "cakes", "gabby", "torpid", "drawer", "deranged", "carry", "acoustics", "growth", "pets", "scared", "fancy", "hole", "bored", "zesty", "mammoth", "road", "shade", "yielding", "fresh", "angry", "mountain", "handsomely", "mixed", "company", "smelly", "kneel", "general", "kind", "group", "plough", "fly", "disappear", "divide", "effect", "male", "month", "joke", "business", "minister", "accurate", "obeisant", "near", "melt", "frogs", "mine", "repulsive", "pencil", "cloistered", "whistle", "thrill", "abashed", "analyze", "smoke", "whine", "plausible", "ray", "agonizing", "decision", "hang", "march", "spiky", "destroy", "hope", "icy", "marry", "greasy", "cheer", "abhorrent", "hard", "bang", "wilderness", "jealous", "carpenter", "bikes", "hypnotic", "cumbersome", "toys", "calculating", "utter", "harass", "queue", "alert", "money", "mouth", "respect", "right", "spiritual", "gun", "giant", "pen", "staking", "pointless", "gorgeous", "confuse", "leather", "building", "protest", "tame", "graceful", "oceanic", "skin", "dance", "decisive", "arrest", "admit", "back", "potato", "milky", "alive", "jellyfish", "hideous", "synonymous", "hobbies", "animated", "perfect", "round", "chicken", "flawless", "behavior", "produce", "plantation", "rely", "terrific", "lace", "used", "successful", "mean", "party", "boil", "meddle", "unruly", "faithful", "introduce", "pizzas", "cluttered", "bad", "industrious", "polite", "rinse", "painstaking", "thank", "choke", "tooth", "machine", "desk", "intelligent", "knife", "guarded", "zip", "realize", "knotty", "roasted", "happy", "phone", "quick", "clumsy", "tremble", "bridge", "huge", "rainstorm", "shut", "shelter", "flaky", "suggestion", "macabre", "enchanted", "tedious", "advertisement", "hill", "pan", "calculate", "godly", "nod", "lavish", "salt", "pat", "hesitant", "dirt", "disagreeable", "rejoice", "kindly", "panoramic", "distance", "fearless", "multiply", "children", "teaching", "toes", "selection", "quartz", "threatening", "wood", "conscious", "bee", "arm", "snakes", "sand", "knock", "scale", "tart", "zonked", "station", "adorable", "self", "cagey", "rifle", "divergent", "sign", "rod", "bare", "snow", "sparkling", "shivering", "serious", "dad", "quarrelsome", "cowardly", "deeply", "blink", "obedient", "interrupt", "library", "hover", "caption", "shoe", "ban", "well-made", "freezing", "lip", "sulky", "dress", "railway", "include", "corn", "wink", "play", "license", "cats", "special", "subdued", "festive", "toy", "understood", "weary", "mass", "misty", "windy", "spotty", "mailbox", "black", "pipe", "accept", "yummy", "jog", "name", "cub", "knee", "sleep", "resonant", "oafish", "curl", "disastrous", "bite", "makeshift", "question", "overwrought", "nutty", "door", "room", "humdrum", "lazy", "scattered", "curtain", "scissors", "hate", "cheerful", "argue", "stay", "ruddy", "report", "swing", "horrible", "girl", "visit", "sturdy", "first", "decorous", "one", "ill-informed", "snatch", "peel", "bow", "strong", "magic", "earthy", "pleasant", "pushy", "shiny", "loaf", "abject", "beginner", "basketball", "belief", "screw", "chop", "stingy", "absorbing", "steel", "laugh", "letters", "obsequious", "strange", "release", "onerous", "ink", "squealing", "sneeze", "judicious", "nose", "contain", "water", "listen", "psychedelic", "town", "liquid", "measure", "curved", "aggressive", "fumbling", "rest", "crowded", "fade", "sloppy", "low", "scarce", "birthday", "bomb", "uneven", "romantic", "rapid", "grandmother", "soothe", "brief", "plate", "lowly", "dare", "rebel", "fog", "income", "dynamic", "ugliest", "decay", "raise", "please", "addicted", "scribble", "dear", "happen", "bolt", "border", "linen", "step", "harbor", "gaping", "bounce", "overt", "decide", "travel", "verdant", "boring", "milk", "better", "parched", "homeless", "immense", "agree", "meaty", "iron", "sour", "horses", "locket", "drain", "lame", "humorous", "continue", "pickle", "look", "long-term", "remember", "trot", "entertain", "plot", "sable", "peck", "vest", "ambiguous", "kettle", "past", "unarmed", "weight", "dull", "brick", "action", "memorize", "matter", "cultured", "quickest", "reply", "control", "miss", "rescue", "ragged", "exciting", "umbrella", "arithmetic", "hissing", "ball", "fertile", "ladybug", "week", "race", "north", "substantial", "account", "well-off", "numerous", "stitch", "calm", "omniscient", "tasteful", "ready", "rigid", "elderly", "standing", "deafening", "plant", "crazy", "glistening", "mind", "increase", "magenta", "coal", "flash", "healthy", "bumpy", "wandering", "melodic", "way", "mix", "drip", "adventurous", "jail", "pause", "wasteful", "feeble", "toothpaste", "truck", "want", "quack", "panicky", "blot", "neck", "vegetable", "fortunate", "harm", "debt", "snobbish", "even", "face", "thankful", "found", "overrated", "spiffy", "plug", "sock", "berserk", "tangible", "flavor", "recognise", "ripe", "snails", "winter", "satisfy", "yell", "exist", "flock", "eminent", "dogs", "charming", "feigned", "paltry", "soda", "vacuous", "tender", "heavenly", "can", "part", "helpless", "equal", "wine", "great", "badge", "depend", "beg", "scent", "attack", "theory", "rush", "rule", "voracious", "invention", "idiotic", "complain", "smile", "hateful", "obtain", "representative", "applaud", "naughty", "houses"

            print("")
            print(Fore.LIGHTGREEN_EX)

            def getusername():
                if data2.username is None:
                    os.system("cls")
                    print(Fore.RED)
                    wanimation("Wrong id! closing program in 5 seconds", True)
                    os.system("timeout 5")
                    time.sleep(10)
                    exit()
                else:
                    for i in tqdm(range(0, 23), desc="Fetching user's ip adress", ascii=" ----------", unit="1 %",
                                  ncols=84,
                                  total=100):
                        time.sleep(random.uniform(.01, .1))
                    os.system('cls')
                    for i in range(4):
                        print("")
                    for i in tqdm(range(23, 62), desc="Fetching user's password", ascii=" ----------", unit="1 %",
                                  ncols=82,
                                  total=100, initial=23):
                        time.sleep(random.uniform(.01, .1))
                    os.system('cls')
                    for i in range(4):
                        print("")
                    for i in tqdm(range(62, 81), desc="Fetching user's credit card info", ascii=" ----------",
                                  unit="1 %",
                                  ncols=91,
                                  total=100, initial=62):
                        time.sleep(random.uniform(.01, .1))
                    os.system('cls')
                    for i in range(4):
                        print("")
                    for i in tqdm(range(81, 100), desc="Fetching user's email", ascii=" ----------", unit="1 %",
                                  ncols=83,
                                  total=100, initial=81):
                        time.sleep(random.uniform(.01, .1))
                    email = "@yahoo.com", "@gmail.com", "@onet.pl", "@o2.pl"
                    rando = random.randint(0, len(email) - 1)
                    separator = '#'
                    mail1 = data2.username.split(separator, 1)[0]
                    if random.randint(0, 1) == 1:
                        rok = random.randint(0, 2022)
                    else:
                        rok = random.randint(1900, 2022)

                    wanimation(
                        f'username: {data2.username.encode("utf-8").decode("unicode-escape")} \ne-mail: {mail1.encode("utf-8").decode("unicode_escape")}{rok}{email[rando]}',
                        True)
                    wanimation(
                        f"password:{random.choice(words_pass)}{random.randint(1950, 2023)}{random.choice(words_pass)}")

            getusername()
            print(" ")
            print(" ")
            wanimation("press [Q] to exit")
            while True:
                key = keyboard.read_event()
                if key.name == "q":
                    exit()


        restofall()
        a = 0

if tudu == "3":
    time.sleep(random.uniform(0.2137, 1.69))
    os.system("title hakier prompt ｜ dancing parrot ｜ easter egg")
    while True:
        print(Fore.RED)
        p1()
        time.sleep(0.05)
        os.system("cls")
        print(Fore.YELLOW)
        p2()
        time.sleep(0.05)
        os.system("cls")
        print(Fore.LIGHTYELLOW_EX)
        p3()
        time.sleep(0.05)
        os.system("cls")
        print(Fore.GREEN)
        p4()
        time.sleep(0.05)
        os.system("cls")
        print(Fore.BLUE)
        p5()
        time.sleep(0.05)
        os.system("cls")
        print(Fore.MAGENTA)
        p7()
        time.sleep(0.05)
        os.system("cls")
        print(Fore.RED)
        p8()
        time.sleep(0.05)
        os.system("cls")
        print(Fore.YELLOW)
        p9()
        time.sleep(0.05)
        os.system("cls")
        print(Fore.LIGHTYELLOW_EX)
        p8()
        time.sleep(0.05)
        os.system("cls")
        print(Fore.GREEN)
        p7()
        time.sleep(0.05)
        os.system("cls")
        print(Fore.BLUE)
        p5()
        time.sleep(0.05)
        os.system("cls")
        print(Fore.MAGENTA)
        p4()
        time.sleep(0.05)
        os.system("cls")
        print(Fore.RED)
        p3()
        time.sleep(0.05)
        os.system("cls")
        print(Fore.WHITE)
        p2()
        time.sleep(0.05)
        os.system("cls")

if tudu == "4":
    os.system(f'title hakier prompt ｜ updates')
    wanimation("work in progress", True)
    wanimation("click [Q] to exit.")
    while True:
        key = keyboard.read_event()
        if key.name == "q":
            exit()

if tudu == "dev1":
    ays = input("are you sure? (y/n)")
    if ays == "y":
        for i in tqdm(range(0, 100), desc="Destroying world", ascii=" ----------", unit="1 %", ncols=72):
            time.sleep(1)
            time.sleep(5)
            os.system("cls")
            wanimation("┏┓┏┓┏┳━━━┳━━━┳┓╋╋┏━━━┓  ┏━━━┳━━━┳━━━┳━━━━┳━━━┳━━━┳━━━┳━━━┓", True)
            wanimation('┃┃┃┃┃┃┏━┓┃┏━┓┃┃╋╋┗┓┏┓┃  ┗┓┏┓┃┏━━┫┏━┓┃┏┓┏┓┃┏━┓┃┏━┓┃┏━━┻┓┏┓┃', True)
            wanimation('┃┃┃┃┃┃┃╋┃┃┗━┛┃┃╋╋╋┃┃┃┃  ╋┃┃┃┃┗━━┫┗━━╋┛┃┃┗┫┗━┛┃┃╋┃┃┗━━┓┃┃┃┃', True)
            wanimation('┃┗┛┗┛┃┃╋┃┃┏┓┏┫┃╋┏┓┃┃┃┃  ╋┃┃┃┃┏━━┻━━┓┃╋┃┃╋┃┏┓┏┫┃╋┃┃┏━━┛┃┃┃┃', True)
            wanimation('┗┓┏┓┏┫┗━┛┃┃┃┗┫┗━┛┣┛┗┛┃  ┏┛┗┛┃┗━━┫┗━┛┃ ┃┃ ┃┃┃┗┫┗━┛┃┗━━┳┛┗┛┃', True)
            wanimation('╋┗┛┗┛┗━━━┻┛┗━┻━━━┻━━━┛  ┗━━━┻━━━┻━━━┛ ┗┛ ┗┛┗━┻━━━┻━━━┻━━━┛', True)
            print("")
            os.system("pause")
            wanimation("Restart in 1minute to finish destoying the world", True)
            wanimation("colosing in 1 miute", True)
            os.system("timeout 60")
            exit()
if tudu == "5" or tudu == 5:
    os.system(f'title hakier prompt ｜ clear cache')
    messagebox.showinfo("WARNING", "THIS WILL WIPE ALL* FILES IN: %TEMP% DIRECORY")
    os.system("del C:/Users/%USERNAME%/AppData/Local/Temp/*.* /Q 2>nul")
    os.system("cls")
    messagebox.showinfo("INFO", "TEMP files cleaned sucesfully")
    messagebox.showinfo("Have a nice day <3", "THANKS FOR USING OUR PROGRAM")
if tudu == "6" or tudu == 6:
    os.system(f'title hakier prompt ｜ calculator')


    def calc():
        a = True
        while a:
            wanimation("Enter your mathematical expression: ", False)
            expression = input()
            a = False
            try:
                result = eval(expression)
                wanimation("Result:", result)
            except:
                wanimation("Invalid expression. Click [ENTER] to try again or [Q] to quit.", True)
                while True:
                    key = keyboard.read_event()
                    if key.name == "q":
                        exit()
                    if key.name == "enter":
                        input()
                        calc()


    calc()
if tudu == "7" or tudu == 7:
    os.system(f'title hakier prompt ｜ speedtest')


    def speedtesta():
        import speedtest
        import time
        print(" ")
        test = speedtest.Speedtest()
        if config.loading_bars is True:
            with tqdm(total=2, desc="testing download & upload", ascii=" ----------", unit="1 %", ncols=84) as pbar:
                download = test.download()
                pbar.update(1)
                upload = test.upload()
                pbar.update(1)
        else:
            wanimation("please wait...", True)
            download = test.download()
            upload = test.upload()

        download_Mbps = download / 10 ** 6
        upload_Mbps = upload / 10 ** 6

        wanimation(f"Download speed: {round(download_Mbps, 2)} Mbps", True)
        wanimation(f"Upload speed: {round(upload_Mbps, 2)} Mbps", True)
        print(" ")
        time.sleep(2)
        wanimation("Click [ENTER] to try again or [Q] to quit.")
        while True:
            key = keyboard.read_event()
            if key.name == "q":
                exit()
            if key.name == "enter":
                input()
                speedtesta()


    speedtesta()
