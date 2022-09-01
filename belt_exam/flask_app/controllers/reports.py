from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, report

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect ('/users/logout')
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template('dashboard.html', this_user = this_user, reports = report.Report.view_all_reports())

@app.route('/report')
def report_sighting():
    if 'user_id' not in session:
        return redirect ('/users/logout')
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template('add_report.html', this_user = this_user)

@app.route('/report/create', methods = ['POST'])
def create_report():
    if report.Report.create_report(request.form):
        return redirect ('/dashboard')
    return redirect ('/report')

@app.route('/delete/<int:id>')
def delete(id):
    report.Report.delete_report(id)
    return redirect ('/dashboard')

@app.route('/view/<int:id>')
def view(id):
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template('view_report.html',this_user = this_user, report = report.Report.view_one_report(id))

@app.route('/edit/<int:id>')
def edit(id):
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template("edit_report.html", this_user = this_user, report = report.Report.view_one_report(id))

@app.route('/edit/report', methods = ['POST'])
def edit_report():
    id = request.form['id']
    if not report.Report.validate_rep_data(request.form):
        return redirect (f"/edit/{id}")
    report.Report.update_report(request.form)
    return redirect ('/dashboard')