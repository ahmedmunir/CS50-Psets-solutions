# this is a simulation website for real stock to buy and sell stocks.
# you have the ability to buy, sell, check history of you stock operations.
# before running, you need to connect to API by export its value : 5PB6PRI2RCC7C8BM from alphavantage.co
# by running command: export API_KEY=value

import os
import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Ensure environment variable is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    global user_pocket
    global user_cash
    global total_stocks_value
    global current_price
    user_pocket = db.execute("SELECT * from index_record WHERE id = :i", i=session["user_id"])
    user_cash = db.execute("SELECT * from users WHERE id = :i", i=session["user_id"])

    # This value will be for adding the values of all owned stocks the user have
    total_stocks_value = 0

    # iterate over user_pocket which contain list of all the shares
    for i in range(len(user_pocket)):

        # getting current price and total and install them to list user_pocket
        current_price = lookup(user_pocket[i]["symbol"])
        user_pocket[i]["price"] = current_price["price"]
        total = current_price["price"] * user_pocket[i]["number_of_shares"]
        user_pocket[i]["Total"] = total
        total_stocks_value += total
    total_stocks_value += user_cash[0]['cash']
    return render_template("index.html", user_pocket=user_pocket, total_stocks_value=total_stocks_value, user_cash=user_cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        # if he didnt enter symbol name or number of shares
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("please fill both fields, symbol and number of shares.", 400)

        # if the name of that symbol is not correct
        elif not lookup(request.form.get("symbol")):
            return apology("Sry there is not symbol with that name", 400)

        # make sure that number of shares is greater than zero or not pure integer
        elif not request.form.get("shares").isdigit() or int(request.form.get("shares")) < 0:
            return apology("Sry number of shares must be positive", 400)

        # when all data input by user are valid
        else:

            # check whether the user can afford the price of those shares
            user_money = db.execute(''' SELECT * from users where id = :i ''', i=session["user_id"])
            symbol_info = lookup(request.form.get("symbol"))
            cost = symbol_info["price"] * int(request.form.get("shares"))
            if cost > user_money[0]["cash"]:
                return apology("sry you can't afford those number of shares", 500)
            else:
                # create new table if not exist, and if exist this command will not be executed
                db.execute("CREATE TABLE IF NOT EXISTS history_record(id INTEGER NOT NULL, state TEXT NOT NULL, symbol TEXT NOT NULL, number_of_shares REAL NOT NULL, price REAL NOT NULL, date DATETIME NOT NULL)")

                # create new Table for indexing the shares owned by user
                db.execute("CREATE TABLE IF NOT EXISTS index_record(id INTEGER NOT NULL,symbol TEXT NOT NULL, number_of_shares REAL NOT NULL)")

                # insert data into history_record table
                db.execute("INSERT INTO history_record(id, state, symbol, number_of_shares, price, date) VALUES (:i, :u, :s, :n, :p, :d)",
                           i=session["user_id"], u="buy", s=symbol_info["symbol"], n=int(request.form.get("shares")), p=cost, d=datetime.datetime.now())

                # update the cash after minus the cost of bought shares
                db.execute("UPDATE users SET cash = :c where id = :i", c=user_money[0]["cash"] - cost, i=session["user_id"])

                # select all data into index_record table
                index_record_tmp = db.execute(''' SELECT * from index_record where id = :q''', q=session["user_id"])

                # if it is the 1st time that user will buy some shares
                if not index_record_tmp:
                    db.execute("INSERT INTO index_record(id, symbol, number_of_shares) VALUES (:i, :s, :n)",
                               i=session["user_id"], s=symbol_info["symbol"], n=int(request.form.get("shares")))

                else:
                    checker_counter = 0  # to know if we reach to the end of index_record_tmp or not

                    # iterate over the data get by idex_tmp to check whether that symbol already inside or not
                    for checker in index_record_tmp:

                        # if we get that symbol, then we need to update the value of its shares by adding new shares to old ones
                        if checker["symbol"] == symbol_info["symbol"]:
                            current_shares = db.execute(''' SELECT * from index_record where symbol = :s AND id = :i''',
                                                        s=symbol_info["symbol"], i=session["user_id"])
                            db.execute(''' UPDATE index_record SET number_of_shares = :n where symbol = :s AND id = :i''',
                                       n=int(request.form.get("shares")) + current_shares[0]["number_of_shares"], s=symbol_info["symbol"], i=session["user_id"])
                            break
                        else:
                            checker_counter += 1

                            # if we reach to the end of list and didnt find that symbol, that means the user doesnt have symbol
                            if checker_counter == len(index_record_tmp):
                                db.execute("INSERT INTO index_record(id, symbol, number_of_shares) VALUES (:i, :s, :n)",
                                           i=session["user_id"], s=symbol_info["symbol"], n=int(request.form.get("shares")))
                    checker_counter = 0
                return index()
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_history = db.execute("SELECT * from history_record where id = :i", i=session["user_id"])
    return render_template("history.html", user_history=user_history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        # if the user didnt enter any symbol to search for
        if not request.form.get("symbol"):
            return apology("You need to enter a symbol", 400)
        else:

            # if there is no symbol with that name and lookup function return NULL
            quote = lookup(request.form.get("symbol"))
            if not quote:
                return apology("there is not symbol with that name, sry", 400)
            else:
                # if lookup returned stock, we pass it to html template
                return render_template("quoted.html", quote=quote)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # assign db as global variable to be able to used
    global db
    """Register user"""
    if request.method == "POST":

        # if the user didnt enter a valid username
        if not request.form.get("username"):
            return apology("You must proved your username to register", 400)

        # if the user didnt enter password
        elif not request.form.get("password"):
            return apology("Please enter your password", 400)

        # if the password and the confirmation didnt match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password not match", 400)
        else:
            # prevent 2 users from having the same username
            i = db.execute(''' SELECT * from users ''')
            x = 0
            for row in i:
                if request.form.get("username") == row["username"]:
                    return apology("that username is already exist, please change it", 400)

            # if user entered valid information, we hash the password and store it inside database
            hashed_password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
            db.execute('''INSERT INTO users(username, hash) VALUES (:u, :h)''', u=request.form.get("username"), h=hashed_password)
            return render_template("login.html")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_sell = db.execute("SELECT * from index_record where id = :i", i=session["user_id"])

    # if the user has no shares to sell
    if not user_sell:
        return apology("Sry, you don't have any share to sell", 400)
    else:
        if request.method == "POST":
            symbol_to_sell = request.form.get("symbol")
            no_of_shares_checker = db.execute("SELECT number_of_shares from index_record where id = :i AND symbol = :s",
                                              i=session["user_id"], s=symbol_to_sell)
            current_cash_s = db.execute("SELECT cash from users where id = :i", i=session["user_id"])
            current_cash_value = current_cash_s[0]["cash"]

            # if number of shares entered is less than what the user already have
            if int(request.form.get("shares")) > no_of_shares_checker[0]["number_of_shares"]:
                return apology("Sry, you dont have enough shares", 400)
            else:

                # getting current price of the share we want to sell
                share_to_sell_price = lookup(symbol_to_sell)

                # total money will be added to cash and update cash of user
                total_money = share_to_sell_price["price"] * int(request.form.get("shares"))

                # update the user cash after adding new money
                db.execute("UPDATE users SET cash = :c where id = :i", c=total_money + current_cash_value, i=session["user_id"])

                # update history_record table by adding it as sell operation
                db.execute("INSERT INTO history_record(id, state, symbol, number_of_shares, price, date) VALUES (:i, :u, :s, :n, :p, :d)",
                           i=session["user_id"], u="sell", s=symbol_to_sell, n=int(request.form.get("shares")), p=total_money, d=datetime.datetime.now())

                # update index_record by minus current share from what sold
                remainder_shares = no_of_shares_checker[0]["number_of_shares"] - int(request.form.get("shares"))

                # delete the whole row if the number of shares become 0
                if remainder_shares == 0:
                    db.execute("DELETE from index_record where id = :i AND symbol = :s", i=session["user_id"], s=symbol_to_sell)
                    return index()
                else:
                    db.execute("UPDATE index_record SET number_of_shares = :n where id = :i AND symbol = :s",
                               n=remainder_shares, i=session["user_id"], s=symbol_to_sell)
                    return index()
        else:
            # if the request is GET request
            return render_template("sell.html", user_sell=user_sell)


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
