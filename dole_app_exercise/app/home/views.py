from flask import render_template, redirect, url_for, request, flash
from markupsafe import Markup

from app.models import User, Department, Tenure
from . import home as home_blueprint
import os
import asyncio
from app.helpers import process_excel_file
# from .forms import CourseForm
from app import database
# import threading
# import concurrent.futures


@home_blueprint.route('/user/<int:user_id>', methods=['GET'])
def user_detail(user_id):
    user = User.query.get(user_id)
    # departments = Department.query.all()
    # department_years = [(department.name, user.get_years_in_department(department)) for department in departments]
    total_years = user.total_tenure()
    # dept_tenure_dict = {department.name: department.get_total_tenure()[department.name] for department in departments}
    # dept_tenure_list = [(department.name, sum([tenure.years for tenure in department.tenures])) for department in departments]
    return render_template('home/user_detail.html',
                            user=user,
                        #     department_years=department_years, 
                           total_years=total_years,
                        #    dept_tenure_dict=dept_tenure_dict, 
                        #    dept_tenure_list=dept_tenure_list
                           )




# @home_blueprint.route('/user/<int:user_id>')
# def user_detail(user_id):
#     user = User.query.get(user_id)
#     if not user:
#         flash('User not found!', 'error')
#         return redirect(url_for('home.all_users'))
#     return render_template('home/user_detail.html', user=user)

# @home_blueprint.route('/user/<int:user_id>', methods=['GET'])
# def user_detail(user_id):
#     user = User.query.get(user_id)
#     departments = Department.query.all()
#     department_years = [(department.name, user.get_years_in_department(department)) for department in departments]
#     total_years = user.get_total_tenure()
#     dept_tenure_dict = {department.name: department.get_total_tenure()[department.name] for department in departments}
#     dept_tenure_list = [(department.name, sum([tenure.years for tenure in department.tenures])) for department in departments]
#     return render_template('home/user_detail.html', user=user, department_years=department_years, 
#                            total_years=total_years, dept_tenure_dict=dept_tenure_dict, 
#                            dept_tenure_list=dept_tenure_list)



# @home_blueprint.route('/user/<int:user_id>', methods=['GET'])
# def user_detail(user_id):
#     user = User.query.get(user_id)
#     departments = Department.query.all()
#     department_years = []
#     total_years = 0
#     for department in departments:
#         years = user.get_years_in_department(department)
#         department_years.append((department.name, years))
#         total_years += years
#     # calculate total company tenure
#     company_tenure = user.get_total_tenure()
#     # create dictionary of department and tenure
#     dept_tenure_dict = {}
#     for department in departments:
#         tenure = Department.get_total_tenure(department)
#         dept_tenure_dict[department.name] = tenure
#     # create a list of tuples containing department and total tenure for all employees
#     dept_tenure_list = [(department.name, department.get_total_tenure()) for department in departments]
#     return render_template('home/user_detail.html', user=user, department_years=department_years, 
#                            total_years=total_years, company_tenure=company_tenure,
#                            dept_tenure_dict=dept_tenure_dict, dept_tenure_list=dept_tenure_list)



@home_blueprint.route('/all/users', methods=['GET', 'POST'])
def all_users():
    if request.method == 'POST':
        excel_file = request.files['file']
        if not excel_file:
            flash('File has to be an excel file!', 'error')
            return redirect(url_for('home.all_users'))
        if not excel_file.filename:
            flash('File name can not be empty', 'error')
            return redirect(url_for('home.all_users'))
        if excel_file.filename.split('.')[-1] not in ['xls', 'xlsx']:
            flash('Invalid file type', 'error')
            return redirect(url_for('home.all_users'))
        
        if len(excel_file.read()) > 1024 * 1024:
            flash('File size exceeds 1MB', 'error')
            return redirect(url_for('home.all_users'))

        # executor = concurrent.futures.ThreadPoolExecutor()
        # executor.submit(process_excel_file, excel_file)
        # executor.shutdown(wait=True)

        asyncio.run(process_excel_file(excel_file))

        flash('File is being uploaded please refresh page in a few seconds', 'success')
        return redirect(url_for('home.all_users'))
    
    # delete_all()
    all_users = User.query.all()

    return render_template('home/home.html',
                           users=all_users,
                           title="Users",)




def delete_all():

    dept = Department.query.all()
    ten = Tenure.query.all()
    all_users = User.query.all()
    for t in ten:
        print(t, 123)
        database.session.delete(t)
        database.session.commit()
    for d in dept:
        database.session.delete(d)
        database.session.commit()
    for us in all_users:
        database.session.delete(us)
        database.session.commit()
    



