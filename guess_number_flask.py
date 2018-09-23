from flask import Flask, request
from time import sleep


app = Flask(__name__)


form = """
    <style>
    * {{text-align:center}}
    p:last-of-type {{font-weight:bold}}
    </style>
    <form action="/guess_number" method="POST">
    <input type="hidden" id="minimum" name="minimum" value="{}">
    <input type="hidden" id="maximum" name="maximum" value="{}">
    <p>Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach.</p>
    <p>Zgaduję: <input type="text" name="ask" value="{}"></p>
    <p>{}</p>
    <input type="submit" name="answer" value="mniej">
    <input type="submit" name="answer" value="trafiłeś">
    <input type="submit" name="answer" value="więcej">
    </form>
    """


@app.route("/guess_number", methods=["GET", "POST"])
def guess_number():
    if request.method == "GET":
        return form.format("0", "1000", "500", "")
    else:
        answer = request.form["answer"]
        if answer == "trafiłeś":
            return "Wygrałem!!!"

        ask = int(request.form["ask"])
        minimum = int(request.form["minimum"])
        maximum = int(request.form["maximum"])
        if answer == "mniej":
            if (ask - minimum == 1) and (maximum - ask == 1):
                return form.format(str(minimum), str(maximum), str(ask), "Czyżby?")
            else:
                maximum = ask
        elif answer == "więcej":
            if (ask - minimum == 1) and (maximum - ask == 1):
                return form.format(str(minimum), str(maximum), str(ask), "Czyżby?")
            else:
                minimum = ask
        else:
            return form.format(str(minimum), str(maximum), str(ask), "Nie oszukuj!")
        guess = int((maximum - minimum) / 2) + minimum
        return form.format(str(minimum), str(maximum), str(guess), "")


if __name__ == "__main__":
    app.run()
