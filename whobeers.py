import json
from tkinter import *
from tkinter import Menu

application = Tk()
application.title("Who beers?")
application.minsize(350, 250)
application.geometry('350x250+400+300')


def main():

    with open("beerorder.json", "r") as beer_order:
        beer_order_data = json.load(beer_order)

    episode_roster = []
    # Set up application and dimensions


    # Create quit menu option
    menu = Menu(application)
    quit_item = Menu(menu, tearoff=0)
    quit_item.add_command(label='Quit', command=application.quit)
    menu.add_cascade(label='File', menu=quit_item)
    application.config(menu=menu)

    # Create buttons
    norrisButton = Button(application, text="Norris", height=1, width=6,
                          command=lambda: norris_roster_append_hide(episode_roster, norrisButton))
    norrisButton.place(x=20, y=20)
    kellyButton = Button(application, text="Kelly", height=1, width=6,
                         command=lambda: kelly_roster_append_hide(episode_roster, kellyButton))
    kellyButton.place(x=140, y=20)
    mattButton = Button(application, text="Matt", height=1, width=6,
                        command=lambda: matt_roster_append_hide(episode_roster, mattButton))
    mattButton.place(x=20, y=60)
    daveButton = Button(application, text="Dave", height=1, width=6,
                        command=lambda: dave_roster_append_hide(episode_roster, daveButton))
    daveButton.place(x=140, y=60)
    stephButton = Button(application, text="Steph", height=1, width=6,
                         command=lambda: steph_roster_append_hide(episode_roster, stephButton))
    stephButton.place(x=260, y=20)
    mikeButton = Button(application, text="Mike", height=1, width=6,
                        command=lambda: mike_roster_append_hide(episode_roster, mikeButton))
    mikeButton.place(x=260, y=60)
    determineButton = Button(application, text="Determine Who Beers", height=2, width=20,
                             command=lambda: determine_button_actions(episode_roster, beer_order_data))
    determineButton.place(x=100, y=120)

    application.mainloop()
    """
    #todo
        fix system if no choice is made
        create an executable
    """

    return


def norrisClick(roster_list):
    roster_list.append('Norris')
    return


def kellyClick(roster_list):
    roster_list.append('Kelly')
    return


def mattClick(roster_list):
    roster_list.append('Matt')
    return


def daveClick(roster_list):
    roster_list.append('Dave')
    return


def stephClick(roster_list):
    roster_list.append('Steph')
    return


def mikeClick(roster_list):
    roster_list.append('Mike')
    return


def norris_roster_append_hide(roster_list, button):
    norrisClick(roster_list)
    button.destroy()


def kelly_roster_append_hide(roster_list, button):
    kellyClick(roster_list)
    button.destroy()


def matt_roster_append_hide(roster_list, button):
    mattClick(roster_list)
    button.destroy()


def dave_roster_append_hide(roster_list, button):
    daveClick(roster_list)
    button.destroy()


def steph_roster_append_hide(roster_list, button):
    stephClick(roster_list)
    button.destroy()


def mike_roster_append_hide(roster_list, button):
    mikeClick(roster_list)
    button.destroy()


def determine_who_beers(roster_list, beer_data):

    person_who_beers = None

    rank = len(beer_data) + 1
    for person in beer_data:
        if person in roster_list and beer_data[person] < rank:
            rank = beer_data[person]
            person_who_beers = person

    return person_who_beers


def update_beer_json(person_who_beers, beer_data):

    rank = beer_data[person_who_beers]

    for person in beer_data:
        if beer_data[person] == rank:
            beer_data[person] = len(beer_data)
        elif beer_data[person] > rank:
            beer_data[person] = beer_data[person] - 1

    print(beer_data)

    with open("beerorder.json", 'w') as file:
        json.dump(beer_data, file)

    return


def determine_button_actions(roster_list, beer_data):
    person_who_beers = determine_who_beers(roster_list, beer_data)
    # beer_label = Label(application, text="Person who beers: {}".format(person_who_beers))
    # beer_label.place(x=110, y=180)

    beer_window = Toplevel(height=20, width=40)
    beer_window.title("Beer Person")
    beer_window.minsize(250, 100)
    beer_window.geometry('250x100+450+350')
    beer_message = Label(beer_window, text="Person who beers is {}".format(person_who_beers))
    beer_message.place(x=60, y=20)
    exit_button = Button(beer_window, text="Exit", height=1, width=6, command=lambda: exit_all(beer_window))
    exit_button.place(x=100, y=50)

    update_beer_json(person_who_beers, beer_data)
    return


def exit_all(window):
    window.destroy()
    application.destroy()
    return


if __name__ == '__main__':
    main()
