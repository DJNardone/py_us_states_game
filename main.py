import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_data = pandas.read_csv("50_states.csv")
state_list = game_data.state.to_list()
all_states = []

while len(all_states) < 50:
    guess_state = screen.textinput(title=f"{len(all_states)}/50 States Correct",
                                   prompt="What's another State name?").title()
    if guess_state == "Exit":
        break
    if guess_state in state_list:
        all_states.append(guess_state)
        st = turtle.Turtle()
        st.penup()
        st.hideturtle()
        good_state = game_data[game_data.state == guess_state]
        st.goto(good_state.x.iloc[0], good_state.y.iloc[0])
        st.write(guess_state)

remaining_states = [i for i in state_list if i not in all_states]
remaining_data = pandas.DataFrame(remaining_states)
remaining_data.to_csv("states_to_learn.csv")
# print(remaining_states)

# def mouse_click_cor(x, y):
#     print(x, y)
# turtle.onscreenclick(mouse_click_cor)
# turtle.mainloop()


