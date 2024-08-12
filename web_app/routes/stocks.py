
# adapted from "web_app/routes/stocks_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.medicare import company_dataframes

stocks_routes = Blueprint("stocks_routes", __name__)


@stocks_routes.route("/stocks/form")
def stocks_form():
    print("STOCKS FORM...")
    return render_template("stocks_form.html")


@stocks_routes.route("/stocks/results", methods=["POST"])
def stocks_results():
    ticker = request.form.get("ticker")
    if not ticker:
        flash("Please enter a ticker symbol.", "warning")
        return redirect("/stocks/form")

    # Check if the ticker symbol is a valid company key
    valid_company_keys = company_dataframes.keys()
    if ticker not in valid_company_keys:
        flash("Invalid ticker symbol.", "danger")
        return redirect("/stocks/form")

    # Use medicare.py data output here
    outputs = medicare.get_data(ticker)

    # Process the company data and generate the desired outputs
    # ...
    # Return the outputs to the website
    return render_template("stocks_results.html", ticker=ticker, outputs=outputs)
        except KeyError:
            flash("Invalid ticker symbol.", "danger")
            return redirect("/stocks/form")