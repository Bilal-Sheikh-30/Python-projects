
def calc_bonus():
    global total_sales
    if total_sales>=7000:
        print('Bonus amount is Rs.',(20*total_sales)/100)
    else:
        print("Bonus can not be granted due to low sales")
    print('\n\n\n')
def set_wage():
    print('''
    SET WAGE RATE FOR:
        1. EMP A
        2. EMP B''')
    print("\n\n")
    wage_setter = input("Enter: ")
    new_wage = int(input('Enter new wage: '))
    if wage_setter=='1':
        global emp_A_wage_rate
        emp_A_wage_rate = new_wage
        print("new wage of emp A is:",emp_A_wage_rate)
    elif wage_setter=='2':
        global emp_B_wage_rate
        emp_B_wage_rate = new_wage
        print("new wage of emp B is:",emp_B_wage_rate)
    print('\n\n\n')
def add_hours_worked():
    print('''
    SET WORKING HOURS FOR:
        1. EMP A
        2. EMP B''')
    print("\n\n")
    hours_setter = input("Enter: ")
    new_hours = int(input('Enter new working hours: '))
    if hours_setter=='1':
        global emp_A_hours
        emp_A_hours = new_hours
        print("working hours of emp A is:",emp_A_hours)
    elif hours_setter=='2':
        global emp_B_hours
        emp_B_hours = new_hours
        print("working hours of emp B is:",emp_B_hours)
    print('\n\n\n')
def calc_payment():
    print('''
    CALCULATE PAYMENT FOR:
        1. EMP A
        2. EMP B''')
    print("\n\n")
    pay_of_emp = input("Enter: ")
    if pay_of_emp=='1':
        print("EMPLOY A's PAYMENT IS: ", emp_A_hours*emp_A_wage_rate)
    elif pay_of_emp=='2':
        print("EMPLOY B's PAYMENT IS: ", emp_B_hours*emp_B_wage_rate)
    print('\n\n\n')
def add_item():
    print('''
    select item:
    1. samaosa
    2. rolls''')
    user_choice_item=input('enter: ')
    print('*'*20)
    user_choice_qty=int(input('enter quantity: '))
    if user_choice_item=='1':
        global samosa_in_stock
        samosa_in_stock+=user_choice_qty
        print('current stock of samosa is: ',samosa_in_stock)
    elif user_choice_item=='2':
        global rolls_in_stock
        rolls_in_stock+=user_choice_qty
        print('current stock of rolls is: ',rolls_in_stock)
def show_stock():
    global samosa_in_stock
    print('current stock of samosa is: ',samosa_in_stock)
    global rolls_in_stock
    print('current stock of rolls is: ',rolls_in_stock)
def cal_bill():
    print('''
    AVAILABLE ITEMS
    1. SAMOSA     RS20/=
    2. ROLL     RS30/=''')
    grand_total=0
    while True:
        order_item=input('select item: ')
        if order_item!='1' and order_item!='2':
            break
        order_qty=input('enter quantity: ')
        if order_item=='1':
            global samosa_unit_price
            total=samosa_unit_price*int(order_qty)
            grand_total+=total
            global samosa_in_stock
            samosa_in_stock-=int(order_qty)
        elif order_item=='2':
            global rolls_unit_price
            total=rolls_unit_price*int(order_qty)
            grand_total+=total
            global rolls_in_stock
            rolls_in_stock-=int(order_qty)
        # else:
            # print("please select the correct option")
            # bake_shop()
    boutique_check = input('HAVE YOU BOUGHT SOMETHING FROM OUR BOUTIQUE? (Y/N): ').upper()
    if boutique_check=='N':
        print('your total amount is Rs.',grand_total)
        global total_sales
        total_sales += grand_total
    elif boutique_check=='Y':
        def boutique_disc():
            boutique_bill = int(input('ENTER YOUR BOUTIQUE TOTAL: '))
            if boutique_bill>=20000:
                # nonlocal grand_total
                print("TOTAL AMOUNT Rs.",grand_total)
                disc_amount = (15*grand_total)/100
                print("DISCOUNT (15%) Rs.",disc_amount)
                net_total = grand_total-disc_amount
                print("AMOUNT PAYABLE Rs.",net_total)
                global total_sales
                total_sales+=net_total
            else:
                print("DISCOUNT IS NOT APPLICABLE")
        boutique_disc()
        
def bake_shop():
    print('''
    SELECT DESIRED COMMAND
    1. CALCULATE BILL
    2. UPDATE STOCKS
    3. CHECK STOCK
    
    MANAGEMENT OPTIONS:
    4. SET EMPLOY WAGE
    5. SET WORKING HOURS
    6. GENERATE EMPLOY PAYMENT
    7. CALCULATE BONUS''')
    admin_choice=input('>>')
    if admin_choice=='1':
        cal_bill()
        print('-'*40)
        print()
        print()
        bake_shop()
    elif admin_choice=='2':
        add_item()
        print('-'*40)
        print()
        print()
        bake_shop()
    elif admin_choice=='3':
        show_stock()
        print('-'*40)
        print()
        print()
        bake_shop()
    elif admin_choice=='4':
        set_wage()
        bake_shop()
    elif admin_choice=='5':
        add_hours_worked()
        bake_shop()
    elif admin_choice=='6':
        calc_payment()
        bake_shop()
    elif admin_choice=='7':
        calc_bonus()
        bake_shop()
emp_A_wage_rate = 800
emp_B_wage_rate = 900
emp_A_hours = 8
emp_B_hours = 8
samosa_in_stock=150
rolls_in_stock=200
samosa_unit_price=20
rolls_unit_price=30
total_sales = 0
bake_shop()