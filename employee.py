"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, onContract, salary = 0, hours = 0, rate = 0, hasComm= False, commBonus = 0, commContracts = 0, commRate = 0):
        self.name = name
        self.onContract = onContract
        self.salary = salary
        self.hours = hours
        self.rate = rate
        self.hasComm = hasComm
        self.commBonus = commBonus
        self.commContracts = commContracts
        self.commRate = commRate

    def get_pay(self):
        pay = 0
        #Check if they have monthly salary or contract
        if self.onContract:
            #add their hours x rate
            pay += self.hours * self.rate
        else:
            #add their salary
            pay += self.salary

        #Check if they have commissions
        if self.hasComm:
            #check if they have bonus commissions or contract
            if self.commBonus:
                #Add bonus commission
                pay += self.commBonus
            else:
                #Add their bonus per contract
                pay += self.commContracts * self.commRate
        self.pay = pay
        return pay

    def __str__(self):
        output = f'{self.name} works on a '
        if self.onContract:
            #add their hours x rate
            output += f'contract of {self.hours} hours at {self.rate}/hour'
        else:
            #add their salary
            output += f'monthly salary of {self.salary}'

        #Check if they have commissions
        if self.hasComm:
            #check if they have bonus commissions or contract
            if self.commBonus:
                #Add bonus commission
                output += f' and receives a bonus commission of {self.commBonus}.'
            else:
                #Add their bonus per contract
                output += f' and receives a commission for {self.commContracts} contract(s) at {self.commRate}/contract.'
        else:
            output += "."
        output += f'  Their total pay is {self.pay}.'
        return output


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',False, salary = 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',True, hours = 100, rate = 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', False, salary = 3000, hasComm = True, commContracts = 4, commRate = 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', True, hours = 150, rate = 25, hasComm = True, commContracts = 3, commRate = 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', False, salary = 2000, hasComm = True, commBonus = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', True, hours = 120, rate = 30, hasComm = True, commBonus = 600)
