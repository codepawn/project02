import os


def num_blanks_maker(answers):
    """
    input: list of answers
    output: list of blanks
    """
    blanks = []
    converter = 1
    for i in range(0, len(answers)):
        result = "__{0}__".format(i + converter)
        blanks.append(result)
    return blanks


def answer_mixer(score, answers):
    """
    input: list of answers
    output: mixed answers
    """
    num_blanks = num_blanks_maker(answers)

    counter = 0
    quiz_list = []
    while(counter < len(easy_answers)):
        if score <= counter:
            quiz_list.append(num_blanks[counter])
        else:
            quiz_list.append(answers[counter])
        counter += 1
    return quiz_list


def easy_blanks(tried, score, intro_check):
    easy_answers = ['world', 'python', 'print', 'html']
    quiz_list = answer_mixer(score, easy_answers)
    if tried == 0 and intro_check == False:
        print "You've chosen easy!\n\nYou will get 5 guesses per problem \n"
    print "The current paragraph reads as such:\nA common first thing to do in a language is display"
    print "'Hello {0}!' In {1} this is particularly easy; all you have to do".format(quiz_list[0], quiz_list[1])
    print "is type in:"
    print "{0} \"Hello {1}!\"".format(quiz_list[2], quiz_list[0])
    print "Of course, that isn't a very useful thing to do. However, it is an"
    print "example of how to output to the user using the {0} command, and".format(quiz_list[2])
    print "produces a program which does something, so it is useful in that capacity.\n"
    print "It may seem a bit odd to do something in a Turing complete language that"
    print "can be done even more easily with an {0} file in a browser, but it's".format(quiz_list[3])
    print "a step in learning {0} syntax, and that's really its purpose.\n\n".format(quiz_list[1])
    if score == 4:
        print "You won!"
    print "score : ", score
    print "tried : ", tried
    print ""


def medium_blanks(tried, score, intro_check):
    if tried == 0 and intro_check == False:
        print "You've chosen medium!\n\nYou will get 5 guesses per problem\n"
    print "The current paragraph reads as such:\n"
    if score == 0:
        quiz1 = "__1__"
    else:
        quiz1 = "function"
    if score < 2:
        quiz2 = "__2__"
    else:
        quiz2 = "arguments"
    if score < 3:
        quiz3 = "__3__"
    else:
        quiz3 = "None"
    if score < 4:
        quiz4 = "__4__"
    else:
        quiz4 = "list"
    print "A {0} is created with the def keyword.  You specify the inputs a".format(quiz1)
    print "{0} takes by adding {1} separated by commas between the parentheses.".format(quiz1, quiz2)
    print "{0}s by default returns {1} if you don't specify the value to retrun.".format(quiz1, quiz3)
    print "{0} can be standard data types such as string, integer, dictionary, tuple,".format(quiz2)
    print "and {0} or can be more complicated such as objects and lambda functions.\n\n".format(quiz4)
    if score == 4:
        print "You won!"
    print "score : ", score
    print "tried : ", tried
    print ""


def hard_blanks(tried, score, intro_check):
    if tried == 0 and intro_check == False:
        print "You've chosen hard!\n\nYou will get 5 guesses per problem\n"
    print "The current paragraph reads as such:\n"
    if score == 0:
        quiz1 = "__1__"
    else:
        quiz1 = "class"
    if score < 2:
        quiz2 = "__2__"
    else:
        quiz2 = "method"
    if score < 3:
        quiz3 = "__3__"
    else:
        quiz3 = "init"
    if score < 4:
        quiz4 = "__4__"
    else:
        quiz4 = "instance"
    if score < 5:
        quiz5 = "__5__"
    else:
        quiz5 = "__repr__"
    if score < 6:
        quiz6 = "__6__"
    else:
        quiz6 = "__add__"
    if score < 7:
        quiz7 = "__7__"
    else:
        quiz7 = "__sub__"
    if score < 8:
        quiz8 = "__8__"
    else:
        quiz8 = "__lt__"
    if score < 9:
        quiz9 = "__9__"
    else:
        quiz9 = "__gt__"
    if score < 10:
        quiz10 = "__10__"
    else:
        quiz10 = "__eq__"
    print "When you create a {0}, certain {1}s are automatically".format(quiz1, quiz2)
    print "generated for you if you don't make them manually. These contain multiple"
    print "underscores before and after the word defining them.  When you write"
    print "a {0}, you almost always include at least the {1} {2}, defining".format(quiz1, quiz3, quiz2)
    print "variables for when {0}s of the {1} get made.  Additionally, you generally".format(quiz4, quiz1)
    print "want to create a {0} {1}, which will allow a string representation".format(quiz5, quiz1)
    print "of the method to be viewed by other developers.\n"
    print "You can also create binary operators, like {0} and {1}, which".format(quiz6, quiz7)
    print "allow + and - to be used by {0} of the {1}.  Similarly, {2},".format(quiz4, quiz1, quiz8)
    print "{0}, and {1} allow {2}s of the {3} to be compared".format(quiz9, quiz10, quiz4, quiz1)
    print "(with <, >, and ==).\n\n"
    if score == 10:
        print "You won!"
    print "score : ", score
    print "tried : ", tried
    print ""


def question_number(score):
    num = score + 1
    return "What should be substituted in for __{0}__? ".format(num)


def difficulty_set():
    """
    square
    inputs: Difficulty level user want
    outputs:
    """
    did_before = False
    while(True):
        os.system('clear')
        print "Please select a game difficulty by typing it in"
        print "Possible choices include easy, medium, and hard."
        if did_before == True:
            print 'Type again'
        difficulty = raw_input("Type : ")
        if difficulty == 'easy':
            return 'easy'
        elif difficulty == 'medium':
            return 'medium'
        elif difficulty == 'hard':
            return 'hard'
        else:
            did_before = True


def main_game(difficulty):
    tried = 0
    score = 0
    tried_max = 5
    score_max = 4
    intro_check = False
    if difficulty == 'easy':
        the_answer = ['world', 'python', 'print', 'html']
        while(score < score_max and tried < tried_max):
            os.system('clear')
            easy_blanks(tried, score, intro_check)
            user_answer = raw_input(question_number(score))
            intro_check = True
            if the_answer[score] == user_answer:
                score += 1
                tried = 0
            else:
                tried += 1
        easy_blanks(tried, score, intro_check)

    if difficulty == 'medium':
        the_answer = ['function', 'arguments', 'None', 'list']
        while(score < score_max and tried < tried_max):
            os.system('clear')
            medium_blanks(tried, score, intro_check)
            user_answer = raw_input(question_number(score))
            intro_check = True
            if the_answer[score] == user_answer:
                score += 1
                tried = 0
            else:
                tried += 1
        medium_blanks(tried, score, intro_check)

    if difficulty == 'hard':
        score_max = 10
        the_answer = ['class', 'method', '__init__', 'instance',
                      '__repr__', "__add__", "__sub__", "__lt__", "__gt__", "__eq__"]
        while(score < score_max and tried < tried_max):
            os.system('clear')
            hard_blanks(tried, score, intro_check)
            user_answer = raw_input(question_number(score))
            intro_check = True
            if the_answer[score] == user_answer:
                score += 1
                tried = 0
            else:
                tried += 1
        hard_blanks(tried, score, intro_check)


# run

main_game(difficulty_set())
